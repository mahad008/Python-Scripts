import requests
from bs4 import BeautifulSoup
import pandas as pd
import time
import random

def scrape_amazon_product(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/142.0.0.0 Safari/537.36",
        "Accept-Language": "en-US,en;q=0.9",
        "Cookie": """ session-id-time=2082787201l; i18n-prefs=USD; lc-main=en_US; sp-cdn="L5Z9:PK"; session-id=143-9460138-9011549; ubid-main=133-1993990-2867106; session-token=ZN0jGgpGw9SLOmaEsZgH2EkW2W7d5FOCtrh4nCRGMr/kciBcQORNw6DuLmGw4pdygoFXdNVyxE+XbSj1zvVE4vdWrBlU2HdjBxrzYFE035bl3ydsVFGlXVvbIPZqkPuA9dCUUL1DizBYEdDP3nF/DslI1OfvdOiVqoiWIMBMZcVxNKbojcT0mmQ616Ki7zh5tL7nTtqaPeMnrhvJbu5bZX06LAAX3CXi+n+QP8P8Yjs79i23HKRPA2Uzv3/whamPdEd3DbbS3Gu71xbxlQ/mZc6wcKEWuKIerahHzsvS8RDt7GfZp6i5M0raxh7SdpbwdmvC2vlcM5IH/FtMWmNlDF8UlIUIDUwc; skin=noskin """
    }

    print(f"scraping: {url}")

    try:
        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.text, "html.parser")

        title = soup.find("span", id="productTitle")
        if title:
            title = title.get_text().strip()
        else:
            title = "Not found"

        price = soup.find("span", class_="a-offscreen")
        if price:
            price = price.get_text().strip()
        else:
            price = "not available"

        rating = soup.find("span", class_="a-icon-alt")
        if rating:
            rating = rating.get_text().strip()
        else:
            rating = "not found"

        return {
            "Product title": title,
            "Product Price": price,
            "Product Rating": rating,
            "URL": url
        }

    except Exception as e:
        print("Error scraping:", e)
        return None


if __name__ == "__main__":

    product_urls = [
        "https://www.amazon.com/GIGABYTE-GeForce-WINDFORCE-Graphics-GV-N5090WF3OC-32GD/dp/B0DT7GMXHB/ref=sr_1_1?crid=OWZY7C9AZLX5&dib=eyJ2IjoiMSJ9.e7UUGt2jKybBTU7o8e30ZnR3U9mRVpVT4d3yzsRThgJGuAYBP-Kv4SJxlm0SuYRXPT-S9UxOe5IJUx8GFWoUqwJ9GqLrCXzPc_lNNSNV_u_Ryy5ttSLkXjvnUxhSFRz1dhoZLrBo5zf2JdvRUZycAh_CQAv8xeXKKwq9i0r1XFlb3Efl912ONgJa2I_psd94ug4JYl6en7nO9D90-25WRlSF2jKw_l7fOt4YtK6u9-M.jeKvw24A_OS0zJxWl_TFyaH2aFlcEfRm_sOjmc6IvrM&dib_tag=se&keywords=5090&qid=1763657542&sprefix=50%2Caps%2C857&sr=8-1&th=1",
        "amazon.com/GIGABYTE-GeForce-WINDFORCE-Graphics-GV-N5070WF3OC-12GD/dp/B0DTQMLX4F/ref=pd_ci_mcx_di_int_sccai_cn_d_sccl_2_5/143-9460138-9011549?pd_rd_w=GmE3w&content-id=amzn1.sym.751acc83-5c05-42d0-a15e-303622651e1e&pf_rd_p=751acc83-5c05-42d0-a15e-303622651e1e&pf_rd_r=KT6BCQRKXAPWH4CTYGZ2&pd_rd_wg=gwCGS&pd_rd_r=320a8533-06bd-4725-b64d-87ccc1837185&pd_rd_i=B0DTQMLX4F&psc=1",
        "https://www.amazon.com/AMD-RyzenTM-9600X-12-Thread-Processor/dp/B0D6NN6TM7/ref=pd_ci_mcx_di_int_sccai_cn_d_sccl_1_12/143-9460138-9011549?pd_rd_w=TNciU&content-id=amzn1.sym.751acc83-5c05-42d0-a15e-303622651e1e&pf_rd_p=751acc83-5c05-42d0-a15e-303622651e1e&pf_rd_r=2GSQS43BMH8RD1QR5TH9&pd_rd_wg=stXr2&pd_rd_r=760b5939-1a83-4fb8-a372-fc72ac5ac1ba&pd_rd_i=B0D6NN6TM7&psc=1"
    ]

    scraped_data = []

    for url in product_urls:
        data = scrape_amazon_product(url)
        if data:
            scraped_data.append(data)

        time.sleep(random.uniform(2, 5))

    df = pd.DataFrame(scraped_data)
    df.to_csv("amazon_products.csv", index=False)

    print("\nDone! Data saved to amazon_products.csv")
