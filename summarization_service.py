# summarization_service.py

import openai


class SummarizationService:
    def summarize(self, transcript, model_name, api_key):
        """Summarize transcript using GPT."""
        openai.api_key = api_key
        messages = [
            {"role": "system", "content": "You will analyze a huge transcript from a video and create a summary in the form of a list useful to the audience. Include important information in the summary. Translate to English if needed."},
            {"role": "user", "content": transcript}
        ]
        response = openai.ChatCompletion.create(
            model=model_name,
            temperature=1,
            messages=messages
        )
        return response.choices[0].message["content"]
