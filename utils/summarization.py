from mistralai import Mistral
import time

def initialize_llm_pipeline():
    api_key = "MMNlnPxuMxBfeIGG4pIGIfSwBdIgjlVA"   # replace with env variable later
    client = Mistral(api_key=api_key)
    return client

def call_with_retry(client, model, messages, retries=10):
    for attempt in range(retries):
        try:
            return client.chat.complete(
                model=model,
                messages=messages
            )
        except Exception as e:
            if "capacity" in str(e).lower() or "429" in str(e):
                time.sleep(5)
            else:
                raise e
    raise Exception("❌ Failed after multiple retries.")

def summarize_table(client, table_text):
    prompt = (
        "Summarize this table data clearly:\n\n"
        f"{table_text}\n\n"
        "Give a concise explanation."
    )

    chat_response = call_with_retry(
        client,
        model="mistral-small-latest",
        messages=[{"role": "user", "content": prompt}]
    )

    return chat_response.choices[0].message.content
