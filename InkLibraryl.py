livros = [] #foi usado uma lista de dicionários, pois é mais adequada quando a ordem dos elementos importa. 



def buscar_livro(titulo):
    for livro in livros:
        if livro["titulo"].lower() == titulo.lower():  # O lower resolve conflitos de letras maiusculas ou minusculas.
            return livro
    return None


def cadastrar_ou_editar(livro_existente=None): #try/ evita que o programa quebre caso o usuário digite valores inválidos. 
    try:
        if not livro_existente:
            titulo = input("Título: ").strip()

            if buscar_livro(titulo):
                print("Erro: Livro já existe.")
                return

            autor = input("Autor: ")
            quantidade = int(input("Quantidade de exemplares: "))

            livros.append({
                "titulo": titulo,
                "autor": autor,
                "quantidade": quantidade
            })

            print("Livro cadastrado!")

        else:
            print(f"Editando: {livro_existente['titulo']}")

            novo_titulo = input(
                "Novo título (Enter para manter): "
            ).strip()

            novo_autor = input(
                "Novo autor (Enter para manter): "
            ).strip()

            if novo_titulo:
                livro_existente["titulo"] = novo_titulo

            if novo_autor:
                livro_existente["autor"] = novo_autor

            print("Livro atualizado!")

    except ValueError:
        print("Erro: dados inválidos.")


def listar_livros():
    if not livros:
        print("Nenhum livro cadastrado.")
        return

    print("\n--- LISTA DE LIVROS ---")

    for livro in livros:
        print(
            f"{livro['titulo']} | "
            f"Autor: {livro['autor']} | "
            f"Qtd: {livro['quantidade']}"
        )


def emprestar_livro():
    titulo = input("Livro a emprestar: ").strip()
    livro = buscar_livro(titulo)

    if not livro:
        print("Livro não encontrado.")
        return

    try:
        quantidade = int(input("Quantidade: "))

        if quantidade <= livro["quantidade"]:
            livro["quantidade"] -= quantidade
            print("Empréstimo realizado!")
        else:
            print("Quantidade insuficiente.")

    except ValueError:
        print("Erro: valor inválido.")


def dashboard():
    total_livros = len(livros)
    total_exemplares = sum(
        livro["quantidade"] for livro in livros
    )

    print("\n--- DASHBOARD ---")
    print(f"Total de livros cadastrados: {total_livros}")
    print(f"Total de exemplares: {total_exemplares}")


def main():
    while True:
        print(
            "\n1-Cadastrar | 2-Listar | 3-Editar | "
            "4-Buscar | 5-Emprestar | 6-Dashboard | 0-Sair"
        )

        op = input("Opção: ")

        if op == "1":
            cadastrar_ou_editar()

        elif op == "2":
            listar_livros()

        elif op == "3":
            titulo = input("Título para editar: ")
            livro = buscar_livro(titulo)

            if livro:
                cadastrar_ou_editar(livro)
            else:
                print("Livro não encontrado.")

        elif op == "4":
            titulo = input("Título para buscar: ")
            livro = buscar_livro(titulo)

            if livro:
                print(livro)
            else:
                print("Não encontrado")

        elif op == "5":
            emprestar_livro()

        elif op == "6":
            dashboard()

        elif op == "0":
            break

        else:
            print("Inválido")


if __name__ == "__main__":
    main()
