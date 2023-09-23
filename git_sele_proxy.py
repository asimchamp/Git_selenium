from selenium import webdriver
from seleniumwire import webdriver
from selenium.webdriver.common.by import By
from pynput.keyboard import Key, Controller
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
import time
import string
from selenium.webdriver.support import expected_conditions as EC
from pyotp import *
from fake_useragent import UserAgent

# Selenium Wire configuration to use a proxy
proxy_username = 'vensthuj'
proxy_password = '283q0te0irs6'
seleniumwire_options = {
    'proxy': {
        'http': f'http://{proxy_username}:{proxy_password}@185.199.228.220:7300',
        'verify_ssl': False,
    },
}

ua = UserAgent()
user_agent = ua.random
print(user_agent)
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
options.add_argument("--disable-blink-features=AutomationControlled")
options.add_argument(f'user-agent={user_agent}')
options.add_experimental_option("useAutomationExtension", "false")
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.binary_location = 'D:\\a\\Git_selenium\\Git_selenium\\chrome-win64\\chrome.exe'
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),
                          options=options, seleniumwire_options=seleniumwire_options)

url1 = 'https://etsy.me/44UNXIY '
url2 = 'https://temp-mail.plus'
name = ''.join(random.choices(string.ascii_lowercase, k=7))
pincode = '110043'
city = 'Delhi'
phone1 = '997'
phone2 = ''.join(random.choices(string.digits, k=7))
phone = (phone1 + phone2)
ifsc = 'HDFC0000362'
bank_act1 = '510223'
bank_act2 = ''.join(random.choices(string.digits, k=7))
bank_act = (bank_act1 + bank_act2)
upi_id = 'yameenalmeer@oksbi'
pan1 = 'CUKPA'
pan2 = ''.join(random.choices(string.digits, k=4))
pan3 = 'C'
address = (pan2 + ' ' + name + ' ' + name)
shop_name_var = (name + pan2)
pan = (pan1 + pan2 + pan3)
file_path = 'D:\\a\\Git_selenium\\Git_selenium\\pic1.png'
password = 'Tatabirlaji@1'

wait = WebDriverWait(driver, 300)

driver.get(url1)
time.sleep(1)
driver.maximize_window()
time.sleep(1)

try:
    print('Performing Privacy Function of Urope')
    accept_privacy = WebDriverWait(driver, 5).until(EC.element_to_be_clickable(
        (By.XPATH, '/html/body/div[7]/div[2]/div/div[2]/div/div[2]/div[2]/button')))
    accept_privacy.click()
    time.sleep(1)
    sign_up = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="content"]/div[1]/button')))
    sign_up.click()
    time.sleep(3)

except TimeoutException:
    print('Non UK region')
    sign_up = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="content"]/div[1]/button')))
    sign_up.click()
    time.sleep(3)

####################### All temp mail Function #####################
####################### Gmailator Function #########################
def gmaillator_open():

    try:
        print('Urope temp mail Confirm')
        temp_mail_consent = WebDriverWait(driver, 5).until(EC.element_to_be_clickable(
            (By.XPATH,
             '/html/body/div[3]/div[2]/div[1]/div[2]/div[2]/button[1]/p')))
        temp_mail_consent.click()
        time.sleep(1)

    except TimeoutException:
        print('No Consent found')
        time.sleep(1)

    un_tick_gmail_plus = wait.until(EC.visibility_of_element_located(
        (By.XPATH, '/html/body/div[1]/div/main/div[1]/div/div/div/div[2]/div/div[4]/div[2]/input')))
    un_tick_gmail_plus.click()
    time.sleep(1)

    un_tick_gmail = wait.until(EC.visibility_of_element_located(
        (By.XPATH, '/html/body/div[1]/div/main/div[1]/div/div/div/div[2]/div/div[4]/div[3]/input')))
    un_tick_gmail.click()
    time.sleep(1)

    un_tick_googlemail = wait.until(EC.visibility_of_element_located(
        (By.XPATH, '/html/body/div[1]/div/main/div[1]/div/div/div/div[2]/div/div[4]/div[4]/input')))
    un_tick_googlemail.click()
    time.sleep(1)

    generate_new_mail = wait.until(EC.visibility_of_element_located(
        (By.XPATH, '/html/body/div[1]/div/main/div[1]/div/div/div/div[2]/div/div[5]/div/button')))
    generate_new_mail.click()
    time.sleep(2)

    pick_new_mail = wait.until(EC.visibility_of_element_located(
        (By.XPATH, '/html/body/div[1]/div/main/div[1]/div/div/div/div[2]/div/div[3]/button')))
    pick_new_mail.click()
    time.sleep(1)

    temp_mailp = wait.until(EC.visibility_of_element_located(
        (By.XPATH, '/html/body/div[1]/div/section/div/div/div[3]/div/div[1]/button[1]')))
    temp_mailp.click()
    time.sleep(1)

# Temp Mail Confirm Function
def gmaillator_confirm():
    # Switch to the new tab
    driver.switch_to.window(driver.window_handles[1])
    time.sleep(1)

    time.sleep(5)

    temp_mail_reload = wait.until(
        EC.visibility_of_element_located(
            (By.XPATH, '/html/body/div[1]/div/section/div/div/div[3]/div/div[2]/div[1]/div[2]/button')))
    temp_mail_reload.click()

    time.sleep(5)

    temp_mail_confirm = wait.until(
        EC.visibility_of_element_located((By.XPATH, '//td[text()="Confirm your Etsy account"]')))
    temp_mail_confirm.click()
    time.sleep(1)

    try:
        print('temp mail Checking ads')
        ads_close1 = WebDriverWait(driver, 3).until(EC.element_to_be_clickable(
            (By.XPATH, '/html/body/div/div/div[1]/div[1]/div/svg')))
        ads_close1.click()

    except TimeoutException:
        print('No ads found to close')
        time.sleep(3)

    try:
        print('first ad not found checking second ad')
        ads_close2 = WebDriverWait(driver, 3).until(EC.element_to_be_clickable(
            (By.XPATH, '/html/body/div[1]/div[2]/div[2]/div/div/div[2]/div/div/div[3]')))
        ads_close2.click()

    except TimeoutException:
        print('Second ad also not found')
        time.sleep(3)

    confirm_url_link = wait.until(EC.visibility_of_element_located(
        (By.XPATH,
         '/html/body/div[1]/div/section/div/div/div[3]/div/div/div[2]/div/div/table/tbody/tr[3]/th/table/tbody/tr/td/table/tbody/tr/td/div[1]/table/tbody/tr/td/div/a'))).get_attribute(
        'href')

    print("Temp mail is = " + confirm_url_link)

    # Open a new tab
    driver.execute_script("window.open('', '_blank');")
    time.sleep(1)

    # Switch to the new tab
    driver.switch_to.window(driver.window_handles[2])
    time.sleep(1)

    # Navigate to a website in the new tab
    driver.get(confirm_url_link)
    time.sleep(5)

    # Switch to the new tab
    driver.switch_to.window(driver.window_handles[0])
    time.sleep(1)

####################### Gmailator Function #########################
###################### Temp Mail plus ################

def temp_plus_copy():

    # Consent Checking
    time.sleep(1)
    try:
        print('Checking Urope Consent in Temp mail Plus')
        temp_mail_plus_consent = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, '//p[contains(text(), "Consent")]')))
        temp_mail_plus_consent.click()
        time.sleep(1)

    except TimeoutException:
        print('No Consent found in Temp Mail Plus')
        time.sleep(1)

    # Cookie Checking
    try:
        print('Checking Cookiie in temp mail')
        temp_mail_plus_cookie = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, '//button[contains(text(), "Allow cookies")]')))
        temp_mail_plus_cookie.click()
        time.sleep(2)

    except TimeoutException:
        print('No Cookie found in Temp Mail Plus')
        time.sleep(10)

    copy_temp_mail = wait.until(EC.visibility_of_element_located(
        (By.XPATH, '/html/body/section[1]/div[2]/div/div/div[1]/div[1]/button')))
    copy_temp_mail.click()
    time.sleep(1)

def tempmail_plus_confirm():
    # Switch to the new tab
    driver.switch_to.window(driver.window_handles[1])
    time.sleep(1)

    driver.find_element(by=By.TAG_NAME, value="body").send_keys(Keys.PAGE_DOWN)

    time.sleep(3)

    temp_plus_open = wait.until(
        EC.visibility_of_element_located((By.XPATH, '/html/body/section[2]/div/div[1]/div[2]/div/div[2]/div[2]/div[1]/div/div[3]/a')))
    temp_plus_open.click()

    time.sleep(1)

    driver.find_element(by=By.TAG_NAME, value="body").send_keys(Keys.PAGE_DOWN)
    time.sleep(1)

    temp_plus_confirm = wait.until(
        EC.visibility_of_element_located((By.XPATH, '//span[contains(text(), "Confirm your Etsy account")]')))
    temp_plus_confirm.click()

    time.sleep(2)

    act = ActionChains(driver)
    act.send_keys(Keys.TAB).perform()
    time.sleep(1)
    act.send_keys(Keys.TAB).perform()
    time.sleep(1)
    act.send_keys(Keys.ENTER).perform()
    time.sleep(1)

    # Switch to the new tab
    driver.switch_to.window(driver.window_handles[2])
    time.sleep(2)

    # Navigate to a website in the new tab
    driver.switch_to.window(driver.window_handles[0])
    time.sleep(1)


####################### All temp mail Function #####################

# Open a new tab
driver.execute_script("window.open('', '_blank');")
time.sleep(1)

# Switch to the new tab
driver.switch_to.window(driver.window_handles[1])
time.sleep(1)

# Navigate to a website in the new tab
driver.get(url2)

if url2 == "https://www.emailnator.com":
    # Code to execute if url is equal to "https://url1.com"
    print("Emailnator function run")
    gmaillator_open()

elif url2 == "https://temp-mail.plus":
    # Code to execute if url is equal to "https://url2.com"
    print("tmailor mail function run")
    temp_plus_copy()

elif url2 == "https://url3.com":
    # Code to execute if url is equal to "https://url3.com"
    print("This is URL 3")

else:
    # Code to execute if url doesn't match any of the above conditions
    print("This is an unknown URL")

# Switch to the first tab
driver.switch_to.window(driver.window_handles[0])
time.sleep(1)

# paste temp mail
paste_mail = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="join_neu_email_field"]')))
# Pasting the copied sentence into the input_area
paste_mail.click()
paste_mail.send_keys(Keys.SHIFT, Keys.INSERT)
time.sleep(1.5)

# Click Continue
click_continue = wait.until(
    EC.visibility_of_element_located((By.XPATH, '//*[@id="join-neu-form"]/div[1]/div/div[5]/div/button')))
click_continue.click()
time.sleep(2)

# etsy name
etsy_name = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="join_neu_first_name_field"]')))
etsy_name.send_keys(name)
time.sleep(2.7)

# etsy password
etsy_pass = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="join_neu_password_field"]')))
etsy_pass.send_keys(password)
time.sleep(2.2)

# etsy register

try:
    print('Urope Register function')
    urope_register = WebDriverWait(driver, 5).until(EC.element_to_be_clickable(
        (By.XPATH, '/html/body/div[7]/div[2]/div/div[5]/div/div/div/div/div/div[2]/form/div[2]/div/div[7]/div/button')))
    urope_register.click()
    time.sleep(1)

except TimeoutException:
    print('Non UK region Register')
    etsy_reg = wait.until(
        EC.visibility_of_element_located((By.XPATH, '//*[@id="join-neu-form"]/div[2]/div/div[6]/div/button')))
    etsy_reg.click()
    time.sleep(5)

print("Welcome to ETSY")
# Welcome ETSY
let_do_it = wait.until(
    EC.visibility_of_element_located((By.XPATH, '//*[@id="content"]/div/div/div/div[3]/div/div[2]/div/div/a/div')))
let_do_it.click()

# skip_question1
skip_ques1 = wait.until(EC.visibility_of_element_located(
    (By.XPATH, '//*[@id="content"]/div/div/div/div[3]/div/div[2]/div/div/div/div/a[2]')))
skip_ques1.click()
time.sleep(1)

# skip_question2
skip_ques2 = wait.until(EC.visibility_of_element_located(
    (By.XPATH, '//*[@id="content"]/div/div/div/div[3]/div/div[2]/div/div/div/div/a[1]')))
skip_ques2.click()
time.sleep(1)

# start_shop
start_shop = wait.until(
    EC.visibility_of_element_located((By.XPATH, '//*[@id="content"]/div/div/div/div[3]/div/div[2]/div/div/div/a')))
start_shop.click()
time.sleep(1)

print("Shop Preferences")
### Shop preferences

# Shop language

shop_lang_click = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="onboard-shop-language"]')))
shop_lang_click.click()

shop_lang_select = wait.until(
    EC.visibility_of_element_located((By.XPATH, '//*[@id="onboard-shop-language"]/optgroup/option[2]')))
shop_lang_select.click()
time.sleep(1)

# Shop country

shop_cont_click = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="address-country"]')))
shop_cont_click.click()

shop_cont_select = wait.until(EC.visibility_of_element_located((By.XPATH,
                                                                '/html/body/div[4]/div[2]/div/div/div[2]/div[2]/div/div/div/div[2]/div[2]/div/div/select/optgroup[2]//option[contains(@value, "122") and text() = "India"]')))
shop_cont_select.click()
time.sleep(1)

# Shop currency

shop_curr_click = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="onboard-shop-currency"]')))
shop_curr_click.click()

shop_curr_select = wait.until(
    EC.visibility_of_element_located((By.XPATH, '//*[@id="onboard-shop-currency"]/optgroup[2]/option[3]')))
shop_curr_select.click()
time.sleep(1)

# Save and continue

save_cont_1 = wait.until(
    EC.visibility_of_element_located((By.XPATH, '//*[@id="content"]/div[3]/div[4]/div/div[1]/button')))
save_cont_1.click()

### Shop Name

shop_name = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="onboarding-shop-name-input"]')))
shop_name.send_keys(shop_name_var)
time.sleep(1)

save_cont_2 = wait.until(
    EC.visibility_of_element_located((By.XPATH, '//*[@id="content"]/div[3]/div[4]/div/div[1]/button')))
save_cont_2.click()
time.sleep(1)

### Create a listing

# upload photo
# to identify element
list_upload_pic = wait.until(EC.visibility_of_element_located((By.XPATH,
                                                               '/html/body/div[4]/div[2]/section/div/div[4]/div/div/div/div[2]/div/div/div/div[3]/div/div/div[2]/div[2]/div[2]/div/div[1]/div/form')))
list_upload_pic.click()

time.sleep(2)

# Simulate keyboard input to type the file path and press Enter
keyboard = Controller()
keyboard.type(file_path)
time.sleep(1)
keyboard.press(Key.enter)
keyboard.release(Key.enter)

time.sleep(2)

# Title
list_title = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="title-input"]')))
list_title.send_keys(name + ' ' + name)
time.sleep(1)

### About Listing

# How Made it
made_click = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="who_made-input"]')))
made_click.click()

made_select = wait.until(
    EC.visibility_of_element_located((By.XPATH, '//*[@id="who_made-input"]/optgroup/option[1]')))
made_select.click()
time.sleep(1)

# What is IT
what_click = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="is_supply-input"]')))
what_click.click()

what_select = wait.until(
    EC.visibility_of_element_located((By.XPATH, '//*[@id="is_supply-input"]/optgroup/option[1]')))
what_select.click()
time.sleep(1)

# When Did
when_click = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="when_made-input"]')))
when_click.click()

when_select = wait.until(
    EC.visibility_of_element_located((By.XPATH, '//*[@id="when_made-input"]/optgroup[2]/option[1]')))
when_select.click()
time.sleep(1)

# Category
category_name = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="taxonomy-search"]')))
category_name.send_keys("Gemstone")
time.sleep(3)
category_name.send_keys(Keys.ENTER)
time.sleep(1)

# Description
list_desc = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="description-text-area-input"]')))
list_desc.send_keys(name + ' ' + name)
time.sleep(1)

# Price
list_price1 = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="price_retail_csp-input"]')))
list_price1.send_keys('100')

list_price2 = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="price_retail-input"]')))
list_price2.send_keys('100')

### Delivery

# Delivery options

list_cont_orig_select = wait.until(
    EC.visibility_of_element_located((By.XPATH, '//*[@id="shipping_country"]/optgroup[1]/option[6]')))
list_cont_orig_select.click()
time.sleep(1)

# Origin PIN code
list_ship_pin = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="origin_postal_code"]')))
list_ship_pin.send_keys(pincode)
time.sleep(1)

## Processing Time
# process Time
process_tine_click = wait.until(EC.visibility_of_element_located((By.XPATH,
                                                                  '/html/body/div[4]/div[2]/section/div/div[4]/div/div/div/div[2]/div/div/div/div[12]/div/div/div[1]/div/div/div[1]/div[3]/div/div[2]/div/div[2]/div/div[1]/div[3]/div/div[2]/div')))
process_tine_click.click()

process_tine_select = wait.until(EC.visibility_of_element_located((By.XPATH,
                                                                   '/html/body/div[4]/div[2]/section/div/div[4]/div/div/div/div[2]/div/div/div/div[12]/div/div/div[1]/div/div/div[1]/div[3]/div/div[2]/div/div[2]/div/div[1]/div[3]/div/div[2]/div/div/select/option[3]')))
process_tine_select.click()

driver.find_element(by=By.TAG_NAME, value="body").send_keys(Keys.ESCAPE)
time.sleep(1)
driver.find_element(by=By.TAG_NAME, value="body").send_keys(Keys.PAGE_DOWN)
time.sleep(1)

# Delivery service India
delivery_tine_ind_click = wait.until(EC.visibility_of_element_located((By.XPATH,
                                                                       '/html/body/div[4]/div[2]/section/div/div[4]/div/div/div/div[2]/div/div/div/div[12]/div/div/div[1]/div/div/div[1]/div[3]/div/div[2]/div/div[2]/div/div[1]/div[4]/div[2]/div[1]/div[1]/div[2]/div[1]/div/div/div[1]/div/div[2]')))
delivery_tine_ind_click.click()

delivery_tine_ind_select = wait.until(EC.visibility_of_element_located((By.XPATH,
                                                                        '/html/body/div[4]/div[2]/section/div/div[4]/div/div/div/div[2]/div/div/div/div[12]/div/div/div[1]/div/div/div[1]/div[3]/div/div[2]/div/div[2]/div/div[1]/div[4]/div[2]/div[1]/div[1]/div[2]/div[1]/div/div/div[1]/div/div[2]/div/select/optgroup[1]/option[1]')))
delivery_tine_ind_select.click()

driver.find_element(by=By.TAG_NAME, value="body").send_keys(Keys.ESCAPE)
time.sleep(1)

# Delivery service Other
delivery_tine_oth_click = wait.until(EC.visibility_of_element_located((By.XPATH,
                                                                       '/html/body/div[4]/div[2]/section/div/div[4]/div/div/div/div[2]/div/div/div/div[12]/div/div/div[1]/div/div/div[1]/div[3]/div/div[2]/div/div[2]/div/div[1]/div[4]/div[2]/div[1]/div[2]/div[2]/div[1]/div/div/div[1]/div/div[2]')))
delivery_tine_oth_click.click()

delivery_tine_oth_select = wait.until(EC.visibility_of_element_located((By.XPATH,
                                                                        '/html/body/div[4]/div[2]/section/div/div[4]/div/div/div/div[2]/div/div/div/div[12]/div/div/div[1]/div/div/div[1]/div[3]/div/div[2]/div/div[2]/div/div[1]/div[4]/div[2]/div[1]/div[2]/div[2]/div[1]/div/div/div[1]/div/div[2]/div/select/optgroup[1]/option')))
delivery_tine_oth_select.click()

driver.find_element(by=By.TAG_NAME, value="body").send_keys(Keys.ESCAPE)
time.sleep(1)

# Save and continue Need to double check
save_cont_3 = wait.until(EC.visibility_of_element_located(
    (By.XPATH, '//*[@id="page-region"]/div/div/div[3]/div/div[1]/div/div/div[2]/button[2]')))
save_cont_3.click()
time.sleep(1)

# Do this later
list_later_click = wait.until(
    EC.visibility_of_element_located((By.XPATH, '//*[@id="content"]/div[3]/div[3]/div/div[1]/div/a[1]')))
list_later_click.click()
time.sleep(1)

# How You will paid.
time.sleep(1)


def paid_first():
    # Region select to india

    tell_street_regi_select = wait.until(EC.visibility_of_element_located((By.XPATH,
                                                                           '/html/body/div[4]/div[16]/div[1]/div/div[2]/div[3]/div/div/div[2]/div[3]/select/optgroup/option[17]')))
    tell_street_regi_select.click()

    tell_street_regi_exit = wait.until(EC.visibility_of_element_located(
        (By.XPATH, '/html/body/div[4]/div[16]/div[1]/div/div[2]/div[3]/div/div/div[2]/div[1]')))
    tell_street_regi_exit.click()

    driver.find_element(by=By.TAG_NAME, value="body").send_keys(Keys.PAGE_DOWN)
    time.sleep(1)

    # Residence select to india
    tell_street_residence = wait.until(EC.visibility_of_element_located(
        (By.XPATH, '/html/body/div[4]/div[16]/div[1]/div/div[2]/div[5]/div[2]/div[1]/div[2]/div[2]/div')))
    tell_street_residence.click()

    tell_street_resid_select = wait.until(EC.visibility_of_element_located((By.XPATH,
                                                                            '/html/body/div[4]/div[16]/div[1]/div/div[2]/div[5]/div[2]/div[1]/div[2]/div[2]/div/select/optgroup[2]/option[17]')))
    tell_street_resid_select.click()

    tell_street_resid_exit = wait.until(EC.visibility_of_element_located(
        (By.XPATH, '/html/body/div[4]/div[16]/div[1]/div/div[2]/div[5]/div[2]/div[1]/div[2]/div[1]/label')))
    tell_street_resid_exit.click()
    time.sleep(1)

    # First Name
    tell_first_name = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="identity-first-name"]')))
    tell_first_name.send_keys(name)
    time.sleep(1)

    # Last Name
    tell_last_name = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="identity-last-name"]')))
    tell_last_name.send_keys(name)
    time.sleep(1)

    # DOB
    dob_day_click = wait.until(EC.visibility_of_element_located(
        (By.XPATH, '/html/body/div[4]/div[16]/div[1]/div/div[2]/div[5]/div[2]/div[1]/fieldset[1]/div[2]/div[1]')))
    dob_day_click.click()

    dob_day_submit = wait.until(EC.visibility_of_element_located((By.XPATH,
                                                                  '/html/body/div[4]/div[16]/div[1]/div/div[2]/div[5]/div[2]/div[1]/fieldset[1]/div[2]/div[1]/select/option[9]')))
    dob_day_submit.click()

    dob_mon_click = wait.until(EC.visibility_of_element_located(
        (By.XPATH, '/html/body/div[4]/div[16]/div[1]/div/div[2]/div[5]/div[2]/div[1]/fieldset[1]/div[2]/div[2]')))
    dob_mon_click.click()

    dob_mon_submit = wait.until(EC.visibility_of_element_located((By.XPATH,
                                                                  '/html/body/div[4]/div[16]/div[1]/div/div[2]/div[5]/div[2]/div[1]/fieldset[1]/div[2]/div[2]/select/option[8]')))
    dob_mon_submit.click()

    dob_yer_click = wait.until(EC.visibility_of_element_located(
        (By.XPATH, '/html/body/div[4]/div[16]/div[1]/div/div[2]/div[5]/div[2]/div[1]/fieldset[1]/div[2]/div[3]')))
    dob_yer_click.click()

    dob_yer_submit = wait.until(EC.visibility_of_element_located((By.XPATH,
                                                                  '/html/body/div[4]/div[16]/div[1]/div/div[2]/div[5]/div[2]/div[1]/fieldset[1]/div[2]/div[3]/select/option[34]')))
    dob_yer_submit.click()

    # Pan Card
    tell_pan_card = wait.until(EC.visibility_of_element_located(
        (By.XPATH, '/html/body/div[4]/div[16]/div[1]/div/div[2]/div[5]/div[2]/div[1]/div[14]/div[2]/div/input')))
    tell_pan_card.click()
    tell_pan_card.send_keys(pan)
    time.sleep(1)

    # Nationality select to india
    tell_street_national = wait.until(EC.visibility_of_element_located(
        (By.XPATH, '/html/body/div[4]/div[16]/div[1]/div/div[2]/div[5]/div[2]/div[1]/div[16]/div[2]/div')))
    tell_street_national.click()

    tell_street_national_select = wait.until(EC.visibility_of_element_located((By.XPATH,
                                                                               '/html/body/div[4]/div[16]/div[1]/div/div[2]/div[5]/div[2]/div[1]/div[16]/div[2]/div/select/option[102]')))
    tell_street_national_select.click()

    tell_street_national_exit = wait.until(EC.visibility_of_element_located(
        (By.XPATH, '/html/body/div[4]/div[16]/div[1]/div/div[2]/div[5]/div[2]/div[1]/div[16]/div[1]/label')))
    tell_street_national_exit.click()
    time.sleep(1)

    # Taxpayer address
    # Street address
    tell_street_add = wait.until(EC.visibility_of_element_located((By.XPATH,
                                                                   '/html/body/div[4]/div[16]/div[1]/div/div[2]/div[5]/div[2]/div[1]/fieldset[2]/div/div[2]/div[2]/div/input')))
    tell_street_add.send_keys(address)
    time.sleep(1)

    tell_street_city = wait.until(EC.visibility_of_element_located((By.XPATH,
                                                                    '/html/body/div[4]/div[16]/div[1]/div/div[2]/div[5]/div[2]/div[1]/fieldset[2]/div/div[2]/div[4]/div/input')))
    tell_street_city.click()
    tell_street_city.send_keys(city)
    time.sleep(1)

    tell_street_pin = wait.until(EC.visibility_of_element_located((By.XPATH,
                                                                   '/html/body/div[4]/div[16]/div[1]/div/div[2]/div[5]/div[2]/div[1]/fieldset[2]/div/div[2]/div[5]/div[1]/input')))
    tell_street_pin.click()
    tell_street_pin.send_keys(pincode)
    time.sleep(1)

    tell_street_phone = wait.until(EC.visibility_of_element_located((By.XPATH,
                                                                     '/html/body/div[4]/div[16]/div[1]/div/div[2]/div[5]/div[2]/div[1]/fieldset[2]/div/div[2]/div[6]/div/input')))
    tell_street_phone.send_keys(phone)
    time.sleep(1)

    tell_street_state = wait.until(EC.visibility_of_element_located((By.XPATH,
                                                                     '/html/body/div[4]/div[16]/div[1]/div/div[2]/div[5]/div[2]/div[1]/fieldset[2]/div/div[2]/div[5]/div[2]/div/div[1]')))
    tell_street_state.click()

    tell_street_select = wait.until(EC.visibility_of_element_located((By.XPATH,
                                                                      '/html/body/div[4]/div[16]/div[1]/div/div[2]/div[5]/div[2]/div[1]/fieldset[2]/div/div[2]/div[5]/div[2]/div/div[1]/select/option[11]')))
    tell_street_select.click()

    tell_street_exit = wait.until(EC.visibility_of_element_located((By.XPATH,
                                                                    '/html/body/div[4]/div[16]/div[1]/div/div[2]/div[5]/div[2]/div[1]/fieldset[2]/div/div[2]/div[5]/div[2]/div/label')))
    tell_street_exit.click()

    driver.find_element(by=By.TAG_NAME, value="body").send_keys(Keys.PAGE_DOWN)
    time.sleep(1)

    # In the past 10 years
    tell_ten_years_click = wait.until(EC.visibility_of_element_located(
        (By.XPATH, '//*[@id="content"]/div[16]/div[1]/div/div[2]/div[8]/div[2]/div[2]/fieldset/div/div[2]/label')))
    tell_ten_years_click.click()

    time.sleep(1)

    # Your bank information
    tell_ifsc = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="bank-bank-code"]')))
    tell_ifsc.send_keys(ifsc)
    time.sleep(1)

    tell_bank_acct = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="bank-account-number"]')))
    tell_bank_acct.send_keys(bank_act)
    time.sleep(1)

    driver.find_element(by=By.TAG_NAME, value="body").send_keys(Keys.PAGE_DOWN)
    time.sleep(1)

    # PayPal Account
    paypal_click = wait.until(EC.visibility_of_element_located(
        (By.XPATH, '/html/body/div[4]/div[16]/div[2]/div/div/div/div[3]/div/div/label/div/div[2]/label')))
    paypal_click.click()
    time.sleep(1)

    paypal_mail_one_click = wait.until(
        EC.visibility_of_element_located((By.XPATH, '/html/body/div[4]/div[7]/div[3]/div[1]/input')))
    paypal_mail_one_click.click()
    paypal_mail_one_click.send_keys(Keys.SHIFT, Keys.INSERT)
    time.sleep(1)

    paypal_mail_second_click = wait.until(
        EC.visibility_of_element_located((By.XPATH, '/html/body/div[4]/div[7]/div[3]/div[2]/input')))
    paypal_mail_second_click.click()
    paypal_mail_second_click.send_keys(Keys.SHIFT, Keys.INSERT)
    time.sleep(2)

    paypal_mail_submit_click = wait.until(
        EC.visibility_of_element_located((By.XPATH, '//*[@id="paypal-overlay"]/div[4]/button[1]')))
    paypal_mail_submit_click.click()
    time.sleep(4)

    ## save and continue
    save_cont_4 = wait.until(
        EC.visibility_of_element_located((By.XPATH, '/html/body/div[4]/div[18]/div/div[1]/div/button')))
    save_cont_4.click()
    time.sleep(4)

    ## Verify your ID

    time.sleep(1)

    # Document Type Country

    try:
        print('Performing old document page')
        verify_country_click = WebDriverWait(driver, 5).until(EC.element_to_be_clickable(
            (By.XPATH, '/html/body/div[4]/div[15]/div/div/div/div[2]/div[2]/div/form/div[2]/div[1]/div[1]/div')))
        verify_country_click.click()

        verify_country_select = wait.until(EC.visibility_of_element_located((By.XPATH,
                                                                             '/html/body/div[4]/div[15]/div/div/div/div[2]/div[2]/div/form/div[2]/div[1]/div[1]/div/select/optgroup/option[18]')))
        verify_country_select.click()

        driver.find_element(by=By.TAG_NAME, value="body").send_keys(Keys.ESCAPE)
        time.sleep(1)

        # Document Type
        verify_type_click = wait.until(EC.visibility_of_element_located(
            (By.XPATH, '/html/body/div[4]/div[15]/div/div/div/div[2]/div[2]/div/form/div[2]/div[1]/div[2]/div')))
        verify_type_click.click()

        verify_type_select = wait.until(EC.visibility_of_element_located((By.XPATH,
                                                                          '/html/body/div[4]/div[15]/div/div/div/div[2]/div[2]/div/form/div[2]/div[1]/div[2]/div/select/optgroup/option[4]')))
        verify_type_select.click()

        driver.find_element(by=By.TAG_NAME, value="body").click()
        time.sleep(1)

        # upload photo
        # to identify element
        identy_upload_pic = wait.until(EC.visibility_of_element_located(
            (By.XPATH,
             '/html/body/div[4]/div[15]/div/div/div/div[2]/div[2]/div/form/div[2]/div[1]/div[3]/div/button')))
        identy_upload_pic.click()

        time.sleep(2)

        # Simulate keyboard input to type the file path and press Enter
        keyboard.type(file_path)
        time.sleep(1)
        keyboard.press(Key.enter)
        keyboard.release(Key.enter)

        time.sleep(2)

        # Save Document
        identy_upload_pic_save = wait.until(EC.visibility_of_element_located(
            (By.XPATH, '/html/body/div[4]/div[15]/div/div/div/div[2]/div[2]/div/form/div[2]/div[2]/button')))
        identy_upload_pic_save.click()

        time.sleep(2)

        # running temp mail confirm function
        print("running temp mail confirm function")
        if url2 == "https://www.emailnator.com":
            # Code to execute if url is equal to "https://url1.com"
            print("Emailnator function Running")
            gmaillator_confirm()

        elif url2 == "https://temp-mail.plus":
            # Code to execute if url is equal to "https://url2.com"
            print("Temp Mail Plus Function Running")
            tempmail_plus_confirm()

        elif url2 == "https://url3.com":
            # Code to execute if url is equal to "https://url3.com"
            print("This is URL 3")

        else:
            # Code to execute if url doesn't match any of the above conditions
            print("This is an unknown URL")

        save_cont_5 = wait.until(
            EC.visibility_of_element_located((By.XPATH, '/html/body/div[4]/div[18]/div/div[1]/div/button')))
        save_cont_5.click()
        time.sleep(5)

    except TimeoutException:
        print('Performing new update document page')
        time.sleep(4)
        driver.refresh()
        time.sleep(1)

        verify_country_click2 = wait.until(EC.visibility_of_element_located(
            (By.XPATH,
             '/html/body/div[4]/div[9]/div/div/div/div[2]/div[2]/div/form/div[2]/div/div/div/form/div[2]/div/div[2]/fieldset/div[1]/div[1]/div[1]/div[1]/div[1]/select')))
        verify_country_click2.click()

        verify_country_select2 = wait.until(EC.visibility_of_element_located((By.XPATH,
                                                                              '/html/body/div[4]/div[9]/div/div/div/div[2]/div[2]/div/form/div[2]/div/div/div/form/div[2]/div/div[2]/fieldset/div/div[1]/div[1]/div[1]/div/select/option[18]')))
        verify_country_select2.click()

        driver.find_element(by=By.TAG_NAME, value="body").send_keys(Keys.ESCAPE)
        time.sleep(1)

        # Document Type
        verify_type_click2 = wait.until(EC.visibility_of_element_located(
            (By.XPATH,
             '/html/body/div[4]/div[9]/div/div/div/div[2]/div[2]/div/form/div[2]/div/div/div/form/div[2]/div/div[2]/fieldset/div[1]/div[1]/div[1]/div[2]/div[1]/select')))
        verify_type_click2.click()

        verify_type_select2 = wait.until(EC.visibility_of_element_located((By.XPATH,
                                                                           '/html/body/div[4]/div[9]/div/div/div/div[2]/div[2]/div/form/div[2]/div/div/div/form/div[2]/div/div[2]/fieldset/div/div[1]/div[1]/div[2]/div/select/option[4]')))
        verify_type_select2.click()

        driver.find_element(by=By.TAG_NAME, value="body").click()
        driver.find_element(by=By.TAG_NAME, value="body").send_keys(Keys.PAGE_DOWN)
        time.sleep(1)

        # upload photo
        # to identify element
        identy_upload_pic2 = wait.until(EC.visibility_of_element_located(
            (By.XPATH,
             '/html/body/div[4]/div[9]/div/div/div/div[2]/div[2]/div/form/div[2]/div/div/div/form/div[2]/div/div[2]/fieldset/div/div[3]/div/div[2]/button')))
        identy_upload_pic2.click()

        time.sleep(2)

        # Simulate keyboard input to type the file path and press Enter
        keyboard.type(file_path)
        time.sleep(1)
        keyboard.press(Key.enter)
        keyboard.release(Key.enter)

        time.sleep(2)

        # Save Document
        identy_upload_pic_save2 = wait.until(EC.visibility_of_element_located(
            (By.XPATH,
             '/html/body/div[4]/div[9]/div/div/div/div[2]/div[2]/div/form/div[2]/div/div/div/form/div[3]/button')))
        identy_upload_pic_save2.click()

        time.sleep(3)

        # running temp mail confirm function
        print("running temp mail confirm function")
        if url2 == "https://www.emailnator.com":
            # Code to execute if url is equal to "https://url1.com"
            print("Emailnator function run")
            gmaillator_confirm()


        elif url2 == "https://temp-mail.plus":
            # Code to execute if url is equal to "https://url2.com"
            print("Temp Mail Plus Function Running")
            tempmail_plus_confirm()

        elif url2 == "https://url3.com":
            # Code to execute if url is equal to "https://url3.com"
            print("This is URL 3")

        else:
            # Code to execute if url doesn't match any of the above conditions
            print("This is an unknown URL")

        save_cont_10 = wait.until(
            EC.visibility_of_element_located((By.XPATH, '/html/body/div[6]/div/div[1]/div/button')))
        save_cont_10.click()
        time.sleep(1)

def paid_second():
    # Region select to india

    tell_street_regi_select = wait.until(EC.visibility_of_element_located((By.XPATH,
                                                                           '/html/body/div[5]/div[16]/div[1]/div/div[2]/div[3]/div/div/div[2]/div[3]/select/optgroup/option[17]')))
    tell_street_regi_select.click()

    tell_street_regi_exit = wait.until(EC.visibility_of_element_located(
        (By.XPATH, '/html/body/div[5]/div[16]/div[1]/div/div[2]/div[3]/div/div/div[2]/div[1]')))
    tell_street_regi_exit.click()

    driver.find_element(by=By.TAG_NAME, value="body").send_keys(Keys.PAGE_DOWN)
    time.sleep(1)

    # Residence select to india
    tell_street_residence = wait.until(EC.visibility_of_element_located(
        (By.XPATH, '/html/body/div[5]/div[16]/div[1]/div/div[2]/div[5]/div[2]/div[1]/div[2]/div[2]/div')))
    tell_street_residence.click()

    tell_street_resid_select = wait.until(EC.visibility_of_element_located((By.XPATH,
                                                                            '/html/body/div[5]/div[16]/div[1]/div/div[2]/div[5]/div[2]/div[1]/div[2]/div[2]/div/select/optgroup[2]/option[17]')))
    tell_street_resid_select.click()

    tell_street_resid_exit = wait.until(EC.visibility_of_element_located(
        (By.XPATH, '/html/body/div[5]/div[16]/div[1]/div/div[2]/div[5]/div[2]/div[1]/div[2]/div[1]/label')))
    tell_street_resid_exit.click()
    time.sleep(1)

    # First Name
    tell_first_name = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="identity-first-name"]')))
    tell_first_name.send_keys(name)
    time.sleep(1)

    # Last Name
    tell_last_name = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="identity-last-name"]')))
    tell_last_name.send_keys(name)
    time.sleep(1)

    # DOB
    dob_day_click = wait.until(EC.visibility_of_element_located(
        (By.XPATH, '/html/body/div[5]/div[16]/div[1]/div/div[2]/div[5]/div[2]/div[1]/fieldset[1]/div[2]/div[1]')))
    dob_day_click.click()

    dob_day_submit = wait.until(EC.visibility_of_element_located((By.XPATH,
                                                                  '/html/body/div[5]/div[16]/div[1]/div/div[2]/div[5]/div[2]/div[1]/fieldset[1]/div[2]/div[1]/select/option[9]')))
    dob_day_submit.click()

    dob_mon_click = wait.until(EC.visibility_of_element_located(
        (By.XPATH, '/html/body/div[5]/div[16]/div[1]/div/div[2]/div[5]/div[2]/div[1]/fieldset[1]/div[2]/div[2]')))
    dob_mon_click.click()

    dob_mon_submit = wait.until(EC.visibility_of_element_located((By.XPATH,
                                                                  '/html/body/div[5]/div[16]/div[1]/div/div[2]/div[5]/div[2]/div[1]/fieldset[1]/div[2]/div[2]/select/option[8]')))
    dob_mon_submit.click()

    dob_yer_click = wait.until(EC.visibility_of_element_located(
        (By.XPATH, '/html/body/div[5]/div[16]/div[1]/div/div[2]/div[5]/div[2]/div[1]/fieldset[1]/div[2]/div[3]')))
    dob_yer_click.click()

    dob_yer_submit = wait.until(EC.visibility_of_element_located((By.XPATH,
                                                                  '/html/body/div[5]/div[16]/div[1]/div/div[2]/div[5]/div[2]/div[1]/fieldset[1]/div[2]/div[3]/select/option[34]')))
    dob_yer_submit.click()

    # Pan Card
    tell_pan_card = wait.until(EC.visibility_of_element_located(
        (By.XPATH, '/html/body/div[5]/div[16]/div[1]/div/div[2]/div[5]/div[2]/div[1]/div[14]/div[2]/div/input')))
    tell_pan_card.click()
    tell_pan_card.send_keys(pan)
    time.sleep(1)

    # Nationality select to india
    tell_street_national = wait.until(EC.visibility_of_element_located(
        (By.XPATH, '/html/body/div[5]/div[16]/div[1]/div/div[2]/div[5]/div[2]/div[1]/div[16]/div[2]/div')))
    tell_street_national.click()

    tell_street_national_select = wait.until(EC.visibility_of_element_located((By.XPATH,
                                                                               '/html/body/div[5]/div[16]/div[1]/div/div[2]/div[5]/div[2]/div[1]/div[16]/div[2]/div/select/option[102]')))
    tell_street_national_select.click()

    tell_street_national_exit = wait.until(EC.visibility_of_element_located(
        (By.XPATH, '/html/body/div[5]/div[16]/div[1]/div/div[2]/div[5]/div[2]/div[1]/div[16]/div[1]/label')))
    tell_street_national_exit.click()
    time.sleep(1)

    # Taxpayer address
    # Street address
    tell_street_add = wait.until(EC.visibility_of_element_located((By.XPATH,
                                                                   '/html/body/div[5]/div[16]/div[1]/div/div[2]/div[5]/div[2]/div[1]/fieldset[2]/div/div[2]/div[2]/div/input')))
    tell_street_add.send_keys(address)
    time.sleep(1)

    driver.find_element(by=By.TAG_NAME, value="body").send_keys(Keys.PAGE_DOWN)
    time.sleep(1)

    tell_street_city = wait.until(EC.visibility_of_element_located((By.XPATH,
                                                                    '/html/body/div[5]/div[16]/div[1]/div/div[2]/div[5]/div[2]/div[1]/fieldset[2]/div/div[2]/div[4]/div/input')))
    tell_street_city.click()
    tell_street_city.send_keys(city)
    time.sleep(1)

    tell_street_pin = wait.until(EC.visibility_of_element_located((By.XPATH,
                                                                   '/html/body/div[5]/div[16]/div[1]/div/div[2]/div[5]/div[2]/div[1]/fieldset[2]/div/div[2]/div[5]/div[1]/input')))
    tell_street_pin.click()
    tell_street_pin.send_keys(pincode)
    time.sleep(1)

    tell_street_phone = wait.until(EC.visibility_of_element_located((By.XPATH,
                                                                     '/html/body/div[5]/div[16]/div[1]/div/div[2]/div[5]/div[2]/div[1]/fieldset[2]/div/div[2]/div[6]/div/input')))
    tell_street_phone.send_keys(phone)
    time.sleep(1)

    tell_street_state = wait.until(EC.visibility_of_element_located((By.XPATH,
                                                                     '/html/body/div[5]/div[16]/div[1]/div/div[2]/div[5]/div[2]/div[1]/fieldset[2]/div/div[2]/div[5]/div[2]/div/div[1]')))
    tell_street_state.click()

    tell_street_select = wait.until(EC.visibility_of_element_located((By.XPATH,
                                                                      '/html/body/div[5]/div[16]/div[1]/div/div[2]/div[5]/div[2]/div[1]/fieldset[2]/div/div[2]/div[5]/div[2]/div/div[1]/select/option[11]')))
    tell_street_select.click()

    tell_street_exit = wait.until(EC.visibility_of_element_located((By.XPATH,
                                                                    '/html/body/div[5]/div[16]/div[1]/div/div[2]/div[5]/div[2]/div[1]/fieldset[2]/div/div[2]/div[5]/div[2]/div/label')))
    tell_street_exit.click()

    # In the past 10 years
    tell_ten_years_click = wait.until(EC.visibility_of_element_located(
        (By.XPATH, '//*[@id="content"]/div[16]/div[1]/div/div[2]/div[8]/div[2]/div[2]/fieldset/div/div[2]/label')))
    tell_ten_years_click.click()

    time.sleep(1)

    # Your bank information
    tell_ifsc = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="bank-bank-code"]')))
    tell_ifsc.send_keys(ifsc)
    time.sleep(1)

    tell_bank_acct = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="bank-account-number"]')))
    tell_bank_acct.send_keys(bank_act)
    time.sleep(1)

    driver.find_element(by=By.TAG_NAME, value="body").send_keys(Keys.PAGE_DOWN)
    time.sleep(1)

    # PayPal Account
    paypal_click = wait.until(EC.visibility_of_element_located(
        (By.XPATH, '/html/body/div[5]/div[16]/div[2]/div/div/div/div[3]/div/div/label/div/div[2]/label')))
    paypal_click.click()
    time.sleep(1)

    paypal_mail_one_click = wait.until(
        EC.visibility_of_element_located((By.XPATH, '/html/body/div[5]/div[7]/div[3]/div[1]/input')))
    paypal_mail_one_click.click()
    paypal_mail_one_click.send_keys(Keys.SHIFT, Keys.INSERT)
    time.sleep(1)

    paypal_mail_second_click = wait.until(
        EC.visibility_of_element_located((By.XPATH, '/html/body/div[5]/div[7]/div[3]/div[2]/input')))
    paypal_mail_second_click.click()
    paypal_mail_second_click.send_keys(Keys.SHIFT, Keys.INSERT)
    time.sleep(2)

    paypal_mail_submit_click = wait.until(
        EC.visibility_of_element_located((By.XPATH, '//*[@id="paypal-overlay"]/div[4]/button[1]')))
    paypal_mail_submit_click.click()
    time.sleep(4)

    ## save and continue
    save_cont_4 = wait.until(
        EC.visibility_of_element_located((By.XPATH, '/html/body/div[5]/div[18]/div/div[1]/div/button')))
    save_cont_4.click()
    time.sleep(4)

    ## Verify your ID

    time.sleep(1)

    # Document Type Country

    try:
        print('Performing old document function')
        verify_country_click = WebDriverWait(driver, 5).until(EC.element_to_be_clickable(
            (By.XPATH, '/html/body/div[5]/div[15]/div/div/div/div[2]/div[2]/div/form/div[2]/div[1]/div[1]/div')))
        verify_country_click.click()

        verify_country_select = wait.until(EC.visibility_of_element_located((By.XPATH,
                                                                             '/html/body/div[5]/div[15]/div/div/div/div[2]/div[2]/div/form/div[2]/div[1]/div[1]/div/select/optgroup/option[18]')))
        verify_country_select.click()

        driver.find_element(by=By.TAG_NAME, value="body").send_keys(Keys.ESCAPE)
        time.sleep(1)

        # Document Type
        verify_type_click = wait.until(EC.visibility_of_element_located(
            (By.XPATH, '/html/body/div[5]/div[15]/div/div/div/div[2]/div[2]/div/form/div[2]/div[1]/div[2]/div')))
        verify_type_click.click()

        verify_type_select = wait.until(EC.visibility_of_element_located((By.XPATH,
                                                                          '/html/body/div[5]/div[15]/div/div/div/div[2]/div[2]/div/form/div[2]/div[1]/div[2]/div/select/optgroup/option[4]')))
        verify_type_select.click()

        driver.find_element(by=By.TAG_NAME, value="body").click()
        time.sleep(1)

        # upload photo
        # to identify element
        identy_upload_pic = wait.until(EC.visibility_of_element_located(
            (By.XPATH,
             '/html/body/div[5]/div[15]/div/div/div/div[2]/div[2]/div/form/div[2]/div[1]/div[3]/div/button')))
        identy_upload_pic.click()

        time.sleep(2)

        # Simulate keyboard input to type the file path and press Enter
        keyboard.type(file_path)
        time.sleep(1)
        keyboard.press(Key.enter)
        keyboard.release(Key.enter)

        time.sleep(2)

        # Save Document
        identy_upload_pic_save = wait.until(EC.visibility_of_element_located(
            (By.XPATH, '/html/body/div[5]/div[15]/div/div/div/div[2]/div[2]/div/form/div[2]/div[2]/button')))
        identy_upload_pic_save.click()
        time.sleep(3)

        # running temp mail confirm function
        print("running temp mail confirm function")
        if url2 == "https://www.emailnator.com":
            # Code to execute if url is equal to "https://url1.com"
            print("Emailnator function run")
            gmaillator_confirm()

        elif url2 == "https://temp-mail.plus":
            # Code to execute if url is equal to "https://url2.com"
            print("Temp Mail Plus Function Running")
            tempmail_plus_confirm()

        elif url2 == "https://url3.com":
            # Code to execute if url is equal to "https://url3.com"
            print("This is URL 3")

        else:
            # Code to execute if url doesn't match any of the above conditions
            print("This is an unknown URL")

        save_cont_5 = wait.until(
            EC.visibility_of_element_located((By.XPATH, '/html/body/div[4]/div[18]/div/div[1]/div/button')))
        save_cont_5.click()
        time.sleep(3)

    except TimeoutException:
        print('Performing new update page')
        time.sleep(4)
        driver.refresh()
        time.sleep(1)

        verify_country_click2 = wait.until(EC.visibility_of_element_located(
            (By.XPATH,
             '/html/body/div[5]/div[9]/div/div/div/div[2]/div[2]/div/form/div[2]/div/div/div/form/div[2]/div/div[2]/fieldset/div[1]/div[1]/div[1]/div[1]/div[1]/select')))
        verify_country_click2.click()

        verify_country_select2 = wait.until(EC.visibility_of_element_located((By.XPATH,
                                                                              '/html/body/div[5]/div[9]/div/div/div/div[2]/div[2]/div/form/div[2]/div/div/div/form/div[2]/div/div[2]/fieldset/div/div[1]/div[1]/div[1]/div/select/option[18]')))
        verify_country_select2.click()

        driver.find_element(by=By.TAG_NAME, value="body").send_keys(Keys.ESCAPE)
        time.sleep(1)

        # Document Type
        verify_type_click2 = wait.until(EC.visibility_of_element_located(
            (By.XPATH,
             '/html/body/div[5]/div[9]/div/div/div/div[2]/div[2]/div/form/div[2]/div/div/div/form/div[2]/div/div[2]/fieldset/div[1]/div[1]/div[1]/div[2]/div[1]/select')))
        verify_type_click2.click()

        verify_type_select2 = wait.until(EC.visibility_of_element_located((By.XPATH,
                                                                           '/html/body/div[5]/div[9]/div/div/div/div[2]/div[2]/div/form/div[2]/div/div/div/form/div[2]/div/div[2]/fieldset/div/div[1]/div[1]/div[2]/div/select/option[4]')))
        verify_type_select2.click()

        driver.find_element(by=By.TAG_NAME, value="body").click()
        driver.find_element(by=By.TAG_NAME, value="body").send_keys(Keys.PAGE_DOWN)
        time.sleep(1)

        # upload photo
        # to identify element
        identy_upload_pic2 = wait.until(EC.visibility_of_element_located(
            (By.XPATH,
             '/html/body/div[5]/div[9]/div/div/div/div[2]/div[2]/div/form/div[2]/div/div/div/form/div[2]/div/div[2]/fieldset/div/div[3]/div/div[2]/button')))
        identy_upload_pic2.click()

        time.sleep(2)

        # Simulate keyboard input to type the file path and press Enter
        keyboard.type(file_path)
        time.sleep(1)
        keyboard.press(Key.enter)
        keyboard.release(Key.enter)

        time.sleep(2)

        # Save Document
        identy_upload_pic_save2 = wait.until(EC.visibility_of_element_located(
            (By.XPATH,
             '/html/body/div[5]/div[9]/div/div/div/div[2]/div[2]/div/form/div[2]/div/div/div/form/div[3]/button')))
        identy_upload_pic_save2.click()

        time.sleep(3)

        # running temp mail confirm function
        print("running temp mail confirm function")
        if url2 == "https://www.emailnator.com":
            # Code to execute if url is equal to "https://url1.com"
            print("Emailnator function run")
            gmaillator_confirm()

        elif url2 == "https://temp-mail.plus":
            # Code to execute if url is equal to "https://url2.com"
            print("Temp Mail Plus Function Running")
            tempmail_plus_confirm()

        elif url2 == "https://url3.com":
            # Code to execute if url is equal to "https://url3.com"
            print("This is URL 3")

        else:
            # Code to execute if url doesn't match any of the above conditions
            print("This is an unknown URL")
        time.sleep(1)

        save_cont_10 = wait.until(
            EC.visibility_of_element_located((By.XPATH, '/html/body/div[7]/div/div[1]/div/button')))
        save_cont_10.click()
        time.sleep(1)

try:
    print('Performing second function 5')
    tell_street_region2 = WebDriverWait(driver, 5).until(EC.element_to_be_clickable(
        (By.XPATH, '/html/body/div[5]/div[16]/div[1]/div/div[2]/div[3]/div/div/div[2]/div[3]')))
    tell_street_region2.click()
    time.sleep(1)
    paid_second()
except TimeoutException:
    print('Performing first function 4')

    tell_street_region1 = WebDriverWait(driver, 5000).until(EC.element_to_be_clickable(
        (By.XPATH, '/html/body/div[4]/div[16]/div[1]/div/div[2]/div[3]/div/div/div[2]/div[3]')))
    tell_street_region1.click()
    time.sleep(1)
    paid_first()

# UPI ID
upi_id_save = wait.until(EC.visibility_of_element_located(
    (By.XPATH, '/html/body/div[4]/div[2]/div/div/div[6]/div[2]/div[2]/div[1]/div/div/div[1]/input')))
upi_id_save.send_keys(upi_id)
time.sleep(1)

save_cont_6 = wait.until(
    EC.visibility_of_element_located((By.XPATH, '/html/body/div[4]/div[3]/div[4]/div/div[1]/button')))
save_cont_6.click()
time.sleep(5)

# user varification process

#verify_method_click = wait.until(EC.visibility_of_element_located(
 #   (By.XPATH, '/html/body/div[4]/div[2]/div/div/div[7]/div/div/div[1]/div/div/div/p[2]')))
#verify_method_click.click()
#time.sleep(1)

act = ActionChains(driver)
act.send_keys(Keys.TAB).perform()
time.sleep(1)
act.send_keys(Keys.TAB).perform()
time.sleep(1)
act.send_keys(Keys.TAB).perform()
time.sleep(1)
act.send_keys(Keys.TAB).perform()
time.sleep(1)
act.send_keys(Keys.TAB).perform()
time.sleep(1)
act.send_keys(Keys.TAB).perform()
time.sleep(1)
act.send_keys(Keys.TAB).perform()
time.sleep(1)
act.send_keys(Keys.ENTER).perform()
time.sleep(1)

verify_method_select = wait.until(EC.visibility_of_element_located(
    (By.XPATH, '/html/body/div[4]/div[2]/div/div/div[7]/div/div/div[1]/div/div/div/div/div/div/div/div/button[3]')))
verify_method_select.click()
time.sleep(1)

driver.find_element(by=By.TAG_NAME, value="body").send_keys(Keys.ESCAPE)
time.sleep(1)

save_cont_7 = wait.until(EC.visibility_of_element_located(
    (By.XPATH, '/html/body/div[4]/div[2]/div/div/div[7]/div/div/div[2]/div/div[1]/button')))
save_cont_7.click()
time.sleep(2)

save_cont_8 = wait.until(EC.visibility_of_element_located(
    (By.XPATH, '/html/body/div[4]/div[2]/div/div/div[7]/div/div/div[2]/div/div[2]/button')))
save_cont_8.click()
time.sleep(1)

### Put 2mfa function

content = wait.until(EC.visibility_of_element_located(
    (By.XPATH, '/html/body/div[4]/div[2]/div/div/div[7]/div/div/div[1]/div/div/span/div[5]/div[1]'))).text

# initialise with your secret key
totp = TOTP(content)

token = totp.now()

print(token)

token_send = wait.until(EC.visibility_of_element_located(
    (By.XPATH, '/html/body/div[4]/div[2]/div/div/div[7]/div/div/div[1]/div/div/fieldset/div[1]/input')))
token_send.click()
time.sleep(1)
token_send.send_keys(token)
time.sleep(1)

save_cont_9 = wait.until(EC.visibility_of_element_located(
    (By.XPATH, '/html/body/div[4]/div[2]/div/div/div[7]/div/div/div[2]/div/div[2]/button')))
save_cont_9.click()
time.sleep(1)

copy_code_click = wait.until(EC.visibility_of_element_located(
    (By.XPATH, '/html/body/div[4]/div[2]/div/div/div[7]/div/div/div[1]/div/div/div/div[3]/button[2]')))
copy_code_click.click()
time.sleep(1)

cpen_shop_click = wait.until(EC.visibility_of_element_located(
    (By.XPATH, '/html/body/div[4]/div[2]/div/div/div[7]/div/div/div[2]/div/div[1]/button')))
cpen_shop_click.click()

try:
    print('UK region checking')
    uk_shop_open = WebDriverWait(driver, 5).until(EC.element_to_be_clickable(
        (By.XPATH, '/html/body/div[6]/div[2]/div/div[3]/div/div[2]/div/button')))
    uk_shop_open.click()
    time.sleep(1)
except TimeoutException:
    print('Performing other region shop open')
    time.sleep(1)

print("Script run successfully")

time.sleep(20)
