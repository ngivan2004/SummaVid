# summarization_service.py

import openai


class SummarizationService:
    def summarize(self, transcript, model_name, api_key, prompt):
        # Summarize transcript using GPT
        openai.api_key = api_key
        messages = [
            {"role": "system", "content": prompt},
            {"role": "user", "content": transcript}
        ]
        response = openai.ChatCompletion.create(
            model=model_name,
            temperature=1,
            messages=messages
        )
        return response.choices[0].message["content"]
