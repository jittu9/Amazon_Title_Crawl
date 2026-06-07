# -*- coding: utf-8 -*-
"""
Created on Sun Jun  7 07:02:49 2026

@author: 91733
"""

import logging

from config import LOG_FILE


def get_logger():

    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s | %(levelname)s | %(message)s",
        handlers=[
            logging.FileHandler(LOG_FILE),
            logging.StreamHandler()
        ]
    )

    return logging.getLogger("amazon_scraper")