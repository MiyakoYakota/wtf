from typing import Optional, List
from dataclasses import dataclass, field


@dataclass
class Record:
    # Personal Information
    firstName: Optional[str] = None
    middleName: Optional[str] = None
    lastName: Optional[str] = None
    
    # Demographics
    gender: Optional[str] = None
    ethnicity: Optional[str] = None
    dob: Optional[str] = None
    
    # Location Information
    address: Optional[str] = None
    city: Optional[str] = None
    state: Optional[str] = None
    zipCode: Optional[str] = None
    country: Optional[str] = None
    continent: Optional[str] = None
    location: Optional[str] = None
    latLong: Optional[str] = None
    
    # Vehicle Information
    autoMake: Optional[str] = None
    autoModel: Optional[str] = None
    autoYear: Optional[str] = None
    autoBody: Optional[str] = None
    autoClass: Optional[str] = None
    vin: Optional[str] = None
    VRN: Optional[str] = None
    
    # Contact Information
    emails: Optional[str] = None
    phoneNumbers: Optional[str] = None
    usernames: Optional[str] = None
    
    # Network Information
    ips: List[str] = field(default_factory=list)
    domain: Optional[str] = None
    asn: Optional[int] = None
    asnOrg: Optional[str] = None
    accuracy_radius: Optional[int] = None
    
    # Financial Information
    income: Optional[str] = None
    
    # Security/Credentials
    passwords: List[str] = field(default_factory=list)
    
    # Metadata
    source: Optional[str] = None
    line: Optional[str] = None
    
    # Optional Multi-valued Fields
    links: List[str] = field(default_factory=list)
    notes: List[str] = field(default_factory=list)
    party: List[str] = field(default_factory=list)
    photos: List[str] = field(default_factory=list)
    