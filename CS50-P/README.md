# Autotrader webscraper
#### Video Demo:  <URL HERE>
#### Description:
The autotrader webscraper utilises selenium webdriver and beautiful soup.

Please note the "upload" function will not work if a my sql database is not configured on the local host i will also explain this in my video
In this case if the upload function is commented out the results will still be printed 

1) The relevant libraries are imported

from selenium import webdriver 
from selenium.webdriver.common.by import By
from selenium.webdriver.common.by import By 
from bs4 import BeautifulSoup (used to parse through all the html data on a website)
import time (to impleement waits so the elenium web driver has enough time to interact with html elements on the web page )
import re  (for regex o?perationg and string formatting)
import mysql.connector (to upload scraped data to a mysql server)

2) The main function is called

3) The "userinput()" function is called 
3a) Purpose : To obtain  input parameters from the user

3b) A while loop & try/except block is used for error handling of the input

3c) The first question is "Do you want to specify the type of car you want? (Yes or No)"

    Answering no will return a generic URL without any specifications for the autotrader search website with the widest range of specifications.

    Answering yes will prompt the user to answer multiple questions based on the type of car they are looking for, 
    All the user inputs are assigned to  variables, this way the user can narrow down their results.

    "What is the minimum year? e.g (2023): "
    "What is the maximum milage ? e.g (100000): "
    "What is your maximum budget? e.g(100000): "
    "What is the maximum engine size? e.g(3.4): "
    "Maximum engine power? e.g(500): "
    "Which brand would you like to assess? type all if this isn't required: " (this input is converted to lower case)

    Answering "semi-automated" is will automatically populate all the variables with the widest range of specifications.
    It will also select consecutive car brands in the "make_list" by using the "runs" variable. 
    Each time the script is run, and this option "semi-automated" is selected a number in an external "run_counter.txt" file is incremented. 
    This is good if you want the maximum amount of results for each car brand. 

    After all the inputs are entered...

4)The "input_check()" function is called within a try except block which will print "Incorrect entry, please try again" if the function returns a ValueError. In this case the function "userinput()" is called again.

4a) There are 4 inputs for this function m,mp,mi,y representing "make", "max price of the car" , " max milage" , "minimum year".

4b) Witihin the input_check() function, it checks a list called "make_list"  which contains all the car brands/makes on the autotrader website.

4c) Next 4 if & elif statements check the inputs match certain criteria , if the inputs do not they return a ValueError (see explanation in no. 4).

4d) If all the inputs match the criteria the final if statements returns True.


5) Continuing from 3c within the "userinput" function
5a) The user input variables once validated are inserted into the URL using an f string

5b) An if else statement checks if the user selected a specific make/brand of car , if the user typed "all" a different URL is generated.

5c) The generated URL is returned to the "URL" variable in the main function

6) Within the "main" function

6a)The user is asked how many pages of results would they like to parse through on the auto trader website this is assigned to the variable "p"
   The maximum on the website is 100 pages of results 

7) The "scraper" function is called within the main function
7a) Purpose: This take the URL generated in (no. 5) as an argument  and the number of pages "total" (No. 6a) and parses through each advert on each page extracting the required data.

7b) The first 7 lines in the scraper function are used to setup the chrome driver which will automate the use of a chrome browser

7c) "driver.get(url)" is used to  open the generated url (see No. 5) in a chrome browser

7d) A popup asking to accept cookies comes up when open the autotrader website.
    "driver.switch_to.frame" switches to the html element containing the popup
    "driver.find_element(By.XPATH,"//button[text()='Accept All']").click()" clicks the accept button

7e) A message is printed "Hello, data extraction has begun, please wait".

7f) A variable "counter" is declared to keep track of the number of pages to be parsed
    An empty list called "carz" is declared to store a list of dictionaries , with each dictionary containing key value pairs of data for each car.

7g) A variable string "page" is the string version of the integer "counter".

7h) A while loop is declared which loops evrytime a page has been parsed.

    An if else statement which checks if "counter" is zero

    If yes (this is the first page of adverts) "counter" is incremented by 1 and 
    "source = driver.page_source" is a selenium method which makes a copy of all the html code on the website and assigns it to the variable "source"

    If no (this is the 2nd , 3rd, 4th etc page of adverts)  the else statement is triggered "counter" is incremented by one.
   
    The next 4 lines of code use the regular expression / re method called "re.sub" to search for the section of the URL which handles the page number of the adverts ""&page=\d"

    A formatted string with the a new page number "page" (see 7g) replaces the previous page number.

7i) A message is printed "print(f"Parsing page {page}") which shows the number of th current page being parsed.

7j) (No. 7c) is repeated and the page source is assigne dto a variable "source" (See 2nd paragraph in 7h).

7k) A beautiful soup object is created by using the "source" variable as an arguement
    
    Next the "soup.find" method is used to find the parent class of all the car adverts on the page within the html code.

    At the same time the "soup.findall" method is used to find the children of the parent class mentioned above. 

    This will return a list to the variable "test" with each element in the list containing the html code for each car advertised on the current webpage.

    Now we are able to extract data for each car by iterating through the list.

7l) For each element in the "test" list 
    an empty dictionary is declared "empty_dict" with keys for each different car attributes

    the "i.find" method from beautiful soup is used to extract the data for the following:

    make/brand of car , 
    price of the car, 
    a list called "rest" ( which covers the car reg & year, car shape/body, milage, engine size, horspower, gearbox type , fuel type),
    number of doors

    An if/else statement checks the "rest" list to see if the current advert/car has the minimum amount of information required (length of list must be 7) 
    
    if no it will print "Bad data quality not enough values skipping advert" and skip the advert

    if yes(there is enough data in the "rest" list)
 
    A try/ except block is initiated for error handling , if any errors are returned during the data formating "Ad skipped data missing or not in correct order skipping advert" is printed and the advert/car is skipped.

    the code within the try block only works if the advert has the formmated as such :
    "2020 (73reg)| SUV | 6,000 miles | 3.0L | 520BHP | automatic | petrol" 
    additional information which includes the number of car doors e.g " any string 5dr"
    depending on the car type the values may be different

    The extracted data is then reformated in multiple ways.
    
    The data is assigned as values to each key in the "empty_dict"
    The "empty_dict" for the current car/advert is appended to the "carz" list

    This is repeated for each advert/car on the webpage. 

7m) The while loop at (see 7h) restarts for the next webpage till the counter reeaches the number specified by the user 

7n) The list "carz" (see 7f) is returned to the variable in the "main" function called "car_list".

    It contains all the car data from every webpage stored as a  list     of dictionaries , with each dictionary representing 1 car e.g 
    
    carz = [ {'make': 'Land Rover Range Rover Sport', 'price': 94490, 'year': 2023, 'reg': 73, 'body': 'SUV', 'milage': 6373, 'enginesize': 3.0, 'bhp': 542.0, 'gearbox': 'Automatic', 'fueltype': 'Petrol Plug-in Hybrid', 'doors': 5}, {'make': 'Nissan Qashqai', 'price': 18000, 'year': 2022, 'reg': 72, 'body': 'SUV', 'milage': 32249, 'enginesize': 1.3, 'bhp': 138.0, 'gearbox': 'Manual', 'fueltype': 'Petrol Hybrid', 'doors': 5} ]

8) The "upload" function is called within the "main" function

8a) it takes the "car_list" as an arguement and loop through each dictioanry in the list

8b) It assigns each value to a variable 

8c) The "mydb = mysql.connector.connect" is used to connect to a database

8d) All the data for each car is uploaded to the database i created in my CS50SQL project  using SQL code injected into the python script

8e) The statements "sqlup1" & "sqlup2" are used to update the foreign keys within a table in my database.

8f) Once all the data for the cars has been uploaded to teh database "Data succesfully inserted into cars database" is printed.

Thansk for reading 
