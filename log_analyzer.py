import openai

openai.api_key = "your_api_key_here"

def analyze_log(log_text):
    prompt = f"Analyze the following log and find the issue:\n{log_text}"
    
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}]
    )
    
    return response['choices'][0]['message']['content']

log = "Error: Database connection timeout at 10:45 PM"

result = analyze_log(log)
print("Analysis:\n", result)
