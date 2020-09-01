from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("https://web.whatsapp.com/")
driver.maximize_window()

def creategroup():
    name = input("Enter group name:")
    confirmation = input("Click Enter After Scanning the QR code.")
    my_list= ["9932991628","8016056090","9933121051"]
    menubutton = driver.find_element_by_xpath('//*[@id="side"]/header/div[2]/div/span/div[3]/div/span')
    menubutton.click()
    newgroup = driver.find_element_by_xpath('//*[@id="side"]/header/div[2]/div/span/div[3]/span/div/ul/li[1]/div')
    newgroup.click()
    i = 0

    for i in range(len(my_list)):
        contactname = driver.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/div[1]/span/div/span/div/div/div[1]/div/div/input')
        contactname.click()
        contactname.send_keys(my_list[i])
        contact = driver.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/div[1]/span/div/span/div/div/div[2]/div[1]/div/div/div/div/div/div[2]/div[1]/div/span/span')
        contact.click()
        i=(i+1)
    
    selectall = driver.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/div[1]/span/div/span/div/div/span/div/span')
    selectall.click()

    groupname = driver.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/div[1]/span/div/span/div/div/div[2]/div/div[2]/div/div[2]')
    groupname.click()
    groupname.send_keys(name)

    entergroupname = driver.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/div[1]/span/div/span/div/div/span/div/div/span')
    entergroupname.click()

creategroup()

