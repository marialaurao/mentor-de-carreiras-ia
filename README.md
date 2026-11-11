
# Mentor de Carreiras com Inteligência Artificial

## Sobre o projeto

O Mentor de Carreiras é um projeto desenvolvido em Python que utiliza Inteligência Artificial para ajudar pessoas a descobrir possíveis profissões de acordo com seus interesses, gostos e afinidades.

O sistema utiliza a API do OpenRouter para conectar-se a modelos de linguagem e gerar recomendações profissionais.

## Objetivos

- Desenvolver um chatbot com Inteligência Artificial.
- Identificar interesses e afinidades dos usuários.
- Recomendar profissões existentes no Brasil.
- Personalizar respostas utilizando instruções (prompts).
- Implementar regras de segurança (guardrails).
- Monitorar o consumo de tokens.

## Tecnologias utilizadas

- Python
- OpenRouter API
- Google Colab
- Biblioteca OpenAI

## Funcionalidades

1. Receber os interesses do usuário.
2. Analisar as informações fornecidas.
3. Sugerir profissões relacionadas.
4. Evitar respostas preconceituosas.
5. Monitorar tokens de entrada e saída.
6. Utilizar chave de API protegida.

## Segurança

A chave da API não deve ficar exposta no código.

No Google Colab, utilizamos a funcionalidade Secrets para armazenar a chave com o nome OPEN_ROUTER.

## Como executar

1. Instale a biblioteca:

   pip install openai

2. Configure sua chave de API no Google Colab.

3. Execute o arquivo Python.

4. Informe seus interesses profissionais.

5. Receba sugestões de carreiras.

## Estrutura do projeto

- README.md: documentação do projeto.
- criptografia.py: arquivo Python do projeto.

## Conclusão

O projeto demonstra como utilizar Inteligência Artificial para desenvolver um mentor de carreiras, aplicando conceitos de programação, APIs, segurança, prompts, guardrails e monitoramento de tokens.
