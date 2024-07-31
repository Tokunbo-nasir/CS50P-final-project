from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import time
import re

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

class cars:
    def __init__(self, make='', reg = '', year = '', price = '', owners ='', enginesize= '', fueltype ='', gearbox ='', 
                 milage ='', hp ='', btype='', doors=''):
        self.make = make
        self.reg = reg
        self.year = year
        self.price = price 
        self.owners = owners
        self.enginesize = enginesize
        self.fueltype = fueltype
        self.gearbox = gearbox
        self.milage = milage 
        self.hp = hp
        self.btype = btype
        self.doors = doors
        
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
    
    
    #TODO USE LIST TRAVERSAL VIDEO TO ITERATE THROUGH EACH ELEMENT AND CHECK THE NUMBER OF INNER ELEMENTS IF YES ADD TO DICTIONARY 
    '''Obtain the page source and use as an input for Beautiful soup'''
    source = driver.page_source
    soup = BeautifulSoup(source, "html.parser")
    test = soup.find("ul", {"class" : "at__sc-1iwoe3s-1 dzbHte"}).findAll("li", recursive=False)
    for i in test:
        print(i)
    
    #TODO get all attributes of the cars from the classes
    #TODO if attribute is missing , set it to null 
     
class cars:
    def __init__(self, make='',price = '',year = '',reg = '',btype='',
                 milage ='',enginesize= '',hp ='',gearbox ='',
                 fueltype ='',owners='', doors=''):
        self.make = make
        self.price = price 
        self.year = year
        self.reg = reg
        self.btype = btype
        self.milage = milage
        self.enginesize = enginesize
        self.hp = hp
        self.gearbox = gearbox
        self.fueltype = fueltype
        self.owners = owners
        self.doors = doors     

def main():
    URL = userinput()
    scraper(URL)
main()