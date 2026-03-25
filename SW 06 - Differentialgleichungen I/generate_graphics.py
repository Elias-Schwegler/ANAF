import numpy as np
import matplotlib.pyplot as plt

# 1. Richtungsfeld und Lösungskurve
def plot_richtungsfeld():
    x = np.linspace(-2, 3, 20)
    y = np.linspace(-2, 3, 20)
    X, Y = np.meshgrid(x, y)
    
    # DGL: y' = x - y
    U = 1
    V = X - Y
    
    # Normalize vectors for plotting
    N = np.sqrt(U**2 + V**2)
    U = U / N
    V = V / N

    plt.figure(figsize=(8, 6))
    plt.quiver(X, Y, U, V, color='#2c3e50', alpha=0.4, angles='xy', scale=25)
    
    # Analytical solution for y' = x - y with y(0) = 1
    x_sol = np.linspace(-2, 3, 100)
    y_sol = 2 * np.exp(-x_sol) + x_sol - 1
    
    plt.plot(x_sol, y_sol, color='#e74c3c', linewidth=2.5, label="Lösungskurve $y(x)=2e^{-x} + x - 1$")
    plt.plot(0, 1, 'ko', label="Anfangswert P(0, 1)", markersize=8)
    
    plt.title("Richtungsfeld und Tangenten-Steigungen für $y' = x - y$", fontsize=14)
    plt.xlabel('x', fontsize=12)
    plt.ylabel('y', fontsize=12)
    plt.xlim(-2, 3)
    plt.ylim(-2, 3)
    plt.grid(True, linestyle='--', alpha=0.6)
    plt.legend(loc='lower right')
    plt.tight_layout()
    plt.savefig('richtungsfeld_erklaerung.png', dpi=150, bbox_inches='tight')
    plt.close()

# 2. Eulersches Polygonzugverfahren
def plot_euler_verfahren():
    # True solution for y' = y, y(0) = 1 => y = e^x
    x_true = np.linspace(0, 2, 100)
    y_true = np.exp(x_true)
    
    plt.figure(figsize=(8, 6))
    plt.plot(x_true, y_true, color='#3498db', linewidth=2.5, label="Exakte Lösung $y = e^x$")
    
    # Euler method
    h = 0.5
    x_euler = [0]
    y_euler = [1]
    
    for i in range(4):
        x_curr = x_euler[-1]
        y_curr = y_euler[-1]
        slope = y_curr  # DGL: y' = y
        x_next = x_curr + h
        y_next = y_curr + h * slope
        
        x_euler.append(x_next)
        y_euler.append(y_next)
        
        # Plot tangent lines
        t_x = np.linspace(x_curr, x_next, 10)
        t_y = y_curr + slope * (t_x - x_curr)
        plt.plot(t_x, t_y, color='#e67e22', linestyle='--', linewidth=1.5, alpha=0.8)

    plt.plot(x_euler, y_euler, color='#e74c3c', marker='o', markersize=8, linewidth=2, label=f"Euler-Näherung (Schrittweite h={h})")
    
    for idx, (xe, ye) in enumerate(zip(x_euler, y_euler)):
        plt.annotate(f"P{idx}", (xe, ye), textcoords="offset points", xytext=(-10, 10), ha='right', color='#c0392b', fontweight='bold')
    
    plt.title("Numerik: Eulersches Polygonzugverfahren ($y' = y$)", fontsize=14)
    plt.xlabel('x', fontsize=12)
    plt.ylabel('y', fontsize=12)
    plt.grid(True, linestyle='--', alpha=0.6)
    plt.legend()
    plt.tight_layout()
    plt.savefig('euler_verfahren_erklaerung.png', dpi=150, bbox_inches='tight')
    plt.close()

# 3. Allgemeine Lösung vs. Partikuläre Lösung (AWP)
def plot_kurvenschar():
    x = np.linspace(-2, 3, 100)
    plt.figure(figsize=(8, 6))
    
    # Family of curves for y' = x - y => y = C*e^-x + x - 1
    for C in [-2, -1, 0, 1, 3, 4]:
        y = C * np.exp(-x) + x - 1
        plt.plot(x, y, color='#95a5a6', alpha=0.6, linestyle='--')
        
    # The AWP solution
    C_awp = 2
    y_awp = C_awp * np.exp(-x) + x - 1
    plt.plot(x, y_awp, color='#8e44ad', linewidth=3, label="Partikuläre Lösung für AWP $y(0)=1$")
    plt.plot(0, 1, 'ko', markersize=8, label="Anfangswert P(0,1)")
    
    plt.title("Allgemeine Lösung (Kurvenschar) und Anfangswertproblem", fontsize=14)
    plt.xlabel('x', fontsize=12)
    plt.ylabel('y', fontsize=12)
    plt.xlim(-2, 3)
    plt.ylim(-4, 4)
    plt.grid(True, linestyle='--', alpha=0.6)
    plt.legend()
    plt.tight_layout()
    plt.savefig('kurvenschar_awp.png', dpi=150, bbox_inches='tight')
    plt.close()

if __name__ == "__main__":
    plot_kurvenschar()
    plot_richtungsfeld()
    plot_euler_verfahren()
    print("Alle Grafiken erfolgreich generiert!")
