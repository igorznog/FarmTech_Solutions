# Changelog

## [1.5.0] - 2026-03-23

### Corrigido

- **Tratamento de CSV vazio/inexistente no R**: o script agora verifica se o arquivo CSV existe e se tem dados antes de executar as analises. Se nao houver dados, exibe mensagem amigavel e para a execucao sem erros.

---

## [1.4.0] - 2026-03-23

### Alterado

- **Padronizacao de nomes de arquivos**: todos os arquivos agora seguem o padrao `farmtech-solutions-*`.
  - `FarmTech Solutions.py` → `farmtech-solutions.py`
  - `faramtech-soluctions-analytics.R` → `farmtech-solutions-analytics.R`
  - `dados_farmtech.csv` → `farmtech-solutions-dados.csv`
- Referencias ao CSV atualizadas no Python e no R.

---

## [1.3.0] - 2026-03-23

### Melhorado

- **Perguntas mais claras para o usuario**: todas as perguntas do Python agora incluem a unidade esperada e um exemplo entre parenteses (ex: `Quantos mL de produto por metro de rua? (ex: 500)`).
- Selecao de cultura agora explica a formula usada (ex: `Café — área calculada como triângulo`).
- Perguntas de area incluem a formula (ex: `triângulo: base x altura / 2`).
- Secao "Manejo de Insumos" separada visualmente com titulo `--- Manejo de Insumos ---`.
- Perguntas padronizadas entre insercao (opcao 1) e atualizacao (opcao 3).

### Corrigido

- `salvar_csv()` agora nao salva CSV vazio — se todos os registros forem deletados, o arquivo e removido.

---

## [1.2.0] - 2026-03-23

### Alterado

- **Padronizacao de termos Python ↔ R**: unificados os nomes de campos entre os dois programas (dose mL/m, numero de ruas, comprimento da rua em metros, total em litros).
- Labels de entrada e exibicao no Python agora usam as mesmas unidades do CSV e do R (`mL/m`, `m`, `litros`).
- Removido comentario duplicado no script R.

---

## [1.1.0] - 2026-03-23

### Novo

- **Persistencia de dados em CSV**: o programa Python agora salva automaticamente os registros no arquivo `dados_farmtech.csv` apos cada operacao (inserir, atualizar, deletar).
- **Carregamento automatico**: ao iniciar, o Python le o CSV existente e restaura os dados da sessao anterior.
- **Integracao Python → R**: o script R agora le o `dados_farmtech.csv` gerado pelo Python em vez de usar dados mock, conectando os dois programas.
- **Menu de produtos**: lista pre-definida de insumos (Herbicida, Fungicida, Inseticida, Adubo, Fertilizante) para selecao, substituindo a digitacao livre.
- **Data de insercao**: cada registro agora armazena a data/hora em que foi criado.
- **Tela de delecao melhorada**: exibe tabela com ID, Cultura, Produto e Data de insercao para identificar corretamente o registro antes de deletar.

### Alterado

- Tela de exibicao de dados (opcao 2) agora mostra ID e data de insercao de cada registro.
- Script R atualizado para ler colunas do novo formato CSV (`id`, `data_insercao`, `cultura`, `area_m2`, `produto`, `dose_ml_metro`, `num_ruas`, `comp_rua_m`, `total_litros`).
- Secao "Registros por data de insercao" adicionada ao R.
- Removidos dados mock do script R — agora depende exclusivamente do CSV.

---

## [1.0.0] - Versao inicial

### Funcionalidades

- CRUD completo (Inserir, Mostrar, Atualizar, Deletar) para culturas Cafe e Soja.
- Calculo de area por figura geometrica (triangulo para Cafe, retangulo para Soja).
- Calculo de manejo de insumos (dose por metro x comprimento x numero de linhas).
- Dados organizados em vetores.
- Menu interativo com validacao de entrada (float e int).
- Script R com analise estatistica: media, desvio padrao, min, max, mediana, quartis, histogramas ASCII e ranking de insumos.
