# Keylogger with Encrypted Logging & Email Reporting

## Description
This is a simple Python keylogger that logs keystrokes, encrypts them before saving, and periodically sends the **decrypted logs via email**. After sending an email, the log file is cleared to prevent duplication.

## Features
- Logs **all keystrokes** and timestamps.
- **Encrypts** logs before saving them to a file.
- **Decrypts** logs before sending them via email.
- **Sends an email every 5 minutes** (300 seconds) with captured keystrokes.
- **Clears the log file** after sending the email.

## Installation & Setup

### 1. **Download from GitHub**
Clone the repository from GitHub:
```bash
git clone https://github.com/daly260/keylogger-project.git
cd keylogger-project
```

### 2. **Install Required Modules**
Make sure you have Python installed. Then, install the required modules:
```bash
pip install pynput
```

### 3. **Enable Gmail SMTP Access**
Since Google blocks direct login from less secure apps, you need to generate an **App Password**:
1. Go to [Google App Passwords](https://myaccount.google.com/apppasswords).
2. Select "Mail" and "Windows Computer" as the app.
3. Generate and **copy the password**.
4. Replace `your_email@gmail.com` and `your_app_password` in the script.

### 4. **Run the Script**
Run the keylogger script using:
```bash
python keylogger.py
```

## How It Works
1. The script starts listening for keystrokes.
2. Keystrokes are encrypted and saved in `keylog.txt`.
3. Every **5 minutes**, the script:
   - Reads `keylog.txt`.
   - **Decrypts** the content.
   - Sends an email with the logs.
   - **Clears** the log file to prevent duplicate logs.

## Notes
- This script is for **educational and ethical security testing purposes only**.
- Using keyloggers **without permission is illegal**.
- **Antivirus software may detect and block the script**. You might need to add an exclusion.

## Future Improvements
- Add **stealth mode** (run the script in the background).
- Save logs to a **remote server** instead of email.
- Improve **encryption** for better security.

---
### **Disclaimer**
**Use this script responsibly. Unauthorized use of keyloggers is illegal and punishable by law.**

