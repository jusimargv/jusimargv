curso = "Curso de Python"
nome_curso = curso
saldo, limite = 200, 200

curso is nome_curso

curso is not nome_curso

saldo is limite

saldo = 1000

limite = 500

saque = 1000
print(saldo is limite)

print(saldo is not limite)

print(saldo is limite is not saque)

print(saldo is not limite)

x =(22-10) * 3
print(x)