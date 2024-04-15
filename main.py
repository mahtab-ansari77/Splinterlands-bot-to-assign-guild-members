import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_obj = Service("D:/chromedriver.exe")  #add your webdriver path here
driver = webdriver.Chrome(service=service_obj)
driver.get("https://splinterlands.com/")
driver.maximize_window()

login = driver.find_element(By.XPATH, "//button[text()='Log In']").click()
driver.implicitly_wait(10)
driver.find_element(By.CSS_SELECTOR, "input[placeholder='EMAIL / USERNAME']").send_keys("your_username")
driver.find_element(By.NAME, "password").send_keys("your_posting_key")
driver.find_element(By.XPATH, "//button[@type = 'submit']").click()
time.sleep(10)
driver.refresh()
time.sleep(10)
driver.find_element(By.XPATH, "//button[normalize-space()='YES']").click()
time.sleep(5)

# Define a list of players to assign
players = ["werkily", "rahulsingh25843", "mdwakil", "zya", "nobitaa", "econom", "krikblock", "aryankk", "dinty", "kasib", "anilkumar125469", "harse", "handsoff"]

# Loop through the list and perform the assignments, skipping index 6
for i, player in enumerate(players):
    index = i + 1
    if index == 6:
        continue
    driver.find_element(By.XPATH, f"(//img[@class='dot-menu'])[{index}]").click()
    driver.find_element(By.CSS_SELECTOR, f"button[onclick = 'openAssignDialog({i});']").click()
    driver.find_element(By.XPATH, f"(//span[normalize-space()='{player}'])[1]").click()
    print(f"{player} is assigned.")
    time.sleep(12)

#I have skipped index 6 above because the index 6 player is a leader and it has some different xpath so it cannot iterate there
#if you are a leader of that guild then below is the code for you to assign yourself automatically.
driver.find_element(By.XPATH, "(//img[@class='dot-menu'])[6]").click()
driver.find_element(By.CSS_SELECTOR, "button[onclick = 'openAssignDialog(5);']").click()
driver.find_element(By.XPATH, "(//span[@class='bio__name__display'][normalize-space()='econom'])[2]").click()
time.sleep(10)

driver.quit()

