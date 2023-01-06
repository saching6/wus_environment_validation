import requests
import json
import re


class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

beta_url = "https://test.wusreport.com"
beta_api_url = "https://test.wusreport.com:5001"
beta_admin_url = "https://test.wusreport.com:5003"


prod_url = "https://wusreport.com"
prod_api_url = "https://wusreport.com:5001"
prod_admin_url = "https://wusreport.com:5003"

input_email = input("Please enter your email: " )
test_count = 0
endpoint = "/test_connection"
email_endpoint = "/testEmail"

 ## Beta/Test Connection 
print("\n\n\n************************* BETA VALIDATION ***********************************")
response = requests.get(beta_url)
if response.status_code == 200:
    test_count+=1
    print(f'{bcolors.OKGREEN}1. Wake Up Safe beta website: SUCCESS')
else:
    print(f'{bcolors.FAIL}1. Wake Up Safe beta website: FAILED')
    print("------------------------ERROR MESSAGE-----------------------------")
    print('Cannot access Wake Up Safe Beta Website') 
    print(response.reason)
    print("------------------------------------------------------------------")

# print("\n\nSending request to backend API")
try:
    response = requests.post(beta_api_url + endpoint, json={"type": "initial"})
    if response.status_code == 200: 
        # print("Successful Response. Sending Acknowledgment ... ")
        ack_response = requests.post(beta_api_url + endpoint, json={"type":"ack"})
        if ack_response.status_code==200:
            print(f'{bcolors.OKGREEN}2. Wake Up Safe beta API: SUCCESS{bcolors.ENDC}')
            test_count+=1
        else:
            print(f"{bcolors.FAIL}2. Wake Up Safe beta API: FAILED{bcolors.ENDC}")
            print("------------------------ERROR MESSAGE-----------------------------")
            print("Acknowledgment Error ")
            print("Status Code:", ack_response.status_code)
            print(ack_response.reason+'\n')
            x = re.sub('<html>.*?</html>', '', ack_response.text, flags=re.DOTALL)
            result = x.split('<!--\n\n')[1].split('\n\n-->')[0]
            print(result)
            print("------------------------------------------------------------------\n\n")
    else:
        print(f"{bcolors.FAIL}2. Wake Up Safe beta API: FAILED{bcolors.ENDC}")
        print("------------------------ERROR MESSAGE-----------------------------")
        print("Initial Request Error ")
        print("Status Code:", response.status_code)
        print(response.reason+'\n')
        x = re.sub('<html>.*?</html>', '', response.text, flags=re.DOTALL)
        result = x.split('<!--\n\n')[1].split('\n\n-->')[0]
        print(result)
        print("------------------------------------------------------------------")

except requests.exceptions.ConnectionError as e:
    print(f"{bcolors.FAIL}2. Wake Up Safe beta API: FAILED{bcolors.ENDC}")
    print("------------------------ERROR MESSAGE-----------------------------")
    print("Unable to send API request")
    print(e)
    print("------------------------------------------------------------------")

try:
    response = requests.post(beta_admin_url + email_endpoint, json={"email": input_email})
    if response.status_code ==200:
        print(f"{bcolors.OKGREEN}3. Wake Up Safe beta Email server: SUCCESS{bcolors.ENDC}")
        test_count+=1
    else:
        print(f"{bcolors.FAIL}3. Wake Up Safe beta Email server: FAILED{bcolors.ENDC}")
        print("------------------------ERROR MESSAGE-----------------------------")
        print("Email Request Error ")
        print("Status Code:", response.status_code)
        print(response.reason+'\n')
        x = re.sub('<html>.*?</html>', '', response.text, flags=re.DOTALL)
        result = x.split('<!--\n\n')[1].split('\n\n-->')[0]
        print(result)
        print("------------------------------------------------------------------")
except requests.exceptions.ConnectionError as e:
    print(f"{bcolors.FAIL}3. Wake Up Safe beta Email server: FAILED{bcolors.ENDC}")
    print("------------------------ERROR MESSAGE-----------------------------")
    print("Connection Exception, unable to send request ")
    print(e)
    print("------------------------------------------------------------------")

print()
print("Beta Server Validation Complete")
print(f"{bcolors.OKGREEN if test_count==3 else bcolors.FAIL}{test_count}/3 tests passed{bcolors.ENDC}")
if(test_count==3):
    print(f"{bcolors.OKGREEN}All tests passed{bcolors.ENDC}")
test_count=0


print("\n\n\n************************* PRODUCTION VALIDATION ***********************************")
response = requests.get(prod_url)
if response.status_code == 200:
    test_count+=1
    print(f'{bcolors.OKGREEN}4. Wake Up Safe production website: SUCCESS')
else:
    print(f'{bcolors.FAIL}4. Wake Up Safe production website: FAILED')
    print("------------------------ERROR MESSAGE-----------------------------")
    print('Cannot access Wake Up Safe Website') 
    print(response.reason)
    print("------------------------------------------------------------------")

# print("\n\nSending request to backend API")
try:
    response = requests.post(prod_api_url + endpoint, json={"type": "initial"})
    if response.status_code == 200: 
        # print("Successful Response. Sending Acknowledgment ... ")
        ack_response = requests.post(prod_api_url + endpoint, json={"type":"ack"})
        if ack_response.status_code==200:
            print(f'{bcolors.OKGREEN}5. Wake Up Safe production API: SUCCESS{bcolors.ENDC}')
            test_count+=1
        else:
            print(f"{bcolors.FAIL}5. Wake Up Safe production API: FAILED{bcolors.ENDC}")
            print("------------------------ERROR MESSAGE-----------------------------")
            print("Acknowledgment Error ")
            print("Status Code:", ack_response.status_code)
            print(ack_response.reason)
            x = re.sub('<html>.*?</html>', '', ack_response.text, flags=re.DOTALL)
            result = x.split('<!--\n')[1].split('-->\n')[0]
            print(result)
            print("------------------------------------------------------------------")
    else:
        print(f"{bcolors.FAIL}5. Wake Up Safe production API: FAILED{bcolors.ENDC}")
        print("------------------------ERROR MESSAGE-----------------------------")
        print("\n\n\nInitial Request Error ")
        print("Status Code:", response.status_code)
        print(response.reason)
        print('####################')
        x = re.sub('<html>.*?</html>', '', response.text, flags=re.DOTALL)
        result = x.split('<!--\n\n')[1].split('\n\n-->')[0]
        print(result)
        print("------------------------------------------------------------------")
except requests.exceptions.ConnectionError as e:
    print(f"{bcolors.FAIL}5. Wake Up Safe production API: FAILED{bcolors.ENDC}")
    print("------------------------ERROR MESSAGE-----------------------------")
    print("Unable to send API request")
    print(e)
    print("------------------------------------------------------------------")

try:
    response = requests.post(prod_admin_url + email_endpoint, json={"email": input_email})
    if response.status_code ==200:
        print(f"{bcolors.OKGREEN}6. Wake Up Safe production Email server: SUCCESS{bcolors.ENDC}")
        test_count+=1
    else:
        print(f"{bcolors.FAIL}6. Wake Up Safe production Email server: FAILED{bcolors.ENDC}")
        print("------------------------ERROR MESSAGE-----------------------------")
        print("Email Request Error ")
        print("Status Code:", response.status_code)
        print(response.reason+'\n')
        x = re.sub('<html>.*?</html>', '', response.text, flags=re.DOTALL)
        result = x.split('<!--\n\n')[1].split('\n\n-->')[0]
        print(result)
        print("------------------------------------------------------------------")
except requests.exceptions.ConnectionError as e:
    print(f"{bcolors.FAIL}6. Wake Up Safe production Email server: FAILED{bcolors.ENDC}")
    print("------------------------ERROR MESSAGE-----------------------------")
    print("Connection Exception, unable to send request ")
    print(e)
    print("------------------------------------------------------------------")

print()
print("Production Server Validation Complete")
print(f"{bcolors.OKGREEN if test_count==3 else bcolors.FAIL}{test_count}/3 tests passed{bcolors.ENDC}")
if(test_count==3):
    print(f"{bcolors.OKGREEN}All tests passed{bcolors.ENDC}")
test_count=0

