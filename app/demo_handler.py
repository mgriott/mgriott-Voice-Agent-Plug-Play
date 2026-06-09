def handle_voice_command(text: str):
    text_lower = text.lower()

    if "estado" in text_lower:
        return "El sistema está operativo."

    if "reporte" in text_lower:
        return "Generando reporte técnico."

    return f"Comando recibido: {text}"
