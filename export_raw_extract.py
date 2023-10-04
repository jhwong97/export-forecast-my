from dotenv import load_dotenv
from logging_export import logger
import requests
from requests.adapters import HTTPAdapter
from urllib3.util import Retry
from bs4 import BeautifulSoup

# Function to extract raw data
def export_extract(url, payload, headers):
    
    MAX_RETRIES = 2
    
    # Define the retry strategy
    retry_strategy = Retry(
        total = MAX_RETRIES,
        backoff_factor = 1.5,
        status_forcelist = [429, 500, 502, 503, 504]
    )
    
    # Create an HTTP adapter with the retry strategy and mount it to session
    adapter = HTTPAdapter(max_retries=retry_strategy)
    
    # Create a new session object
    session = requests.Session()
    session.mount('http://', adapter)
    session.mount('https://', adapter)
    
    # Make a request using the session object
    
    raw_data = session.post(url, data=payload, headers=headers)    
    logger.info('Extracting raw data in progres......')
    
    if raw_data.status_code == 200:
        logger.info('SUCCESS: Raw Data has been extracted')
    else:
        logger.warning('FAILED: Raw Data failed to be extracted.')

    raw_data = BeautifulSoup(raw_data.text, 'html.parser') # Parse the HTML
    
    return raw_data