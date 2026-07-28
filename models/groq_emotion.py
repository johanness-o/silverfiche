from models.groq_client import client, MODEL_NAME

EMOTION_LABELS = ["Positive", "Neutral", "Dark", "Sad", "Hopeful"]


def classify_emotion(description: str) -> str:
    prompt = f"""
You are an emotion classifier for books.

Given this book description, choose ONE dominant emotional tone from:
{", ".join(EMOTION_LABELS)}.

Return ONLY the emotion word.

Description:
{description}
"""
    resp = client.chat.completions.create(
        model=MODEL_NAME,
        messages=[{"role": "user", "content": prompt}],
        temperature=0.0,
    )
    return resp.choices[0].message.content.strip()