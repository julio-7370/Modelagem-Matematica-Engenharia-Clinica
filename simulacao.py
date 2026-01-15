import numpy as np
import matplotlib.pyplot as plt

np.random.seed(42)
plt.style.use('ggplot')

def simular_mm_c(dias, num_equipamentos, taxa_falha, num_tecnicos, produtividade_tecnico):
    """
    Simula um sistema de filas M/M/c para manutenção de equipamentos.

    Parâmetros:
    > dias: Horizonte de simulação (em dias).
    > num_equipamentos: Total de equipamentos em operação.
    > taxa_falha: Taxa diária de falha por equipamento (λ).
    > num_tecnicos: Número de técnicos disponíveis.
    > produtividade_tecnico: Taxa média de atendimento por técnico por dia (μ).

    -> Retorno: Backlog diário do sistema.
    """

    lambda_diario = num_equipamentos * taxa_falha
    mu = produtividade_tecnico

    backlog = 0
    historico_backlog = []

    for _ in range(dias):
        # Chegadas (Poisson)
        chegadas = np.random.poisson(lambda_diario)

        # Atendimentos por técnico (Poisson ~ aproximação discreta do exp.)
        atendimentos = sum(np.random.poisson(mu) for _ in range(num_tecnicos))

        backlog = max(0, backlog + chegadas - atendimentos)
        historico_backlog.append(backlog)

    return historico_backlog


DIAS = 180 # 6 meses
TOTAL_EQUIP = 2000
TAXA_FALHA = 0.005 # 0.5% ao dia
PROD_TECNICO = 3 # 3 equipamentos/dia

# Equipe subdimensionada
# Sistema instável, com 3 técnicos
backlog_instavel = simular_mm_c(DIAS, TOTAL_EQUIP, TAXA_FALHA, num_tecnicos=3, produtividade_tecnico=PROD_TECNICO)

# Equipe otimizada
# Sistema estável, com 4 técnicos
backlog_estavel = simular_mm_c(DIAS, TOTAL_EQUIP, TAXA_FALHA, num_tecnicos=4, produtividade_tecnico=PROD_TECNICO)

plt.figure(figsize=(12, 6))
plt.plot(backlog_instavel, color= '#e74c3c', label='Equipe Caótica', linewidth=2)
plt.plot(backlog_estavel, color= '#27ae60', label='Equipe Otimizada', linewidth=2)
plt.xlabel('Dias de Operação', fontsize=12)
plt.ylabel('Equipamentos parados (Backlog)', fontsize=12)
plt.title('Backlog do Setor de Manutenção', fontsize=12)
plt.legend(fontsize=11)
plt.grid(True, alpha=0.3)
plt.axhline(y=20, color='orange', linestyle='--', alpha=0.5, label='Limite de Alerta')


plt.tight_layout()
plt.show()
