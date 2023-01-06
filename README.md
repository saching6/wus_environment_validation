# Wake Up Safe Connection Test

This test is to verify if the hospital network is able to communicate with the Wake Up Safe website. The script will run tests to check if your hospital systems are able to access our _**beta**_ and _**production**_ servers. Please report any errors or issues in the feedback form.

This script will test access to the following:

1. Wake Up Safe beta website. 
2. Wake Up Safe beta API
3. Wake Up Safe beta Email server
4. Wake Up Safe production website
5. Wake Up Safe production API
6. Wake Up Safe production Email server

### Prerequisites 

- python >= 3.8.13
- requests >= 2.28.1


### Steps to test the connection with Wake Up Safe servers

1. Clone this repository and run the following command
  ```
  python test_connection.py
  ````
2. **Feedback:** Once you have finished running this script please fill out this <a href="https://forms.gle/TSxQupnFK53GmEBz7" target="_blank">form</a>. If you see any error messsages, please put them in this form.  

### Output

_You will be asked to enter your organizational email address as soon as you run the script. This is to test the accessibility and availailibility of our email service._ 


You should see a command line output with Success or Error messages for each of these steps.
For 3 and 6, you will also receive two test emails one from our test server and one from our production server. 

If all tests pass you will see an success message in your command line as shown in the following image. You can also find a screenshot of a test email that you will receive from the wake up safe email server. 

**Success Message**<br>
<img width="756" alt="image" src="https://user-images.githubusercontent.com/23667069/211047939-1ed4bad9-604d-40a2-ae7e-9fa6503916de.png">


If there is an issue establishing the connection, you will see an error (example shown below). Please reach out to the Wake Up Safe support team with the error message to get it resolved. 

**Error Message**
<img width="1433" alt="image" src="https://user-images.githubusercontent.com/23667069/211054383-fc38d544-86db-46f5-8199-709a814ef052.png">

**Sample of the test email**
<img width="1215" alt="image" src="https://user-images.githubusercontent.com/23667069/210497848-33286280-c05d-418e-a1e7-b8d9d4f5688a.png">



