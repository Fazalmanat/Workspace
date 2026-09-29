from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()

driver.get("https://m.dailyhunt.in/news/india/english/mykhel-epaper-mykhel/india+vs+afghanistan+live+weather+updates+asian+games+2026+toss+delayed+sky+remains+dark+covers+on-newsid-n728413286?listname=topicsList&topic=sports&index=1&topicIndex=3&mode=pwa&action=click")

title = driver.find_element(By.TAG_NAME, "h1").text

paragraphs = driver.find_elements(By.TAG_NAME, "p")

with open("data.txt", "w", encoding="utf-8") as file:
    file.write(title + "\n\n")

    for p in paragraphs:
        if p.text.strip():
            file.write(p.text + "\n\n")
    

driver.quit()

print("Saved to data.txt")