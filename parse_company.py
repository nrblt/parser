from company_helper import Bs

def parse(company_id):
    url = 'https://registers.centralbank.ie/FirmDataPage.aspx?firmReferenceNumber=' + company_id
    bs = Bs(url)

    entity_type = bs.get_company_entity_type()
    name = bs.get_company_name()

    descr = bs.get_company_descr()
    answer_dict = {'county': 'Ireland', 'white_list': 'white_list',
                'source': 'https://registers.centralbank.ie/FirmSearchPage.aspx',
                'name': name, 'organizational_and_legal_form': entity_type,
                'remarks': descr}
    return answer_dict
