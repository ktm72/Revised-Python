class EmailService:

  def _connect(self):
    print("connecting .....")

  def _authenticate(self):
    print("authenticating .....")

  def send_email(self):
    self._connect()
    self._authenticate()
    print(f"Sending email")
    self._disconnect()
  
  def _disconnect(self):
    print("disconnecting .....")

email = EmailService()
email.send_email()