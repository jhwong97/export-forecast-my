from dotenv import load_dotenv
from logging_export import logger
import requests
from requests.adapters import HTTPAdapter
from urllib3.util import Retry

# Function to extract data
def export_extract(url, payload, headers, end_year):
    
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
    
    if raw_data.status_code == 200:
        logger.info(f"SUCCESS: Data for {end_year} has been extracted")
    else:
        logger.info(f"FAILED: Data for {end_year} not able to be extracted")
    
    return raw_data