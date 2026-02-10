import re

from utils.logs import logger
from typing import List

emailRe = re.compile(r'^[^@\s]+@[^@\s]+\.[^@\s]+$')

publicEmailDomains = [
    "@gmail.",
    "@yahoo.",
    "@outlook.",
    "@hotmail.",
    "@aol.",
    "@icloud.",
    "@mail.",
    "@protonmail.",
    "@zoho.",
    "@gmx.",
    "@yandex.",
    "@fastmail.",
    "@hushmail.",
    "@tutanota.",
    "@mailfence.",
    "@runbox.",
    "@posteo.",
    "@countermail.",
    "@startmail.",
    "@mailbox.",
    "@lavabit.",
    "@disroot.",
    "@mailbox.",
    "@cock.li",
    "@safe-mail.net",
]

def extract(emails, original: dict):
    results = []

    if isinstance(emails, str):
        emails = [emails]

    for email in emails:
        if isinstance(email, str) and emailRe.match(email):
            results.append({'emails': email})

            if not any(domain in email for domain in publicEmailDomains):
                results.append({'domain': email.split('@')[-1]})

    return results