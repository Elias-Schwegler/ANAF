# Zusammenfassung Woche 01 – Trigonometrie

**Modul:** Fortgeschrittene Analysis (ANA-F)  
**Dozenten:** Ron Porath, Joachim Wirth  
**Quelle:** Papula Band 1, Teil III, Kap. 9, 10, 10.5

---

## Lernziele

- Sicherer Umgang mit sin, cos, tan, cot und deren Umkehrfunktionen
- Ableitungen der trigonometrischen Funktionen und ihrer Umkehrfunktionen berechnen
- Lösen trigonometrischer Gleichungen

---

# 1. Trigonometrische Funktionen

> Papula Band 1, Kap. 9, Seiten 243–258

## 1.1 Grundlagen

### Definitionen am rechtwinkligen Dreieck

| Funktion | Formel |
|---|---|
| sin(α) | Gegenkathete / Hypotenuse |
| cos(α) | Ankathete / Hypotenuse |
| tan(α) | Gegenkathete / Ankathete = sin(α) / cos(α) |
| cot(α) | Ankathete / Gegenkathete = cos(α) / sin(α) = 1 / tan(α) |

### Einheitskreis

| Grad | 0° | 30° | 45° | 60° | 90° | 135° | 180° | 225° | 270° | 315° | 360° |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Radiant | 0 | π/6 | π/4 | π/3 | π/2 | 3π/4 | π | 5π/4 | 3π/2 | 7π/4 | 2π |
| sin | 0 | 1/2 | √2/2 | √3/2 | 1 | √2/2 | 0 | −√2/2 | −1 | −√2/2 | 0 |
| cos | 1 | √3/2 | √2/2 | 1/2 | 0 | −√2/2 | −1 | −√2/2 | 0 | √2/2 | 1 |

### Umrechnung Grad ↔ Radiant

Grundgleichung: φ / 360 = s / 2π

- **Grad → Radiant:** s = φ · π / 180
- **Radiant → Grad:** φ = s · 180 / π

## 1.2 Wichtige Formeln

### Trigonometrischer Pythagoras

$$\sin^2(x) + \cos^2(x) = 1$$

### Additionstheoreme

$$\sin(x \pm y) = \sin(x)\cos(y) \pm \cos(x)\sin(y)$$

$$\cos(x \pm y) = \cos(x)\cos(y) \mp \sin(x)\sin(y)$$

$$\tan(x \pm y) = \frac{\tan(x) \pm \tan(y)}{1 \mp \tan(x)\tan(y)}$$

### Doppelwinkelformeln (aus Additionstheoremen mit x₁ = x₂ = x)

$$\sin(2x) = 2 \cdot \sin(x) \cdot \cos(x)$$

$$\cos(2x) = \cos^2(x) - \sin^2(x)$$

### Halbwinkelformeln

$$\sin^2(x) = \frac{1}{2}[1 - \cos(2x)]$$

$$\cos^2(x) = \frac{1}{2}[1 + \cos(2x)]$$

### Beziehung Sinus ↔ Kosinus

$$\cos(x) = \sin\left(x + \frac{\pi}{2}\right)$$

$$\sin(x) = \cos\left(x - \frac{\pi}{2}\right)$$

## 1.3 Eigenschaften von sin und cos

| Eigenschaft | y = sin(x) | y = cos(x) |
|---|---|---|
| Definitionsbereich | −∞ < x < ∞ | −∞ < x < ∞ |
| Wertebereich | −1 ≤ y ≤ 1 | −1 ≤ y ≤ 1 |
| Periode | 2π | 2π |
| Symmetrie | ungerade | gerade |
| Nullstellen | x_k = k·π | x_k = π/2 + k·π |

## 1.4 Eigenschaften von tan und cot

| Eigenschaft | y = tan(x) | y = cot(x) |
|---|---|---|
| Definitionsbereich | x ≠ π/2 + k·π | x ≠ k·π |
| Wertebereich | −∞ < y < ∞ | −∞ < y < ∞ |
| Periode | π | π |
| Symmetrie | ungerade | ungerade |
| Nullstellen | x_k = k·π | x_k = π/2 + k·π |
| Pole | x_k = π/2 + k·π | x_k = k·π |

## 1.5 Allgemeine Sinusfunktion

$$y = a \cdot \sin(bx + c)$$

| Parameter | Wirkung | Formel |
|---|---|---|
| a > 0 | Amplitude (Dehnung/Stauchung in y-Richtung) | Wertebereich: −a ≤ y ≤ a |
| b > 0 | Frequenz (Dehnung/Stauchung in x-Richtung) | Periode: p = 2π/b |
| c | Phasenverschiebung | 1. Nullstelle: x₀ = −c/b |

## 1.6 Aufgabentypen

1. **Umrechnung Grad ↔ Bogenmaß** (Aufg. 1)
2. **Funktionswerte berechnen** mit Taschenrechner (Aufg. 2)
3. **Parabelannäherung** an Sinuskurve (Aufg. 4)
4. **Allgemeine Sinusfunktion analysieren**: Amplitude, Periode, Phasenverschiebung bestimmen und skizzieren (Aufg. 5, 6)
5. **Schwingungen beschreiben**: Physikalische Anwendungen als Sinusfunktionen formulieren (Aufg. 7, 8, 9)

---

# 2. Arkusfunktionen (Umkehrfunktionen)

> Papula Band 1, Kap. 10, Seiten 271–277

## 2.1 Das Problem

Trigonometrische Funktionen sind **nicht umkehrbar** (fehlende Monotonie durch Periodizität). Lösung: Einschränkung auf ein **monotones Intervall**.

## 2.2 Übersicht Arkusfunktionen

| Funktion | Einschränkungsintervall | Definitionsbereich | Wertebereich | Monotonie |
|---|---|---|---|---|
| y = arcsin(x) | −π/2 ≤ x ≤ π/2 | −1 ≤ x ≤ 1 | −π/2 ≤ y ≤ π/2 | steigend |
| y = arccos(x) | 0 ≤ x ≤ π | −1 ≤ x ≤ 1 | 0 ≤ y ≤ π | fallend |
| y = arctan(x) | −π/2 < x < π/2 | −∞ < x < ∞ | −π/2 < y < π/2 | steigend |
| y = arccot(x) | 0 < x < π | −∞ < x < ∞ | 0 < y < π | fallend |

### Wichtige Quadranten

| Funktion | Liefert Winkel aus... |
|---|---|
| arcsin | 1. und 4. Quadrant |
| arccos | 1. und 2. Quadrant |
| arctan | 1. und 4. Quadrant |
| arccot | 1. und 2. Quadrant |

### Nützliche Beziehung

$$\text{arccot}(x) = \frac{\pi}{2} - \arctan(x)$$

## 2.3 Wichtige Werte

| x | arcsin(x) | arccos(x) |
|---|---|---|
| 0 | 0 | π/2 |
| 0.5 | π/6 (30°) | π/3 (60°) |
| 1 | π/2 (90°) | 0 |

arctan(1) = π/4 (45°)

## 2.4 Aufgabentypen

1. **Arkusfunktionswerte berechnen** mit Taschenrechner (Aufg. 13)
2. **Schwingungsüberlagerung**: Amplitude und Phase aus Zeigerdiagramm bestimmen (Aufg. 14, 15)

---

# 3. Trigonometrische Gleichungen

> Papula Band 1, Kap. 10.5, Seiten 278–279

## 3.1 Lösungsstrategie

Es gibt **kein allgemeines Lösungsverfahren** — der Weg ist von Fall zu Fall verschieden. Typische Schritte:

1. **Argumente vereinheitlichen** (z.B. sin(2x) = 2·sin(x)·cos(x) verwenden)
2. **Faktorisieren** (Produkt = 0 → mindestens ein Faktor = 0)
3. **Nicht durch trig. Funktionen dividieren** (Lösungen gehen verloren!)
4. **Hauptwert** mit Arkusfunktion bestimmen
5. **Alle Lösungen** durch Periodizität angeben (+ k·2π bzw. + k·π)

## 3.2 Beispiel: sin(2x) = 1.5·cos(x)

**Schritt 1:** Doppelwinkelformel anwenden:
$$2\sin(x)\cos(x) = 1.5\cos(x)$$

**Schritt 2:** Umstellen und faktorisieren:
$$\cos(x)(2\sin(x) - 1.5) = 0$$

**Schritt 3:** Fälle lösen:

**Fall 1:** cos(x) = 0
→ x₁ₖ = π/2 + k·π (k ∈ ℤ)

**Fall 2:** sin(x) = 0.75
→ x₂ₖ = arcsin(0.75) + k·2π = 0.848 + k·2π
→ x₃ₖ = π − arcsin(0.75) + k·2π = 2.294 + k·2π

## 3.3 Lösungsmuster für Standardgleichungen

| Gleichung | Hauptwert | Alle Lösungen |
|---|---|---|
| sin(x) = a | x₀ = arcsin(a) | x = x₀ + k·2π **und** x = π − x₀ + k·2π |
| cos(x) = a | x₀ = arccos(a) | x = ±x₀ + k·2π |
| tan(x) = a | x₀ = arctan(a) | x = x₀ + k·π |

## 3.4 Aufgabentypen

1. **Trigonometrische Gleichungen lösen**: Substitution + Arkusfunktion + Periodizität (Aufg. 16)

---

# 4. Empfohlene Übungsaufgaben

> Papula Band 1, Teil III, Seiten 317–320 | Lösungen: Seiten 756–761

| Aufgabe | Thema | Beschreibung |
|---|---|---|
| **1** | Umrechnung | Grad ↔ Bogenmaß umrechnen |
| **4** | Parabelapproximation | Sinuskurve durch Parabel annähern |
| **5** | Allgemeine Sinusfunktion | Amplitude, Periode, Phase bestimmen (sin/cos) |
| **13** | Arkusfunktionen | Werte berechnen |
| **16** | Trig. Gleichungen | Gleichungen lösen mit Substitution |

---

# 5. Lösungen der empfohlenen Aufgaben

## Aufgabe 1 – Umrechnung Grad ↔ Bogenmaß

| Grad | 40.36° | 81.19° | −322.08° | 278.19° | −78.46° | 4.83° | 118.6° |
|---|---|---|---|---|---|---|---|
| Bogenmaß | 0.7044 | 1.4171 | −5.6213 | 4.8553 | −1.3694 | 0.0843 | 2.0700 |

## Aufgabe 4 – Parabelapproximation

Nullstellen: x₁ = 0, x₂ = π → Produktansatz: y = a·x·(x − π)

Maximum bei x = π/2: y(π/2) = 1 → a = −4/π²

**Ergebnis:** y = −(4/π²)·x² + (4/π)·x

## Aufgabe 5 – Allgemeine Sinusfunktion

Für y = A·sin(bx + c) bzw. y = A·cos(bx + c): Bestimme A, p = 2π/b, x₀ = −c/b

| Teil | A | Periode p | x₀ |
|---|---|---|---|
| a) | 2 | 2π/3 | π/18 |
| b) | 5 | π | −2.1 |
| c) | 10 | 2 | 3 |
| d) | 2.4 | π/2 | π/8 |

## Aufgabe 13 – Arkusfunktionen

| Teil | Wert |
|---|---|
| a) | 0.5980 |
| b) | −1.2614 |
| c) | 1.0781 |
| d) | 4.4304 |
| e) | 0.8084 |
| f) | 0.3082 |
| g) | 1.1837 |
| h) | 2.8198 |

## Aufgabe 16 – Trigonometrische Gleichungen

### a) sin(2x + 5) = 0.4

Substitution u = 2x + 5 → sin(u) = 0.4

- u₁ₖ = arcsin(0.4) + k·2π = 0.4115 + k·2π
- u₂ₖ = (π − arcsin(0.4)) + k·2π = 2.7301 + k·2π

Rücksubstitution x = 0.5·(u − 5):
- x₁ₖ = −2.2943 + k·π
- x₂ₖ = −1.1350 + k·π

### b) tan(2(x + 1)) = 1

Substitution u = 2(x + 1) → tan(u) = 1

- uₖ = π/4 + k·π

Rücksubstitution: x = 0.5·(u − 2)
- xₖ = −0.6073 + k·π/2

### c) √(1 − sin²(x)) = cos(x − 1) → cos(x) = 0.5

Substitution u = x − 1 → cos(u) = 0.5

- x₁ₖ = 2.0472 + k·2π (arccos(0.5) + 1)
- x₂ₖ = −0.0472 + k·2π (−arccos(0.5) + 1)

### d) sin(x) = √(1 − sin²(x))

Quadrieren: sin²(x) = cos²(x) → tan²(x) = 1 → tan(x) = ±1

Da sin(x) ≥ 0 (Wurzel!), nur 1./2. Quadrant:
- x₁ₖ = π/4 + k·2π
- x₂ₖ = 3π/4 + k·2π

---

# 6. Python / NumPy – Trigonometrie in der Praxis

> NumPy bietet alle trigonometrischen Funktionen und Arkusfunktionen direkt an. Alle Funktionen arbeiten standardmässig im **Bogenmaß (Radiant)**.

## 6.1 Grundfunktionen – Übersicht

| Mathematik | NumPy | Beschreibung |
|---|---|---|
| sin(x) | `np.sin(x)` | Sinus |
| cos(x) | `np.cos(x)` | Kosinus |
| tan(x) | `np.tan(x)` | Tangens |
| arcsin(x) | `np.arcsin(x)` | Arkussinus |
| arccos(x) | `np.arccos(x)` | Arkuskosinus |
| arctan(x) | `np.arctan(x)` | Arkustangens |
| Grad → Rad | `np.deg2rad(x)` oder `np.radians(x)` | Umrechnung |
| Rad → Grad | `np.rad2deg(x)` oder `np.degrees(x)` | Umrechnung |
| π | `np.pi` | Kreiszahl |

## 6.2 Umrechnung Grad ↔ Radiant (→ Aufg. 1)

```python
import numpy as np

# Einzelwert
grad = 45
rad = np.deg2rad(grad)          # 0.7854 (= π/4)
zurueck = np.rad2deg(rad)       # 45.0

# Array (wie Aufgabe 1)
grade = np.array([40.36, 81.19, -322.08, 278.19, -78.46, 4.83, 118.6])
bogenmass = np.deg2rad(grade)
print(np.round(bogenmass, 4))
# [ 0.7044  1.4171 -5.6213  4.8553 -1.3694  0.0843  2.07  ]
```

## 6.3 Wertetabelle & Einheitskreis (→ Lernziel: Sicherer Umgang)

```python
import numpy as np

# Spezielle Winkel
winkel_grad = np.array([0, 30, 45, 60, 90, 180, 270, 360])
winkel_rad = np.deg2rad(winkel_grad)

# Alle trig. Funktionen auf einmal
print("sin:", np.round(np.sin(winkel_rad), 4))
print("cos:", np.round(np.cos(winkel_rad), 4))

# Trigonometrischer Pythagoras prüfen
x = np.linspace(0, 2*np.pi, 100)
check = np.sin(x)**2 + np.cos(x)**2   # Immer 1.0!
print("sin²+cos² =", np.allclose(check, 1))  # True
```

## 6.4 Allgemeine Sinusfunktion analysieren (→ Aufg. 5)

```python
import numpy as np

# y = A * sin(b*x + c)
# Aufgabe 5a: y = 2*sin(3x + π/6)
A, b, c = 2, 3, np.pi/6
periode = 2 * np.pi / b          # 2π/3 ≈ 2.094
x0 = -c / b                      # -π/18 ≈ -0.1745
print(f"Amplitude: {A}, Periode: {periode:.4f}, 1. Nullstelle: {x0:.4f}")

# Funktionswerte berechnen
x = np.linspace(-np.pi, 2*np.pi, 500)
y = A * np.sin(b * x + c)
```

## 6.5 Arkusfunktionen (→ Aufg. 13)

```python
import numpy as np

# arcsin, arccos, arctan liefern Radiant
print(np.arcsin(0.5))            # π/6 = 0.5236
print(np.arccos(0.5))            # π/3 = 1.0472
print(np.arctan(1))              # π/4 = 0.7854

# In Grad umrechnen
print(np.rad2deg(np.arcsin(0.5)))  # 30°
print(np.rad2deg(np.arccos(0.5)))  # 60°

# arccot(x) = π/2 - arctan(x)
def arccot(x):
    return np.pi/2 - np.arctan(x)

print(arccot(1))                 # π/4 = 0.7854
```

## 6.6 Trigonometrische Gleichungen lösen (→ Aufg. 16)

```python
import numpy as np

# Aufgabe 16a: sin(2x + 5) = 0.4
# Substitution: u = 2x + 5, sin(u) = 0.4
u1 = np.arcsin(0.4)              # Hauptwert: 0.4115
u2 = np.pi - np.arcsin(0.4)     # Symmetrielösung: 2.7301

# Rücksubstitution: x = (u - 5) / 2
x1 = (u1 - 5) / 2               # -2.2943
x2 = (u2 - 5) / 2               # -1.1350
print(f"x1 = {x1:.4f} + k·π")
print(f"x2 = {x2:.4f} + k·π")

# Alle Lösungen im Intervall [0, 4π] generieren
loesungen = []
for k in range(-5, 6):
    for x_base in [x1, x2]:
        x_val = x_base + k * np.pi
        if 0 <= x_val <= 4 * np.pi:
            loesungen.append(round(x_val, 4))
print("Lösungen in [0, 4π]:", sorted(loesungen))
```

## 6.7 Additionstheoreme verifizieren

```python
import numpy as np

x, y = np.pi/6, np.pi/4

# sin(x+y) = sin(x)*cos(y) + cos(x)*sin(y)
links = np.sin(x + y)
rechts = np.sin(x)*np.cos(y) + np.cos(x)*np.sin(y)
print(f"sin(x+y) = {links:.6f} == {rechts:.6f}? {np.isclose(links, rechts)}")

# Doppelwinkelformel: sin(2x) = 2*sin(x)*cos(x)
print(np.isclose(np.sin(2*x), 2*np.sin(x)*np.cos(x)))  # True
```
