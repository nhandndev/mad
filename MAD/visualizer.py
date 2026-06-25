import matplotlib.pyplot as plt
import networkx as nx
import pandas as pd
import seaborn as sns

def plot_network_communities(G, communities, title="Network Communities"):
    """Vẽ bản đồ mạng lưới với màu sắc phân biệt các cộng đồng."""
    plt.figure(figsize=(10, 8))
    pos = nx.spring_layout(G, seed=42)
    
    try:
        cmap = plt.colormaps['tab20']
    except AttributeError:
        cmap = plt.cm.get_cmap('tab20')
    
    for i, comm in enumerate(communities):
        color = cmap(i % 20)
        nx.draw_networkx_nodes(G, pos, nodelist=list(comm), node_color=[color], node_size=300, alpha=0.8)
    
    nx.draw_networkx_edges(G, pos, alpha=0.5)
    nx.draw_networkx_labels(G, pos, font_size=10, font_color="black")
    
    plt.title(title)
    plt.axis('off')
    plt.tight_layout()
    plt.savefig(f"{title.replace(' ', '_')}.png")
    plt.close()
    print(f"[Huy] Đã xuất biểu đồ mạng lưới: {title.replace(' ', '_')}.png")

def plot_modularity_trend(csv_file):
    """Vẽ biểu đồ đường xu hướng biến thiên điểm Modularity từ file CSV."""
    df = pd.read_csv(csv_file)
    
    fig, axes = plt.subplots(1, 2, figsize=(16, 6), sharey=True)
    
    # Biểu đồ 1: Louvain
    sns.lineplot(data=df[df['Algorithm'] == 'Louvain'], 
                 x='Removal_Percentage', y='Modularity', hue='Centrality_Metric', 
                 markers=True, dashes=False, ax=axes[0])
    axes[0].set_title('Thuật toán Louvain', fontsize=14)
    axes[0].set_xlabel('Tỷ lệ xóa Node VIP (%)')
    axes[0].set_ylabel('Điểm Modularity (Q)')
    axes[0].grid(True, linestyle='--', alpha=0.7)
    
    # Biểu đồ 2: Girvan-Newman
    sns.lineplot(data=df[df['Algorithm'] == 'Girvan-Newman'], 
                 x='Removal_Percentage', y='Modularity', hue='Centrality_Metric', 
                 markers=True, dashes=False, ax=axes[1])
    axes[1].set_title('Thuật toán Girvan-Newman', fontsize=14)
    axes[1].set_xlabel('Tỷ lệ xóa Node VIP (%)')
    axes[1].set_ylabel('')
    axes[1].grid(True, linestyle='--', alpha=0.7)
    
    plt.suptitle('Xu hướng sụt giảm Modularity khi loại bỏ VIP Nodes', fontsize=16, fontweight='bold')
    plt.tight_layout()
    plt.savefig("Modularity_Trend.png")
    plt.close()
    print("[Huy] Đã xuất biểu đồ xu hướng: Modularity_Trend.png (đã tách 2 khung)")
