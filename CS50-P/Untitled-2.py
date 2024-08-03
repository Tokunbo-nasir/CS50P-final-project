
import re

def main():
    counter = 0
    for i in range(5):
        counter += 1
        page = str(counter)
        
        url ="https://www.autotrader.co.uk/car-search?advertising-location=at_cars&fuel-type=Petrol&fuel-type=Diesel&fuel-type=Petrol%20Plug-in%20Hybrid&fuel-type=Diesel%20Plug-in%20Hybrid&fuel-type=Petrol%20Hybrid&fuel-type=Diesel%20Hybrid&max-engine-power=1000&maximum-badge-engine-size=7.0&maximum-mileage=100000&moreOptions=visible&postcode=SW1A%201AA&price-to=100000&sort=most-recent&year-from=1900&page=1"
        pattern = "&page=\d"
        replacement = f"&page={page}"
        url = re.sub(pattern, replacement, url )
        print(url)
main()