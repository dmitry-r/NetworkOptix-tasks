# -*- coding: utf-8 -*-
import argparse
import json
import sys
from datetime import datetime

import grequests
import requests
from requests import ConnectionError
from requests.auth import HTTPDigestAuth, HTTPBasicAuth


def get_auth_type(url):
    try:
        r = requests.get(url)
    except ConnectionError, e:
        print(e)
        exit(1)
    auth_type = r.headers.get('WWW-Authenticate', '').split(' ')[0]
    return auth_type


def check_authentication(url, username='', password=''):
    auth_type = get_auth_type(url)
    if auth_type == 'Basic':
        if not (username or password):
            print('Basic authentication')
            username = raw_input('Username: ')
            password = raw_input('Password: ')
        auth = HTTPBasicAuth(username, password)
    elif auth_type == 'Digest':
        if not (username or password):
            print('Digest authentication')
            username = raw_input('Username: ')
            password = raw_input('Password: ')
        auth = HTTPDigestAuth(username, password)
    else:
        auth = None

    r = requests.get(url, auth=auth)
    try:
        json_obj = r.json()
        print('\nJSON from response: ')
        print(json.dumps(json_obj, indent=4, sort_keys=True))
    except ValueError:
        print('\nNo JSON object')
    return r.status_code, auth


def make_requests_single_thread(url, num, auth):
    print('\nSingle thread:')
    print('URL: ' + url)
    print('Number of requests: ' + str(num))
    t1 = datetime.now()
    for i in xrange(num):
        r = requests.get(url, auth=auth)
        print('Status code: ' + str(r.status_code))
    t2 = datetime.now()
    return (t2 - t1).total_seconds()


def make_requests_multi_thread(url, num, auth):
    print('\nMulti-thread:')
    print('URL: ' + url)
    print('Number of requests: ' + str(num))
    rs = (grequests.get(url, auth=auth) for i in range(num))
    t1 = datetime.now()
    r_list = grequests.map(rs)
    t2 = datetime.now()

    for r in r_list:
        print('Status code: ' + str(r.status_code))
    return (t2 - t1).total_seconds()


def make_requests(url, num, username='', password=''):
    status_code, auth = check_authentication(url, username, password)
    if status_code != 200:
        print('\nAuthentication failed')
        exit(1)
    time_single_thread = make_requests_single_thread(url, num, auth)
    time_multi_thread = make_requests_multi_thread(url, num, auth)
    print('\nUsing single thread: ' + str(time_single_thread) + ' seconds')
    print('Using multi-thread: ' + str(time_multi_thread) + ' seconds')
    print('Difference: ' + str(time_single_thread - time_multi_thread) + ' seconds')
    exit()


def parse_args(args):
    parser = argparse.ArgumentParser(description='Comparison of time successively and concurrent requests')
    parser.add_argument('url', type=str, help='URL')
    parser.add_argument('-n', '--number', type=int, default=1, help='Number of requests')
    parser.add_argument('-u', '--user', type=str, help='user')
    parser.add_argument('-p', '--password', type=str, help='password')
    if not args:
        parser.print_help()
    args = parser.parse_args()
    if not args.url.startswith('http://'):
        print('URL must starts with http://')
        exit(1)
    return parser.parse_args()


if __name__ == '__main__':
    args = parse_args(sys.argv[1:])
    if args.url:
        make_requests(args.url, args.number, args.user, args.password)
