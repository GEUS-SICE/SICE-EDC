import smtplib    
smtp = smtplib.SMTP('smtp.office365.com')    
smtp.ehlo()    
max_limit_in_bytes = int( smtp.esmtp_features['size'] )
print("john")
print(max_limit_in_bytes)
postconf -e "message_size_limit = + " str(max_limit_in_bytes * 10)