import pytest
from unittest.mock import patch 
from src.util.detector import detect_duplicates


# develop your test cases here

@pytest.mark.unit
@patch("src.util.parser.parse")
def test_detect_duplicates_only_one_artical(mock_parse):
    data = [{"key": "12345",
    "doi": "20020"}]
    mock_parse.return_value = data
    with pytest.raises(ValueError):
        detect_duplicates(data)

@pytest.mark.unit
def test_detect_duplicates_no_dublicate():
    data = [{"key": "12345",
    "doi": "20020"},{"key": "12343",
    "doi": "20202"}]
    expect = [""]
    with patch("src.util.parser.parse") as mock_pars:
        mock_pars.return_value = data
        assert detect_duplicates(data) == expect


@pytest.mark.unit
@patch("src.util.parser.parse")
def test_detect_duplicates_dublict_DOI_no_dublicat_key():
    data = [{"key": "12345",
    "doi": "20020"},{"key": "12343",
    "doi": "20020"}]
    expect = [{"key": "12345",
    "doi": "20020"}]
    with patch("src.util.parser.parse") as mock_pars:
        mock_pars.return_value = data
        assert detect_duplicates(data) == expect

@pytest.mark.unit
def test_detect_duplicates_no_DOI_and_not_dublicat_key():
    data = [{"key": "12345",
    "doi": ""},{"key": "12343",
    "doi": ""}]
    expect = [""]
    with patch("src.util.parser.parse") as mock_pars:
        mock_pars.return_value = data
        assert detect_duplicates(data) == expect

@pytest.mark.unit
def test_detect_duplicates_one_no_DOI_and_not_dublicat_key():
    data = [{"key": "12345",
    "doi": ""},{"key": "12343",
    "doi": "20202"}]
    expect = [""]
    with patch("src.util.parser.parse") as mock_pars:
        mock_pars.return_value = data
        assert detect_duplicates(data) == expect

@pytest.mark.unit
def test_detect_duplicates_one_no_DOI_and_dublicat_key():
    data = [{"key": "12345",
    "doi": ""},{"key": "12345",
    "doi": "20202"}]
    expect = [{"key": "12345",
    "doi": "20202"}]
    with patch("src.util.parser.parse") as mock_pars:
        mock_pars.return_value = data
        assert detect_duplicates(data) == expect

@pytest.mark.unit
def test_detect_duplicates_no_DOI_and_dublicat_key():
    data = [{"key": "12345",
    "doi": ""},{"key": "12345",
    "doi": ""}]
    expect = [{"key": "12345",
    "doi": ""}]
    with patch("src.util.parser.parse") as mock_pars:
        mock_pars.return_value = data
        assert detect_duplicates(data) == expect