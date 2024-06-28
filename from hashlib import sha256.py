from hashlib import sha256
import time
import random

def aplicar_sha256(texto):
    return sha256(texto.encode("ascii")).hexdigest()

def minerar(num_bloco, transacoes, hash_anterior, qtde_zeros):
    nonce = 0
    while True:
        texto = str(num_bloco) + transacoes + hash_anterior + str(nonce)
        meu_hash = aplicar_sha256(texto)
        if meu_hash.startswith("0" * qtde_zeros):
            print("\n** BLOCK MINED! **")
            return nonce, meu_hash
        nonce += 1

if __name__ == "__main__":
    num_bloco = 848.428
    qtde_zeros = 19
    hash_anterior = "0000000000000000000000000000000000000000000000000000000000000000"

    while True:
        transacoes = ""
        for i in range(random.randint(1, 10)):  # generate random number of transactions
            sender = f"User{random.randint(1, 100)}"
            receiver = f"User{random.randint(1, 100)}"
            amount = random.randint(1, 100)
            transacoes += f"{sender}->{receiver}->{amount}\n"

        inicio = time.time()
        resultado = minerar(num_bloco, transacoes, hash_anterior, qtde_zeros)
        print(f"Block {num_bloco} mined!")
        print(f"Nonce: {resultado[0]}")
        print(f"Hash: {resultado[1]}")
        print(f"Time: {time.time() - inicio} seconds")
        print("")

        num_bloco += 1
        hash_anterior = resultado[1]