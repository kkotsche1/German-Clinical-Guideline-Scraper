from selenium import webdriver
import time
from bs4 import BeautifulSoup
from tqdm import tqdm

download_dir = "C:\\Users\\Admin\\PycharmProjects\\Leitlinien"  # for linux/*nix, download_dir="/usr/Public"
options = webdriver.ChromeOptions()

profile = {"plugins.plugins_list": [{"enabled": False, "name": "Chrome PDF Viewer"}],  # Disable Chrome's PDF Viewer
           "download.default_directory": download_dir, "download.extensions_to_open": "applications/pdf"}
options.add_experimental_option("prefs", profile)
driver = webdriver.Chrome(chrome_options=options)  # Optional argument, if not specified will search path.

driver.get("https://register.awmf.org/de/leitlinien/aktuelle-leitlinien")
time.sleep(5)
htmlSource = driver.page_source
soup = BeautifulSoup(htmlSource, "html.parser")

sub_pages = soup.find_all(class_ = "link")

for page in tqdm(sub_pages[91:]):
        try:
                link = page.find_next("a")["href"]
                link__ = link
                driver.get(link)
                time.sleep(3)
                htmlSource = driver.page_source
                soup = BeautifulSoup(htmlSource, "html.parser")

                import re

                link = soup.find("a", href=re.compile(".pdf"))
                title = soup.find("h1").text

                link_ = f"https://register.awmf.org{link['href']}"
                import requests

                url = link_
                r = requests.get(url, stream=True)

                with open(title.replace("/", "") + "_" + link_.split("/")[-1], 'wb') as f:
                    f.write(r.content)

        except:
                print(link__)
                print(title, link)

