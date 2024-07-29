from selenium import webdriver

def main():
    options = webdriver.ChromeOptions()
    options.add_argument("--disable-webusb")
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    options.add_experimental_option("detach", True)
    driver = webdriver.Chrome(options=options)
    driver.get("https://www.facebook.com/login/")
    
    print(f"working")
    

main()