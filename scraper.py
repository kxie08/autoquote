import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select


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
    driver.find_element_by_name("CustomerForm:mailingZip").send_keys("02138")
    driver.find_element_by_name("CustomerForm:birthMonth").send_keys("06")
    driver.find_element_by_name("CustomerForm:birthDay").send_keys("06")
    driver.find_element_by_name("CustomerForm:birthYear").send_keys("1990")

    driver.find_element_by_id("CustomerForm:fqUnmarriedDriver:0").click()

    driver.find_element_by_id("CustomerForm:continueBtn").click()

    # If taken to the Welcome Back page
    if elementcheck("ProactiveCustomerIdentityForm:forgotPassword"):
        driver.find_element_by_id("ProactiveCustomerIdentityForm:forgotPassword").click()

    # Page 2: Vehicles

    # to do: create struct of vehicles, vehicle_counts

    # for i in vehicles:

    selection("VehicleForm:yearRowTR", "Year", "2009")
    selection("VehicleForm:make", "Make", "ACURA")
    selection("VehicleForm:model", "Model", "MDX AWD")

    # to do: some cars have a 'body style' form option

    driver.find_element_by_id("VehicleForm:numberOwners:0").click()

    driver.find_element_by_id("VehicleForm:ownership").click()

    # if ownershipstatus == "owned":
    selection("VehicleForm:ownership", "Ownership", "O")

    # elif ownershipstatus == "financed":
    #   selection("VehicleForm:ownership", "Ownership", "F")

    #elif ownershipstatus == "leased":
    #   selection("VehicleForm:ownership", "Ownership", "L")

    # if vehicleusage == "commute":
    selection("VehicleForm:otherBusiness", "Use", "C")
    selection("VehicleForm:daysDriven", "DaysDriven", "5")
    driver.find_element_by_id("VehicleForm:milesDriven").send_keys("20")

    # selection("VehicleForm:estimatedMileage", "Mileage", "10000")

    # elif vehicleusage == "pleasure":
    #   selection("VehicleForm:otherBusiness", "Use", "P")
    #   if mileage >= 0 & mileage =< 2999:
    #       selection("VehicleForm:estimatedMileage", "Mileage", "10000")
    #   elif mileage >= 30000:
    #       selection("VehicleForm:estimatedMileage", "Mileage", "30000")
    #   else:
    #       thousandmiles = str(int(mileage/1000))
    #       selection("VehicleForm:estimatedMileage", "Mileage", thousandmiles)

    # elif vehicleusage == "business":
    #   selection("VehicleForm:otherBusiness", "Use", "B")
    #   selection("VehicleForm:businessrule", "BusinessType", "018")
    #   if mileage >= 0 & mileage = < 2999:
    #       selection("VehicleForm:estimatedMileage", "Mileage", "10000")
    #   elif mileage >= 30000:
    #       selection("VehicleForm:estimatedMileage", "Mileage", "30000")
    #   else:
    #       thousandmiles = str(int(mileage/1000))
    #       selection("VehicleForm:estimatedMileage", "Mileage", thousandmiles)

    driver.find_element_by_id("VehicleForm:addNo").click()
    driver.find_element_by_id("VehicleForm:addNo").click()

    # Page 3

    # loop through struct drivers
    # for i in drivers:

    selection("DriverForm:maritalStatus", "MarriedStatus", "S")
    driver.find_element_by_id("DriverForm:gender:0").click()
    selection("DriverForm:curInsComp", "CurrentInsurance", "O")

    driver.find_element_by_id("DriverForm:firstUSLicenseAge").send_keys("18")

    # if age >= 34: (check if this condition is correct)
    #   if licensed_before_34:
    #       driver.find_element_by_id("DriverForm:drivingExperience:1").click()
    #   else:
    #       driver.find_element_by_id("DriverForm:drivingExperience:0").click()
    #       driver.find_element_by_id("DriverForm:firstUSLicenseAge").send_keys(licenseage)

    # if fulltimestudent:
    driver.find_element_by_id("DriverForm:fulltimeStudent:0").click()

    #   if age >= cutoff: (check for this cutoff)
    #       selection("DriverForm:highestEduLevel", "EduLevel", EduValue)
    #       selection("DriverForm:employmentStatus", "Employment", EmploymentValue)
    #       question: do we want to include military options? could make things more complicated

    #   else:
    driver.find_element_by_id("DriverForm:yearMovedInYear").send_keys("2008")
    driver.find_element_by_id("DriverForm:yearMovedInYear").send_keys(Keys.RETURN)

    driver.find_element_by_id("DriverForm:employmentStatus").click()
    selection("DriverForm:employmentStatus", "MilitaryStatus", "15")

    driver.find_element_by_id("DriverForm:addNo").click()

    # Page 4: Incident Reports

    # if accidents:
    driver.find_element_by_id("DriHisForm:select:0").click()
    driver.find_element_by_id("DriHisForm:continueBtn").click()

    # loop through accidents struct:
    # for i in accidents:
    #   if accidenttype == "accident":
    selection("DriverHistory2Form:incidentType","IncidentType","ACC2")
    driver.find_element_by_id("DriverHistory2Form:atFault:1").click()
    driver.find_element_by_id("DriverHistory2Form:pipPayoutInd:1").click()

    # if accidenttype == "violation":
    #    selection("DriverHistory2Form:incidentType", "IncidentType", "CVI")
    #    selection("DriverHistory2Form:convictionDescription", "ViolationType", violationtype)
    #    selection("DriverHistory2Form:DriverHistory2Form:incidentDate", "ViolationDate", violationdaterange)

    selection("DriverHistory2Form:incidentDate","IncidentDate","05/01/2012")

    driver.find_element_by_id("DriverHistory2Form:continueBtn").click()

    # No more incidents to report
    driver.find_element_by_id("DriverHistory2Form:continueBtn").click()

    # if not accidents:
    # driver.find_element_by_id("DriHisForm:select:1").click()

    # Page 5: Current Insurance Information

    # if currentlyinsured:
    selection("CurrentInsuranceForm:yearsWithInsComp", "CurrentInsuranceYears", "3")
    selection("CurrentInsuranceForm:currentBodilyInjury", "OBDcoverage", "038")

    driver.find_element_by_id("CurrentInsuranceForm:continueBtn").click()

    # Page 6: Discounts

    driver.find_element_by_id("DiscountsForm:boatCrossSellSelect:1").click()

    driver.find_element_by_id("DiscountsForm:emailAddress").click()
    driver.find_element_by_id("DiscountsForm:emailAddress").send_keys("cs50.autoquote@gmail.com")
    driver.find_element_by_id("DiscountsForm:emailAddress").send_keys(Keys.RETURN)

    driver.find_element_by_id("DiscountsForm:continueBtn").click()

    # Page 7: Scrape Results

    dollars = driver.find_element_by_class_name("amount").text
    cents = driver.find_element_by_class_name("cents").text
    payment = dollars + "." + cents

    optional_bi_value = Select(driver.find_element_by_id("CoveragesForm:limit_deductible_P_001_01_1")).first_selected_option
    optional_bi = optional_bi_value.text

    propertydamage_liability = Select(driver.find_element_by_id("CoveragesForm:limit_deductible_P_002_02_1")).first_selected_option
    pdi = propertydamage_liability.text

    personal_injury = Select(driver.find_element_by_id("CoveragesForm:limit_deductible_P_018_03_1")).first_selected_option
    pip = personal_injury.text

    medical_payments = Select(driver.find_element_by_id("CoveragesForm:limit_deductible_P_003_04_1")).first_selected_option

    if medical_payments.text == "I decline":
        med = "$0"
    else:
        med = medical_payments.text

    uninsured_motorist = Select(driver.find_element_by_id("CoveragesForm:limit_deductible_P_004_05_1")).first_selected_option
    uninsured_cov = uninsured_motorist.text

    underinsured_motorist = Select(driver.find_element_by_id("CoveragesForm:limit_deductible_P_089_06_1")).first_selected_option
    underinsured_cov = underinsured_motorist.text

    print("Monthly payment is ${}".format(payment))
    print("Optional bodily injury liability is {}".format(optional_bi))
    print("Property damage liabiliy is {}".format(pdi))
    print("Personal injury protection is {}".format(pip))
    print("Medical payments are {}".format(med))
    print("Uninsured motorist coverage is {}".format(uninsured_cov))
    print("Underinsured motorist coverage is {}".format(underinsured_cov))

def selection(formid, name, key):
    try:
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, formid))
        )
    finally:
        print("Can't find element {}!".format(formid))

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