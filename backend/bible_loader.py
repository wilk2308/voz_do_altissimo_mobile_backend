import json
import os

def carregar_biblia():
    caminho = os.path.join("data", "biblia.json")
    with open(caminho, "r", encoding="utf-8") as f:
        return json.load(f)

def buscar_versiculos_por_palavra_chave(biblia, palavra_chave):
    resultados = []

    for livro, capitulos in biblia.items():
        for capitulo, versiculos in capitulos.items():
            for numero, texto in versiculos.items():
                if palavra_chave.lower() in texto.lower():
                    resultados.append(f"{livro} {capitulo}:{numero} - {texto}")

    return resultados[:3]  # limita a 3 resultados para não sobrecarregar o prompt
