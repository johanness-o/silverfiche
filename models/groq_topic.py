from models.groq_client import client, MODEL_NAME

TOPIC_LABELS = [
    "Fiction",
    "Nonfiction",
    "Fantasy",
    "Science",
    "History",
    "Romance",
    "Mystery",
    "Biography",
    "Young Adult",
    "General",
]


def classify_topic(description: str) -> str:
    prompt = f"""
You are a book topic classifier.

Given this book description, choose ONE best topic from:
{", ".join(TOPIC_LABELS)}.

Return ONLY the topic word.

Description:
{description}
"""
    resp = client.chat.completions.create(
        model=MODEL_NAME,
        messages=[{"role": "user", "content": prompt}],
        temperature=0.0,
    )
    return resp.choices[0].message.content.strip()