from mistralai import Mistral

def chatbot_response(client, all_summaries, question):
    prompt = f"""
You are an intelligent assistant. Answer the user's question based ONLY on the following summarized data:

Summaries:
{all_summaries}

User question:
{question}

Give a short and clear answer.
"""
    
    response = client.chat.complete(
        model="mistral-small-latest",
        messages=[{"role": "user", "content": prompt}]
    )
    
    return response.choices[0].message.content
