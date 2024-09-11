from selenium import webdriver
from bs4 import BeautifulSoup
import time
import os

def taeste_func():
    url = "https://www.google.com/"

    # Use headless mode
    options = webdriver.FirefoxOptions()
    options.headless = True

    # Set the path of the Firefox binary
    firefox_binary_path = "/usr/bin/firefox-esr"
    options.binary_location = firefox_binary_path

    # Set the display port as an environment variable
    display_port = os.environ.get("DISPLAY_PORT", "99")
    display = f":{display_port}"
    os.environ["DISPLAY"] = display

    # Start the Xvfb server
    xvfb_cmd = f"Xvfb {display} -screen 0 1024x768x24 -nolisten tcp &"
    os.system(xvfb_cmd)

    # Start the Firefox driver
    driver = webdriver.Firefox(options=options)

    # Go to Google.com
    driver.get(url)

    # Print the page source
    print(driver.page_source)

    # Close the browser
    driver.quit()

def browser():
    # Use headless mode
    options = webdriver.FirefoxOptions()
    options.headless = True

    # Set the path of the Firefox binary
    firefox_binary_path = "/usr/bin/firefox-esr"
    options.binary_location = firefox_binary_path

    # Set the display port as an environment variable
    display_port = os.environ.get("DISPLAY_PORT", "99")
    display = f":{display_port}"
    os.environ["DISPLAY"] = display

    # Start the Xvfb server
    xvfb_cmd = f"Xvfb {display} -screen 0 1024x768x24 -nolisten tcp &"
    os.system(xvfb_cmd)

    # Start the Firefox driver
    ##########options.add_argument("--headless")
    browserr = webdriver.Firefox(options=options)
    #browserr = webdriver.Chrome(service=config, options=options)
    return browserr

def getPaginaDinamica(browser,url):
    pag_result=browser.get(url)
    time.sleep(2)
    return pag_result

chr=browser()
pg=getPaginaDinamica(chr,"https://stats.nba.com/players/traditional/?PerMode=Totals&Season=2019-20&SeasonType=Regular%20Season&sort=PLAYER_NAME&dir=-1")

print('teste')
print(chr)
print(pg)

#PULO DO GATO OBTENÇÃO DOS ELEMENTOS, USANDO JS E CSS VIA SELENIUM
element = chr.find_element('xpath', '//*[@id="__next"]/div[2]/div[2]/div[3]/section[2]/div/div[2]/div[3]/table/tbody')
html = element.get_attribute('outerHTML')
#print(html)

bs = BeautifulSoup(html, 'html.parser')
nomes = bs.find_all("td", {'class' : 'Crom_text__NpR1_ Crom_primary__EajZu Crom_stickySecondColumn__29Dwf'})

lista_nomes = []

for nome in nomes:
    item = nome.findChildren('a')
    lista_nomes.append(item[0].text)
    print(item[0].text)

#arquivo_txt = open('nomes_jogadores.txt', "w")

#for nome in lista_nomes:
#    arquivo_txt.write(f'{nome}\n')
