import requests
from toripchanger import TorIpChanger
import os
import time
TOR_PASSWORD = os.environ['TOR_PASSWORD'] 
tor_ip_changer = TorIpChanger(tor_password=TOR_PASSWORD, tor_port=9051, local_http_proxy='tor-proxy:8118',tor_address="tor-proxy",reuse_threshold=0,new_ip_max_attempts=50)
import logging

if __name__ == "__main__":
    print("1 change")
    print("Current ip(with proxies): {}".format(requests.get('https://api.myip.com/', proxies={'https': 'tor-proxy:8118'}).json()))
    print("Real ip: {}".format(requests.get("https://api.myip.com/").json()))
    print("Changing IP: {}".format(tor_ip_changer.get_new_ip()))
    time.sleep(5)
    print("2 change")
    print("Current ip(with proxies): {}".format(requests.get('https://api.myip.com/', proxies={'https': 'tor-proxy:8118'}).json()))
    print("Real ip: {}".format(requests.get("https://api.myip.com/").json()))
    print("Changing IP: {}".format(tor_ip_changer.get_new_ip()))
    time.sleep(5)
    print("3 change")
    print("Current ip(with proxies): {}".format(requests.get('https://api.myip.com/', proxies={'https': 'tor-proxy:8118'}).json()))
    print("Real ip: {}".format(requests.get("https://api.myip.com/").json()))
    print("Changing IP: {}".format(tor_ip_changer.get_new_ip()))
    time.sleep(5)
    print("4 change")
    print("Current ip(with proxies): {}".format(requests.get('https://api.myip.com/', proxies={'https': 'tor-proxy:8118'}).json()))
    print("Real ip: {}".format(requests.get("https://api.myip.com/").json()))
    print("Changing IP: {}".format(tor_ip_changer.get_new_ip()))
    time.sleep(5)
    print("5 change")
    print("Current ip(with proxies): {}".format(requests.get('https://api.myip.com/', proxies={'https': 'tor-proxy:8118'}).json()))
    print("Real ip: {}".format(requests.get("https://api.myip.com/").json()))
    print("Changing IP: {}".format(tor_ip_changer.get_new_ip()))
    time.sleep(5)
    print("6 change")
    print("Current ip(with proxies): {}".format(requests.get('https://api.myip.com/', proxies={'https': 'tor-proxy:8118'}).json()))
    print("Real ip: {}".format(requests.get("https://api.myip.com/").json()))
    print("Changing IP: {}".format(tor_ip_changer.get_new_ip()))

