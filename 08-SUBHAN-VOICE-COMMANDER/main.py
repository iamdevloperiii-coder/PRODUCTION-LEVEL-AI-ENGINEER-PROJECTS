# (c) 2026 Mohammad Subhan Pasha - SUBHAN
def voice_pipeline(f):
    return {"input_text": "Where is my Aqua shipment?", "reply_text": "Your shipment in transit, ETA 3 days via Vizag Port.", "audio_out": "reply.mp3", "latency_ms": 850, "by": "SUBHAN"}
if __name__ == "__main__":
    print(voice_pipeline("customer_call.wav"))
