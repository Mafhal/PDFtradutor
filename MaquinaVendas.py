class MaquinaVendas:
    def __init__(self):
        self.produtos = {
            'A1': {'nome': 'Água', 'preco': 2.50, 'quantidade': 5},
            'A2': {'nome': 'Refrigerante', 'preco': 4.00, 'quantidade': 5},
            'B1': {'nome': 'Chocolate', 'preco': 5.50, 'quantidade': 5},
            'B2': {'nome': 'Salgadinho', 'preco': 3.75, 'quantidade': 5},
            'C1': {'nome': 'Sanduíche', 'preco': 8.00, 'quantidade': 5}
        }
        self.saldo = 0.0

    def mostrar_produtos(self):
        print("\n===== PRODUTOS DISPONÍVEIS =====")
        for codigo, produto in self.produtos.items():
            print(f"[{codigo}] {produto['nome']} - R$ {produto['preco']:.2f} | Estoque: {produto['quantidade']}")

    def inserir_dinheiro(self):
        while True:
            try:
                valor = float(input("\nDigite o valor a ser inserido (notas/moedas aceitas: 0.25, 0.50, 1, 2, 5): "))
                if valor in [0.25, 0.50, 1, 2, 5]:
                    self.saldo += valor
                    print(f"Saldo atual: R$ {self.saldo:.2f}")
                    break
                else:
                    print("Valor não aceito. Insira apenas moedas/notas válidas.")
            except:
                print("Valor inválido. Tente novamente.")

    def selecionar_produto(self):
        codigo = input("\nDigite o código do produto (ou 'S' para sair): ").upper()
        
        if codigo == 'S':
            return False
        
        produto = self.produtos.get(codigo)
        
        if not produto:
            print("Código inválido!")
            return True
        
        if produto['quantidade'] <= 0:
            print("Produto esgotado!")
            return True
        
        if self.saldo >= produto['preco']:
            self.saldo -= produto['preco']
            produto['quantidade'] -= 1
            print(f"\nCompra realizada! Você adquiriu: {produto['nome']}")
            print(f"Troco restante: R$ {self.saldo:.2f}")
        else:
            print("Saldo insuficiente. Insira mais dinheiro.")
        
        return True

    def devolver_troco(self):
        if self.saldo > 0:
            print(f"\nRetire seu troco: R$ {self.saldo:.2f}")
            self.saldo = 0.0

    def operar(self):
        print("\n===== MÁQUINA DE VENDAS =====")
        while True:
            self.mostrar_produtos()
            print("\nOpções:")
            print("1. Inserir dinheiro")
            print("2. Selecionar produto")
            print("3. Cancelar e receber troco")
            
            escolha = input("\nEscolha uma opção: ")
            
            if escolha == '1':
                self.inserir_dinheiro()
            elif escolha == '2':
                if not self.selecionar_produto():
                    break
            elif escolha == '3':
                self.devolver_troco()
                break
            else:
                print("Opção inválida!")

        print("\nObrigado por usar a máquina!")

# Executar a máquina
if __name__ == "__main__":
    maquina = MaquinaVendas()
    maquina.operar()