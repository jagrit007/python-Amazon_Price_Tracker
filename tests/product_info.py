from AmazonApp.client.amazonUtils import AmazonClient


amazon = AmazonClient()
prod_1 = amazon.fetchUrl("https://www.amazon.in/roboCraze-Arduino-Development-Board-cable/dp/B07G4C4D8F")
print(prod_1)