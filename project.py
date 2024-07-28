from selenium import webdriver


DRIVER_PATH = 'C:/Users/tokun/Downloads/Compressed/chromedriver-win64/chromedriver-win64'


def input_check(m,mp,mi,y):
make_list = []
    
    
def userinput():
    while True: 
        ans1 = input("Do you want to search all cars with no specifications? (Yes or No)").lower()
        if ans1 == 'yes':
            URL = 'https://www.autotrader.co.uk/search-form?postcode=SW1A%201AA&sort=year-dsc'
            return URL
        elif ans1 == 'no':
                try:
                    make = input("Which brand would you like to assess? ")
                    maxprice = input("What is your maximum budget? e.g(100000): ")
                    milage = input("What is the maximum milage ? e.g (100000): ")
                    year = input("What is the minimum year?: ")
                    check = input_check(make, maxprice, milage, year)
                except ValueError:
                    print(f"Incorrect entry, please try again")
                    userinput()
                    
                

    
    
            
            
            #TODO function to check inputs 
            
        
            
            
                        
            
            
            
            
def main():
    driver = webdriver.Chrome()
    URL = 'https://www.autotrader.co.uk/car-search?advertising-location=at_cars&body-type=Coupe&fuel-consumption=OVER_30&fuel-type=Petrol&make=BMW&max-engine-power=600&maximum-badge-engine-size=4.5&maximum-mileage=45000&min-engine-power=100&minimum-badge-engine-size=1.4&minimum-mileage=10000&moreOptions=visible&postcode=SW1A%201AA&price-from=2500&price-to=40000&radius=20&sort=relevance&transmission=Automatic&year-from=2010&year-to=2019&zero-to-60=4_TO_6&zero-to-60=TO_4'
    response = driver.get(URL)
main()
