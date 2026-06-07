# -*- coding: utf-8 -*-
"""
Created on Sun Jun  7 06:55:09 2026

@author: 91733
"""


from bs4 import BeautifulSoup
import pandas as pd

from config import (
    BASE_URL,
)



def scrape_asin(driver, asin_list, logger) -> dict:
    """
    Scrape a single ASIN and return structured data.
    """
    
    final_df = pd.DataFrame()
    
    for asin in asin_list:
        
        print(asin)
        logger.info("Processing ASIN: %s", asin)
    
        url = f"{BASE_URL}/{asin}"
    
        try:
            driver.get(url)
    
            soup = BeautifulSoup(driver.page_source, "html.parser")
    
            title_tag = soup.title
    
            if title_tag:
                title = title_tag.get_text(separator="\n", strip=True)
            else:
                title = "No title found"
                
        except Exception as e:
    
            logger.exception("Failed for ASIN: %s", asin)
            
    
            title = e
            
    
        out_df = pd.DataFrame([{'ASIN': asin, 'title': title}])
        
        final_df = pd.concat([final_df, out_df], ignore_index=True)
        
        
    return final_df
        
        
    

