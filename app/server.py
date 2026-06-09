from fastapi import FastAPI, UploadFile, File
import tempfile
import os

from app.voice_agent import VoiceAgent
from app.demo_handler import handle_voice_command

app = FastAPI(title="Plug and Play Voice Agent")

agent = VoiceAgent(handler=handle_voice_command)

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/voice")
async def process_voice(file: UploadFile = File(...)):
    suffix = os.path.splitext(file.filename)[1] or ".wav"

    with tempfile.NamedTemporaryFile(delete=False, suffix=suffix) as temp:
        temp.write(await file.read())
        audio_path = temp.name

    try:
        return agent.transcribe_file(audio_path)
    finally:
        os.remove(audio_path)
