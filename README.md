# Wake Up Safe Connection Test

### Prerequisites

- python >= 3.8.13
- requests >= 2.28.1

Clone this repository and run the following command
```
python test_connection.py
````

You will be asked to enter your email address (to verify if the WUS email server is able to send you emails) 
This script will test the connection to the following:
- Wake Up Safe test website. 
- Wake Up Safe test API
- Wake Up Safe production website
- Wake Up Safe production API

Additionally, you will receive two test emails one from our test server and one from our production server. 

If all tests pass you will see an success message in your command line as shown in the following image. You can also find a screenshot of a test email that you will receive from the wake up safe email server. 

**Success Message**<br>
<img width="802" alt="image" src="https://user-images.githubusercontent.com/23667069/210029788-30f79fc8-ab30-48b1-94b9-67bb32fe7db6.png">

If there is an issue establishing the connection, you will see an error (example shown below). Please reach out to the Wake Up Safe support team with the error message to get it resolved. 

**Error Message**
<img width="1042" alt="image" src="https://user-images.githubusercontent.com/23667069/210029662-b7f40d91-cfbc-4fea-8fc9-a032363bcc4c.png">

**Sample of the test email**


Once you have finished running this script please fill out this <a href="https://forms.gle/TSxQupnFK53GmEBz7" target="_blank">form</a>
