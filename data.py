import html
import requests
# Function to fetch quiz data with parameters
def fetch_quiz_data(amount=10, question_type="boolean"):
    url = "https://opentdb.com/api.php"
    params = {
        "amount": amount,
        "type": question_type
    }
    response = requests.get(url, params=params)
    response.raise_for_status()
    data = response.json()

    # Process and clean up the data
    question_data = [
        {
            "question": html.unescape(item['question']),
            "correct_answer": html.unescape(item['correct_answer'])
        }
        for item in data['results']
    ]
    return question_data

question_data = fetch_quiz_data(amount=10, question_type="boolean")
