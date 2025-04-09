import os
from dotenv import load_dotenv
import openai
from bible_loader import carregar_biblia, buscar_versiculos_por_palavra_chave

# Carrega variáveis do .env
load_dotenv()

# CONFIGURAÇÃO PARA OPENROUTER
openai.api_base = "https://openrouter.ai/api/v1"
openai.api_key = os.getenv("OPENAI_API_KEY")

# Teste de carregamento da chave (DEBUG)
if not openai.api_key:
    print("❌ ERRO: OPENAI_API_KEY não foi carregada!")

# Carrega a Bíblia
biblia = carregar_biblia()

def gerar_resposta(mensagem_usuario):
    palavras_chave = mensagem_usuario.lower().split()
    versiculos = []

    for palavra in palavras_chave:
        encontrados = buscar_versiculos_por_palavra_chave(biblia, palavra)
        versiculos.extend(encontrados)
        if len(versiculos) >= 3:
            break

    contexto_biblico = "\n".join(versiculos[:3]) if versiculos else "Nenhum versículo encontrado."

    prompt = f"""
Você é Deus Todo-Poderoso respondendo com amor e sabedoria.
Use os versículos abaixo como base para sua resposta:

{contexto_biblico}

Usuário: "{mensagem_usuario}"
Deus:
"""

    resposta = openai.ChatCompletion.create(
        model="openchat/openchat-3.5-0106",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.7,
        max_tokens=300
    )

    return resposta.choices[0].message["content"].strip()