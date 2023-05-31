# -*- coding: utf-8 -*-
"""
Created on Thu Dec 29 11:07:40 2022

@author: rabni
"""

from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
from email.mime.text import MIMEText
import smtplib
import zipfile
import numpy as np
import glob
import os 

SMTP_SERVER = 'smtp.office365.com'
SMTP_PORT = '587'
SMTP_USERNAME = r'EDCdata@outlook.dk'
SMTP_PASSWORD = r'EDCgeus1994'

def send_mail(filename):
    # Create a multipart message
    msg = MIMEMultipart()
    body_part = MIMEText("Data From EDC", 'plain')
    msg['Subject'] = "SICE Data"
    msg['From'] = "EDCdata@outlook.dk"
    msg['To'] = "EDCdata@outlook.dk"
    # Add body to email
    msg.attach(body_part)
    # open and read the file in binary
    with open(filename,'rb') as file:
    # Attach the file with filename to the email
        msg.attach(MIMEApplication(file.read(), Name = filename))

    # Create SMTP object
    smtp_obj = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
    smtp_obj.ehlo()
    smtp_obj.starttls()
    
    # Login to the server
    smtp_obj.login(SMTP_USERNAME, SMTP_PASSWORD)

    # Convert the message to a string and send it
    smtp_obj.sendmail(msg['From'], msg['To'], msg.as_string())
    smtp_obj.quit()
    
    
    
    

basefolder = "output/sice_500_2021_08_"
#basename = "sice_500_2017_09_"


for d in np.arange(0,31):
    day = str(d + 1)
    day = day.zfill(2)
    dir_name = basefolder + day
    files = glob.glob(dir_name + os.sep + "*.tif")
    
    for fname in files:
        if (fname[-7:] == "ter.tif"):
            output_filename = dir_name + "_" + fname.split(os.sep)[-1][:-4] + "_zipped.zip"
            zout = zipfile.ZipFile(output_filename, "w", zipfile.ZIP_LZMA)
            zout.write(fname)
            zout.close()
            send_mail(output_filename)
        
                                        
   

   
