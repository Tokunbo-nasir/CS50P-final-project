from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import time

def input_check(m,mp,mi,y):
    make_list =['abarth' ,'ac' ,'aixam' , 'ak', 'alfa romeo', 'alpine', 'alvis', 
                'ariel', 'aston martin','auburn', 'audi', 'austin', 'bac', 'beauford',
                'bentley', 'bmw', 'bristol', 'bugatti','buick', 'byd','cadillac','caterham',
                'chesil','chevrolet','chrysler','citroen','corvette','cupra','custom vehicle',
                'baeia','dacia','daewoo','daewoo','daihatsu','daihatsu','daimler','datsun',
                'dax','de tomaso','dfsk','dodge','ds automobiles','ferrari','fiat','fiat','fisker',
                'ford','gardner douglas','genesis','gmc','great wall','gwm ora','hillman',
                'honda','hummer','hyundai','ineos','infiniti','isuzu','jaguar','jeep','jensen',
                'kgm','kia','ktm','lada','lamborghini','lancia','land rover','levc','lexus',
                'leyland','ligier','lincoln','lister','locust','london taxis international',
                'lotus','mahindra','marcos','maserati','maxus','maybach','mazda','mclaren',
                'mercedes-benz','mev','mg','microcar','mini','mitsubishi','mitsuoka','mnr','moke',
                'morgan','morris','nardini','ng','nissan','noble','oldsmobile','omoda','opel',
                'pagani','panther','perodua','peugeot','pgo','piaggio','pilgrim','polaris',
                'polestar','pontiac','porsche','proton','radical','rage','rayvolution','rcr',
                'reliant','renault','replica','reva','riley','robin hood','rolls-royce','rover',
                'royale','saab','seat','sebring','shelby','skoda','smart','ssangyong','subaru',
                'sunbeam','suzuki','tesla','tiger','toyota','triumph','tvr','ultima','vauxhall',
                'volkswagen','volvo','westfield','yamaha','zenos']
    if m not in make_list:
        return ValueError
    elif mp.isnumeric() == False:
        return ValueError
    elif mi.isnumeric() == False:
        return ValueError
    elif (y.isnumeric() == False) or (len(y)!= 4):
        return ValueError
    else:
        return True
    
def userinput():
    while True: 
        ans1 = input("Do you want to search all cars with no specifications? (Yes or No)").lower()
        if ans1 == 'yes':
            URL1 = "https://www.autotrader.co.uk/car-search?postcode=SW1A%201AA&sort=year-dsc"
            return URL1
        elif ans1 == 'no':
                try:
                    make = input("Which brand would you like to assess? ").lower()
                    maxprice = input("What is your maximum budget? e.g(100000): ")
                    milage = input("What is the maximum milage ? e.g (100000): ")
                    year = input("What is the minimum year? e.g (2023): ")
                    input_check(make, maxprice, milage, year)
                    URL2 = f"https://www.autotrader.co.uk/car-search?make={make}&maximum-mileage={milage}&postcode=SW1A%201AA&price-to={maxprice}&sort=year-dsc&year-from={year}"
                    return URL2
                except ValueError:
                    print(f"Incorrect entry, please try again")
                    userinput()

def scraper(url):
    '''Use selenium to open a broswer page and click the accept cookies button'''
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    options.add_argument("--disable-webusb")
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    driver = webdriver.Chrome(options=options)
    driver.get(url)
    driver.switch_to.frame("sp_message_iframe_1086457")
    driver.find_element(By.XPATH,"//button[text()='Accept All']").click()
    print(f"hello")
    
    '''Obtain the page source and use as an input for Beautiful soup'''
    source = driver.page_source
    soup = BeautifulSoup(source, "html.parser")
    print(soup)
    #TODO scrape data from page 1 then click page 2 scrape data from page 2
    # x = 1
    # m_list = []
    # for i in range(16):
    #     try:
    #         path = f'/html/body/div[3]/div[1]/main/article/div[2]/ul/li[{x}]/section/div[1]/div/div/section/section/a/h3'
    #         m_list.append(driver.find_element(By.XPATH, path))
    #         x += 1
    #     except NoSuchElementException:
    #         pass
    # print(f"{m_list}")
 
   

def main():
    URL = userinput()
    scraper(URL)
main()