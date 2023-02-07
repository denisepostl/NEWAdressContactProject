import sqlite3
import logging
import pytest

try:
    import adress
except ModuleNotFoundError as e:
    logging.error("Module not found %s", e)


def test_query_search_by_invalid_input():
    """Test the output if invalid Names are used."""
    query = adress.QuerySearchBy()
    query.askin_query('Jane', 'Doe')
    assert query.contact == []


def test_query_search_by_empty_input():
    """Test the output if no Names are used."""
    query = adress.QuerySearchBy()
    query.askin_query('', '')
    assert query.contact == []


def test_query_search_by_null_input():
    """Test the output by null input."""
    query = adress.QuerySearchBy()
    query.askin_query(None, None)
    assert query.contact == []


def test_query_search_by_valid_input():
    """Test if the output is correct"""
    query = adress.Ask()
    query.askin('Daniel', 'Sonnleitner')
    assert query.contacts == [('Daniel', 'Sonnleitner', 'Hartberg', '8230', 'Hartberg', '012', '0641212')]
