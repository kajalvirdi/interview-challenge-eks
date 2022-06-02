import requests
import os
import sys
import logging


# initilize logging
logger = logging.getLogger()

# logging with k8s
handler = logging.FileHandler('/proc/1/fd/1', mode='w')
logger.setLevel(logging.DEBUG)
logs_format = '[%(asctime)s] %(levelname)s - %(message)s'
formatter = logging.Formatter(logs_format)
handler.setFormatter(formatter)
logger.addHandler(handler)

health_api_response = False
try:
    # sending /health request
    health_api_response = requests.get('http://localhost/health', verify=False)
    logger.info(f"The api /health response: {health_api_response.status_code}")
except Exception as e:
    logger.error(f"Failed to check /health response, {e}")

average_load_value = False
try:
    # Check Average CPU load value
    average_load_value = os.getloadavg()[0] / os.cpu_count() * 100
    logger.info(f"Average Load value: {average_load_value}")
except Exception as e:
    logger.error(f"Error getting Average Load Usage value, {e}")

# /health validation
if not health_api_response:
    api_test_fail = True
    logger.error(f"Could not get /health response, the test has been failed!")
elif health_api_response.status_code != 200:
    api_test_fail = True
    logger.error(f"Bad /health response, the test has been failed!")
elif health_api_response.status_code == 200:
    logger.debug(f"Success /health API test,")

logger.info(f"all tests passed, test is succeeful!, exiting")
sys.exit(0)
