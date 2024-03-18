
What I use in this project?

Selenium, Bs4, fastapi, mongodb


Before run 
    -set your mongodb urls, 

    -make sure that you have Firefox browser,

    -make sure that you have Rabbitmq server,
    
    -make sure that you have installed python on your device

How to run?
    1. start run_selenium_and_worker.sh script by using this command
        sh run_selenium_and_worker.sh
        
    2. start create_and_runserver.sh script by using this command
        sh create_and_runserver.sh

In the end you will have data.json json file, there will be all parsed data, output.txt there will be company_id-s and running Fastapi server which url is http://127.0.0.1:8000/companies , that will return all parsed information, and also you can give extra filter by writing name, organizational_and_legal_form as parameter
http://127.0.0.1:8000/companies?name=...
http://127.0.0.1:8000/companies?organizational_and_legal_form=...
