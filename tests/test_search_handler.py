import pytest
from search_handler import SearchHandler

@pytest.fixture
def handler():
    return SearchHandler("tests/test_data.txt", reread_on_query=False)

def test_string_exists(handler):
    assert handler.search("test_string") == "STRING EXISTS"

def test_string_not_found(handler):
    assert handler.search("non_existent_string") == "STRING NOT FOUND"