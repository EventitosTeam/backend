import unittest, os, sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))
from unittest.mock import patch
from io import StringIO
import smtplib
from swagger_server.mail.function import send_mail

class TestSendMail(unittest.TestCase):

    @patch('smtplib.SMTP')
    def test_send_mail(self, mock_smtp):
        # Configurar el mock SMTP
        instance = mock_smtp.return_value
        instance.starttls.return_value = (220, 'Service ready')
        instance.login.return_value = (235, 'Authentication successful')
        to_address = 'recipient@example.com'
        subject = 'Testing email sending'
        body = 'This is a test email.'
        send_mail(to_address, subject, body)
        instance.sendmail.assert_called_once()
        call_args = instance.sendmail.call_args[0]
        self.assertIn(to_address, call_args[0])
        self.assertIn(subject, call_args[1])
        self.assertIn(body, call_args[2])

    @patch('smtplib.SMTP')
    def test_smtp_error_handling(self, mock_smtp):
        # Configurar el mock SMTP para simular un error de conexión
        instance = mock_smtp.return_value
        instance.starttls.side_effect = smtplib.SMTPException('StartTLS failed')

        # Definir variables para la prueba
        to_address = 'recipient@example.com'
        subject = 'Testing email sending'
        body = 'This is a test email.'

        # Llamar a la función de enviar correo y capturar excepciones
        with self.assertRaises(smtplib.SMTPException):
            send_mail(to_address, subject, body)

if __name__ == '__main__':
    unittest.main()