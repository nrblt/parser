from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
from celery import Celery

#initing used libs
options = webdriver.FirefoxOptions()
driver = webdriver.Firefox(options=options)
app = Celery('app', broker='amqp://nurbo:nurbo@localhost:5672/myvhost')

#firstly I write core functions
def index_page(page='https://registers.centralbank.ie/FirmSearchResultsPage.aspx?searchEntity=Institution&searchType=Name&searchText=&registers=2%2c13&firmType=CreditInstitutions'):
    driver.get(page)

def quit_driver():
    driver.quit()

def set_soup_url(url):
    pass# requests get html from
def get_soup():
    page_source = get_page_source()
    soup = BeautifulSoup(page_source, 'html.parser')
    return soup

def go_to_previous_page():
    find_by_id_and_click('ctl00_cphRegistersMasterPage_gvwSearchResults_ctl18_btnPrev')

#finding functions
def find_by_id_and_click(id):
    element=driver.find_element(By.ID, id)
    element.click()

def find_by_class_and_click(class_name):
    element=driver.find_element(By.ID, class_name)
    element.click()

#infomation returning functions
def get_company_ids():
    soup = get_soup()
    td_tags = soup.find_all('td', class_='gvwColumn')

    texts = [tag.text for tag in td_tags]
    return texts

def get_page_source():
    page_source = driver.page_source
    return page_source

def get_entity_type(span_element):
    if span_element:
        a_tag = span_element.find('a')
    if a_tag:
        text = a_tag.text
        return text
    return ""

def get_text_from_span(span_element):
    if span_element:
        if span_element.text:
            return span_element.text
        return ""

def get_current_page():
    soup = get_soup()
    select = soup.find('select', id='ctl00_cphRegistersMasterPage_gvwSearchResults_ctl18_ddlPages')
    selected_option = select.find('option', selected=True)

    if selected_option:
        selected_value = selected_option['value']
        return selected_value
    return 1
