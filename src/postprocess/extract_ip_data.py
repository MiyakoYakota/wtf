import os
import re
from utils.logs import get_logger
import geoip2.database

logger = get_logger(__name__)

ASN_PATTERN = re.compile(r'(AS\d+)', re.IGNORECASE)

geoip_path = os.path.join(os.path.dirname(__file__), 'resources', 'GeoLite2-City.mmdb')
asn_path = os.path.join(os.path.dirname(__file__), 'resources', 'GeoLite2-ASN.mmdb')

# Initialize Readers
try:
    geo_reader = geoip2.database.Reader(geoip_path)
except Exception as e:
    logger.error(f"Failed to load GeoLite2-City database: {e}")
    geo_reader = None

try:
    asn_reader = geoip2.database.Reader(asn_path)
except Exception as e:
    logger.error(f"Failed to load GeoLite2-ASN database: {e}")
    asn_reader = None
def extract(record):
    # --- 1. Validate Existing ASN Format ---
    existing_asn = record.get("asn")
    if existing_asn:
        match = ASN_PATTERN.search(str(existing_asn))
        if match:
            record["asn"] = match.group(1).upper()
        else:
            record["asn"] = None

    # Check if we even need to do work
    needs_geo = not all(record.get(k) for k in ["city", "state", "country"])
    needs_asn = not record.get("asn")

    if not (needs_geo or needs_asn):
        return record

    ip_list = record.get("ips", [])
    for ip in ip_list:
        try:
            # --- 2. Location Enrichment ---
            if geo_reader and needs_geo:
                response = geo_reader.city(ip)
                if not record.get("city") and response.city.name:
                    record["city"] = response.city.name
                if not record.get("state") and response.subdivisions:
                    record["state"] = response.subdivisions.most_specific.name
                if not record.get("country") and response.country.name:
                    record["country"] = response.country.name
                if not record.get("continent") and response.continent.name:
                    record["continent"] = response.continent.name
                if not record.get("latLong") and response.location.latitude:
                    record["latLong"] = f"{response.location.latitude},{response.location.longitude}"
                if not record.get("accuracy_radius") and response.location.accuracy_radius:
                    record["accuracy_radius"] = response.location.accuracy_radius

            # --- 3. ASN Enrichment ---
            if asn_reader and needs_asn:
                asn_response = asn_reader.asn(ip)
                if asn_response.autonomous_system_number:
                    record["asn"] = f"AS{asn_response.autonomous_system_number}"
                if not record.get("isp") and asn_response.autonomous_system_organization:
                    record["isp"] = asn_response.autonomous_system_organization

            break # Exit IP loop once enrichment is successful

        except Exception as e:
            logger.debug(f"Lookup failed for {ip}: {e}")
            continue

    return record