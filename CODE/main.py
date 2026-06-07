# -*- coding: utf-8 -*-
"""
Created on Sun Jun  7 06:55:27 2026

@author: 91733
"""

import pandas as pd

from config import (
    INPUT_FILE,
    OUTPUT_FILE
)

from logger import (
    get_logger
)

from driver_setup import (
    get_driver
)

from scraper import (
    scrape_asin
)


def load_asins():

    return (
        pd.read_csv(INPUT_FILE)["ASIN"]
        .dropna()
        .astype(str)
        .unique()
        .tolist()
    )


def main():

    logger = get_logger()

    logger.info(
        "Loading ASIN file"
    )

    asin_list = load_asins()

    logger.info(
        "Total ASINs found: %s",
        len(asin_list)
    )


    driver = get_driver()

    try:
        final_df = scrape_asin(
                    driver,
                    asin_list,
                    logger
                )
            

    finally:

        driver.quit()

        logger.info(
            "Chrome driver closed"
        )


    final_df.to_excel(
        OUTPUT_FILE,
        index=False
    )

    logger.info(
        "Output saved: %s",
        OUTPUT_FILE
    )


if __name__ == "__main__":
    main()