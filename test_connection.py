import requests
import json
import re

# prod_api_url = "http://wusreport.com:5005"
# prod_url = "http://wusreport.com:3000"


# alpha_url = "https://test.wusreport.com:3000"
# test_api_url = "https://test.wusreport.com:5001"
# test_admin_url = "https://test.wusreport.com:5003"

alpha_url = "http://alpha.wusreport.com"
alpha_api_url = "http://alpha.wusreport.com:5001"
alpha_admin_url = "http://alpha.wusreport.com:5003"

# local_url = "http://alpha.wusreport.com"
# local_api_url = "http://alpha.wusreport.com:5001"
# alpha_admin_url = "http://alpha.wusreport.com:5003"

input_email = input("Please enter your email: " )

endpoint = "/test_connection"
email_endpoint = "/testEmail"
 ## Beta/Test Connection 
print("\n\n\n************************* TEST URL VALIDATION ***********************************")
response = requests.get(alpha_url)
if response.status_code == 200:
    print('Wake Up Safe website works')
else:
    print('Cannot access Wake Up Safe Website') 
    print("------------------------ERROR MESSAGE-----------------------------")
    print(response.reason)
print("------------------------------------------------------------------")

print("\n\nSending request to backend API")
try:
    response = requests.post(alpha_api_url + endpoint, json={"type": "initial"})
    if response.status_code == 200: 
        print("Successful Response. Sending Acknowledgment ... ")
        ack_response = requests.post(alpha_api_url + endpoint, json={"type":"ack"})
        if ack_response.status_code==200:
            print("Successful. Received Acknowledgment Response... ")
        else:
            print("\n\n\nAcknowledgment Error ")
            print("Status Code:", ack_response.status_code)
            print("------------------------ERROR MESSAGE-----------------------------")
            print(ack_response.reason)
            x = re.sub('<html>.*?</html>', '', ack_response.text, flags=re.DOTALL)
            result = x.split('<!--\n')[1].split('-->\n')[0]
            print(result)
            print("------------------------------------------------------------------")
    else:
        print("\n\n\nInitial Request Error ")
        print("Status Code:", response.status_code)
        print("------------------------ERROR MESSAGE-----------------------------")
        print(response.reason)
        print("------------------------------------------------------------------")

except requests.exceptions.ConnectionError as e:
    print("Unable to send request")
    print(e)
## TEST EMAIL Connection 
print("\n\n************************* TESTING EMAIL (TEST) SERVER *************************")
try:
    response = requests.post(alpha_admin_url + email_endpoint, json={"email": input_email})
    if response.status_code ==200:
        print("Successful. Communication with Email server established")
    else:
        print("\n\nEmail Request Error ")
        print("Status Code:", response.status_code)
        print("------------------------ERROR MESSAGE-----------------------------")
        print(response.reason)
        print("------------------------------------------------------------------")
except requests.exceptions.ConnectionError as e:
    print("\n\n\n Connection Exception, unable to send request ")
    print("------------------------ERROR MESSAGE-----------------------------")
    print(e)
    print("------------------------------------------------------------------")



print("\n\n\************************* PRODUCTION URL VALIDATION ***********************************")
response = requests.get(alpha_url)
if response.status_code == 200:
    print('Wake Up Safe website works')
else:
    print('Cannot access Wake Up Safe Website') 
    print("------------------------ERROR MESSAGE-----------------------------")
    print(response.reason)
print("------------------------------------------------------------------")

print("\n\nSending request to backend API")
try:
    response = requests.post(alpha_api_url + endpoint, json={"type": "initial"})
    if response.status_code == 200: 
        print("Successful Response. Sending Acknowledgment ... ")
        ack_response = requests.post(alpha_api_url + endpoint, json={"type":"ack"})
        if ack_response.status_code==200:
            print("Successful. Received Acknowledgment Response... ")
        else:
            print("\n\n\nAcknowledgment Error ")
            print("Status Code:", ack_response.status_code)
            print("------------------------ERROR MESSAGE-----------------------------")
            print(ack_response.reason)
            x = re.sub('<html>.*?</html>', '', ack_response.text, flags=re.DOTALL)
            result = x.split('<!--\n')[1].split('-->\n')[0]
            print(result)
            print("------------------------------------------------------------------")
    else:
        print("\n\n\nInitial Request Error ")
        print("Status Code:", response.status_code)
        print("------------------------ERROR MESSAGE-----------------------------")
        print(response.reason)
        print("------------------------------------------------------------------")

except requests.exceptions.ConnectionError as e:
    print("Unable to send request")
    print(e)

print("************************* TESTING EMAIL (PRODUCTION) SERVER *************************")
try:
    response = requests.post(alpha_admin_url + email_endpoint, json={"email": input_email})
    if response.status_code ==200:
        print("Successful. Communication with Email server established")
    else:
        print("\n\n\nEmail Request Error ")
        print("Status Code:", response.status_code)
        print("------------------------ERROR MESSAGE-----------------------------")
        print(response.reason)
        print("------------------------------------------------------------------")
except requests.exceptions.ConnectionError as e:
    print("\n\n\n Connection Exception, unable to send request ")
    print("------------------------ERROR MESSAGE-----------------------------")
    print(e)
    print("------------------------------------------------------------------")
