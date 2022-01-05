"""precisa atualizar pois nao esta funcionando devido asnovas atualizacoes do googel"""

from string import Template
from datetime import datetime
import os

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
import smtplib


def atual_path() -> str:
    caminho = os.path.realpath(__file__)
    caminho = caminho.split('\\')
    caminho.pop()
    return '\\'.join(caminho)

meu_email = ''
minha_senha = ''
email_clinte = ''

with open(atual_path() + '\\template.html') as html:
    template = Template(html.read())
    data_atual = datetime.now().strftime('%d/%m/%Y')
    corpo_msg = template.safe_substitute(nome='William Ribeiro', data=data_atual)

msg = MIMEMultipart()
msg['from'] = 'William Riberio'
msg['to'] = email_clinte
msg['subject'] = 'Email de teste'

with open(atual_path() + '\\angular.png', 'rb') as imgfile:
    img = MIMEImage(imgfile.read())
    msg.attach(img)

corpo = MIMEText(corpo_msg, 'html')
msg.attach(corpo)


with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    smtp.ehlo_or_helo_if_needed()
    smtp.starttls()
    smtp.login(meu_email, minha_senha)
    smtp.send_message(msg)

