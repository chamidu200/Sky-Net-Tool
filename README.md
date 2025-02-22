# Wi-Fi & Drone Hacking Tools

<p align="center">
  <img src="https://github.com/chamidu200/Sky-Net-Tool/blob/b5698ca4348f527510730f99cc577b51bc5b8814/Drone.jpeg" alt="Wi-Fi & Drone Hacking" />
</p>

## ⚠️ Disclaimer

<p align="center">
  <img src="https://github.com/chamidu200/Sky-Net-Tool/blob/44a8bc5829f05cef1235f01080c326106d476e81/Capture.PNG" alt="Warning Image" />
</p>
**This tool is strictly for educational and ethical penetration testing purposes only.** Unauthorized use of this tool for malicious activities is illegal and punishable by law. Use responsibly and only on networks you own or have explicit permission to test.

---

## 🚀 Features
- **Evil Twin Attack** - Fake Access Point impersonation
- **SSLStrip** - Intercept HTTPS traffic
- **Captive Portal** - Phishing Wi-Fi login pages
- **Continuous Deauthentication Attack** - Disconnect users from Wi-Fi
- **DNS Spoofing Attack** - Redirect DNS queries
- **Wi-Fi Signal Monitoring**
- **Drone Signal Jamming & GPS Spoofing**

---

## 🛠️ Installation
```bash
sudo apt update && sudo apt install aircrack-ng ettercap sslstrip
```
Ensure you have **Python3** installed:
```bash
sudo apt install python3
```

Clone the repository:
```bash
git clone https://github.com/your-repo/wifi-drone-tools.git
cd wifi-drone-tools
```

---

## 🔥 Usage
Run the tool:
```bash
python3 tool.py
```
Select the desired attack:
1. Wi-Fi Tools
2. Drone Tools

Follow the prompts to execute your attack of choice.

### Example: Evil Twin Attack
```bash
Enter interface: wlan0
Enter Real BSSID: 00:11:22:33:44:55
Enter Real ESSID: MyWiFi
```

---

## 📜 Logging
All attacks are logged in `attack_log.csv` for reference.

---

## 📌 Important Notes
- Run the script with `sudo` to ensure proper permissions.
- Ensure monitor mode is enabled on your Wi-Fi adapter.
- **Use only for ethical hacking purposes.**

---

## 📢 Contributing
Feel free to fork and contribute! Submit a pull request with your improvements.

---

## 📧 Contact
For any queries, contact: `your-email@example.com`

---

© 2025 Wi-Fi & Drone Hacking Tools | Ethical Hacking Only

