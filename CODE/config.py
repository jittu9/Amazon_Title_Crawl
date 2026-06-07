import os

import datetime as dt

timestamp = dt.datetime.now().strftime("%d-%b-%y_%H-%M")


BASE_URL = r"https://www.amazon.in/dp"

# Directory where config.py exists
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Folders
DATA_DIR = os.path.join(BASE_DIR, "SOURCE")
OUTPUT_DIR = os.path.join(BASE_DIR, "OUTPUT")
LOG_DIR = os.path.join(BASE_DIR, "LOGS")

# Create folders if they don't exist
os.makedirs(OUTPUT_DIR, exist_ok=True)
os.makedirs(LOG_DIR, exist_ok=True)

# Files
INPUT_FILE = os.path.join(
    DATA_DIR,
    "amazon_asins.csv"
)

OUTPUT_FILE = os.path.join(
    OUTPUT_DIR,
    f"amazon_product_details_{timestamp}.xlsx"
)

LOG_FILE = os.path.join(
    LOG_DIR,
    "amazon_scraper.log"
)