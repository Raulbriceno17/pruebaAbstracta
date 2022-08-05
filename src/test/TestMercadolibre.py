import sys
sys.path.insert(0, "./src")
from ObjectRepo.ElementosPage import Elementos
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
#from selenium.webdriver.common import by
import time


#Inicializar webdriver

options = webdriver.ChromeOptions()
options.add_argument('--start-maximized')
options.add_argument('--disable-extensions')

driver_path = '/Users/usuario/Documents/pruebaAbstracta/chromedriver'

driver = webdriver.Chrome(driver_path, chrome_options=options)

driver.set_window_position(2000,0)
driver.maximize_window()
time.sleep(3)

##Ingresar a la pagina
driver.get('https://www.mercadolibre.cl/')
time.sleep(10)
driver.find_element_by_id(Elementos.inputbuscador).send_keys('camisetas')
driver.find_element_by_id(Elementos.inputbuscador).send_keys(Keys.ENTER)
time.sleep(10)


avisos = driver.find_elements_by_xpath(Elementos.avisocamisa)

for i in range (3):

    avisos = driver.find_elements_by_xpath(Elementos.avisocamisa)

    for aviso in avisos:
        titulo_aviso = aviso.find_element_by_xpath(Elementos.tituloaviso).text
        precio_aviso = aviso.find_element_by_xpath(Elementos.precioaviso).text
        link_aviso = aviso.find_element_by_xpath(Elementos.linkcompra).get_attribute("href")
        resultado = open("Avisos.txt","a")
        resultado.write("Titulo : " + titulo_aviso + " \nPrecio: " + precio_aviso + "\nLink : " + link_aviso + "\n")
        resultado.close() 

    driver.find_element_by_xpath(Elementos.btnSiguiente).click()
driver.quit()




