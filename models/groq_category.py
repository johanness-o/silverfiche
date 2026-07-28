from models.groq_client import client, MODEL_NAME

TARGET_CATEGORIES = [
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


def normalize_category(raw_category: str) -> str:
    prompt = f"""
You normalize messy book categories.

Map this category to ONE of:
{", ".join(TARGET_CATEGORIES)}.

Return ONLY the target category.

Raw category:
{raw_category}
"""
    resp = client.chat.completions.create(
        model=MODEL_NAME,
        messages=[{"role": "user", "content": prompt}],
        temperature=0.0,
    )
    return resp.choices[0].message.content.strip()