# important_dates_service.py

import openai


class ImportantDatesService:
    def get_dates(self, transcript, model_name, api_key):
        """Summarize transcript using GPT."""
        openai.api_key = api_key
        messages = [
            {"role": "system", "content": "You will analyze a huge transcript of a lecture and create a summary of all mentioned important dates, such as assignment, quiz, test, and final dates, in the form of a list."},
            {"role": "user", "content": transcript}
        ]
        response = openai.ChatCompletion.create(
            model=model_name,
            temperature=1,
            messages=messages
        )
        return response.choices[0].message["content"]
