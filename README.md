# Amazon ASIN Title Scraper

## Overview
Production-ready Amazon ASIN title scraper built with Python, Selenium, BeautifulSoup, and Pandas.

### Features
- ASIN-based title extraction
- Automated ChromeDriver management
- Headless browser support
- Structured logging
- Excel exports
- Modular architecture
- Easy deployment

## Installation

```bash
git clone https://github.com/<username>/Amazon_Title_Crawl.git
cd Amazon_Title_Crawl
pip install -r requirements.txt
```

## Run

```bash
python CODE/main.py
```

## Tech Stack
- Python
- Selenium
- BeautifulSoup
- Pandas
- OpenPyXL

## Project Structure

```text
Amazon_Title_Crawl/
│
├── CODE/                       # Application source code
│   ├── main.py                 # Entry point
│   ├── scraper.py              # Amazon scraping logic
│   ├── driver_setup.py         # Selenium WebDriver configuration
│   ├── config.py               # Global configuration and paths
│   ├── logger.py               # Logging setup
│   └── __init__.py
│
├── SOURCE/                     # Input files
│   └── amazon_asins.csv
│
├── OUTPUT/                     # Generated Excel outputs
│
├── LOGS/                       # Application logs
│
│
├── README.md                   # Project documentation
├── requirements.txt            # Python dependencies
├── .gitignore                  # Git ignore rules
├── LICENSE                     # MIT License
├── CHANGELOG.md                # Version history
└── CONTRIBUTING.md             # Contribution guidelines
```
## Author
Jitendra Damu
