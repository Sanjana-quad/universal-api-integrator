from src.nlp.text_cleaner import clean_text

sample = "Hello!!!  This   is   SANJANA 😊\n\nNew line."
print(clean_text(sample))
# Expected output: "hello this is sanjana new line"