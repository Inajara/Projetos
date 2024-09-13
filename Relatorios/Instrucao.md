Para automatizar o envio de relatórios diários por e-mail usando Python, podemos usar a biblioteca `smtplib` para enviar e-mails e `schedule` para agendar a execução do script diariamente. Aqui está um exemplo de script que envia um relatório diário por e-mail:

### Script Python para Envio de Relatórios Diários por E-mail

```python
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

```

### Configuração

Para configurar e executar este script:

1. **Instale as bibliotecas necessárias:**
   Certifique-se de ter instaladas as bibliotecas `smtplib`, `schedule` e `email`. Se não tiver, instale usando `pip`:

   ```
   pip install schedule
   ```

2. **Configure as credenciais do remetente:**
   - Substitua `'seu_email@gmail.com'` pela sua própria conta de e-mail.
   - Substitua `'sua_senha'` pela senha da sua conta de e-mail (recomenda-se utilizar variáveis de ambiente para não expor senhas diretamente no código).

3. **Configure o destinatário:**
   - Substitua `'destinatario@email.com'` pelo e-mail do destinatário do relatório.

4. **Defina a lógica para gerar o relatório:**
   - A função `gerar_relatorio()` contém um exemplo simples. Você deve substituir esta função com a lógica real para gerar o seu relatório diário.

5. **Agende o envio do relatório:**
   - A linha `schedule.every().day.at("08:00").do(gerar_relatorio)` agendará a função `gerar_relatorio()` para ser executada todos os dias às 08:00. Você pode ajustar o horário conforme necessário.

6. **Execute o script:**
   - Execute o script Python. Ele ficará em um loop verificando se há tarefas agendadas para serem executadas.

Este script configura um sistema simples para enviar um relatório diário por e-mail usando Python. Certifique-se de ajustar e testar o script de acordo com suas necessidades específicas antes de colocá-lo em produção.