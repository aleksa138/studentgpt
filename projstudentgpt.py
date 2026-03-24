from openai import OpenAI
import os
import json

client = OpenAI(api_key=os.environ.get("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"))

def handler(request):
    try:
        body = json.loads(request.body)
        text = body.get("text", "")
        mode = body.get("mode", "summary")

        if mode == "summary":
            prompt = f"Сделай краткий конспект:\n{text}"
        elif mode == "flashcards":
            prompt = f"Создай flashcards:\n{text}"
        else:
            prompt = f"Создай тест:\n{text}"

        response = client.chat.completions.create(
            model="gpt-4.1-mini",
            messages=[
                {"role": "system", "content": "Ты помощник для студентов."},
                {"role": "user", "content": prompt}
            ]
        )

        return {
            "statusCode": 200,
            "body": json.dumps({
                "result": response.choices[0].message.content
            })
        }

    except Exception as e:
        return {
            "statusCode": 500,
            "body": str(e)
        }