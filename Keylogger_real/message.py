from smtplib import SMTP
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
from email.mime.base import MIMEBase
from email.encoders import encode_base64
from datetime import datetime


def sendMail(emisor,receptor,psw,nombreimg,ruta_img,ruta_txt):
    print("Enviando mensaje....")
    msg = MIMEMultipart()
    msg['From']=emisor
    msg['To']=receptor
    msg['Subject']=nombreimg

    image = open(ruta_img, "rb")
    file_txt = open(ruta_txt,"rb")
    attach_image = MIMEImage(image.read())
    attach_txt = MIMEBase("application","octect-stream")
    attach_txt.set_payload(file_txt.read())
    attach_image.add_header('Content-Disposition', 'attachment; filename = {}.png'.format(nombreimg))
    attach_txt.add_header('Content-Disposition', 'attachment; filename = {}.txt'.format(msg['Subject']))
    msg.attach(attach_image)
    msg.attach(attach_txt)

    mailServer = SMTP('smtp.gmail.com',587)
    #mailServer.ehlo()
    mailServer.starttls()
    #mailServer.ehlo()
    mailServer.login(msg['From'],psw)

    mailServer.sendmail(msg['From'], msg['To'], msg.as_string())

    mailServer.close()
    print("Mensaje enviado.")
