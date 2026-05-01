from transformers import pipeline

classifier = pipeline("sentiment-analysis")

texts = input("Enter items separated by comma: ").split(",")


def single_text_analyzer(text):
    result = classifier(text)[0]
    return {
        "label": result["label"],
        "score": round(result["score"] * 100, 2),
        "emoji": "😊" if result["label"] == "POSITIVE" else "😞"
    }


def multiple_text_analyze(texts):
    results = []
    for text in texts:
        if text.strip():
            analysis = single_text_analyzer(text)
            analysis["text"] = text.strip()
            results.append(analysis)
    return results


def get_summary(results):
    positive = sum(1 for r in results if r["label"] == "POSITIVE")
    negative = len(results) - positive
    return {
        "total": len(results),
        "POSITIVE": positive,
        "NEGATIVE": negative,
        "POSITIVE PERCENTAGE": round((positive / len(results)) * 100, 1) if results else 0
    }

results = multiple_text_analyze(texts)
for r in results:
    print(f"\nText: {r['text']}")
    print(f"Label: {r['label']}")
    print(f"Score: {r['score']}%")
    print(f"Emoji: {r['emoji']}")

print("\nSummary:", get_summary(results))

