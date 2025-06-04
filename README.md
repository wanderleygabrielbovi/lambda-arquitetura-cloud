Validador de CPF com AWS Lambda

Este projeto é uma função Lambda na AWS que recebe um CPF pela URL e retorna se ele é válido ou não. A função é feita em Python e usa a regra oficial do CPF para validar os números.

---

Como funciona?

Você envia uma requisição para a URL da Lambda, passando o CPF como parâmetro na query string, assim:

?cpf=SEU_CPF_AQUI

Exemplo:  
https://sua-lambda-url.lambda-url.us-east-2.on.aws/?cpf=12345678909

A função vai ler esse CPF, limpar qualquer caractere que não seja número, e verificar se ele segue as regras de validação.

---

O que a função faz?

1. Remove qualquer coisa que não seja número no CPF (como pontos e traços).  
2. Verifica se o CPF tem 11 dígitos e não é uma sequência repetida (tipo 11111111111).  
3. Calcula os dígitos verificadores para garantir que o CPF é válido.  
4. Retorna uma resposta JSON dizendo se o CPF é válido ou inválido.

---

Resposta da função

Se tudo estiver certo, a resposta será assim:

{
  "cpf": "12345678909",
  "valid": "O documento digitado é VÁLIDO!"
}

Se o CPF for inválido:

{
  "cpf": "12345678900",
  "valid": "O documento digitado é INVÁLIDO!"
}

Se o parâmetro "cpf" não for passado na URL, a resposta será:

{
  "error": "CPF not provided in query string. Use ?cpf=SEUCNPJ"
}

---

Arquivos do projeto

- lambda_function.py: código da função Lambda  
- README.md: essa documentação (também disponível em txt)

---

Observações importantes

- A função só aceita requisições via URL (query string).  
- Não salva nenhum dado, apenas valida e responde.  
- Fique atento ao uso para evitar cobranças na AWS.  
- O código está livre de erros básicos e vulnerabilidades.

---

Autor

Wander – Faculdade UMFG – Arquitetura em Cloud – Junho 2025

Contato: seuemail@exemplo.com

---

Licença

Projeto para fins educacionais conforme a disciplina Arquitetura em Cloud.

# lambda-arquitetura-cloud
