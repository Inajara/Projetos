import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import schedule
import time

# Função para enviar e-mail
def enviar_email(relatorio):
    # Configurações do servidor SMTP do remetente
    remetente_email = 'seu_email@gmail.com'  # Substitua pelo seu e-mail
    remetente_senha = 'sua_senha'  # Substitua pela sua senha
    destinatario_email = 'destinatario@email.com'  # Substitua pelo e-mail do destinatário

    # Criando a mensagem
    msg = MIMEMultipart()
    msg['From'] = remetente_email
    msg['To'] = destinatario_email
    msg['Subject'] = 'Relatório Diário'

    # Corpo da mensagem
    corpo = relatorio
    msg.attach(MIMEText(corpo, 'plain'))

    # Configuração do servidor SMTP
    servidor_smtp = 'smtp.gmail.com'  # Servidor SMTP do Gmail
    porta_smtp = 587  # Porta para conexão TLS

    # Criando uma conexão segura com o servidor SMTP
    server = smtplib.SMTP(host=servidor_smtp, port=porta_smtp)
    server.starttls()
    server.login(remetente_email, remetente_senha)

    # Enviando o e-mail
    texto_email = msg.as_string()
    server.sendmail(remetente_email, destinatario_email, texto_email)

    # Encerrando a conexão
    server.quit()

    print('E-mail enviado com sucesso para', destinatario_email)

# Função para gerar o relatório diário (substitua esta função com sua lógica de geração de relatório)
def gerar_relatorio():
    # Aqui você pode colocar a lógica para gerar o relatório
    relatorio = "Este é o relatório diário."

    # Chamando a função para enviar e-mail com o relatório gerado
    enviar_email(relatorio)

# Agendando o envio do relatório diariamente
schedule.every().day.at("08:00").do(gerar_relatorio)  # Horário pode ser ajustado conforme necessário

# Loop para verificar o agendamento
while True:
    schedule.run_pending()
    time.sleep(60)  # Aguarda 60 segundos antes de verificar novamente

