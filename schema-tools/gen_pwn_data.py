#!/usr/bin/python3
import sys
import elasticsearch
from datetime import datetime
import random
from random import randrange
from datetime import timedelta


def random_ip():
    """
    :return:  tuple for IP & hostname
    """
    hosts = {"10.0.0.10": "DC01", "10.0.0.11": "Win7-dev", "10.0.1.12": "ubuntu-dns",
             "10.0.1.13": "centos-web", "10.0.0.14": "Win10", "10.0.1.15": "PfSense"}

    return list(random.choice(list(hosts.items())))


def random_proc():
    """
    :return:  string for random value
    """

    procs = ["calc", "explorer.exe", "sshd", "pam", "bind", "svchost"]
    random.shuffle(procs)
    return procs[0]


def random_date(start, end):
    """
    This function will return a random datetime between two datetime 
    objects.
    """
    delta = end - start
    #int_delta = (delta.days * 24 * 60 * 60) + delta.seconds
    int_delta = (2* 24 * 60 * 60)
    random_second = randrange(int_delta)
    return start + timedelta(seconds=random_second)

def random_time():
    """
    :return: return time for callback time
    """

    d1 = datetime.strptime('11/13/2020 12:00 AM', '%m/%d/%Y %I:%M %p')
    d2 = datetime.strptime('11/15/2020 11:50 PM', '%m/%d/%Y %I:%M %p')
    return (random_date(d1, d2))


def random_agent():
    """
    :return: random agent name
    """
    agents = ["molevar", "CS", "meterpreter", "pam_bd", "reptile", "poshc2", "merlin"]
    random.shuffle(agents)
    return agents[0]


def get_user():
    """
    :return random user for graphs
    """
    users = ["user_1", "user_2", "user_3", "user_4", "user_5"]
    random.shuffle(users)
    return users[0]

if __name__ == '__main__':

    while True:
        pwn_dict = {"@timestamp": random_time(),
                    "Host": random_ip()[1],
                    "IPv4": random_ip()[0],
                    "Agent": random_agent(),
                    "Proc": random_proc(),
                    "PID": random.randint(0, 65535),
                    "operator": get_user()
                    }

        try:
            es = elasticsearch.Elasticsearch(['localhost'], scheme="http", port=9200)
            print(pwn_dict)
            es.index(index="pwn", body=pwn_dict)
        except elasticsearch.ConnectionError as con_error:
            print("[!] Connection error!\n %s" % con_error)
            sys.exit(1)

