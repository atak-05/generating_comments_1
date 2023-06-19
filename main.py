import openai
import requests
import json
from dotenv import load_dotenv
import os


# .env dosyasını yükle
load_dotenv()
# # API anahtarını .env dosyasından al
api_key = os.getenv("API_KEY")

openai.api_key = api_key



headers = {
    'Content-Type': 'application/json'
}

user_message = 'This hotel is great but should develop clean'
hotel_name = 'ABC Hotel'  # Otelin adını burada belirtin

data = {
    'model': 'gpt-3.5-turbo-0613',
    'messages': [
        {'role': 'system', 'content': 'You are an assistant responding to reviews about hotels'},
        {'role': 'user', 'content': user_message},
        {'role': 'system', 'content': 'give a short and persuasive answer and no questions'},
        {'role': 'system', 'content': 'generate more human-like answers to questions'},
        {'role': 'assistant', 'content': 'We appreciate your feedback and strive to continuously improve our facilities and services. We understand the importance of cleanliness and will take your comment into consideration to further enhance our cleanliness standards. Thanks again for your valuable input, and we hope to have the opportunity to welcome you back in the near future.'}
    ],
    'max_tokens': 100  # Yanıtın maksimum uzunluğunu belirtin
}

response = requests.post(
    'https://api.openai.com/v1/chat/completions',
    headers=headers,
    auth=('api_key', openai.api_key),
    data=json.dumps(data)
)

response_content = response.json()['choices'][0]['message']['content']
response_content += f"Thank you for choosing our hotel, {hotel_name}!"
response_content = response_content.split('\n')[0].strip()  # İlk satırı alın ve boşlukları temizleyin
print(response_content)
