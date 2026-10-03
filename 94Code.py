messages = [
    {"text": "Hello", "score": 0.9},
    {"text": "Bad message", "score": 0.3},
    {"text": "Great answer", "score": 0.8},
    {"text": "Poor answer", "score": 0.2}
]

print([message["text"] for message in messages if message["score"] >=.8])