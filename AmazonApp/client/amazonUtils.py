from AmazonApp.session.amazon_session import AmazonSession
from bs4 import BeautifulSoup
from AmazonApp.data_class.AmazonProduct import AmazonProduct
import re

class AmazonClient:
    """Amazon client for scraping and extracting information using AmazonSession
    """
    def __init__(self, affiliate_tag='scipple-21', domain='in') -> None:
        self.AFFILIATE_TAG = affiliate_tag
        self.AMAZON_DOMAIN = domain
        self.AMAZON_ASIN_PATTERN = re.compile(r"(?:[/dp/]|$)([A-Z0-9]{10})")

    def fetchProduct(self, product_url):
        session = AmazonSession()
        response = session.makeRequest(url=product_url)
        soup = BeautifulSoup(response.content, "lxml")
        price = self._getPrice(soup=soup)
        product_title = self._getTitle(soup=soup)
        product_id = self._getProductID(url=product_url)
        affiliate_url = self.__getAffiliateLink(product_id=product_id)
        return AmazonProduct(
            title=product_title,
            currencySymbol="₹",
            price=price,
            availability=True,
            productUrl=affiliate_url,
            productID=product_id
            )

    def _getProductID(self, url):
        product_id = ''
        try:
            product_id = self.AMAZON_ASIN_PATTERN.search(url).group(1)
        except Exception as e:
            print(e)
            pass
        return product_id        
    
    def __getAffiliateLink(self, product_id):
        return f"https://www.amazon.{self.AMAZON_DOMAIN}/dp/{product_id}?tag={self.AFFILIATE_TAG}"
    
    def _getPrice(self, soup):
        price = round(float(0.00), 2)
        try:
            price = soup.find(class_="a-offscreen").get_text()
            price_without_currency = price.split("₹")[1]
            price = round(float(price_without_currency), 2)
        except Exception as e:
            print(e)
            pass
        return price

    def _getTitle(self, soup):
        try:
            title = soup.find("span", attrs={"id": 'productTitle'})
            title_value = title.string
            title_string = title_value.strip().replace(',', '')
            
        except AttributeError:
                title_string = "NA"
        return title_string

