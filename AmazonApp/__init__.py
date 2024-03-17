import os

from dotenv import load_dotenv

load_dotenv('config.env')

AFFILIATE_TAG = os.environ.get('AFFILIATE_TAG', 'scipple-21')
AMAZON_COUNTRY = os.environ.get('AMAZON_COUNTRY', 'in')