from models.groq_client import client, MODEL_NAME


def enrich_vocab_word(word: str, context: str = "") -> dict:
    prompt = f"""
You are a vocabulary tutor.

For the word: "{word}"

Context (optional):
{context}

Return:
- definition
- 3 synonyms
- 1 example sentence
- difficulty (1-5, 1 = very easy, 5 = very hard)

Format as JSON with keys:
definition, synonyms, example, difficulty.
"""
    resp = client.chat.completions.create(
        model=MODEL_NAME,
        messages=[{"role": "user", "content": prompt}],
        temperature=0.2,
    )
    import json
    content = resp.choices[0].message.content
    return json.loads(content)