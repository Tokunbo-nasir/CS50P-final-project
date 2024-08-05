from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from bs4 import BeautifulSoup
import time
import re
import mysql.connector
import os

#Script does not include fully electric cars because they have a different dataset spec sheet
#Autotrader is limited to 100 pages of results.

#All the data is appended to the MySQL database
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
                'sunbeam','suzuki','tiger','toyota','triumph','tvr','ultima','vauxhall',
                'volkswagen','volvo','westfield','yamaha','zenos']
    
def userinput():
    while True: 
        ans1 = input("Do you want to specify the type of car you want? (Yes, No, Semi automated): ").lower()
        if ans1 == 'no':
            URL1 = "https://www.autotrader.co.uk/car-search?postcode=SW1A%201AA&sort=year-dsc&page=1"
            return URL1
        elif ans1 == 'yes':
                try:
                    in_year = input("What is the minimum year? e.g (2023): ")
                    in_milage = input("What is the maximum milage ? e.g (100000): ")
                    in_maxprice = input("What is your maximum budget? e.g(100000): ")
                    in_enginesize = input("What is the maximum engine size? e.g(3.4): ")
                    in_hp = input("Maximum engine power? e.g(500): ")
                    in_make =  input("Which brand would you like to assess? type 'all' if you're not picky: ").lower()
                    input_check(in_make,in_maxprice,in_milage,in_year,)
                    
                    if in_make == "all":
                        URL2 = f"https://www.autotrader.co.uk/car-search?advertising-location=at_cars&fuel-type=Petrol&fuel-type=Diesel&fuel-type=Petrol%20Plug-in%20Hybrid&fuel-type=Diesel%20Plug-in%20Hybrid&fuel-type=Petrol%20Hybrid&fuel-type=Diesel%20Hybrid&max-engine-power={in_hp}&maximum-badge-engine-size={in_enginesize}&maximum-mileage={in_milage}&moreOptions=visible&postcode=SW1A%201AA&price-to={in_maxprice}&sort=most-recent&year-from={in_year}&page=1"
                    else:
                        URL2 = f"https://www.autotrader.co.uk/car-search?advertising-location=at_cars&fuel-type=Petrol&fuel-type=Diesel&fuel-type=Petrol%20Plug-in%20Hybrid&fuel-type=Diesel%20Plug-in%20Hybrid&fuel-type=Petrol%20Hybrid&fuel-type=Diesel%20Hybrid&make={in_make}&max-engine-power={in_hp}&maximum-badge-engine-size={in_enginesize}&maximum-mileage={in_milage}&moreOptions=visible&postcode=SW1A%201AA&price-to={in_maxprice}&sort=most-recent&year-from={in_year}&page=1"
                    make_index += 1
                    return URL2
                except ValueError:
                    print(f"Incorrect entry, please try again")
                    userinput()
        elif ans1 == 'semi automated' or ans1 == 'sa':
            #Run script multiple times to get a 100 pages of adverts for all car brands  
            #Each time "semi-automated" is selected it will move onto the next car brand in the "make_list" list    
            if os.path.exists ("run_counter.txt")  == False:     #check if file that counts how many time script has been run, exists
                with open("run_counter.txt", "w") as mc:
                    mc.write("0")
                    runs = int(mc.read()) 
            else:
                with open("run_counter.txt", "r") as mc:
                    runs = int(mc.read()) #assign variable to show how many times script has been run not including the present execution.
                       
            in_year = '1900' 
            in_milage = '200000' 
            in_maxprice = '2000000' 
            in_enginesize = '7.0' 
            in_hp = '2000' 
            in_make =  make_list[runs] 
            URL3 = f"https://www.autotrader.co.uk/car-search?advertising-location=at_cars&fuel-type=Petrol&fuel-type=Diesel&fuel-type=Petrol%20Plug-in%20Hybrid&fuel-type=Diesel%20Plug-in%20Hybrid&fuel-type=Petrol%20Hybrid&fuel-type=Diesel%20Hybrid&make={in_make}&max-engine-power={in_hp}&maximum-badge-engine-size={in_enginesize}&maximum-mileage={in_milage}&moreOptions=visible&postcode=SW1A%201AA&price-to={in_maxprice}&sort=most-recent&year-from={in_year}&page=1"
    
            runs += 1 #increment runs by 1 and write back to run counter file 
            with open("run_counter.txt", "w") as mc:
                    mc.write(str(runs))
            print(f"current make is: {in_make}")
            return URL3 #return the URL with the changed car make/brand 
            
                    
def input_check(m,mp,mi,y):
    '''Error handling for inputs'''
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

def scraper(url, total):
    '''Use selenium to open a broswer page and click the accept cookies button'''
    #setup the chromedriver
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    options.add_argument("--disable-webusb")
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    driver = webdriver.Chrome(options=options)
    
    #open the genrated url on a chrome browser
    driver.get(url)
    time.sleep(2)
    #switch to an iframe within the html code to be able to click the "accept cookies button"
    driver.switch_to.frame("sp_message_iframe_1086457")
    driver.find_element(By.XPATH,"//button[text()='Accept All']").click() #click accept cookies
    print(f"Hello, data extraction has begun, please wait")
    
    '''Obtain the page source and use as an input for Beautiful soup'''
    counter = 1
    carz =[]
 
    while counter <= total:
        page = str(counter)
        results = 0 #used to keep track of how many adverts have been parsed without error
        if counter == 1:
            counter += 1
            print(f"Parsing page {page}")
            time.sleep(1)
            source = driver.page_source #source for current page
        else:
            counter += 1
            pattern = "&page=\d+"                    # use regex for find part of url string that handles the current page 
            replacement = f"&page={page}"           # replace with the next page 
            url = re.sub(pattern, replacement, url )
            
            print(f"Parsing page {page}")
            driver.get(url)
            time.sleep(1)
            source = driver.page_source #source for consecutive page 
        
        try:
            #create beautiful soup object from source   
            soup = BeautifulSoup(source, "html.parser")
            #Find all adverts based on the html class and tag 
            test = soup.find("ul", {"class" : "at__sc-1iwoe3s-1 dzbHte"}).findAll("li", {"class" :"at__sc-1iwoe3s-2 hGhRgM"}, recursive=False)
            time.sleep(1)
            if len(test) < 2:
                raise TypeError
        except TypeError:  #error handling for when the adverts are no longer on the page
            print ("Final page has been reached")
            break
            

        #loop through each advert on the page 
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
                print("Bad data quality not enough values skipping advert")
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
                    
                    #populate empty dict with details of current advert 
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
                    
                    results += 1
                    # append dictionary of each car to carz list
                    carz.append(empty_dict) 
                except ValueError:
                    print("Ad skipped data missing or not in correct order skipping advert") 
                    # the code within the try block only works if the advert has the formmated as such "2020 (73reg)| SUV | 6,000 miles | 3.0L | 520BHP | automatic | petrol" and -
                    # additional information which inclues the number of car doors e.g " any string 5dr" 
                    continue        
        #print how many succesful adverts were parsed on the page 
        print(f"{results} adverts were extracted on this page")
    
    if len(carz) == 0:
        print("No search results found on autotrader")
    else:
        print(carz)
    return carz

def upload(cl):
    #reformat each dictionary as a list to use as inputs for an insert SQL query 
    #cl stands for "cars_list"
    for i in cl:
        mk = i['make']
        prc = i['price']
        yr = i['year']
        rg = i['reg']
        bdy = i['body']
        mil = i['milage']
        eng = i['enginesize']
        hpw = i['bhp']
        gbx = i['gearbox']
        ful = i['fueltype']
        drs = i['doors']  
        inp_body = [bdy, drs, gbx]
        inp_eng = [eng, ful, hpw]
        inp_car = [mk, rg, yr, prc, mil]
        
        #connect to database
        mydb = mysql.connector.connect(
            host="localhost",
            user="Nasir",
            password="root",
            database="cars"
            )
        #create cursor object for database
        mycursor = mydb.cursor()
        
        #sql insert queries
        sqlbody="INSERT INTO bodyspec(bodytype, doors, gearbox) VALUES(%s, %s, %s)"  
        sqleng="INSERT INTO enginespec(enginesize, fueltype, horsepower) VALUES(%s, %s, %s)" 
        sqlcar ="INSERT INTO carspec(make, reg, year, price, milage) VALUES(%s, %s, %s, %s, %s)"
        
        #execute queries
        mycursor.execute(sqlbody, inp_body)
        mycursor.execute(sqleng, inp_eng)
        mycursor.execute(sqlcar, inp_car)
        
        mydb.commit()
        
        #queries to update foreign keys engine_id & body_id in the carspec table
        sqlup1 = "UPDATE `carspec` JOIN `bodyspec` ON `bodyspec`.`id`=`carspec`.`id` SET `carspec`.`body_id` = `bodyspec`.`id`"
        sqlup2 = "UPDATE `carspec` JOIN `enginespec` ON `enginespec`.`id`=`carspec`.`id` SET `carspec`.`engine_id` = `enginespec`.`id`"
        
        #execute queries
        mycursor.execute(sqlup1)
        mycursor.execute(sqlup2)
        
        mydb.commit()
    results_num = len(cl)    
    print(f"Data succesfully inserted into cars database, {results_num} cars inserted")
    
def main():
    #TODO SET DEFAULT CRITERIA SO SCRIPT CAN RUN AUTOMATICALLY
    URL = userinput()
    p = int(input("How many pages would you like to parse through? e.g 10 (max 100):  "))
    car_list = scraper(URL,p)
    upload(car_list)  
main()

