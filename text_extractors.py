from src.nlp.text_cleaner import extract_emails, extract_phone_numbers, extract_dates, extract_urls, extract_hashtags, extract_mentions, extract_numbers

text = """
Contact us at support@example.com or hr@company.org
Phone: 9876543210, Office: 08012345678
Invoice date: 12/05/2023  
DOB: 01-11-1999
url: https://example.com
#hashtags #NLP @user_mentions
9275%
"""

print(extract_emails(text))
print(extract_phone_numbers(text))
print(extract_dates(text))
print(extract_urls(text))
print(extract_hashtags(text))
print(extract_mentions(text))
print(extract_numbers(text))