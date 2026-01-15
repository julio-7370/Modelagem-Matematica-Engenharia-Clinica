# Simulação Estocástica de Backlog em Engenharia Clínica  
## Uma abordagem via Teoria das Filas (Modelo M/M/c)

Este repositório apresenta um estudo exploratório baseado em **simulação estocástica** para modelar o comportamento do backlog em um setor de manutenção de equipamentos médicos, utilizando fundamentos da **Teoria das Filas**, em especial o modelo **M/M/c**.

O trabalho tem como objetivo demonstrar como a dinâmica da manutenção hospitalar pode ser compreendida como um **sistema dinâmico probabilístico**, no qual pequenas variações nos parâmetros operacionais podem conduzir o sistema da estabilidade ao regime caótico.

---

## 1. Introdução

Setores de Engenharia Clínica frequentemente operam sob condições de:

- alta variabilidade na chegada de chamados,
- recursos humanos limitados,
- equipamentos com diferentes criticidades clínicas.

Essas características tornam a gestão da manutenção um problema clássico de **Pesquisa Operacional**, no qual decisões empíricas podem levar a **instabilidade sistêmica**, refletida em crescimento contínuo do backlog e redução da disponibilidade dos ativos.

A Teoria das Filas fornece uma estrutura matemática adequada para modelar, analisar e simular esse tipo de sistema.

---

## 2. Fundamentação Teórica

### 2.1 Modelo M/M/c

O sistema é modelado como uma fila do tipo **M/M/c**, caracterizada por:

- Chegadas Markovianas (Poisson)
- Tempos de atendimento Markovianos (exponenciais)
- `c` servidores paralelos (técnicos)

#### Notação:

- $\lambda$: taxa média de chegada de falhas  
- $\mu$: taxa média de atendimento por servidor  
- $c$: número de técnicos  
- $\rho$: fator de utilização do sistema  

---

### 2.2 Processo de Chegadas

Assume-se que cada equipamento falha de forma independente, com taxa diária \( \lambda_e \).

Assim, a taxa total de chegada é dada por:

$$
\lambda = N \cdot \lambda_e
$$

onde:
- $N$ é o número total de equipamentos em operação.

O número de falhas diárias é modelado como:

$$
A(t) \sim \text{Poisson}(\lambda)
$$

---

### 2.3 Processo de Atendimento

Cada técnico possui uma produtividade média $\mu$ (equipamentos/dia).

O número de atendimentos diários por técnico é aproximado por:

$$
S_i(t) \sim \text{Poisson}(\mu)
$$

O atendimento total diário do sistema é:

$$
S(t) = \sum_{i=1}^{c} S_i(t)
$$

---

### 2.4 Dinâmica do Backlog

O backlog $B(t)$ evolui segundo a equação de balanço discreta:

$$
B(t+1) = \max \left( 0,\; B(t) + A(t) - S(t) \right)
$$

Este modelo representa um **processo estocástico de tempo discreto**, no qual o backlog atua como variável de estado do sistema.

---

### 2.5 Condição de Estabilidade

Para sistemas M/M/c, a condição clássica de estabilidade é:

$$
\rho = \frac{\lambda}{c \mu} < 1
$$

- Se $\rho < 1$ : sistema estável (backlog limitado)
- Se $\rho \geq 1$ : sistema instável (backlog tende a crescer)

A simulação permite observar empiricamente essa transição entre regimes.

---

## 3. Metodologia de Simulação

A simulação foi implementada em Python utilizando Monte Carlo, considerando:

- Horizonte de simulação: **180 dias**
- Número de equipamentos: **2000**
- Taxa diária de falha por equipamento
- Produtividade média por técnico

Para cada dia:
1. Gera-se o número de falhas (Poisson)
2. Gera-se o número de atendimentos por técnico
3. Atualiza-se o backlog conforme a equação de estado

O uso de semente fixa garante reprodutibilidade dos resultados.

---

## 4. Cenários Analisados

### 4.1 Sistema Instável (Regime Caótico)

- Número de técnicos insuficiente
- $\rho \geq 1$
- Crescimento progressivo do backlog

Este cenário ilustra como o sistema entra em colapso mesmo sem variações extremas de demanda.

---

### 4.2 Sistema Estável (Regime Ordenado)

- Número de técnicos ajustado ao fluxo médio
- $\rho < 1$
- Backlog limitado e controlável

Este regime representa uma operação sustentável do setor de manutenção.

---

## 5. Resultados

A comparação gráfica entre os dois cenários evidencia:

- Sensibilidade do sistema à variabilidade estocástica
- Transição abrupta entre estabilidade e instabilidade
- Natureza não linear do backlog ao longo do tempo

Esses resultados reforçam que **backlog elevado é, frequentemente, um problema estrutural**, e não apenas operacional.

---

## 6. Discussão

Mesmo com hipóteses simplificadoras, o modelo captura aspectos fundamentais da Engenharia Clínica real:

- imprevisibilidade das falhas,
- limitação de recursos humanos,
- impacto sistêmico de decisões de dimensionamento.

A simulação mostra que abordagens quantitativas podem auxiliar gestores a **antecipar riscos**, em vez de apenas reagir a eles.

---

## 7. Limitações do Modelo

- Equipamentos não são diferenciados por criticidade
- Tempos de atendimento são homogêneos
- Não há priorização ou SLA explícito

Essas limitações abrem espaço para extensões futuras.

---

## 8. Trabalhos Futuros

- Introdução de Cadeias de Markov para estados operacionais
- Modelagem multi-classe de equipamentos
- Inclusão de políticas de priorização
- Calibração com dados reais de hospitais

---

## 9. Conclusão

Este estudo demonstra que a Engenharia Clínica pode ser formalmente tratada como um **problema de sistemas dinâmicos estocásticos**, no qual a Matemática fornece ferramentas valiosas para apoiar a gestão hospitalar.



Projeto desenvolvido por um estagiário em Engenharia Clínica com interesse em **Matemática Aplicada, Física Estatística e Sistemas de Saúde**.
