import json
from src.models.history_model import HistoryModel


# Req. 7
def test_request_history():
    json_response = json.loads(HistoryModel.list_as_json())

    for item in json_response:
        item.pop("_id", None)

    expected_response = [
        {
            "text_to_translate": "Hello, I like videogame",
            "translate_from": "en",
            "translate_to": "pt",
        },
        {
            "text_to_translate": "Do you love music?",
            "translate_from": "en",
            "translate_to": "pt",
        }
    ]

    assert json_response == expected_response
