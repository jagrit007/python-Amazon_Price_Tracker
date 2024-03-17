from AmazonApp.client.amazonUtils import AmazonClient
from AmazonApp import AMAZON_COUNTRY, AFFILIATE_TAG


if __name__ == '__main__':
    client = AmazonClient(AFFILIATE_TAG, AMAZON_COUNTRY)
    print("-------------------------")
    product_link = input("Enter product link: ")
    if product_link:
        fetchedProduct = client.fetchProduct(product_url=product_link)
        print(fetchedProduct)
        # TO-DO Track Product for Price changes and alert via Telegram / E-mail