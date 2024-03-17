from dataclasses import dataclass

@dataclass
class AmazonProduct:
    """Data Class to represent Amazon product information."""
    title: str
    currencySymbol: str
    price: float
    availability: bool
    productUrl: str
    productID: str

    def __str__(self):
        return f"---\nTitle: {self.title}\nPrice: {self.currencySymbol}{self.price}\nAvailability: {'Available' if self.availability else 'Not Available'}\nLink: {self.productUrl}\nProduct ID: {self.productID}\n---"
