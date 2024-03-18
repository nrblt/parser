from helper import *
from tasks import *

index_page()
find_by_class_and_click('ctl00_cphRegistersMasterPage_gvwSearchResults_ctl18_btnLast')
cur_page = get_current_page()
all_companies = []
while int(cur_page) > 1:
    companies = get_company_ids()
    add_to_queue(companies)
    all_companies += companies
    go_to_previous_page()
    cur_page = get_current_page()
companies = get_company_ids()
add_to_queue(companies)

all_companies += companies
file_path = "output.txt"

with open(file_path, "w") as file:
    for item in all_companies:
        file.write(str(item) + "\n")
quit_driver()
