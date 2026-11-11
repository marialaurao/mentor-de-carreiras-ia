
from openai import OpenAI
from google.colab import userdata

# Recuperando a chave armazenada nos Secrets
API_KEY = userdata.get("OPEN_ROUTER")

if not API_KEY:
    raise ValueError("Chave OPEN_ROUTER não encontrada.")

# Conectando ao OpenRouter
client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=API_KEY
)

# Instruções do Mentor de Carreiras
INSTRUCTIONS = """
Você é um mentor de carreiras.

Sua função é ajudar pessoas a descobrir
profissões de acordo com seus interesses.

Regras:
1. Liste profissões reais no Brasil.
2. Seja breve e objetivo.
3. Não utilize emojis.
4. Não seja preconceituoso.
5. Não faça julgamentos sobre o usuário.
6. Considere os interesses e afinidades apresentados.
7. Faça perguntas quando precisar de mais informações.
8. Não solicite dados pessoais confidenciais.
"""

# Recebendo os interesses do usuário
prompt = input(
    "Quais são suas afinidades e interesses? "
).strip()

if not prompt:
    raise ValueError("Informe seus interesses.")

# Enviando a solicitação para a IA
response = client.responses.create(
    model="openrouter/free",
    instructions=INSTRUCTIONS,
    input=prompt
)

# Apresentando o resultado
print("\n===== MENTOR DE CARREIRAS =====")
print(response.output_text)

# Monitorando os tokens
usage = response.usage

if usage:
    print("\n===== CONSUMO DE TOKENS =====")
    print("Tokens de entrada:", usage.input_tokens)
    print("Tokens de saída:", usage.output_tokens)
    print("Total de tokens:", usage.total_tokens)
