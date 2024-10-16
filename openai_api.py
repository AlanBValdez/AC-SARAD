import openai
from config import Config

openai.api_key = Config.OPENAI_API_KEY

def validar_texto_con_openai(texto):
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=f"Valida el siguiente texto: {texto}",
        max_tokens=100
    )
    return response.choices[0].text.strip()
