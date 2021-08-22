import requests


TRIVIA_API ="https://opentdb.com/api.php?amount=10&category=18&type=boolean"

data = requests.get(TRIVIA_API)
question_data = data.json()["results"]
