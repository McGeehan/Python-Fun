import smtplib
 
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login("mmcgeehan@paduaacademy.org", "tera4815162342soup")
 
msg = "YOUR MESSAGE!"
server.sendmail("mmcgeehan@paduaacademy.org", "mmcgeehan@paduaacademy.org", hi)
server.quit()
