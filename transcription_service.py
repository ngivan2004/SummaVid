# transcription_service.py

import whisper


class TranscriptionService:
    def transcribe(self, link, model_name, api_key):
        """Transcribe audio using Whisper."""
        model = whisper.load_model(model_name)
        result = model.transcribe(audio=link, verbose=True)
        return result["text"]
