# PythonProject


Calculate the number of responses from employees for a certain year and month   To run this project, first we have to download few dependencies, P.s (I have used venv(python virtual environment)   If you have python installed then to activate the the virtual environment  here are the few steps  
1.  pip install virtualenv (install virtual environment)
2.  virtualenv mypython (To create a virtual environment, you must specify a path. For example to create one in the local directory called ‘mypython’, type the following command above)
3.  source mypython/bin/activate (ctivate the python environment by running the following command above) 


After that, 
Let’s get you set up for your first Google Drive API project.
First, go to https://console.developers.google.com/ from your browser. This will take you to Google Console page (just like AWS console page, if you’re familiar with it) where you can manage your API and services, IAM and admin.

If this is your first time, from the left navigation bar, go to APIs & Services > Dashboard.
￼

It will bring you to Google API & Services Dashboard where it lists all the projects you have, if any. But, since this is your first time, you will have no project listed. Go on and click on CREATE.

￼


Now, you will land on a page where you can create a new project and specify the name of it (and Organization, if you manage an organisation or else you can leave this blank). In this example, we will name our project as First Medium Project. Go on and click on CREATE.

The first thing we need to do is to enable the Google Sheets API. Now, open your browser and go to https://console.developers.google.com/apis/dashboard. Then, make sure you are on the right project and if not, select the right project from the drop down list.

Go ahead and click on it. Once you land on the Google Sheets API page, click on the ENABLE button to enable this API.
￼


￼

After that, if you just go to the Credentials tab, you will see that it says our credentials we set up earlier for Google Drive API is compatible with the Sheets API. This means we can use the credentials that we already have and set up for our script. 🙂


Create Credentials
After you enable the Google Drive API, it’s time to create credentials so that you application can authenticate itself when trying to access Google Drive resources later on.


￼


At first, it might be overwhelming to choose the type of credentials that you need. Google has done a great job in creating a set of questions to help you figure out which credentials to create. Just follow the instructions on the next few photos


￼
 In the above screenshot, select the Google Sheets Api 



Set Up OAuth Consent Screen and Add API Scope
After you fill up the above questionnaire, Google will recommend that you application requires the OAuth client ID and before you can set this up, you need to set up OAuth consent screen.

￼


￼




Now, we are going to add the scope that we want our application to be able to do. Scope is like giving permissions to our credentials which then determine what our application has access to. For this tutorial, we need our application to be able to see, download, create, edit and delete all of your files in Google Drive. (You can include whatever scope you would like here, best practice is to only include what your application will do).

￼

After that, select all checkboxes 


￼


Once finished, click the Add button and then it will take us to the previous page. Go on and click Save.



Create Credentials: Client Secret (OAuth Client ID)
Next, we are going to add our credentials so that Google can identify who our application is and what scope it has, etc. This is known as the Client Secret. Go on and click on Create credentials > OAuth client ID.

￼


For this, we are going to select Other as our Application type as we will build a command line application. But, you can choose whatever type of application you want to build.

￼


After this step, you are going to have your Client Secret, which you can download so your application can use it to authenticate itself. Go on and click on the Download, which is the down arrow icon. Your client secret is a JSON file. Rename it to client_secret.json.



￼


In order to be able to access the API resources, we need to get the access token. Since the API resources that we want to access contain sensitive scope (accessing files in Google Drive), we need to do a browser authentication for the first time.




MacBook-Pro:~ bobthedude$ virtualenv venv_google_api
MacBook-Pro:~ bobthedude$ source venv_google_api/bin/activate
# install all the dependent packages
(venv_google_api) MacBook-Pro:~ bobthedude$ pip install google-api-python-client oauth2client



Create a folder in the project directory called credentials to store your client_secret.json which you can download from your Google Console


Your project structure should look like this to begin with. The connect_to_google_drive.py is the Python file that contains instructions to connect to Google Drive API.


￼


Let’s write the code that needs to go into connect_to_google_drive.py.

from apiclient import discovery
from httplib2 import Http
from oauth2client import client, file, tools


# define path variables
credentials_file_path = './credentials/credentials.json'
clientsecret_file_path = './credentials/client_secret.json'

# define API scope
SCOPE = 'https://www.googleapis.com/auth/drive'

# define store
store = file.Storage(credentials_file_path)
credentials = store.get()
# get access token
if not credentials or credentials.invalid:
    flow = client.flow_from_clientsecrets(clientsecret_file_path, SCOPE)
    credentials = tools.run_flow(flow, store)




Your access token will be stored in credentials/credentials.json upon the browser authentication, which I will go through after this.
Now, save the file and go to your terminal. Follow below commands to get your access token. Note: if you execute the above script from an IDE (I use PyCharm), you would get an error. For the first time only, you need to execute the script from your terminal

￼


A browser tab will open after the above command execution. Select the Google account on which you set up your API and credentials in the previous step. Then click on Allow.


￼


Once again, Google will prompt you and ask for a confirmation if you want to allow your First Medium Application to access your Google Drive files. Go on and click on Allow.

￼


If successful, your browser will return a page with the following text The authentication flow has completed. And if you go back to your terminal, you should see an additional 2 lines (indicating authentication success) printed as follows.


￼


Additionally, you will see a new file credentials.json gets created in the credentials folder. Awesome job! We have now obtained our access token which we can use to connect to Google Drive API resources.


￼


After the credentials verification   

Nice! Our code becomes so much cleaner and easier to follow now. 🙂
With this new main.py script, the way we can call it from the command line is as follows



With this new main.py script, the way we can call it from the command line is as follows

Run this program   $ python main.py --spreadsheet-name "Christmas Plan" --sheet-name Sheet2

It would download the csv and then you can apply the logic to get the desired luck 
