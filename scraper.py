import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException


def main():
    # Define path for chromedriver executable
    chromedriver = "C:\Users\Kevin Xie\PycharmProjects\quotes\chromedriver\chromedriver.exe"
    os.environ["webdriver.chrome.driver"] = chromedriver

    # Inititalize driver
    global driver
    driver = webdriver.Chrome(chromedriver)

    # Geico scrape
    driver.get("https://sales2.geico.com/internetsales/iSnapPreQuote.xhtml?execution=e1s1&pg=iSnapCustomer")

    # Page 1: Customer
    driver.find_element_by_name("CustomerForm:firstName").send_keys("Joe")

    driver.find_element_by_name("CustomerForm:lastName").send_keys("Smith")

    driver.find_element_by_name("CustomerForm:customerMailingAddress").send_keys("58 Plympton St Cambridge MA")

    zipcode = driver.find_element_by_name("CustomerForm:mailingZip")
    zipcode.send_keys("02138")
    zipcode.send_keys(Keys.RETURN)

    dob_mth = driver.find_element_by_name("CustomerForm:birthMonth")
    dob_mth.send_keys("06")
    dob_mth.send_keys(Keys.RETURN)

    dob_day = driver.find_element_by_name("CustomerForm:birthDay")
    dob_day.send_keys("06")
    dob_day.send_keys(Keys.RETURN)

    dob_yr = driver.find_element_by_name("CustomerForm:birthYear")
    dob_yr.send_keys("1990")
    dob_yr.send_keys(Keys.RETURN)

    unmarried_driver = driver.find_element_by_id("CustomerForm:fqUnmarriedDriver:0")
    unmarried_driver.click()

    driver.find_element_by_id("CustomerForm:continueBtn").click()

    # If taken to the Welcome Back page
    if elementcheck("ProactiveCustomerIdentityForm:forgotPassword"):
        driver.find_element_by_id("ProactiveCustomerIdentityForm:forgotPassword").click()

    # Page 2: Vehicles

    selection("VehicleForm:yearRowTR", "Year", "2009")
    selection("VehicleForm:make", "Make", "ACURA")
    selection("VehicleForm:model", "Model", "MDX AWD")
    selection("VehicleForm:ownership", "Ownership", "O")
    selection("VehicleForm:otherBusiness", "Use", "C")

    selection("VehicleForm:daysDriven", "DaysDriven", "5")
    dailymiles = driver.find_element_by_id("VehicleForm:milesDriven")
    dailymiles.send_keys("20")

    selection("VehicleForm:estimatedMileage", "Mileage", "10000")

    originalowner = driver.find_element_by_id("VehicleForm:numberOwners:0")
    originalowner.click()

    driver.find_element_by_id("VehicleForm:addNo").click()

    # Page 3

    selection("DriverForm:maritalStatus", "MarriedStatus", "S")
    driver.find_element_by_id("DriverForm:gender:0").click()
    selection("DriverForm:curInsComp", "CurrentInsurance", "O")

    driver.find_element_by_id("DriverForm:firstUSLicenseAge").send_keys("18")
    driver.find_element_by_id("DriverForm:fulltimeStudent:0").click()

    driver.find_element_by_id("DriverForm:yearMovedInYear").send_keys("2008")
    driver.find_element_by_id("DriverForm:yearMovedInYear").send_keys(Keys.RETURN)

    driver.find_element_by_id("DriverForm:addNo").click()

    selection("DriverForm:employmentStatus", "MilitaryStatus", "15")
    driver.find_element_by_id("DriverForm:addNo").click()

    # Page 4: Incident Reports
    driver.find_element_by_id("DriHisForm:select:0").click()
    driver.find_element_by_id("DriHisForm:continueBtn").click()

    selection("DriverHistory2Form:incidentType","IncidentType","ACC2")
    driver.find_element_by_id("DriverHistory2Form:atFault:1").click()
    driver.find_element_by_id("DriverHistory2Form:incidentDate").click()
    selection("DriverHistory2Form:incidentDate","IncidentDate","05/01/2012")

    driver.find_element_by_id("DriverHistory2Form:pipPayoutInd:1").click()
    driver.find_element_by_id("DriverHistory2Form:continueBtn").click()

    # No more incidents to report
    driver.find_element_by_id("DriverHistory2Form:continueBtn").click()

    # Page 5: Current Insurance Information

    selection("CurrentInsuranceForm:yearsWithInsComp", "CurrentInsuranceYears", "3")
    selection("CurrentInsuranceForm:currentBodilyInjury", "OBDcoverage", "038")

    driver.find_element_by_id("CurrentInsuranceForm:continueBtn").click()

    # Page 6: Discounts

    driver.find_element_by_id("DiscountsForm:boatCrossSellSelect:1").click()

    driver.find_element_by_id("DiscountsForm:emailAddress").click()
    driver.find_element_by_id("DiscountsForm:emailAddress").send_keys("cs50.autoquote@gmail.com")
    driver.find_element_by_id("DiscountsForm:emailAddress").send_keys(Keys.RETURN)

    driver.find_element_by_id("DiscountsForm:continueBtn").click()



def selection(formid, name, key):
    element = driver.find_element_by_id(formid)
    options = element.find_elements_by_tag_name("option")
    for option in options:
        print(option.get_attribute("value"))
        if option.get_attribute("value") == key:
            option.click()

def elementcheck(formid):
    try:
        driver.find_element_by_id(formid)
    except NoSuchElementException:
        return False
    return True

if __name__ == "__main__":
    main()