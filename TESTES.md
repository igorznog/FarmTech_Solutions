# Roteiro de Testes — FarmTech Solutions

## Pre-requisitos

- Python 3 instalado
- R / RStudio instalado
- Terminal aberto na pasta do projeto (`FarmTech-Solutions-1`)

---

## 1. Python — Primeira execucao (sem CSV)

**Objetivo:** Verificar que o programa inicia sem erros quando nao existe CSV.

| Passo | Acao | Resultado esperado |
|-------|------|--------------------|
| 1.1 | Deletar `farmtech-solutions-dados.csv` se existir | Arquivo removido |
| 1.2 | Rodar `python farmtech-solutions.py` | Exibe "Bem-vindo ao sistema" SEM mensagem de registros carregados |
| 1.3 | Escolher opcao 2 (Mostrar dados) | Exibe "Nenhum dado cadastrado" |
| 1.4 | Escolher opcao 3 (Atualizar) | Exibe "Nenhum dado cadastrado" |
| 1.5 | Escolher opcao 4 (Deletar) | Exibe "Nenhum dado cadastrado" |
| 1.6 | Escolher opcao 5 (Sair) | Programa encerra normalmente |

---

## 2. Python — Inserir dados (opcao 1)

**Objetivo:** Inserir 4 registros cobrindo todas as variacoes.

### Registro 1 — Cafe + Herbicida

| Pergunta | Digitar |
|----------|---------|
| Escolha uma opcao | `1` |
| Cultura | `1` (Cafe) |
| Base do terreno (em metros) | `120` |
| Altura do terreno (em metros) | `80` |
| Produto | `1` (Herbicida) |
| Quantos mL por metro de rua? | `500` |
| Comprimento de cada rua? | `200` |
| Quantas ruas? | `4` |

**Resultado esperado:**
- Area: `4800.0` (120 x 80 / 2)
- Total de insumo: `400000.0 litros` (500 x 200 x 4)

### Registro 2 — Soja + Fungicida

| Pergunta | Digitar |
|----------|---------|
| Escolha uma opcao | `1` |
| Cultura | `2` (Soja) |
| Comprimento do terreno (em metros) | `200` |
| Largura do terreno (em metros) | `150` |
| Produto | `2` (Fungicida) |
| Quantos mL por metro de rua? | `300` |
| Comprimento de cada rua? | `250` |
| Quantas ruas? | `5` |

**Resultado esperado:**
- Area: `30000.0` (200 x 150)
- Total de insumo: `375000.0 litros` (300 x 250 x 5)

### Registro 3 — Cafe + Inseticida

| Pergunta | Digitar |
|----------|---------|
| Escolha uma opcao | `1` |
| Cultura | `1` (Cafe) |
| Base do terreno (em metros) | `95` |
| Altura do terreno (em metros) | `70` |
| Produto | `3` (Inseticida) |
| Quantos mL por metro de rua? | `400` |
| Comprimento de cada rua? | `180` |
| Quantas ruas? | `3` |

**Resultado esperado:**
- Area: `3325.0` (95 x 70 / 2)
- Total de insumo: `216000.0 litros` (400 x 180 x 3)

### Registro 4 — Soja + Adubo

| Pergunta | Digitar |
|----------|---------|
| Escolha uma opcao | `1` |
| Cultura | `2` (Soja) |
| Comprimento do terreno (em metros) | `160` |
| Largura do terreno (em metros) | `120` |
| Produto | `4` (Adubo) |
| Quantos mL por metro de rua? | `250` |
| Comprimento de cada rua? | `200` |
| Quantas ruas? | `6` |

**Resultado esperado:**
- Area: `19200.0` (160 x 120)
- Total de insumo: `300000.0 litros` (250 x 200 x 6)

---

## 3. Python — Mostrar dados (opcao 2)

**Objetivo:** Verificar que os 4 registros sao exibidos corretamente.

| Passo | Acao | Resultado esperado |
|-------|------|--------------------|
| 3.1 | Escolher opcao 2 | Lista 4 registros |
| 3.2 | Verificar cada registro | ID, data de insercao, cultura, area, produto, dose, ruas, total corretos |
| 3.3 | Confirmar unidades | mL/m, m, litros |

---

## 4. Python — Validacao de entrada

**Objetivo:** Verificar que entradas invalidas sao tratadas.

| Passo | Acao | Resultado esperado |
|-------|------|--------------------|
| 4.1 | No menu, digitar `0` | "Valor invalido" |
| 4.2 | No menu, digitar `6` | "Valor invalido" |
| 4.3 | No menu, digitar `abc` | "Digite um numero valido" |
| 4.4 | Na escolha de cultura, digitar `3` | "Escolha 1 para Cafe ou 2 para Soja" |
| 4.5 | Na escolha de produto, digitar `6` | "Escolha entre 1 e 5" |
| 4.6 | Em campo numerico, digitar `abc` | "Digite um numero valido" |

---

## 5. Python — Atualizar dados (opcao 3)

**Objetivo:** Atualizar o registro 1 de Cafe para Soja.

| Pergunta | Digitar |
|----------|---------|
| Escolha uma opcao | `3` |
| Qual registro deseja atualizar | `1` |
| Cultura | `2` (Soja) |
| Comprimento do terreno | `180` |
| Largura do terreno | `100` |
| Produto | `5` (Fertilizante) |
| Quantos mL por metro de rua? | `350` |
| Comprimento de cada rua? | `150` |
| Quantas ruas? | `5` |

**Resultado esperado:**
- "Registro atualizado com sucesso!"
- Area recalculada: `18000.0` (180 x 100)
- Total de insumo: `262500.0` (350 x 150 x 5)

**Verificacao:** Escolher opcao 2 e confirmar que o registro 1 agora e Soja/Fertilizante.

---

## 6. Python — Deletar dados (opcao 4)

**Objetivo:** Deletar um registro e verificar a tabela de confirmacao.

| Passo | Acao | Resultado esperado |
|-------|------|--------------------|
| 6.1 | Escolher opcao 4 | Exibe tabela com ID, Cultura, Produto, Data |
| 6.2 | Digitar ID `1` | "Registro deletado com sucesso!" |
| 6.3 | Escolher opcao 2 | Restam 3 registros, IDs renumerados |

---

## 7. Python — Persistencia de dados (CSV)

**Objetivo:** Verificar que os dados sobrevivem ao reinicio.

| Passo | Acao | Resultado esperado |
|-------|------|--------------------|
| 7.1 | Escolher opcao 5 (Sair) | Programa encerra |
| 7.2 | Verificar que `farmtech-solutions-dados.csv` existe | Arquivo presente com dados |
| 7.3 | Rodar `python farmtech-solutions.py` novamente | "X registro(s) carregado(s) do arquivo CSV" |
| 7.4 | Escolher opcao 2 | Registros iguais aos da sessao anterior |

---

## 8. Python — Deletar todos os registros

**Objetivo:** Verificar que o CSV e removido ao deletar tudo.

| Passo | Acao | Resultado esperado |
|-------|------|--------------------|
| 8.1 | Deletar todos os registros um por um (opcao 4) | Cada um exibe "Registro deletado com sucesso!" |
| 8.2 | Verificar pasta do projeto | `farmtech-solutions-dados.csv` NAO existe |
| 8.3 | Escolher opcao 2 | "Nenhum dado cadastrado" |

---

## 9. R — Sem CSV (arquivo nao existe)

**Objetivo:** Verificar que o R trata a ausencia do CSV.

| Passo | Acao | Resultado esperado |
|-------|------|--------------------|
| 9.1 | Garantir que `farmtech-solutions-dados.csv` nao existe | - |
| 9.2 | No RStudio: `setwd("C:/Users/danil/Development/FIAP/FarmTech-Solutions-1")` | - |
| 9.3 | `source("farmtech-solutions-analytics.R")` | Exibe "Nenhum dado encontrado" e para sem erros |

---

## 10. R — Com CSV vazio

**Objetivo:** Verificar que o R trata CSV sem registros.

| Passo | Acao | Resultado esperado |
|-------|------|--------------------|
| 10.1 | Criar CSV vazio manualmente (so cabecalho) | - |
| 10.2 | `source("farmtech-solutions-analytics.R")` | Exibe "O arquivo CSV existe mas esta vazio" e para sem erros |

---

## 11. R — Com dados (fluxo completo)

**Objetivo:** Verificar que o R le e analisa os dados do Python.

**Pre-requisito:** Rodar o Python e inserir os 4 registros do teste 2.

| Passo | Acao | Resultado esperado |
|-------|------|--------------------|
| 11.1 | `source("farmtech-solutions-analytics.R")` | "Dados carregados com sucesso! Total de registros: 4" |
| 11.2 | Secao REGISTROS COMPLETOS | 4 registros com ID, data, cultura, area, produto, dose, ruas, total |
| 11.3 | Secao ESTATISTICAS GERAIS | Media, desvio padrao, min, max, mediana, Q1/Q3 para cada variavel (sem NaN) |
| 11.4 | Secao SUMMARY COMPLETO | Saida do summary() do R |
| 11.5 | Secao ESTATISTICAS POR CULTURA | Cafe (2 registros) e Soja (2 registros) com estatisticas separadas |
| 11.6 | Secao HISTOGRAMAS | 3 histogramas ASCII sem erros |
| 11.7 | Secao REGISTROS POR DATA | Contagem de registros por dia |
| 11.8 | Secao RANKING DE INSUMOS | Consumo por produto e por cultura ordenados |
| 11.9 | Mensagem final | "Script executado com sucesso" |

---

## 12. Integracao Python → R

**Objetivo:** Verificar que alteracoes no Python refletem no R.

| Passo | Acao | Resultado esperado |
|-------|------|--------------------|
| 12.1 | No Python, inserir um novo registro | CSV atualizado com 5 registros |
| 12.2 | No RStudio, rodar `source(...)` | "Total de registros: 5" |
| 12.3 | No Python, deletar um registro | CSV atualizado com 4 registros |
| 12.4 | No RStudio, rodar `source(...)` | "Total de registros: 4" |
| 12.5 | No Python, atualizar um registro | CSV atualizado |
| 12.6 | No RStudio, rodar `source(...)` | Registro atualizado visivel no R |

---

## Resumo de cobertura

| Cenario | Python | R |
|---------|--------|---|
| Sem dados | OK | OK |
| Inserir (Cafe/triangulo) | OK | - |
| Inserir (Soja/retangulo) | OK | - |
| Todos os 5 produtos | OK | - |
| Mostrar dados | OK | OK |
| Atualizar dados | OK | - |
| Deletar dados | OK | - |
| Validacao de entrada | OK | - |
| Persistencia CSV | OK | OK |
| CSV vazio | OK | OK |
| CSV inexistente | OK | OK |
| Estatisticas | - | OK |
| Histogramas | - | OK |
| Rankings | - | OK |
| Integracao Python → R | OK | OK |
