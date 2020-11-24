# GmailEgoNetwork




## How to run
* Clone or download repository
* Go to https://developers.google.com/gmail/api/quickstart/python
    * In Step 1 Click this button to create a new Cloud Platform project and automatically enable the Gmail API
    * In resulting dialog click _DOWNLOAD CLIENT CONFIGURATION_ and save the file credentials.json to your working directory.
*  Install dependencies
```
pip3 install --upgrade google-api-python-client google-auth-httplib2 google-auth-oauthlib
```
*  Download emails from Gmail account as CSV
```
python3 main.py
```
* Create edges between emails
```
python3 analysis_email.py
```
* Create edges between domains, ignore same domain in recipient and sender
```
python3 analysis_domain.py
```
* Create edges between words in same email subject
```
python3 analysis_subject.py
```
