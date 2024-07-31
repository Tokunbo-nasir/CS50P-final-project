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
                    in_year = input("What is the minimum year? e.g (2023): ")
                    #in_make = input("Which brand would you like to assess? ").lower()
                    in_milage = input("What is the maximum milage ? e.g (100000): ")
                    in_maxprice = input("What is your maximum budget? e.g(100000): ")
                    in_enginesize = input("What is the maximum engine size? e.g(3.4): ")
                    in_hp = input("Maximum engine power? e.g(500)")
                    input_check(in_year, in_milage, in_maxprice)
                    URL2 = f"https://www.autotrader.co.uk/car-search?fuel-type=Diesel&fuel-type=Petrol%20Plug-in%20Hybrid&fuel-type=Diesel%20Plug-in%20Hybrid&fuel-\
                    type=Petrol%20Hybrid&fuel-type=Diesel%20Hybrid&fuel-type=Petrol&max-engine-power={in_hp}&maximum-badge-engine-size={in_enginesize}&maximum-mileage={in_milage}&\
                    postcode=SW1A%201AA&price-to={in_maxprice}&sort=relevance&year-from={in_year}"
                    
                    return URL2
                except ValueError:
                    print(f"Incorrect entry, please try again")
                    userinput()

class cars:
    def __init__(self, make='', reg = '', year = '', price = '', enginesize= '', fueltype ='', gearbox ='', 
                 milage ='', hp ='', btype='', doors=''):
        self.make = make
        self.reg = reg
        self.year = year
        self.price = price 
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
    
    '''Obtain the page source and use as an input for Beautiful soup'''
    time.sleep(5)
    source = driver.page_source
    soup = BeautifulSoup(source, "html.parser")
    test = soup.find("ul", {"class" : "at__sc-1iwoe3s-1 dzbHte"}).findAll("li", {"class" :"at__sc-1iwoe3s-2 hGhRgM"}, recursive=False)
    time.sleep(5)
    carz =[]
    
    for i in test:
        #empty_dict = dict.fromkeys(['make', 'price', 'year', 'reg', 'btpye', 'milage', 'enginesize', 'hp', 'gearbox', 'fueltype', 'doors'])
        
        #make_car = i.find("h3", {"class" : "at__sc-1n64n0d-7 fcDnGr"})
        #price_car = i.find("span", {"class" : "at__sc-1mc7cl3-5 edXwbj"})
        rest = i.find_all("li", {"class": "at__sc-1n64n0d-9 hYdVyl"})
        for i in rest:
            print(i.get_text())
        
        #empty_dict['make'] = make_car 
        #empty_dict['price'] = price_car
        #empty_dict['year']=
        #empty_dict['reg'] =
        #empty_dict['btpye']=
        #empty_dict['milage']=
        #empty_dict['enginesize']=
        #empty_dict['hp']=
        #empty_dict['gearbox']=
        #empty_dict['fueltype']=
        #empty_dict['doors']=
        #carz.append(empty_dict) # append dictionary of each car to carz list 
    
    #print(carz)
    
    #TODO get all attributes of the cars from the classes
    #TODO if attribute is missing , set it to null 
     
# class cars:
#     def __init__(self, make='',price = '',year = '',reg = '',btpye='',
#                  milage ='',enginesize= '',hp ='',gearbox ='',
#                  fueltype ='', doors=''):
#         self.make = make
#         self.price = price 
#         self.year = year
#         self.reg = reg
#         self.btype = btype
#         self.milage = milage
#         self.enginesize = enginesize
#         self.hp = hp
#         self.gearbox = gearbox
#         self.fueltype = fueltype
#         self.doors = doors     

def main():
    URL = userinput()
    scraper(URL)
main()