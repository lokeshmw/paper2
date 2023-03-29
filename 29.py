from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By

driver = webdriver.Chrome("C://Users//HP//Downloads//chromedriver_win32//chromedriver.exe")

driver.maximize_window()

driver.get("https://www.flipkart.com/")

wait = WebDriverWait(driver, 10)
wait.until(ec.title_contains("Online Shopping Site for Mobiles, Electronics, Furniture, Grocery, Lifestyle, Books & "
                             "More. Best Offers!"))

login_btn = driver.find_element_by_xpath("//a[text()='Login']")
login_btn.click()
wait.until(ec.visibility_of_element_located((By.XPATH, "//span[text()='Enter Email/Mobile number']")))
email_input = driver.find_element_by_xpath("//input[@class='_2IX_2- VJZDxU']")
email_input.send_keys("your_email@domain.com")
password_input = driver.find_element_by_xpath("//input[@type='password']")
password_input.send_keys("your_password")
password_input.send_keys(Keys.RETURN)

search_box = driver.find_element_by_name("q")
search_box.send_keys("Dell laptop")
search_box.send_keys(Keys.RETURN)
wait.until(ec.visibility_of_element_located((By.XPATH, "//div[@class='_1YokD2 _3Mn1Gg']/span[text()='Filters']")))
processor_filter = driver.find_element_by_xpath("//div[@class='_1YokD2 _3Mn1Gg']/span[text()='Processor']")
processor_filter.click()
wait.until(ec.visibility_of_element_located((By.XPATH, "//div[@class='_1YokD2 _3Mn1Gg']/span[text()='Core i5']")))
core_i5_filter = driver.find_element_by_xpath("//div[@class='_1YokD2 _3Mn1Gg']/span[text()='Core i5']")
core_i5_filter.click()

laptops = driver.find_elements_by_xpath("//div[@class='_2kHMtA']")
for laptop in laptops:
    name = laptop.find_element_by_xpath(".//a[@class='_1fQZEK']")
    model = laptop.find_element_by_xpath(".//div[@class='_2kHMtA']/ul/li[1]")
    price = laptop.find_element_by_xpath(".//div[@class='_30jeq3 _1_WHN1']")
    ram = laptop.find_element_by_xpath(".//div[@class='_2kHMtA']/ul/li[2]")
    print("Name: ", name.text)
    print("Model: ", model.text)
    print("Price: ", price.text)
    print("RAM: ", ram.text)

product = driver.find_element_by_xpath("//div[@class='_2kHMtA'][1]")
product_name = product.find_element_by_xpath(".//a[@class='_1fQZEK']")
product_name.click()
wait.until(ec.visibility_of_element_located((By.XPATH, "//button[text()='ADD TO CART']")))
add_to_cart = driver.find_element_by_xpath("//button[text()='ADD TO CART']")
add_to_cart.click()

wait.until(ec.visibility_of_element_located((By.XPATH, "//a[@href='/viewcart?otracker=Cart_Icon_Click']")))
cart = driver.find_element_by_xpath("//a[@href='/viewcart?otracker=Cart")
