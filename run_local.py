from app.voice_agent import VoiceAgent
from app.demo_handler import handle_voice_command

agent = VoiceAgent(handler=handle_voice_command)

while True:
    result = agent.listen_from_microphone(seconds=5)
    print("Texto:", result["text"])
    print("Respuesta:", result["response"])
