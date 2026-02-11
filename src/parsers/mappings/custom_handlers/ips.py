import ipaddress
from utils.regex import IPV4_REGEX, IPV6_REGEX
from utils.logs import get_logger

logger = get_logger(__name__)
from typing import List


def extract(ips, original_key: str, original_dict: dict):
    results = []

    if isinstance(ips, str):
        ips = [ips]

    for ip in ips:
        if IPV4_REGEX.match(ip):
            results.append({'ips': ip})
        elif IPV6_REGEX.match(ip):
            results.append({'ips': ip})

        elif ip.isdigit():
            try:
                ip_int = int(ip)
                
                if ip_int <= 0xFFFFFFFF:  # Maximum value for IPv4
                    ip_obj = ipaddress.IPv4Address(ip_int)
                else:
                    ip_obj = ipaddress.IPv6Address(ip_int)  # Treat it as IPv6 if it's out of IPv4 range
                
                results.append({'ips': str(ip_obj)})
            except ValueError as e:
                logger.warning(f"Failed to convert integer to IP: {ip}, Error: {e}")
        else:
            logger.warning(f"Unknown IP format: {ip}")

    return results
