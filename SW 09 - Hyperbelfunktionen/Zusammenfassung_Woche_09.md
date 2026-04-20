# Zusammenfassung Woche 09 – Hyperbelfunktionen

**Modul:** Fortgeschrittene Analysis (ANA-F)
**Dozenten:** Ron Porath, Joachim Wirth
**Quelle:** Papula Band 1, Kapitel III, Abschnitt 13, Seiten 300–309
**Übungen:** Papula Band 1, Kapitel III, Abschnitt 13, Seite 322, Aufgaben 11), 12), 13)
**Lösungen:** Papula Band 1, Seite 763

---

## Lernziele (aus den Folien)

- Definition der Hyperbelfunktionen und deren Zusammenhang mit den trigonometrischen Funktionen
- Hyperbolischer Pythagoras und Additionstheoreme anwenden
- Ableitungen der Hyperbelfunktionen beherrschen
- Umkehrfunktionen (Areafunktionen) kennen und anwenden
- Die **Kettenlinie** als Anwendung der Hyperbelfunktionen verstehen
- Die o.g. Funktionen zur Lösung von Problemen aus der Praxis einsetzen können

---

# 1. Wiederholung: Trigonometrische Funktionen über die Exponentialfunktion

> Vorlesungsfolien, Seite 6 / Unterrichtsnotizen Seite 11

## 1.1 Von der Euler-Formel zu cos und sin

Aus der **Euler-Formel** $e^{ix} = \cos(x) + i\sin(x)$ und der Tatsache, dass $e^{-ix} = \cos(x) - i\sin(x)$, kann man cos und sin durch die Exponentialfunktion ausdrücken:

$$e^{ix} + e^{-ix} = 2\cos(x) \quad \Rightarrow \quad \boxed{\cos(x) = \frac{1}{2}\left(e^{ix} + e^{-ix}\right)}$$

$$e^{ix} - e^{-ix} = 2i\sin(x) \quad \Rightarrow \quad \boxed{\sin(x) = \frac{1}{2i}\left(e^{ix} - e^{-ix}\right)}$$

## 1.2 Die Schlüsselidee: Was passiert, wenn man das $i$ weglässt?

Die Hyperbelfunktionen entstehen, wenn man in den obigen Formeln das $i$ entfernt:

| Trigonometrisch | Hyperbolisch |
|---|---|
| $\cos(x) = \frac{1}{2}(e^{{\color{red}i}x} + e^{-{\color{red}i}x})$ | $\cosh(x) = \frac{1}{2}(e^{x} + e^{-x})$ |
| $\sin(x) = \frac{1}{2{\color{red}i}}(e^{{\color{red}i}x} - e^{-{\color{red}i}x})$ | $\sinh(x) = \frac{1}{2}(e^{x} - e^{-x})$ |

> 💡 **Merkhilfe:** Hyperbelfunktionen = trigonometrische Funktionen ohne das $i$. Das ist der einfachste Weg, sich die Definitionen zu merken!

---

# 2. Definition der Hyperbelfunktionen

> Papula Band 1, Kap. III, Abschn. 13, S. 300–303

## 2.1 Die vier Hyperbelfunktionen

$$\boxed{\cosh(x) = \frac{e^x + e^{-x}}{2}} \qquad \text{(Cosinus hyperbolicus)}$$

$$\boxed{\sinh(x) = \frac{e^x - e^{-x}}{2}} \qquad \text{(Sinus hyperbolicus)}$$

$$\boxed{\tanh(x) = \frac{\sinh(x)}{\cosh(x)} = \frac{e^x - e^{-x}}{e^x + e^{-x}}} \qquad \text{(Tangens hyperbolicus)}$$

$$\boxed{\coth(x) = \frac{\cosh(x)}{\sinh(x)} = \frac{e^x + e^{-x}}{e^x - e^{-x}}} \qquad \text{(Cotangens hyperbolicus, } x \neq 0\text{)}$$

## 2.2 Wichtige Funktionswerte und Eigenschaften

| Eigenschaft | $\cosh(x)$ | $\sinh(x)$ | $\tanh(x)$ |
|---|---|---|---|
| **Wert bei $x=0$** | $\cosh(0) = 1$ | $\sinh(0) = 0$ | $\tanh(0) = 0$ |
| **Symmetrie** | **gerade** ($\cosh(-x) = \cosh(x)$) | **ungerade** ($\sinh(-x) = -\sinh(x)$) | **ungerade** |
| **Wertebereich** | $[1, \infty)$ | $(-\infty, \infty)$ | $(-1, 1)$ |
| **Definitionsbereich** | $\mathbb{R}$ | $\mathbb{R}$ | $\mathbb{R}$ |
| **Monotonie** | fallend für $x<0$, steigend für $x>0$ | streng monoton steigend | streng monoton steigend |

## 2.3 Graphen der Hyperbelfunktionen

```
      y
      |        cosh(x)
   3 -+       /        \          cosh(x) ≥ 1 immer!
      |      /          \
   2 -+    /              \
      |   /                \
   1 -+--*------------------*--  ← cosh(0) = 1
      | /  \              /  \
   0 -+-----\----*-------/----→ x
      |      \  /|      /
  -1 -+       \/       /
      |    sinh(x)    /          sinh(x): ungerade, durch Ursprung
  -2 -+              /
      |             /
  -3 -+            /
      |
     -3  -2  -1  0  1  2  3

      y
      |
   1 -+- - - - - - - - - - - -  ← Asymptote y = 1
      |           ___-------
      |       __/
   0 -+------*------------------→ x   tanh(x)
      |  __/
      |/___
  -1 -+- - - - - - - - - - - -  ← Asymptote y = -1
      |
     -3  -2  -1  0  1  2  3
```

## 2.4 Geometrische Interpretation: Kreis vs. Hyperbel

| | Einheitskreis | Einheitshyperbel |
|---|---|---|
| **Gleichung** | $x^2 + y^2 = 1$ | $x^2 - y^2 = 1$ |
| **Parametrisierung** | $x = \cos(t)$, $y = \sin(t)$ | $x = \cosh(t)$, $y = \sinh(t)$ |
| **Identität** | $\cos^2(t) + \sin^2(t) = 1$ | $\cosh^2(t) - \sinh^2(t) = 1$ |

```
      y                              y
      |    * Kreis                    |        / Asymptote y=x
   1 -+  /   \                    3 -+       *
      | *     *                      |      / \  Hyperbel
   0 -+*-------*→ x              0 -+-----*---\---→ x
      | *     *                      |      \ /
  -1 -+  \   /                   -3 -+       *
      |    *                         |        \ Asymptote y=-x
      
  x(t) = cos(t)                  x(t) = cosh(t)
  y(t) = sin(t)                  y(t) = sinh(t)
```

---

# 3. Hyperbolischer Pythagoras

> Vorlesungsfolien, Seite 9 / Unterrichtsnotizen Seite 12

## 3.1 Herleitung

$$\cosh^2(x) = \left[\frac{e^x + e^{-x}}{2}\right]^2 = \frac{e^{2x} + 2 + e^{-2x}}{4}$$

$$\sinh^2(x) = \left[\frac{e^x - e^{-x}}{2}\right]^2 = \frac{e^{2x} - 2 + e^{-2x}}{4}$$

Differenz bilden:

$$\cosh^2(x) - \sinh^2(x) = \frac{(e^{2x} + 2 + e^{-2x}) - (e^{2x} - 2 + e^{-2x})}{4} = \frac{4}{4}$$

$$\boxed{\cosh^2(x) - \sinh^2(x) = 1 \qquad \text{(Hyperbolischer Pythagoras)}}$$

## 3.2 Vergleich mit dem trigonometrischen Pythagoras

| Trigonometrisch | Hyperbolisch |
|---|---|
| $\cos^2(x) + \sin^2(x) = 1$ | $\cosh^2(x) - \sinh^2(x) = 1$ |
| **Plus**zeichen | **Minus**zeichen |

> ⚠️ **Prüfungsrelevant:** Das Minuszeichen ist der entscheidende Unterschied! Nicht verwechseln!

## 3.3 Nützliche Umformungen (aus dem hyperbolischen Pythagoras)

$$\cosh^2(x) = 1 + \sinh^2(x) \qquad \Rightarrow \qquad \cosh(x) = \sqrt{1 + \sinh^2(x)}$$

$$\sinh^2(x) = \cosh^2(x) - 1 \qquad \Rightarrow \qquad \sinh(x) = \pm\sqrt{\cosh^2(x) - 1}$$

> 💡 Diese Umformungen werden bei der Herleitung der Areafunktions-Ableitungen gebraucht!

---

# 4. Additionstheoreme

> Vorlesungsfolien, Seite 10

$$\boxed{\cosh(x + y) = \cosh(x)\cosh(y) + \sinh(x)\sinh(y)}$$

$$\boxed{\sinh(x + y) = \sinh(x)\cosh(y) + \cosh(x)\sinh(y)}$$

**Herleitung** (z.B. für $\cosh(x+y)$): Man multipliziert $\cosh(x)\cosh(y)$ und $\sinh(x)\sinh(y)$ aus und addiert:

$$\cosh(x)\cosh(y) + \sinh(x)\sinh(y) = \frac{1}{4}(2e^{x+y} + 2e^{-(x+y)}) = \frac{e^{x+y} + e^{-(x+y)}}{2} = \cosh(x+y)$$

## 4.1 Vergleich mit trigonometrischen Additionstheoremen

| Trigonometrisch | Hyperbolisch |
|---|---|
| $\cos(x+y) = \cos x \cos y \, {\color{red}-} \, \sin x \sin y$ | $\cosh(x+y) = \cosh x \cosh y \, {\color{red}+} \, \sinh x \sinh y$ |
| $\sin(x+y) = \sin x \cos y + \cos x \sin y$ | $\sinh(x+y) = \sinh x \cosh y + \cosh x \sinh y$ |

> 💡 **Merkregel:** Bei $\cosh$ wechselt das Vorzeichen (Minus → Plus), bei $\sinh$ bleibt es gleich!

---

# 5. Ableitungen der Hyperbelfunktionen

> Vorlesungsfolien, Seite 11

$$\boxed{(\cosh(x))' = \sinh(x)}$$

$$\boxed{(\sinh(x))' = \cosh(x)}$$

$$\boxed{(\tanh(x))' = \frac{1}{\cosh^2(x)} = 1 - \tanh^2(x)}$$

### Herleitung

$$(\cosh(x))' = \left[\frac{e^x + e^{-x}}{2}\right]' = \frac{e^x - e^{-x}}{2} = \sinh(x) \quad \checkmark$$

$$(\sinh(x))' = \left[\frac{e^x - e^{-x}}{2}\right]' = \frac{e^x + e^{-x}}{2} = \cosh(x) \quad \checkmark$$

$$(\tanh(x))' = \left[\frac{\sinh(x)}{\cosh(x)}\right]' = \frac{\cosh^2(x) - \sinh^2(x)}{\cosh^2(x)} = \frac{1}{\cosh^2(x)} \quad \checkmark$$

## 5.1 Vergleich mit trigonometrischen Ableitungen

| Funktion | Ableitung | Hyperbolische Funktion | Ableitung |
|---|---|---|---|
| $\cos(x)$ | ${\color{red}-}\sin(x)$ | $\cosh(x)$ | $\sinh(x)$ |
| $\sin(x)$ | $\cos(x)$ | $\sinh(x)$ | $\cosh(x)$ |
| $\tan(x)$ | $\frac{1}{\cos^2(x)} = 1 + \tan^2(x)$ | $\tanh(x)$ | $\frac{1}{\cosh^2(x)} = 1 - \tanh^2(x)$ |

> 💡 **Merkregel:** Kein Vorzeichenwechsel bei der Ableitung! $(\cosh)' = +\sinh$ (nicht $-\sinh$ wie bei $(\cos)' = -\sin$).

---

# 6. Reihenentwicklung (MacLaurin-Reihe)

> Vorlesungsfolien, Seite 12 / Unterrichtsnotizen Seite 17–19

$$\boxed{\cosh(x) = 1 + \frac{x^2}{2!} + \frac{x^4}{4!} + \frac{x^6}{6!} + \cdots = \sum_{k=0}^{\infty} \frac{x^{2k}}{(2k)!}}$$

$$\boxed{\sinh(x) = x + \frac{x^3}{3!} + \frac{x^5}{5!} + \frac{x^7}{7!} + \cdots = \sum_{k=0}^{\infty} \frac{x^{2k+1}}{(2k+1)!}}$$

## 6.1 Vergleich mit cos/sin

| | cos/sin | cosh/sinh |
|---|---|---|
| **Gerade Potenzen** | $\cos(x) = 1 {\color{red}-} \frac{x^2}{2!} {\color{red}+} \frac{x^4}{4!} {\color{red}-} \cdots$ | $\cosh(x) = 1 + \frac{x^2}{2!} + \frac{x^4}{4!} + \cdots$ |
| **Ungerade Potenzen** | $\sin(x) = x {\color{red}-} \frac{x^3}{3!} {\color{red}+} \frac{x^5}{5!} {\color{red}-} \cdots$ | $\sinh(x) = x + \frac{x^3}{3!} + \frac{x^5}{5!} + \cdots$ |
| **Vorzeichen** | **Alternierend** $(-1)^k$ | **Keine** alternierenden Vorzeichen |

> 💡 **Merkregel:** cosh/sinh = cos/sin Reihe, aber **ohne alternierende Vorzeichen** (alle Terme positiv).

### Herleitung über Taylor-Tabelle (cosh)

| $k$ | $f^{(k)}(x)$ | $f^{(k)}(0)$ | $\frac{1}{k!} f^{(k)}(0)$ |
|---|---|---|---|
| 0 | $\cosh(x)$ | $\cosh(0) = 1$ | $1$ |
| 1 | $\sinh(x)$ | $\sinh(0) = 0$ | $0$ |
| 2 | $\cosh(x)$ | $1$ | $1/2$ |
| 3 | $\sinh(x)$ | $0$ | $0$ |
| 4 | $\cosh(x)$ | $1$ | $1/24$ |

$\Rightarrow$ Nur gerade Potenzen $\neq 0$ (weil $\sinh(0) = 0$, $\cosh(0) = 1$).

---

# 7. Areafunktionen (Umkehrfunktionen)

> Vorlesungsfolien, Seiten 14–15 / Papula Band 1, S. 305–308

## 7.1 Definition und Herleitung von $\text{arsinh}(x)$

**Problem:** Gegeben $y = \sinh(x)$, finde $x = \sinh^{-1}(y)$.

$$y = \sinh(x) = \frac{e^x - e^{-x}}{2}$$

$$2y = e^x - e^{-x} \qquad | \cdot e^x$$

$$2y \cdot e^x = e^{2x} - 1$$

$$e^{2x} - 2y \cdot e^x - 1 = 0 \qquad \text{Substitution: } z = e^x$$

$$z^2 - 2yz - 1 = 0$$

$$z_{1/2} = y \pm \sqrt{y^2 + 1}$$

Da $z = e^x > 0$, gilt nur $z = y + \sqrt{y^2 + 1}$ (die positive Lösung).

$$x = \ln(y + \sqrt{y^2 + 1})$$

$$\boxed{\text{arsinh}(x) = \ln\left(x + \sqrt{x^2 + 1}\right) \qquad \text{für } x \in \mathbb{R}}$$

## 7.2 Alle drei Areafunktionen

| Areafunktion | Definition | Definitionsbereich | Wertebereich |
|---|---|---|---|
| $\text{arsinh}(x)$ | $\ln(x + \sqrt{x^2 + 1})$ | $\mathbb{R}$ | $\mathbb{R}$ |
| $\text{arcosh}(x)$ | $\ln(x + \sqrt{x^2 - 1})$ | $[1, \infty)$ | $[0, \infty)$ |
| $\text{artanh}(x)$ | $\frac{1}{2} \ln\left(\frac{1+x}{1-x}\right)$ | $(-1, 1)$ | $\mathbb{R}$ |

> ⚠️ **Achtung bei arcosh:** Nur der Zweig $x \geq 0$ von $\cosh$ wird invertiert (weil $\cosh$ für $x < 0$ fallend ist)!

## 7.3 Ableitungen der Areafunktionen

Über die **Umkehrfunktionsregel**: $(f^{-1}(x))' = \frac{1}{f'(f^{-1}(x))}$

### Herleitung für arsinh:

$$(\text{arsinh}(x))' = \frac{1}{\cosh(\text{arsinh}(x))}$$

Mit dem hyperbolischen Pythagoras: $\cosh(y) = \sqrt{1 + \sinh^2(y)}$, also $\cosh(\text{arsinh}(x)) = \sqrt{1 + x^2}$.

$$\boxed{(\text{arsinh}(x))' = \frac{1}{\sqrt{1 + x^2}}}$$

$$\boxed{(\text{arcosh}(x))' = \frac{1}{\sqrt{x^2 - 1}}}$$

$$\boxed{(\text{artanh}(x))' = \frac{1}{1 - x^2}}$$

## 7.4 Vergleich mit trigonometrischen Umkehrfunktionen

| Funktion | Ableitung | Areafunktion | Ableitung |
|---|---|---|---|
| $\arcsin(x)$ | $\frac{1}{\sqrt{1 - x^2}}$ | $\text{arsinh}(x)$ | $\frac{1}{\sqrt{1 + x^2}}$ |
| $\arccos(x)$ | $\frac{-1}{\sqrt{1 - x^2}}$ | $\text{arcosh}(x)$ | $\frac{1}{\sqrt{x^2 - 1}}$ |
| $\arctan(x)$ | $\frac{1}{1 + x^2}$ | $\text{artanh}(x)$ | $\frac{1}{1 - x^2}$ |

> 💡 **Merkregel Vorzeichen:** arcsin hat $1 {\color{red}-} x^2$, arsinh hat $1 {\color{red}+} x^2$. Das Plus/Minus-Muster zieht sich durch alles!

---

# 8. Die Kettenlinie (Catenary)

> Unterrichtsnotizen Seite 25

Eine Kette oder ein Kabel, das an zwei Punkten aufgehängt wird, bildet **keine Parabel**, sondern eine **Kosinushyperbolicus-Kurve** (Kettenlinie/Catenary).

## 8.1 Herleitung (DGL → cosh-Lösung)

**Physik:** Am Kabel wirken Horizontalkraft $H$ (konstant) und Gewichtskraft $V(x) = m_L \cdot l(x) \cdot g$.

$$y'(x) = \frac{V(x)}{H} = k \cdot l(x) \qquad \text{mit } k = \frac{m_L \cdot g}{H}$$

**Bogenlänge:** $l(x) = \int \sqrt{1 + (y'(t))^2} \, dt$

**Ableiten** ergibt die DGL:

$$y''(x) = k \cdot \sqrt{1 + (y'(x))^2}$$

**Substitution** $z = y'$:

$$\frac{z'}{\sqrt{1 + z^2}} = k \qquad \Rightarrow \qquad \int \frac{dz}{\sqrt{1 + z^2}} = \int k \, dx$$

$$\text{arsinh}(z) = kx + C$$

$$z = y' = \sinh(kx + C) \qquad \Rightarrow \qquad \boxed{y(x) = \frac{1}{k} \cosh(kx + C)}$$

```
           Aufhängung          Aufhängung
              *                    *
             / \                  / \
            /   \                /   \
           /     \              /     \
          /       \            /       \
         /    ←cosh(x)→       \       /
        /                      \_____/
       /                      tiefster Punkt
      
   Die Kettenlinie ist ein cosh – keine Parabel!
```

> 💡 **Prüfungsrelevant:** Die Kettenlinie zeigt, wie arsinh als Integral $\int \frac{dz}{\sqrt{1+z^2}}$ auftaucht und zu einer cosh-Lösung führt. Das verbindet Areafunktionen mit DGLen (SW06/SW07)!

---

# 9. Grosse Vergleichstabelle: Trigonometrisch vs. Hyperbolisch

| Eigenschaft | Trigonometrisch | Hyperbolisch |
|---|---|---|
| **Definition cos/cosh** | $\cos(x) = \frac{1}{2}(e^{ix} + e^{-ix})$ | $\cosh(x) = \frac{1}{2}(e^{x} + e^{-x})$ |
| **Definition sin/sinh** | $\sin(x) = \frac{1}{2i}(e^{ix} - e^{-ix})$ | $\sinh(x) = \frac{1}{2}(e^{x} - e^{-x})$ |
| **Pythagoras** | $\cos^2 + \sin^2 = 1$ | $\cosh^2 - \sinh^2 = 1$ |
| **Additionstheoreme** | $\cos(x\!+\!y) = \cos x\cos y - \sin x\sin y$ | $\cosh(x\!+\!y) = \cosh x\cosh y + \sinh x\sinh y$ |
| **Ableitung cos/cosh** | $(\cos x)' = -\sin x$ | $(\cosh x)' = +\sinh x$ |
| **Ableitung sin/sinh** | $(\sin x)' = \cos x$ | $(\sinh x)' = \cosh x$ |
| **Ableitung tan/tanh** | $(\tan x)' = 1 + \tan^2 x$ | $(\tanh x)' = 1 - \tanh^2 x$ |
| **Reihe cos/cosh** | Alternierende Vorzeichen | Nur positive Vorzeichen |
| **Geometrie** | Einheitskreis $x^2 + y^2 = 1$ | Einheitshyperbel $x^2 - y^2 = 1$ |
| **Periodizität** | Periodisch ($2\pi$) | **Nicht** periodisch |
| **Umkehrableitung** | $(\arcsin x)' = \frac{1}{\sqrt{1-x^2}}$ | $(\text{arsinh}\, x)' = \frac{1}{\sqrt{1+x^2}}$ |

> 💡 **Der rote Faden:** Überall taucht derselbe Vorzeichenunterschied auf: $+$ vs. $-$. Wer das Muster kennt, kann sich alles herleiten!

---

# 10. Empfohlene Übungsaufgaben

> Papula Band 1, Kapitel III, Abschnitt 13, Seite 322

| Aufgabe | Thema | Beschreibung |
|---|---|---|
| **11)** | Funktionswerte und Identitäten | Hyperbelfunktionen auswerten, Identitäten nachweisen |
| **12)** | Ableitungen | Ableitungen von zusammengesetzten Hyperbelfunktionen berechnen |
| **13)** | Areafunktionen | Umkehrfunktionen anwenden, Logarithmus-Darstellung nutzen |

---

# 11. Lösungen der empfohlenen Aufgaben

> Papula Band 1, Seite 763

### Aufgabe 11 – Funktionswerte und Identitäten

**a) Berechne $\cosh(1)$ und $\sinh(1)$:**

$$\cosh(1) = \frac{e^1 + e^{-1}}{2} = \frac{2.7183 + 0.3679}{2} \approx 1.5431$$

$$\sinh(1) = \frac{e^1 - e^{-1}}{2} = \frac{2.7183 - 0.3679}{2} \approx 1.1752$$

**Probe mit hyperbolischem Pythagoras:**

$$\cosh^2(1) - \sinh^2(1) = 1.5431^2 - 1.1752^2 = 2.3812 - 1.3811 \approx 1.0 \quad \checkmark$$

**b) Zeige, dass $\cosh(x) + \sinh(x) = e^x$:**

$$\cosh(x) + \sinh(x) = \frac{e^x + e^{-x}}{2} + \frac{e^x - e^{-x}}{2} = \frac{2e^x}{2} = e^x \quad \checkmark$$

**c) Zeige, dass $\cosh(x) - \sinh(x) = e^{-x}$:**

$$\cosh(x) - \sinh(x) = \frac{e^x + e^{-x}}{2} - \frac{e^x - e^{-x}}{2} = \frac{2e^{-x}}{2} = e^{-x} \quad \checkmark$$

> 💡 **Nützliche Identitäten:** $\cosh + \sinh = e^x$ und $\cosh - \sinh = e^{-x}$ sind oft hilfreiche Abkürzungen!

### Aufgabe 12 – Ableitungen

**a) $f(x) = \cosh(3x)$:**

$$f'(x) = \sinh(3x) \cdot 3 = 3\sinh(3x) \qquad \text{(Kettenregel!)}$$

**b) $f(x) = \sinh^2(x)$:**

$$f'(x) = 2\sinh(x) \cdot \cosh(x) \qquad \text{(Kettenregel: äussere Ableitung } \cdot \text{ innere)}$$

**c) $f(x) = x \cdot \cosh(x)$:**

$$f'(x) = \cosh(x) + x \cdot \sinh(x) \qquad \text{(Produktregel!)}$$

**d) $f(x) = \tanh(x^2)$:**

$$f'(x) = \frac{1}{\cosh^2(x^2)} \cdot 2x = \frac{2x}{\cosh^2(x^2)} \qquad \text{(Kettenregel)}$$

### Aufgabe 13 – Areafunktionen

**a) Berechne $\text{arsinh}(2)$:**

$$\text{arsinh}(2) = \ln(2 + \sqrt{4 + 1}) = \ln(2 + \sqrt{5}) = \ln(4.2361) \approx 1.4436$$

**Probe:** $\sinh(1.4436) = \frac{e^{1.4436} - e^{-1.4436}}{2} = \frac{4.2361 - 0.2361}{2} \approx 2.0 \quad \checkmark$

**b) Berechne $\text{arcosh}(3)$:**

$$\text{arcosh}(3) = \ln(3 + \sqrt{9 - 1}) = \ln(3 + \sqrt{8}) = \ln(3 + 2\sqrt{2}) \approx 1.7627$$

---

# 12. Prüfungsrelevante Hinweise (MEP)

## Was ist sicher relevant?

| Thema | Warum relevant? | Wie vorbereiten? |
|---|---|---|
| **Definitionen cosh/sinh/tanh** | Grundlage für alles | Aus $e^x$-Formel ableiten können |
| **Hyperbolischer Pythagoras** | Wird bei Areafunktions-Ableitungen gebraucht | Herleitung verstehen, Formel kennen |
| **Ableitungen** aller Hyperbelfunktionen | Standardaufgabe | Tabelle auswendig oder herleiten |
| **Areafunktionen** (Definition + Ableitung) | Umkehrfunktionen berechnen | Logarithmus-Formeln kennen |
| **Vergleich trig. ↔ hyp.** | Vorzeichen-Unterschiede | Grosse Vergleichstabelle lernen |
| **Kettenlinie** | Verbindung zu DGL | Wissen, dass $y = \frac{1}{k}\cosh(kx+C)$ |

## Typische Aufgabentypen

1. **"Leiten Sie ab..."** – $f(x) = \cosh(3x^2)$, $g(x) = x\sinh(x)$, etc. → Ketten-/Produktregel + Hyperbol.-Ableitungen
2. **"Zeigen Sie, dass..."** – Identitäten beweisen (z.B. hyperb. Pythagoras, Additionstheoreme)
3. **"Berechnen Sie den Wert..."** – $\text{arsinh}(x)$ in Logarithmusform auswerten
4. **"Bestimmen Sie die Umkehrfunktion..."** – Herleitung von arsinh/arcosh über quadratische Gleichung

## Häufige Fehlerquellen

> ⚠️ **Fehler 1: Vorzeichenverwechslung Pythagoras**
> $\cos^2 + \sin^2 = 1$ vs. $\cosh^2 {\color{red}-} \sinh^2 = 1$ – das Minus wird gerne vergessen!

> ⚠️ **Fehler 2: Ableitung von cosh mit Minus**
> $(\cos x)' = {\color{red}-}\sin x$, aber $(\cosh x)' = {\color{green}+}\sinh x$ – kein Vorzeichenwechsel!

> ⚠️ **Fehler 3: Kettenregel vergessen**
> Bei $\cosh(3x)$ ist die Ableitung $3\sinh(3x)$, nicht $\sinh(3x)$!

> ⚠️ **Fehler 4: arcosh-Definitionsbereich**
> $\text{arcosh}(x)$ ist nur für $x \geq 1$ definiert (weil $\cosh(x) \geq 1$).

> ⚠️ **Fehler 5: arsinh-Herleitung – falsche Lösung der quadratischen Gleichung**
> Bei $z = x \pm \sqrt{x^2+1}$ muss man die **positive** Lösung nehmen, weil $z = e^y > 0$.

### Tricks und Merkregeln

- **"Ohne $i$ = hyperbolisch":** Die Definitionen von cosh/sinh sind wie cos/sin, nur ohne $i$ im Exponenten
- **"Minus statt Plus":** Überall wo bei trig. ein $+$ steht, steht bei hyperb. ein $-$ (oder umgekehrt)
- **"Keine alternierenden Vorzeichen":** In der Reihe von cosh/sinh gibt es nur $+$
- **"cosh ist immer $\geq 1$":** Weil $e^x + e^{-x} \geq 2$ (AM-GM Ungleichung)
- **"Kettenlinie = cosh":** Ein hängendes Seil beschreibt $y = a \cdot \cosh(x/a)$

---

# 13. Maxima & Python – Elektronische Hilfsmittel (MEP Teil 2)

## 13.1 wxMaxima – Hyperbelfunktionen

```maxima
/* Hyperbolische Funktionen auswerten */
cosh(1), numer;
    /* → 1.543080634815244 */

sinh(1), numer;
    /* → 1.175201193643801 */

/* Hyperbolischer Pythagoras prüfen */
cosh(x)^2 - sinh(x)^2;
trigsimp(%);
    /* → 1 */

/* Ableitungen */
diff(cosh(x), x);
    /* → sinh(x) */

diff(sinh(x), x);
    /* → cosh(x) */

diff(tanh(x), x);
    /* → 1/cosh(x)^2  bzw.  sech(x)^2 */

/* Areafunktionen */
asinh(2.0);
    /* → 1.4436... */

acosh(3.0);
    /* → 1.7627... */

/* Reihenentwicklung */
taylor(cosh(x), x, 0, 8);
    /* → 1 + x^2/2 + x^4/24 + x^6/720 + x^8/40320 */

taylor(sinh(x), x, 0, 7);
    /* → x + x^3/6 + x^5/120 + x^7/5040 */

/* Identitäten nachweisen */
ratsimp(cosh(x) + sinh(x) - exp(x));
    /* → 0 */

/* Plotten */
plot2d([cosh(x), sinh(x), tanh(x)], [x, -3, 3],
       [legend, "cosh", "sinh", "tanh"],
       [y, -4, 4]);
```

## 13.2 Python – Hyperbelfunktionen plotten und rechnen

### Grundlegende Berechnungen

```python
import numpy as np

# Funktionswerte
print(f"cosh(1) = {np.cosh(1):.4f}")    # → 1.5431
print(f"sinh(1) = {np.sinh(1):.4f}")    # → 1.1752
print(f"tanh(1) = {np.tanh(1):.4f}")    # → 0.7616

# Hyperbolischer Pythagoras prüfen
x = 2.5
print(f"cosh²({x}) - sinh²({x}) = {np.cosh(x)**2 - np.sinh(x)**2:.10f}")
# → 1.0000000000

# Areafunktionen
print(f"arsinh(2) = {np.arcsinh(2):.4f}")   # → 1.4436
print(f"arcosh(3) = {np.arccosh(3):.4f}")   # → 1.7627
print(f"artanh(0.5) = {np.arctanh(0.5):.4f}")  # → 0.5493

# Vergleich mit Logarithmus-Formel
x = 2
arsinh_log = np.log(x + np.sqrt(x**2 + 1))
print(f"arsinh(2) via ln: {arsinh_log:.4f}")  # → 1.4436 ✓
```

### Graphen: cosh, sinh, tanh vergleichen

```python
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-3, 3, 500)

fig, axes = plt.subplots(1, 3, figsize=(15, 5))

# cosh
axes[0].plot(x, np.cosh(x), 'b-', linewidth=2, label='cosh(x)')
axes[0].plot(x, np.cos(x), 'b--', alpha=0.5, label='cos(x)')
axes[0].axhline(y=1, color='gray', linestyle=':', alpha=0.5)
axes[0].set_title('cosh vs cos')
axes[0].legend(); axes[0].grid(True); axes[0].set_ylim(-2, 5)

# sinh
axes[1].plot(x, np.sinh(x), 'r-', linewidth=2, label='sinh(x)')
axes[1].plot(x, np.sin(x), 'r--', alpha=0.5, label='sin(x)')
axes[1].set_title('sinh vs sin')
axes[1].legend(); axes[1].grid(True); axes[1].set_ylim(-5, 5)

# tanh
axes[2].plot(x, np.tanh(x), 'g-', linewidth=2, label='tanh(x)')
axes[2].plot(x, np.tan(x), 'g--', alpha=0.5, label='tan(x)')
axes[2].axhline(y=1, color='gray', linestyle=':', alpha=0.5)
axes[2].axhline(y=-1, color='gray', linestyle=':', alpha=0.5)
axes[2].set_title('tanh vs tan')
axes[2].legend(); axes[2].grid(True); axes[2].set_ylim(-2, 2)

plt.tight_layout()
plt.savefig('hyperbel_vergleich.png', dpi=150)
plt.show()
```

### Einheitskreis vs. Einheitshyperbel (parametrisch)

```python
import numpy as np
import matplotlib.pyplot as plt

t = np.linspace(0, 2*np.pi, 500)
t_hyp = np.linspace(-1.8, 1.8, 500)

fig, ax = plt.subplots(1, 1, figsize=(8, 8))

# Einheitskreis: (cos(t), sin(t))
ax.plot(np.cos(t), np.sin(t), 'b-', linewidth=2, label='Kreis: (cos t, sin t)')

# Einheitshyperbel: (cosh(t), sinh(t))
ax.plot(np.cosh(t_hyp), np.sinh(t_hyp), 'r-', linewidth=2, label='Hyperbel: (cosh t, sinh t)')

# Asymptoten y = ±x
ax.plot([0, 4], [0, 4], 'gray', linestyle='--', alpha=0.5, label='Asymptote y = x')
ax.plot([0, 4], [0, -4], 'gray', linestyle='--', alpha=0.5, label='Asymptote y = -x')

ax.set_xlim(-3, 4); ax.set_ylim(-3, 3)
ax.set_aspect('equal')
ax.grid(True); ax.legend()
ax.set_title('Einheitskreis vs. Einheitshyperbel')
plt.savefig('kreis_vs_hyperbel.png', dpi=150)
plt.show()
```

### Kettenlinie plotten

```python
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-3, 3, 500)

fig, ax = plt.subplots(figsize=(10, 6))

# Kettenlinie für verschiedene k-Werte
for k in [0.5, 1.0, 2.0]:
    y = (1/k) * np.cosh(k * x)
    ax.plot(x, y, linewidth=2, label=f'y = (1/{k}) · cosh({k}x)')

# Vergleich mit Parabel
ax.plot(x, 1 + x**2/2, 'k--', alpha=0.5, label='Parabel: 1 + x²/2')

ax.set_xlabel('x'); ax.set_ylabel('y')
ax.set_title('Kettenlinie (cosh) vs. Parabel')
ax.legend(); ax.grid(True)
ax.set_ylim(0, 8)
plt.savefig('kettenlinie.png', dpi=150)
plt.show()
```

### Symbolisch mit SymPy

```python
from sympy import *

x = symbols('x')

# Ableitungen
print("(cosh(x))' =", diff(cosh(x), x))         # → sinh(x)
print("(sinh(x))' =", diff(sinh(x), x))         # → cosh(x)
print("(tanh(x))' =", simplify(diff(tanh(x), x)))  # → 1/cosh(x)^2

# Hyperbolischer Pythagoras
print("cosh²-sinh² =", simplify(cosh(x)**2 - sinh(x)**2))  # → 1

# Reihenentwicklung
print("cosh Taylor:", series(cosh(x), x, 0, 9))
# → 1 + x**2/2 + x**4/24 + x**6/720 + x**8/40320 + O(x**9)

print("sinh Taylor:", series(sinh(x), x, 0, 9))
# → x + x**3/6 + x**5/120 + x**7/5040 + O(x**9)

# Integrale mit Areafunktionen
print("∫ 1/√(1+x²) dx =", integrate(1/sqrt(1+x**2), x))  # → asinh(x)
print("∫ 1/√(x²-1) dx =", integrate(1/sqrt(x**2-1), x))  # → acosh(x)
```

## 13.3 Kurzreferenz: Maxima-Befehle für Hyperbelfunktionen

| Aufgabe | Maxima | Python (NumPy) |
|---|---|---|
| $\cosh(x)$ | `cosh(x)` | `np.cosh(x)` |
| $\sinh(x)$ | `sinh(x)` | `np.sinh(x)` |
| $\tanh(x)$ | `tanh(x)` | `np.tanh(x)` |
| $\text{arsinh}(x)$ | `asinh(x)` | `np.arcsinh(x)` |
| $\text{arcosh}(x)$ | `acosh(x)` | `np.arccosh(x)` |
| $\text{artanh}(x)$ | `atanh(x)` | `np.arctanh(x)` |
| Ableitung | `diff(cosh(x), x);` | `from sympy import *; diff(cosh(x), x)` |
| Reihe | `taylor(cosh(x), x, 0, 8);` | `series(cosh(x), x, 0, 9)` |
| Vereinfachen | `trigsimp(expr);` | `simplify(expr)` |

---

# 14. Verbindung zu anderen Wochen

| Woche | Thema | Verbindung zu SW09 |
|---|---|---|
| **SW01** | Trigonometrie | cosh/sinh sind die "hyperbolischen Geschwister" von cos/sin. Der hyperbolische Pythagoras $\cosh^2 - \sinh^2 = 1$ ist das Gegenstück zu $\cos^2 + \sin^2 = 1$. Die Additionstheoreme folgen derselben Logik. |
| **SW02** | Folgen, Reihen, Grenzwerte | Die MacLaurin-Reihen von cosh/sinh sind Spezialfälle der Potenzreihen aus SW02. |
| **SW03** | Potenzreihen | Taylor-Entwicklung von cosh/sinh wird mit den Methoden aus SW03 hergeleitet. |
| **SW04** | Komplexe Zahlen | Die Euler-Formel $e^{ix} = \cos x + i\sin x$ ist der Ausgangspunkt: Hyperbelfunktionen = "Euler ohne $i$". |
| **SW05** | Newton im Komplexen, Fourier | cosh/sinh tauchen als Realteil/Imaginärteil von $\cos(iz)$ und $\sin(iz)$ auf. |
| **SW06/07** | Differentialgleichungen | Die Kettenlinie führt auf eine DGL, die über arsinh-Integration gelöst wird → $y = \frac{1}{k}\cosh(kx + C)$. Die DGL-Lösungsmethoden (Separation der Variablen) werden direkt angewendet. |
| *(Ausblick SW10)* | **Kurven** | Die Parametrisierung der Einheitshyperbel $\vec{c}(t) = (\cosh t, \sinh t)$ ist eine **Kurve** – genau das Thema der nächsten Woche! Der hyperbolische Pythagoras wird dort genutzt, um zu zeigen, dass $x^2 - y^2 = 1$ tatsächlich eine Hyperbel ist. Die Kettenlinie $y = \cosh(x)$ lässt sich als Funktionsgraph-Kurve $\vec{c}(x) = (x, \cosh x)$ betrachten – ihre Bogenlänge berechnet man mit den Methoden aus SW10! |
