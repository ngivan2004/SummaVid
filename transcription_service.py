# transcription_service.py

import whisper


def _format_timestamp(seconds: float) -> str:
    """Return HH:MM:SS representation of seconds."""
    seconds = int(seconds)
    hours = seconds // 3600
    minutes = (seconds % 3600) // 60
    secs = seconds % 60
    return f"{hours:02d}:{minutes:02d}:{secs:02d}"


class TranscriptionService:
    def transcribe(self, link, model_name, api_key):
        """Transcribe audio and return text with timestamps."""
        model = whisper.load_model(model_name)
        result = model.transcribe(audio=link, verbose=True)

        if "segments" not in result:
            return result.get("text", "")

        lines = []
        for seg in result["segments"]:
            ts = _format_timestamp(seg.get("start", 0))
            lines.append(f"[{ts}] {seg.get('text', '').strip()}")

        return "\n".join(lines)
