# -*- coding: utf-8 -*-
import pytest
from rest_requests import *


def test_get_auth_type_digest():
    url = 'http://httpbin.org/digest-auth/auth/user/passwd'
    auth_type = get_auth_type(url)
    assert auth_type == 'Digest'


def test_get_auth_type_basic():
    url = 'http://httpbin.org/basic-auth/user/passwd'
    auth_type = get_auth_type(url)
    assert auth_type == 'Basic'


def test_get_auth_type_without():
    url = 'http://httpbin.org/get'
    auth_type = get_auth_type(url)
    assert auth_type == ''


def test_check_authentication_correct_credential_basic():
    url = 'http://httpbin.org/basic-auth/user/passwd'
    username = 'user'
    password = 'passwd'
    status_code, auth = check_authentication(url, username, password)
    assert status_code == 200


def test_check_authentication_incorrect_credential_basic():
    url = 'http://httpbin.org/basic-auth/user/passwd'
    username = 'user'
    password = 'pa'
    status_code, auth = check_authentication(url, username, password)
    assert status_code == 401


def test_check_authentication_correct_credential_digest():
    url = 'http://httpbin.org/digest-auth/auth/user/passwd'
    username = 'user'
    password = 'passwd'
    status_code, auth = check_authentication(url, username, password)
    assert status_code == 200


def test_check_authentication_incorrect_credential_digest():
    url = 'http://httpbin.org/digest-auth/auth/user/passwd'
    username = 'user'
    password = 'pa'
    status_code, auth = check_authentication(url, username, password)
    assert status_code == 401


def test_check_authentication_without_auth():
    url = 'http://httpbin.org/get'
    status_code, auth = check_authentication(url)
    assert status_code == 200


@pytest.fixture(scope='function')
def without_auth_setup(request):
    url = 'http://httpbin.org/get'
    status_code, auth = check_authentication(url)
    return url, auth


@pytest.fixture(scope='function')
def basic_auth_setup(request):
    url = 'http://httpbin.org/basic-auth/user/passwd'
    username = 'user'
    password = 'passwd'
    status_code, auth = check_authentication(url, username, password)
    return url, auth


@pytest.fixture(scope='function')
def digest_auth_setup(request):
    url = 'http://httpbin.org/digest-auth/auth/user/passwd'
    username = 'user'
    password = 'passwd'
    status_code, auth = check_authentication(url, username, password)
    return url, auth


def test_make_requests_single_thread_10_without_auth(without_auth_setup):
    url, auth = without_auth_setup
    num = 10
    make_requests_single_thread(url, num, auth)


def test_make_requests_single_thread_10_basic_auth(basic_auth_setup):
    url, auth = basic_auth_setup
    num = 10
    make_requests_single_thread(url, num, auth)


def test_make_requests_single_thread_10_digest_auth(digest_auth_setup):
    url, auth = digest_auth_setup
    num = 10
    make_requests_single_thread(url, num, auth)


def test_make_requests_multi_thread_10_without_auth(without_auth_setup):
    url, auth = without_auth_setup
    num = 10
    make_requests_multi_thread(url, num, auth)


def test_make_requests_multi_thread_10_basic_auth(basic_auth_setup):
    url, auth = basic_auth_setup
    num = 10
    make_requests_multi_thread(url, num, auth)


def test_make_requests_multi_thread_10_digest_auth(digest_auth_setup):
    url, auth = digest_auth_setup
    num = 10
    make_requests_multi_thread(url, num, auth)


def test_make_requests_10_without_auth():
    url = 'http://httpbin.org/get'
    num = 10
    with pytest.raises(SystemExit):
        make_requests(url, num)


def test_make_requests_10_basic_auth():
    url = 'http://httpbin.org/basic-auth/user/passwd'
    username = 'user'
    password = 'passwd'
    num = 10
    with pytest.raises(SystemExit):
        make_requests(url, num, username, password)


def test_make_requests_10_digest_auth():
    url = 'http://httpbin.org/digest-auth/auth/user/passwd'
    username = 'user'
    password = 'passwd'
    num = 10
    with pytest.raises(SystemExit):
        make_requests(url, num, username, password)
