Python 3.13.3 (tags/v3.13.3:6280bb5, Apr  8 2025, 14:47:33) [MSC v.1943 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> def desafio_1():
...         INDICE = 13
...             SOMA = 0
...                 K = 0
...                     while K < INDICE:
...                                     K += 1
...                                             SOMA += K
...                                                 print(f"Desafio 1: Soma final = {SOMA}")
...
  File "<python-input-0>", line 3
    SOMA = 0
IndentationError: unexpected indent
>>> def desafio_2(numero):
...             # Sequência Fibonacci gerada até passar do número informado
...                             a, b = 0, 1
...                                 fib_seq = [a, b]
...                                     while b < numero:
...                                                         a, b = b, a + b
...                                                                 fib_seq.append(b)
...                                                                     if numero in fib_seq:
...                                                                                         print(f"Desafio 2: O número\ {numero} pertence à sequência de Fibonacci.")
...                                                                                             else:
...                                                                                                                 pri\nt(f"Desafio 2: O número {numero} NÃO pertence à sequência de Fibonacci.")
...
  File "<python-input-1>", line 4
    fib_seq = [a, b]
IndentationError: unexpected indent
>>> def desafio_3(dados):
...                 # dados: lista de dicts com {"dia": int, "valor": float}
...                                     valores_validos = [d["valor"] for d in dados if d["valor"] > 0]
...                                         menor = min(valores_validos) if valores_validos else None
...                                             maior = max(valores_validos) if valores_validos else None
...                                                 media = sum(valores_validos)  len(valores_validos) if valores_valid\os else None
...                                                     dias_acima_media = sum(1 for d in dados if d["valor"] > media) \if media else 0
...
  File "<python-input-2>", line 4
    menor = min(valores_validos) if valores_validos else None
IndentationError: unexpected indent
>>>     print("Desafio 3:")
  File "<python-input-3>", line 1
    print("Desafio 3:")
IndentationError: unexpected indent
>>>     print(f"Menor faturamento: {menor:.2f}" if menor is not None else "Sem dados válidos")
  File "<python-input-4>", line 1
    print(f"Menor faturamento: {menor:.2f}" if menor is not None else "Sem dados válidos")
IndentationError: unexpected indent
>>>     print(f"Maior faturamento: {maior:.2f}" if maior is not None else "Sem dados válidos")
  File "<python-input-5>", line 1
    print(f"Maior faturamento: {maior:.2f}" if maior is not None else "Sem dados válidos")
IndentationError: unexpected indent
>>>     print(f"Dias com faturamento acima da média: {dias_acima_media}")
  File "<python-input-6>", line 1
    print(f"Dias com faturamento acima da média: {dias_acima_media}")
IndentationError: unexpected indent
>>>
>>> def desafio_4():
...                     faturamento = {
...                             "SP": 67836.43,
...                                     "RJ": 36678.66,
...                                             "MG": 29229.88,
...                                                     "ES": 27165.48,
...                                                             "Outros": 19849.53
...                                                                 }
...                                                                     total = sum(faturamento.values())
...                                                                         print("Desafio 4: Percentual por estado:")
...                                                                             for estado, valor in faturamento.items(\):
...                                                                                                         perc = (val\or  total) * 100
...                                                                                                                 pri\nt(f"{estado}: {perc:.2f}%")
...
  File "<python-input-8>", line 9
    total = sum(faturamento.values())
IndentationError: unexpected indent
>>> def desafio_5(texto):
...                         # Inverter string sem usar reverse ou funções prontas
...                                                     invertido = ""
...                                                         for i in range(len(texto)-1, -1, -1):
...                                                                                         invertido += texto[i]
...                                                                                             print(f"Desafio 5: Stri\ng invertida: '{invertido}'")
...
  File "<python-input-9>", line 4
    for i in range(len(texto)-1, -1, -1):
IndentationError: unexpected indent
>>> def main():
...                             # Testes dos desafios
...                                                             desafio_1()
...
>>>     # Para o desafio 2, número pode ser definido aqui:
>>>     numero_teste = 21
  File "<python-input-12>", line 1
    numero_teste = 21
IndentationError: unexpected indent
>>>     desafio_2(numero_teste)
  File "<python-input-13>", line 1
    desafio_2(numero_teste)
IndentationError: unexpected indent
>>>
>>>     # Dados para o desafio 3 (exemplo simplificado, substitua pelo JSON real)
>>>     dados_exemplo = [
  File "<python-input-16>", line 1
    dados_exemplo = [
IndentationError: unexpected indent
>>>         {"dia": 1, "valor": 22174.1664},
  File "<python-input-17>", line 1
    {"dia": 1, "valor": 22174.1664},
IndentationError: unexpected indent
>>>         {"dia": 2, "valor": 24537.6698},
  File "<python-input-18>", line 1
    {"dia": 2, "valor": 24537.6698},
IndentationError: unexpected indent
>>>         {"dia": 3, "valor": 26139.6134},
  File "<python-input-19>", line 1
    {"dia": 3, "valor": 26139.6134},
IndentationError: unexpected indent
>>>         {"dia": 4, "valor": 0.0},
  File "<python-input-20>", line 1
    {"dia": 4, "valor": 0.0},
IndentationError: unexpected indent
>>>         {"dia": 5, "valor": 0.0},
  File "<python-input-21>", line 1
    {"dia": 5, "valor": 0.0},
IndentationError: unexpected indent
>>>         {"dia": 6, "valor": 26742.6612},
  File "<python-input-22>", line 1
    {"dia": 6, "valor": 26742.6612},
IndentationError: unexpected indent
>>>         # ... continue com os dados completos ...
>>>     ]
  File "<python-input-24>", line 1
    ]
IndentationError: unexpected indent
>>>     desafio_3(dados_exemplo)
  File "<python-input-25>", line 1
    desafio_3(dados_exemplo)
IndentationError: unexpected indent
>>>
>>>     desafio_4()
  File "<python-input-27>", line 1
    desafio_4()
IndentationError: unexpected indent
>>>
>>>     # Texto para o desafio 5
>>>     texto_teste = "Exemplo"
  File "<python-input-30>", line 1
    texto_teste = "Exemplo"
IndentationError: unexpected indent
>>>     desafio_5(texto_teste)
  File "<python-input-31>", line 1
    desafio_5(texto_teste)
IndentationError: unexpected indent
>>>
>>> if __name__ == "__main__":
...                                 main()
...
