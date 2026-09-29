import re
from html import unescape

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def clean(text):
    
    return " ".join(text.split())


def text_of(el):
    
    html = el.get_attribute("innerHTML")
    return clean(unescape(re.sub(r"<[^>]+>", " ", html)))


driver = webdriver.Chrome()

try:
    driver.get("https://www.icc-cricket.com/rankings")

    WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.TAG_NAME, "table"))
    )

    elements = driver.find_elements(By.XPATH, "//h2 | //table")
    print("Tables:", sum(1 for e in elements if e.tag_name.lower() == "table"))

    with open("icc_rankings.txt", "w", encoding="utf-8") as file:
        for el in elements:
            tag = el.tag_name.lower()

            if tag == "h2":
                title = text_of(el)
                if "ranking" in title.lower():
                    file.write(f"\n{'=' * 60}\n{title}\n{'=' * 60}\n")

            # Ranking table
            elif tag == "table":
                card = el.find_element(
                    By.XPATH, "./ancestor::*[contains(., 'Rankings')][1]"
                )
                label = text_of(card).split("POS")[0].strip().upper()
                file.write(f"\n{label or '(no label found)'}\n{'-' * 40}\n")

                for row in el.find_elements(By.TAG_NAME, "tr"):
                    cells = row.find_elements(By.CSS_SELECTOR, "th, td")
                    data = [text_of(c) for c in cells]
                    data = [d for d in data if d]

                    if not data or data[0].lower() == "full rankings":
                        continue

                    
                    parts = data[0].split()
                    pos = parts[0]
                    if pos == "POS":
                        change = "CHG"
                    else:
                        change = parts[1] if len(parts) > 1 else ""

                    file.write(" | ".join([pos, change] + data[1:]) + "\n")

    print("Rankings saved to icc_rankings.txt")

finally:
    driver.quit()