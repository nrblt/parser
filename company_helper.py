from bs4 import BeautifulSoup
import requests

class Bs:
    url = ''
    soup = None
    def __init__(self, url):
        self.url = url
        self.soup = BeautifulSoup(requests.get(url).content, "html.parser")

    def get_company_descr(self):
        descr_span = self.get_span_by_class('f3_ctl00_cphRegistersMasterPage_c1wrptData')
        descr = self.get_text_from_span(descr_span)
        return descr

    def get_company_name(self):
        name_span = self.get_span_by_class('f8_ctl00_cphRegistersMasterPage_c1wrptData')
        name = self.get_text_from_span(name_span)
        return name

    def get_company_entity_type(self):
        entity_span = self.get_span_by_class('f2_ctl00_cphRegistersMasterPage_c1wrptData')
        # span_element = soup.find('span', class_='f2_ctl00_cphRegistersMasterPage_c1wrptData')
        entity_type = self.get_entity_type(entity_span)
        return entity_type

    def get_span_by_class(self, class_name):
        span_element = self.soup.find('span', class_=class_name)
        return span_element

    def get_text_from_span(self, span_element):
        if span_element:
            if span_element.text:
                return span_element.text
            return ""

    def get_entity_type(self, span_element):
        if span_element:
            a_tag = span_element.find('a')
        if a_tag:
            text = a_tag.text
            return text
        return ""
