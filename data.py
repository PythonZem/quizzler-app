from requests import get
URL = "https://opentdb.com/api.php"
parameters = {
    "amount": 10,
    "type": "boolean",
    "category": 23,
    "difficulty": "medium"
}
question_data = get(url=URL, params=parameters).json()["results"]
