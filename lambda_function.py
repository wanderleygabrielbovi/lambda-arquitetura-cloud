import json
import re

def validate_cpf(cpf: str) -> bool:
    cpf = re.sub(r'\D', '', cpf)

    if len(cpf) != 11 or cpf == cpf[0] * 11:
        return False

    def calculate_digit(digits, factor):
        total = sum(int(d) * f for d, f in zip(digits, range(factor, 1, -1)))
        remainder = (total * 10) % 11
        return 0 if remainder == 10 else remainder

    first_digit = calculate_digit(cpf[:9], 10)
    second_digit = calculate_digit(cpf[:10], 11)

    return first_digit == int(cpf[9]) and second_digit == int(cpf[10])

def lambda_handler(event, context):
    params = event.get("queryStringParameters", {})
    cpf = params.get("cpf") if params else None

    if not cpf:
        return {
            "statusCode": 400,
            "body": json.dumps({"error": "CPF not provided in query string. Use ?cpf=SEUCPF"})
        }

    is_valid = validate_cpf(cpf)

    text_is_or_not_valid = ""
    if is_valid:
        text_is_or_not_valid = "O documento digitado é VÁLIDO!"
    else:
        text_is_or_not_valid = "O documento digitado é INVÁLIDO!"

    return {
        "statusCode": 200,
        "body": json.dumps({
            "cpf": cpf,
            "valid": text_is_or_not_valid
        }),
        "headers": {
            "Content-Type": "application/json"
        }
    }
