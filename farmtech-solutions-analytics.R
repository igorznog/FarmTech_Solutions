# FarmTech Solutions — Análise Estatística em R

# Funções utilitárias de formatação

linha <- function(char = "-", n = 60) cat(strrep(char, n), "\n")

titulo <- function(texto) {
  cat("\n")
  linha("=")
  cat(paste0("  ", texto, "\n"))
  linha("=")
}

secao <- function(texto) {
  cat("\n")
  linha("-")
  cat(paste0("  ", texto, "\n"))
  linha("-")
}

# Leitura dos dados gerados pelo Python (CSV)

arquivo_csv <- file.path(dirname(sys.frame(1)$ofile %||% "."), "farmtech-solutions-dados.csv")
if (!file.exists(arquivo_csv)) {
  arquivo_csv <- "farmtech-solutions-dados.csv"
}

titulo("FARMTECH SOLUTIONS — ANÁLISE ESTATÍSTICA EM R")

if (!file.exists(arquivo_csv)) {
  cat("\n  Nenhum dado encontrado.\n")
  cat("  Execute o programa Python primeiro para gerar os dados:\n")
  cat("  > python farmtech-solutions.py\n\n")
  cat("  Apos inserir registros, rode este script novamente.\n\n")
} else {

registros <- read.csv(arquivo_csv, stringsAsFactors = FALSE, encoding = "UTF-8")

if (nrow(registros) == 0) {
  cat("\n  O arquivo CSV existe mas esta vazio.\n")
  cat("  Insira registros pelo Python e rode este script novamente.\n\n")
} else {

# Exibição dos registros

cat("\n  Dados carregados com sucesso!\n")
cat(paste0("  Total de registros: ", nrow(registros), "\n"))

secao("REGISTROS COMPLETOS")
for (i in seq_len(nrow(registros))) {
  r <- registros[i, ]
  cat(sprintf("\n  [ID %d] Inserido em: %s\n",
              r$id, r$data_insercao))
  cat(sprintf("  Cultura: %-10s | Área: %8.1f m²\n",
              r$cultura, r$area_m2))
  cat(sprintf("  Produto: %-10s | Dose: %.0f mL/m | Ruas: %d | Comp: %.1f m | Total: %.1f L\n",
              r$produto, r$dose_ml_metro, r$num_ruas, r$comp_rua_m, r$total_litros))
}

# Estatísticas gerais

titulo("ESTATÍSTICAS GERAIS (TODAS AS CULTURAS)")

variaveis <- list(
  "Área plantada (m²)"       = registros$area_m2,
  "Total de insumo (litros)" = registros$total_litros,
  "Dose aplicada (mL/metro)" = registros$dose_ml_metro,
  "Nº de ruas"               = registros$num_ruas,
  "Comprimento da rua (m)"   = registros$comp_rua_m
)

for (nome in names(variaveis)) {
  v <- variaveis[[nome]]
  cat(sprintf("\n  %s\n", nome))
  cat(sprintf("    Média:          %10.2f\n",  mean(v)))
  cat(sprintf("    Desvio padrão:  %10.2f\n",  sd(v)))
  cat(sprintf("    Mínimo:         %10.2f\n",  min(v)))
  cat(sprintf("    Máximo:         %10.2f\n",  max(v)))
  cat(sprintf("    Mediana:        %10.2f\n",  median(v)))
  cat(sprintf("    Q1 / Q3:        %10.2f / %.2f\n",
              quantile(v, 0.25), quantile(v, 0.75)))
}

secao("SUMMARY COMPLETO (R nativo)")
print(summary(registros[, c("area_m2", "total_litros", "dose_ml_metro",
                            "num_ruas", "comp_rua_m")]))

# Estatísticas por cultura

titulo("ESTATÍSTICAS POR CULTURA")

culturas <- unique(registros$cultura)

for (cult in culturas) {
  sub <- registros[registros$cultura == cult, ]
  secao(paste0("Cultura: ", cult, " (", nrow(sub), " registros)"))

  cat(sprintf("  Área (m²)        — Média: %8.1f | DP: %7.1f | Min: %7.1f | Max: %7.1f\n",
              mean(sub$area_m2), sd(sub$area_m2), min(sub$area_m2), max(sub$area_m2)))
  cat(sprintf("  Insumo (litros)  — Média: %8.1f | DP: %7.1f | Min: %7.1f | Max: %7.1f\n",
              mean(sub$total_litros), sd(sub$total_litros),
              min(sub$total_litros), max(sub$total_litros)))

  prod_freq <- sort(table(sub$produto), decreasing = TRUE)
  cat(sprintf("  Produto mais usado: %s (%d registro(s))\n",
              names(prod_freq)[1], prod_freq[1]))
}

# Histogramas ASCII

titulo("HISTOGRAMAS — DISTRIBUIÇÃO DE FREQUÊNCIA")

histograma_ascii <- function(valores, titulo_hist, n_faixas = 5) {
  secao(titulo_hist)
  breaks    <- seq(min(valores), max(valores), length.out = n_faixas + 1)
  contagens <- hist(valores, breaks = breaks, plot = FALSE)$counts
  faixas    <- hist(valores, breaks = breaks, plot = FALSE)$breaks
  max_cont  <- max(contagens)

  for (i in seq_along(contagens)) {
    label <- sprintf("  [%7.1f – %7.1f] ", faixas[i], faixas[i + 1])
    barra <- strrep("█", round(contagens[i] / max_cont * 30))
    cat(paste0(label, barra, " (", contagens[i], ")\n"))
  }
}

histograma_ascii(registros$area_m2,       "Área Plantada (m²)")
histograma_ascii(registros$total_litros,  "Total de Insumo (litros)")
histograma_ascii(registros$dose_ml_metro, "Dose Aplicada (mL/metro)")

# Registros por data

titulo("REGISTROS POR DATA DE INSERÇÃO")

datas <- sub(" .*", "", registros$data_insercao)  # extrai só a data (sem hora)
freq_datas <- sort(table(datas), decreasing = TRUE)

for (i in seq_along(freq_datas)) {
  cat(sprintf("  %s → %d registro(s)\n", names(freq_datas)[i], freq_datas[i]))
}

# Ranking de insumos

titulo("RANKING DE INSUMOS")

secao("Consumo total por produto (litros)")
por_produto <- aggregate(total_litros ~ produto, data = registros, FUN = sum)
por_produto <- por_produto[order(-por_produto$total_litros), ]
rownames(por_produto) <- NULL

for (i in seq_len(nrow(por_produto))) {
  cat(sprintf("  %d. %-12s → %8.1f L\n",
              i, por_produto$produto[i], por_produto$total_litros[i]))
}

secao("Consumo total por cultura (litros)")
por_cultura <- aggregate(total_litros ~ cultura, data = registros, FUN = sum)
por_cultura <- por_cultura[order(-por_cultura$total_litros), ]
rownames(por_cultura) <- NULL

for (i in seq_len(nrow(por_cultura))) {
  cat(sprintf("  %d. %-10s → %8.1f L\n",
              i, por_cultura$cultura[i], por_cultura$total_litros[i]))
}

titulo("FIM DA ANÁLISE — FarmTech Solutions")
cat("  Script executado com sucesso.\n\n")

} # fim do else (nrow > 0)
} # fim do else (file.exists)
