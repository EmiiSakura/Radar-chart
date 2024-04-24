import numpy as np
import matplotlib.pyplot as plt
from ipywidgets import interact

# função para criar gráfico de radar
def radar_chart(ax, labels, values, title):
    num_vars = len(labels)
    # Calcula os ângulos para cada variável
    angles = np.linspace(0, 2 * np.pi, num_vars, endpoint=False).tolist()
    angles += [angles[0]]
    values += [values[0]]
    
    # Cria o gráfico
    ax.fill(angles, values, color='red', alpha=0.7)
    ax.plot(angles, values, color='red', linewidth=1.5, linestyle='solid')
    
    # Adiciona os rótulos
    ax.set_yticklabels([])
    ax.set_xticks(angles[:-1])
    ax.set_xticklabels(labels, fontsize=10, fontweight='bold', color='red')
    
    # Adiciona o título
    ax.set_title(title, size=15, color='red', fontweight='bold')
    ax.title.set_position([0.5, 1.15])

    # Adiciona detalhes
    for angle, label in zip(angles[:-1], labels):
        x = np.cos(angle)
        y = np.sin(angle)
        ax.text(angle, 11, label, fontsize=8, ha='center', va='center', color='red', fontweight='bold')
        ax.plot([0, x], [0, y], color='red', linewidth=0.5, linestyle='--')

# Dados do gráfico
labels = ['Knowledge', 'Kindness', 'Efficiency', 'Determination', 'Self-care']
stats = [9, 8, 7, 6, 7]

# Função para atualizar os valores dos stats
def update_stats(knowledge, kindness, efficiency, determination, self_care):
    global stats
    stats = [knowledge, kindness, efficiency, determination, self_care]
    update_plot()

# Função para atualizar o gráfico
def update_plot():
    ax.clear()
    radar_chart(ax=ax, labels=labels, values=stats, title='Personal Stats')
    plt.ylim(0, 12)
    ax.axis('off')
    plt.show()

# Cria a figura
fig, ax = plt.subplots(figsize=(8, 8), subplot_kw=dict(polar=True))

# Chama a função para criar o gráfico de radar
radar_chart(ax=ax, labels=labels, values=stats, title='Personal Stats')

# Cria sliders interativos para atualizar os valores dos stats
interact(update_stats, knowledge=(0, 10, 1), kindness=(0, 10, 1), efficiency=(0, 10, 1), determination=(0, 10, 1), self_care=(0, 10, 1))

# Ajusta os limites
plt.ylim(0, 12)

# Remove os eixos
ax.axis('off')

# Mostra o gráfico
plt.show()