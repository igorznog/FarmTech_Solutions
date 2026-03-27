# 🌱 FarmTech Solutions

Sistema completo de **gestão agrícola + análise de dados**, desenvolvido com foco em organização de lavouras, cálculo de insumos e geração de insights.

---

## 📌 Sobre o Projeto

O **FarmTech Solutions** é uma aplicação que permite:

* Cadastrar culturas agrícolas (Café e Soja)
* Calcular automaticamente a área de plantio
* Estimar a quantidade de insumos necessários
* Gerenciar registros (CRUD completo)
* Analisar dados utilizando **R**

📍 **Observação:**
Este projeto foi desenvolvido como parte de um **trabalho acadêmico em grupo**, com foco em aplicar conceitos de programação, lógica e análise de dados em um cenário real.

---

## 🚀 Funcionalidades

### 🧾 Sistema em Python

* Inserção de dados agrícolas
* Cálculo automático de área:

  * Café → área triangular
  * Soja → área retangular
* Cálculo de insumos
* Listagem de registros
* Atualização inteligente de dados
* Remoção de registros

### 📊 Análise de Dados (R)

* Leitura do dataset `.csv`
* Análise exploratória
* Geração de insights

### 🧪 Testes

* Casos de uso documentados
* Validação manual do sistema

---

## 🛠️ Tecnologias Utilizadas

* **Python**
* **R**
* **CSV**
* **VS Code**
* **RStudio**

---

## 📂 Estrutura do Projeto

```
farmtech-solutions/
│
├── farmtech-solutions.py
├── farmtech-solutions-dados.csv
├── farmtech-solutions-analytics.R
│
├── TESTES.md
├── CHANGELOG.md
├── video.txt
└── README.md
```

---

## ⚙️ Requisitos para Execução

Você precisa ter instalado:

* Visual Studio Code
* Python (3.x)
* RStudio
* R

---

## ▶️ Como Executar

### 🔹 Python

```bash
python farmtech-solutions.py
```

### 🔹 R

* Abra o arquivo `.R` no RStudio
* Execute o script para análise do CSV

---

## 📊 Lógica do Sistema

### 🌾 Área

**Café:**

```
Área = (base * altura) / 2
```

**Soja:**

```
Área = comprimento * largura
```

### 🧪 Insumos

```
Total = quantidade_por_metro * comprimento_linha * numero_linhas
```

---

## 🧠 Diferenciais

* Validação de entrada (robustez)
* Atualização dinâmica inteligente
* Integração Python + R
* Estrutura simples e funcional (nível iniciante evoluído)

---

## 🎥 Demonstração

📎 Link disponível em:

```
video.txt
```

---

## 📄 Licença

Uso educacional.
