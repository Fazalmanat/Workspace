from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def clean(text):
    return " ".join(text.split())

# Runs in the browser: find the card around a table and return the text before the table
GET_LABEL_JS = """
const table = arguments[0];
let node = table;
while (node.parentElement) {
    const parent = node.parentElement;
    if (parent.querySelectorAll('table').length > 1) break;  // parent holds other tables too
    node = parent;
}
// node is now the largest container with only this table
const parts = [];
const walker = document.createTreeWalker(node, NodeFilter.SHOW_TEXT);
while (walker.nextNode()) {
    const t = walker.currentNode;
    if (table.contains(t)) break;            // stop when we reach the table itself
    const s = t.textContent.trim();
    if (s) parts.push(s);
}
return parts.join(' ');
"""

driver = webdriver.Chrome()
try:
    driver.get("https://www.icc-cricket.com/rankings")
    WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.TAG_NAME, "table"))
    )

    elements = driver.find_elements(By.XPATH, "//h2 | //table")

    with open("icc_rankings.txt", "w", encoding="utf-8") as f:
        for el in elements:
            tag = el.tag_name.lower()

            if tag == "h2":
                title = clean(el.get_attribute("textContent"))
                if "ranking" in title.lower():
                    f.write(f"\n{'=' * 60}\n{title}\n{'=' * 60}\n")

            elif tag == "table":
                label = clean(driver.execute_script(GET_LABEL_JS, el))
                f.write(f"\n{label or '(no label found)'}\n{'-' * 40}\n")

                for row in el.find_elements(By.TAG_NAME, "tr"):
                    cells = row.find_elements(By.CSS_SELECTOR, "th, td")
                    data = [clean(c.get_attribute("textContent")) for c in cells]
                    data = [d for d in data if d]
                    if data:
                        f.write(" | ".join(data) + "\n")
finally:
    driver.quit()