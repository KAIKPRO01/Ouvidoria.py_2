
from operacoesbd import *

numero = int(input('Digite um número: '))

conexao = criarConexao('128.0.0.1', 'root', ':8k&7!/hudswJ9q', 'ouvidoria')

def listar_manifestacoes(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM manifestacoes")
    manifestacoes = cursor.fetchall()
    if not manifestacoes:
        print("Não existem manifestações cadastradas.")
    else:
        for manifestacao in manifestacoes:
            print(manifestacao)

def listar_manifestacoes_por_tipo(conn):
    tipo = input("Digite o tipo de manifestação (reclamação, elogio, sugestão): ").strip()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM manifestacoes WHERE tipo = %s", (tipo,))
    manifestacoes = cursor.fetchall()
    if not manifestacoes:
        print(f"Não existem manifestações do tipo '{tipo}' cadastradas.")
    else:
        for manifestacao in manifestacoes:
            print(manifestacao)

def criar_manifestacao(conn):
    tipo = input("Digite o tipo de manifestação (reclamação, elogio, sugestão): ").strip()
    nome = input("Digite seu nome: ").strip()
    email = input("Digite seu email: ").strip()
    mensagem = input("Digite sua mensagem: ").strip()

    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO manifestacoes (tipo, nome, email, mensagem) VALUES (%s, %s, %s, %s)",
        (tipo, nome, email, mensagem)
    )
    conn.commit()
    print("Nova manifestação criada com sucesso!")

# Exibir quantidade de manifestações
def quantidade_manifestacoes(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(*) FROM manifestacoes")
    count = cursor.fetchone()[0]
    print(f"Quantidade de manifestações: {count}")

def pesquisar_manifestacao_por_codigo(conn):
    codigo = int(input("Digite o código da manifestação: ").strip())
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM manifestacoes WHERE id = %s", (codigo,))
    manifestacao = cursor.fetchone()
    if not manifestacao:
        print("Não foi encontrada manifestação com o código fornecido.")
    else:
        print(manifestacao)


# Excluir uma Manifestação pelo Código
def excluir_manifestacao_por_codigo(conn):
    codigo = int(input("Digite o código da manifestação a ser excluída: ").strip())
    cursor = conn.cursor()
    cursor.execute("DELETE FROM manifestacoes WHERE id = %s", (codigo,))
    conn.commit()
    if cursor.rowcount == 0:
        print("Não foi encontrada manifestação com o código fornecido.")
    else:
        print("Manifestação excluída com sucesso!")

def menu():
    conn = conectar()
    while True:
        print("\nMenu do Sistema de Ouvidoria")
        print("1) Listagem das Manifestações")
        print("2) Listagem de Manifestações por Tipo")
        print("3) Criar uma nova Manifestação")
        print("4) Exibir quantidade de manifestações")
        print("5) Pesquisar uma manifestação por código")
        print("6) Excluir uma Manifestação pelo Código")
        print("7) Sair do Sistema")

        opcao = int(input("Escolha uma opção: ").strip())

        if opcao == 1:
            listar_manifestacoes(conn)
        elif opcao == 2:
            listar_manifestacoes_por_tipo(conn)
        elif opcao == 3:
            criar_manifestacao(conn)
        elif opcao == 4:
            quantidade_manifestacoes(conn)
        elif opcao == 5:
            pesquisar_manifestacao_por_codigo(conn)
        elif opcao == 6:
            excluir_manifestacao_por_codigo(conn)
        elif opcao == 7:
            print("Saindo do sistema...")
            break
        else:
            print("Opção inválida, por favor tente novamente.")
    conn.close()


if __name__ == "__main__":
    menu()

    encerrarBancoDados(con)
print("Obrigado por usar a nossa ouvidoria!")