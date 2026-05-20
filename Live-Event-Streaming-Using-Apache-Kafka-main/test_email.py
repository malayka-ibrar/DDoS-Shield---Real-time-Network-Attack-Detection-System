# test_email.py - Test email functionality
from ddos_detector import send_email_alert

# Test with a sample IP
send_email_alert("192.168.1.100", 150, "HIGH", "Test attack")
print("Test email sent!")