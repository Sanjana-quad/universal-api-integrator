import re
import unicodedata
from src.logger.logger import get_logger

log = get_logger("text_cleaner")

def normalize_whitespace(text: str) -> str:
    """Replace multiple spaces/newlines/tabs with a single space."""
    log.debug("Normalizing whitespace")
    return re.sub(r"\s+", " ", text).strip()

def remove_punctuation(text: str) -> str:
    """Remove punctuation."""
    log.debug("Removing punctuation")
    return re.sub(r"[^\w\s]", "", text)

def lowercase(text: str) -> str:
    """Convert text to lowercase."""
    log.debug("Lowercasing text")
    return text.lower()

def remove_accents(text: str) -> str:
    """Remove accents like café → cafe."""
    log.debug("Removing accents")
    nfkd = unicodedata.normalize("NFKD", text)
    return "".join([c for c in nfkd if not unicodedata.combining(c)])

def clean_text(text: str) -> str:
    """Full cleaning pipeline."""
    log.info("Cleaning text")
    text = remove_accents(text)
    text = lowercase(text)
    text = remove_punctuation(text)
    text = normalize_whitespace(text)
    return text

#new extraction functions added below

def extract_emails(text: str):
    log.info("Extracting emails")
    return re.findall(r"[\w\.-]+@[\w\.-]+\.\w+", text)

def extract_phone_numbers(text: str):
    log.info("Extracting phone numbers")
    return re.findall(r"\d{10}", text)

def extract_dates(text: str):
    log.info("Extracting dates")
    return re.findall(r"\d{2}[/-]\d{2}[/-]\d{4}", text)

def extract_urls(text: str):
    log.info("Extracting URLs")
    return re.findall(r"https?://[^\s]+", text)

def extract_hashtags(text: str):
    log.info("Extracting hashtags")
    return re.findall(r"#\w+", text)    

def extract_mentions(text: str):
    log.info("Extracting mentions")
    return re.findall(r"@\w+", text)

def extract_numbers(text: str):
    log.info("Extracting numbers")
    return re.findall(r"\b\d+\b", text)

