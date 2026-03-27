import time
import csv
import os
from datetime import datetime

#FUNÇÃO DE VALIDAÇÃO FLOAT
def ler_float(mensagem):
    while True:
        try:
            return float(input(mensagem))
        except ValueError:
            print("Digite um número válido")

#FUNÇÃO DE VALIDÇÃO INT
def ler_int(mensagem):
    while True:
        try:
            return int(input(mensagem))
        except ValueError:
            print("Digite um número válido")
            

PRODUTOS = ["Herbicida", "Fungicida", "Inseticida", "Adubo", "Fertilizante"]

def escolher_produto():
    print("\nEscolha o produto:")
    for i, p in enumerate(PRODUTOS, 1):
        print(f"  {i} - {p}")
    while True:
        opcao = ler_int("Produto: ")
        if 1 <= opcao <= len(PRODUTOS):
            return PRODUTOS[opcao - 1]
        print(f"Escolha entre 1 e {len(PRODUTOS)}.")

ARQUIVO_CSV = os.path.join(os.path.dirname(os.path.abspath(__file__)), "farmtech-solutions-dados.csv")

def salvar_csv():
    if len(cultura) == 0:
        if os.path.exists(ARQUIVO_CSV):
            os.remove(ARQUIVO_CSV)
        return
    with open(ARQUIVO_CSV, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["id", "data_insercao", "cultura", "area_m2", "produto",
                         "dose_ml_metro", "num_ruas", "comp_rua_m", "total_litros"])
        for i in range(len(cultura)):
            writer.writerow([
                i + 1,
                data_insercao[i],
                cultura[i],
                area[i],
                produto[i],
                quantidade_por_metro[i],
                numero_linhas[i],
                comprimento_linha[i],
                total_insumo[i]
            ])

cultura = []
area = []
produto = []
quantidade_por_metro = []
comprimento_linha = []
numero_linhas = []
total_insumo = []
data_insercao = []

def carregar_csv():
    if not os.path.exists(ARQUIVO_CSV):
        return
    with open(ARQUIVO_CSV, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            cultura.append(row["cultura"])
            area.append(float(row["area_m2"]))
            produto.append(row["produto"])
            quantidade_por_metro.append(float(row["dose_ml_metro"]))
            numero_linhas.append(int(row["num_ruas"]))
            comprimento_linha.append(float(row["comp_rua_m"]))
            total_insumo.append(float(row["total_litros"]))
            data_insercao.append(row.get("data_insercao", "N/A"))

carregar_csv()

print("\nBem-vindo ao sistema de gestão agrícola da FarmTech Solutions!")
if len(cultura) > 0:
    print(f"{len(cultura)} registro(s) carregado(s) do arquivo CSV.")

while True:
    choice = ler_int("""
1 - Inserir dados
2 - Mostrar dados
3 - Atualizar dados
4 - Deletar dados
5 - Sair
Escolha uma opção: """)

    print("")

    if choice == 5:
        print("Obrigado por usar o sistema da FarmTech Solutions!\n")
        break

    elif choice < 1 or choice > 5:
        print("Valor invalido")
        time.sleep(1)
        print("Por favor, selecione uma das opcoes abaixo:")
        time.sleep(1)
        continue

    elif choice == 1:

        print("Qual cultura deseja cadastrar?")
        print("  1 - Café (área calculada como triângulo)")
        print("  2 - Soja (área calculada como retângulo)")
        # -------------------------
        # CULTURA ESCOLHIDA
        # -------------------------

        while True:
            cultura_escolhida = ler_int("Cultura: ")
            if cultura_escolhida == 1 or cultura_escolhida == 2:
                break
            else:
                print("Escolha 1 para Café ou 2 para Soja.")
        # -------------------------
        # CULTURA CAFÉ
        # -------------------------
    
        if cultura_escolhida == 1:

            cultura.append("Café")

            print("\nMedidas da área de plantação (Café — triângulo: base x altura / 2)")
            base = ler_float("Base do terreno (em metros): ")
            altura = ler_float("Altura do terreno (em metros): ")

            area_calculada = (base * altura) / 2
            print("Área da plantação:", area_calculada)

            area.append(area_calculada)

        # -------------------------
        # CULTURA SOJA
        # -------------------------

        elif cultura_escolhida == 2:

            cultura.append("Soja")

            print("\nMedidas da área de plantação (Soja — retângulo: comprimento x largura)")
            comprimento = ler_float("Comprimento do terreno (em metros): ")
            largura = ler_float("Largura do terreno (em metros): ")

            area_calculada = comprimento * largura
            print("Área da plantação:", area_calculada)

            area.append(area_calculada)

        # -------------------------
        # INSUMOS AGRÍCOLAS
        # -------------------------

        print("\n--- Manejo de Insumos ---")
        produto_input = escolher_produto()
        produto.append(produto_input)

        quantidade = ler_float("Quantos mL de produto por metro de rua? (ex: 500): ")
        quantidade_por_metro.append(quantidade)

        comprimento_linha_input = ler_float("Qual o comprimento de cada rua? (em metros, ex: 200): ")
        comprimento_linha.append(comprimento_linha_input)

        linhas = ler_int("Quantas ruas tem a lavoura? (ex: 4): ")
        numero_linhas.append(linhas)

        insumo_linha = quantidade * comprimento_linha_input
        total = insumo_linha * linhas

        total_insumo.append(total)

        data_insercao.append(datetime.now().strftime("%d/%m/%Y %H:%M"))

        print("Total de insumo necessário:", total, "litros")
        salvar_csv()

    # ---------------------------------
    # MOSTRAR DADOS
    # ---------------------------------

    elif choice == 2:

        if len(cultura) == 0:
            print("Nenhum dado cadastrado. Por favor, insira os dados primeiro.")
        else:
            for i in range(len(cultura)):
                print(f"ID: {i + 1} | Inserido em: {data_insercao[i]}\n")
                print(f"Cultura: {cultura[i]}")
                print(f"Área: {area[i]} m²")
                print(f"Produto: {produto[i]}")
                print(f"Dose por metro: {quantidade_por_metro[i]} mL/m")
                print(f"Comprimento da rua: {comprimento_linha[i]} m")
                print(f"Número de ruas: {numero_linhas[i]}")
                print(f"Total de insumo necessário: {total_insumo[i]} litros\n")
                print("-" * 50)

    # ---------------------------------
    # ATUALIZAR
    # ---------------------------------

    elif choice == 3:

        if len(cultura) == 0:
            print("Nenhum dado cadastrado. Por favor, insira os dados primeiro.")
        else:
            for i in range(len(cultura)):
                print(f"{i + 1} - {cultura[i]}")

            # Validação do registro a ser atualizado
            while True:
                registro = ler_int("Qual registro deseja atualizar: ")
                if 1 <= registro <= len(cultura):
                    break
                else:
                    print("Por favor, selecione um registro válido.")
              
            index = registro - 1
            print("Atualizando registro:", cultura[index])

            # Escolha da nova cultura
            print("Escolha a cultura:")
            print("1 - Café")
            print("2 - Soja")
            
            while True:
                    cultura_escolhida = ler_int("Cultura: ")
                    if cultura_escolhida == 1 or cultura_escolhida == 2:
                        break
                    else:
                        print("Escolha 1 para Café ou 2 para Soja.")
                        
            # Atualizar cultura e área
            if cultura_escolhida == 1:
                cultura[index] = "Café"
                print("Medidas da plantação (Café — triângulo: base x altura / 2):")
                base = ler_float("Base do terreno (em metros): ")
                altura = ler_float("Altura do terreno (em metros): ")
                area[index] = (base * altura) / 2  # mantém igual ao cadastro

            else:
                cultura[index] = "Soja"
                print("Medidas da plantação (Soja — retângulo: comprimento x largura):")
                comprimento = ler_float("Comprimento do terreno (em metros): ")
                largura = ler_float("Largura do terreno (em metros): ")
                area[index] = comprimento * largura  # mantém igual ao cadastro

            # Atualizar insumos
            produto[index] = escolher_produto()
            quantidade_por_metro[index] = ler_float("Quantos mL de produto por metro de rua? (ex: 500): ")
            comprimento_linha[index] = ler_float("Qual o comprimento de cada rua? (em metros, ex: 200): ")
            numero_linhas[index] = ler_int("Quantas ruas tem a lavoura? (ex: 4): ")

            # Recalcular total de insumo
            total = quantidade_por_metro[index] * comprimento_linha[index] * numero_linhas[index]
            total_insumo[index] = total

            print("Registro atualizado com sucesso!")
            print("Área recalculada:", area[index])
            print("Total de insumo necessário:", total_insumo[index])
            salvar_csv()

    # ---------------------------------
    # DELETAR
    # ---------------------------------
    
    elif choice == 4:
        if len(cultura) == 0:
            print("Nenhum dado cadastrado.")
            continue
        
        print(f"{'ID':<4} {'Cultura':<10} {'Produto':<15} {'Data de inserção'}")
        print("-" * 50)
        for i in range(len(cultura)):
            print(f"{i + 1:<4} {cultura[i]:<10} {produto[i]:<15} {data_insercao[i]}")

        while True:
            registro = ler_int("\nQual ID deseja deletar: ")
            if 1 <= registro <= len(cultura):
                break
            else:
                print("Por favor, selecione um ID válido.")

        index = registro - 1

        del cultura[index]
        del area[index]
        del produto[index]
        del quantidade_por_metro[index]
        del comprimento_linha[index]
        del numero_linhas[index]
        del total_insumo[index]
        del data_insercao[index]

        print("")
        time.sleep(1)
        print("Registro deletado com sucesso!")
        salvar_csv()
 
