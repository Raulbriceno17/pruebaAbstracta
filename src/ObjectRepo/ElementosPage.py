from selenium.webdriver.common.by import By

class Elementos():

    inputbuscador   =   'cb1-edit'
    btnbuscador=   "//button[@class='nav-search-btn']"
    contProd =   "//*[@class='ui-search-layout ui-search-layout--stack']"
    btnSiguiente = '//li[@class="andes-pagination__button andes-pagination__button--next"]/a[@role="button"]'
    avisocamisa= "//li[@class='ui-search-layout__item']"
    linkcompra= './/div/div/div[2]/div[@class="ui-search-item__group ui-search-item__group--title"]/a[@class="ui-search-item__group__element ui-search-link"]'
    tituloaviso= ".//h2[@class='ui-search-item__title']"
    precioaviso= ".//div/div/div/div/span/span/span[@class='price-tag-fraction']"
        