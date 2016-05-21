# -*- coding: utf-8 -*-

import pytest
from atm.store import Store

FILE_CONTENT = """\
new_account,0\r
account_100,100\r
"""

LIST_CONTENT = [['new_account', '0'],
                ['account_100', '100']]

@pytest.fixture
def empty_file_name(tmpdir):
    empty_file = tmpdir.mkdir("bank").join("empty.csv")
    empty_file.write("")
    return str(empty_file)

@pytest.fixture
def csv_file_name(tmpdir):
    csv_file = tmpdir.mkdir("bank").join("db.csv")
    csv_file.write(FILE_CONTENT)
    return str(csv_file)


def test_store_creation():
    store = Store('some_file')
    assert store.filename == 'some_file'

def test_sotre_load(csv_file_name):
    store = Store(csv_file_name)
    it = store.load()
    assert it.next() == LIST_CONTENT[0]
    assert it.next() == LIST_CONTENT[1]
    with pytest.raises(StopIteration):
        it.next()

def test_store_iter(csv_file_name):
    store = Store(csv_file_name)
    assert list(store) == LIST_CONTENT

def test_store_save(empty_file_name):
    store = Store(empty_file_name)
    store.save(iter(LIST_CONTENT))
    with open(empty_file_name, 'rb') as non_empty_file:
        assert non_empty_file.read() == FILE_CONTENT
