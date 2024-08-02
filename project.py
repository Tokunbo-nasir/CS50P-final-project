from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import time
import re

#script does not include fully electric cars because they have a different dataset spec sheet
#dev branch created
def input_check(m,mp,mi,y):
    #input error handling 
    make_list =['abarth' ,'ac' ,'aixam' , 'ak', 'alfa romeo','all','alpine', 'alvis', 
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
                    in_milage = input("What is the maximum milage ? e.g (100000): ")
                    in_maxprice = input("What is your maximum budget? e.g(100000): ")
                    in_enginesize = input("What is the maximum engine size? e.g(3.4): ")
                    in_hp = input("Maximum engine power? e.g(500)")
                    in_make = input("Which brand would you like to assess? type all if this isn't required: ").lower()
                    input_check(in_make,in_maxprice,in_milage,in_year,)
                    
                    if in_make == "all":
                        URL2 = f"https://www.autotrader.co.uk/car-search?advertising-location=at_cars&fuel-type=Petrol&fuel-type=Diesel&fuel-type=Petrol%20Plug-in%20Hybrid&fuel-type=Diesel%20Plug-in%20Hybrid&fuel-type=Petrol%20Hybrid&fuel-type=Diesel%20Hybrid&max-engine-power={in_hp}&maximum-badge-engine-size={in_enginesize}&maximum-mileage={in_milage}&moreOptions=visible&postcode=SW1A%201AA&price-to={in_maxprice}&sort=most-recent&year-from={in_year}"
                    else:
                        URL2 = f"https://www.autotrader.co.uk/car-search?advertising-location=at_cars&fuel-type=Petrol&fuel-type=Diesel&fuel-type=Petrol%20Plug-in%20Hybrid&fuel-type=Diesel%20Plug-in%20Hybrid&fuel-type=Petrol%20Hybrid&fuel-type=Diesel%20Hybrid&make={in_make}&max-engine-power={in_hp}&maximum-badge-engine-size={in_enginesize}&maximum-mileage={in_milage}&moreOptions=visible&postcode=SW1A%201AA&price-to={in_maxprice}&sort=most-recent&year-from={in_year}"
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
    counter = 1
    carz =[]
    while counter < 3:
        page = f"{counter}"
        if counter == 1:
            counter += 1
            time.sleep(5)
            source = driver.page_source #source for current page
        else:
            counter += 1
            url = url + "&page=" + page
            driver.get(url)
            time.sleep(5)
            source = driver.page_source #source for second page 
             
        soup = BeautifulSoup(source, "html.parser")
        test = soup.find("ul", {"class" : "at__sc-1iwoe3s-1 dzbHte"}).findAll("li", {"class" :"at__sc-1iwoe3s-2 hGhRgM"}, recursive=False)
        time.sleep(5)

        for i in test:
            empty_dict = dict.fromkeys(['make', 'price', 'year', 'reg', 'body', 'milage', 'enginesize', 'bhp', 'gearbox', 'fueltype', 'doors'])
            make_car = i.find("h3", {"class" : "at__sc-1n64n0d-7 fcDnGr"})
            price_car = i.find("span", {"class" : "at__sc-1mc7cl3-5 edXwbj"})
            rest = i.find_all("li", {"class": "at__sc-1n64n0d-9 hYdVyl"})
            doors_car = i.find("p", {"data-testid" : "search-listing-subtitle"})
            
            # check if all required data is present in the html element if not skip ad
            # the code within the try block only works if the advert has the formmated as such :
            # "2020 (73reg)| SUV | 6,000 miles | 3.0L | 520BHP | automatic | petrol" 
            # additional information which includes the number of car doors e.g " any string 5dr"
            # depending on the car type the values may be different
            if len(rest) < 7:
                print("bad data quality not enough values")
                continue
            else:
                try:
                    #format price
                    p = price_car.get_text()
                    p = int(p.replace("£","").replace(",", ""))
                    
                    #format year and reg month
                    info = rest[0].get_text().split(" ")
                    if len(info) > 1: #error handling in case year and reg are not specified as such 2020 (20 reg)
                        y = int(info[0])
                        r = int(info[1].replace("(","").replace("reg)",""))
                    else:
                        y = int(info[0])
                        r = 0
                    
                    #format milage
                    mi = rest[2].get_text()
                    mi = int(mi.replace(",", "").replace(" miles",""))
                    
                    #format engine size
                    es = float(rest[3].get_text().replace("L", ""))
                    
                    #recalculate brake horse power in if unit PS , reformat string to remove unit text
                    hp = rest[4].get_text()
                    if hp[-2:] == "PS":
                        ps = float(hp.replace("PS",""))
                        hp =  ps * 0.98632
                        hp = round(hp,4)
                    else:
                        hp = float(hp.replace("BHP",""))
                    
                    #format number of car doors 
                    door = doors_car.get_text()
                    try:
                        d = re.search("\ddr", door)
                        d = int(d.group(0).replace("dr", ""))
                    except AttributeError:
                        d = 0
                        continue
                    
                    empty_dict['make'] = make_car.get_text()
                    empty_dict['price'] = p
                    empty_dict['year']= y
                    empty_dict['reg'] = r
                    empty_dict['body']= rest[1].get_text()
                    empty_dict['milage']= mi
                    empty_dict['enginesize']= es
                    empty_dict['bhp']= hp
                    empty_dict['gearbox']= rest[5].get_text()
                    empty_dict['fueltype']= rest[6].get_text()
                    empty_dict['doors']= d
                    
                    carz.append(empty_dict) # append dictionary of each car to carz list
                except ValueError:
                    print("Ad skipped data missing or not in correct order") 
                    # the code within the try block only works if the advert has the formmated as such "2020 (73reg)| SUV | 6,000 miles | 3.0L | 520BHP | automatic | petrol" and -
                    # additional information which inclues the number of car doors e.g " any string 5dr" 
                    continue        
        for i in carz:
            print(i)   


#class cars:
#     def __init__(self, make='', reg = '', year = '', price = '', enginesize= '', fueltype ='', gearbox ='', 
#                  milage ='', hp ='', btype='', doors=''):
#         self.make = make
#         self.reg = reg
#         self.year = year
#         self.price = price 
#         self.enginesize = enginesize
#         self.fueltype = fueltype
#         self.gearbox = gearbox
#         self.milage = milage 
#         self.hp = hp
#         self.btype = btype
#         self.doors = doors

def main():
    URL = userinput()
    scraper(URL)
    
main()