from selenium import webdriver

DRIVER_PATH = 'C:/Users/tokun/Downloads/Compressed/chromedriver-win64/chromedriver-win64'


def main():
    driver = webdriver.Chrome()
    URL = 'https://www.autotrader.co.uk/car-search?advertising-location=at_cars&body-type=Coupe&fuel-consumption=OVER_30&fuel-type=Petrol&make=BMW&max-engine-power=600&maximum-badge-engine-size=4.5&maximum-mileage=45000&min-engine-power=100&minimum-badge-engine-size=1.4&minimum-mileage=10000&moreOptions=visible&postcode=SW1A%201AA&price-from=2500&price-to=40000&radius=20&sort=relevance&transmission=Automatic&year-from=2010&year-to=2019&zero-to-60=4_TO_6&zero-to-60=TO_4'
    response = driver.get(URL)
    print(response)
main()
