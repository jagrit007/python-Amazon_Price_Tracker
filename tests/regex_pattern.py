import re

AMAZON_ASIN_PATTERN = re.compile(r"(?:[/dp/]|$)([A-Z0-9]{10})")

print(AMAZON_ASIN_PATTERN.search("https://www.amazon.in/roboCraze-Arduino-Development-Board-cable/dp/B07G4C4D8F").group(1))