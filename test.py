import pytest
import requests
from unittest.mock import patch
from main import get_random_cat_image  # Замените 'your_module' на имя вашего файла


def test_get_random_cat_image_success():
    # Имитация успешного ответа от TheCatAPI
    with patch('requests.get') as mock_get:
        mock_response = mock_get.return_value
        mock_response.status_code = 200
        mock_response.json.return_value = [{'url': 'https://example.com/cat.jpg'}]

        result = get_random_cat_image()

        assert result == 'https://example.com/cat.jpg'
        mock_get.assert_called_once_with("https://api.thecatapi.com/v1/images/search")


def test_get_random_cat_image_failure():
    # Имитация неуспешного ответа от TheCatAPI (например, 404)
    with patch('requests.get') as mock_get:
        mock_response = mock_get.return_value
        mock_response.status_code = 404
        mock_response.raise_for_status.side_effect = requests.exceptions.HTTPError

        result = get_random_cat_image()

        assert result is None
        mock_get.assert_called_once_with("https://api.thecatapi.com/v1/images/search")
