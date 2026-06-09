from faster_whisper import WhisperModel
import sounddevice as sd
from scipy.io.wavfile import write
import tempfile
import os

class VoiceAgent:
    def __init__(self, handler, model_size="base", device="cpu"):
        self.handler = handler
        self.model = WhisperModel(model_size, device=device, compute_type="int8")

    def listen_from_microphone(self, seconds=5, sample_rate=16000):
        print("Escuchando...")
        audio = sd.rec(
            int(seconds * sample_rate),
            samplerate=sample_rate,
            channels=1,
            dtype="int16"
        )
        sd.wait()

        with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as f:
            write(f.name, sample_rate, audio)
            path = f.name

        try:
            return self.transcribe_file(path)
        finally:
            os.remove(path)

    def transcribe_file(self, audio_path: str):
        segments, _ = self.model.transcribe(audio_path, language="es")
        text = " ".join(segment.text.strip() for segment in segments)

        if not text:
            return {"text": "", "response": None}

        response = self.handler(text)

        return {"text": text, "response": response}
