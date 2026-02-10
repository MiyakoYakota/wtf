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
    party: Optional[str] = None
    
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
    emails: List[str] = field(default_factory=list)
    phoneNumbers: List[str] = field(default_factory=list)
    usernames: List[str] = field(default_factory=list)
    
    # Network Information
    ips: List[str] = field(default_factory=list)
    domain: Optional[str] = None
    asn: Optional[int] = None
    asnOrg: Optional[str] = None
    accuracy_radius: Optional[int] = None
    links: List[str] = field(default_factory=list)
    
    # Financial Information
    income: Optional[str] = None
    
    # Security/Credentials
    passwords: List[str] = field(default_factory=list)
    
    # Metadata
    source: Optional[str] = None
    line: Optional[str] = None
    
    # Additional Fields
    notes: List[str] = field(default_factory=list)
    photos: List[str] = field(default_factory=list)
    

    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            if hasattr(self, key):
                setattr(self, key, value)
    
    def add_or_set_value(self, key: str, value):
        if hasattr(self, key):
            current_value = getattr(self, key)
            if isinstance(current_value, list):
                if isinstance(value, list):
                    current_value.extend(value)
                else:
                    current_value.append(value)
            else:
                if isinstance(current_value, list):
                    if current_value is None:
                        setattr(self, key, [value])
                    else:
                        current_value.append(value)
                else:
                    setattr(self, key, value)