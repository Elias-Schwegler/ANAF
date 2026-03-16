# Zusammenfassung Woche 05: Newton-Verfahren im Komplexen, Fourier-Analyse

**Modul:** Fortgeschrittene Analysis (ANA-F)
**Dozenten:** Ron Porath und Joachim Wirth
**Quellen:**
- Folien: ana-f-sw-05-folien.pdf
- Lehrbuch: Papula, Band 2, Kapitel II, Abschnitt 1 (Mathematik für Ingenieure und Naturwissenschaftler)

## Lernziele
- Das Newton-Verfahren beherrschen und im **Komplexen** anwenden können.
- Eine periodische Funktion in eine **Fourier-Reihe** entwickeln können (reelle und komplexe Form).

---

## 1. Newton-Verfahren im Komplexen
*Quelle: Folien 1–2, Vorlesungsnotizen*

### Formeln & Definitionen

**Iterationsformel (identisch zum Reellen, nun mit $z \in \mathbb{C}$)**
$$ z_{n+1} = z_n - \frac{f(z_n)}{f'(z_n)} $$

Das Verfahren konvergiert gegen diejenige Nullstelle, in deren **Einzugsgebiet** (Basin of Attraction) der Startwert $z_0$ liegt. Im Komplexen entstehen dabei fraktale Gebietsgrenzen.

**Wichtige Punkte:**
- Jede Gleichung $z^n = a$ besitzt genau $n$ Lösungen in $\mathbb{C}$, die ein regelmässiges $n$-Eck bilden.
- Der Startwert $z_0$ bestimmt, zu welcher der $n$ Nullstellen das Verfahren konvergiert.
- Die Abbruchbedingung bleibt $|f(z_n)| < \varepsilon$ oder $|z_{n+1} - z_n| < \varepsilon$.

### Vorlesungsnotizen

Die folgende Skizze aus der Vorlesung zeigt die Lage der vier Lösungen von $z^4 - 1 = 0$ in der komplexen Ebene. Die Nullstellen bilden ein Quadrat ($z = 1, -1, j, -j$). Bei $z^6 - 1 = 0$ wäre es ein regelmässiges Sechseck.

![Nullstellen von z^4 - 1 = 0 in der komplexen Ebene – die vier Lösungen bilden ein Quadrat](wenn%20es%20z%20hoch%20sechs%20wäre%20dann%20wäre%20es%20ein%20sechseck.png)

Die folgende Notiz zeigt ein Beispiel zum Newton-Verfahren mit komplexem Startwert für $f(x) = x^2 + 5$. Solche Aufgaben müssen an der MEP nicht in diesem Aufwandsgrad von Hand gerechnet werden.

![Newton-Verfahren mit komplexem Startwert – Beispiel f(x) = x^2 + 5](muss%20an%20der%20Mep%20so%20nicht%20in%20diesem%20aufwandsgran%20von%20hand%20gerechnet%20werden..png)

### Aufgabentypen
- **Nullstellen im Komplexen finden:** Gleichungen $z^n = a$ mit dem Newton-Verfahren lösen, ausgehend von verschiedenen komplexen Startwerten.
- **Konvergenzverhalten analysieren:** Für verschiedene Startwerte bestimmen, zu welcher Nullstelle das Verfahren konvergiert.

---

## 2. Reelle Fourier-Reihe
*Quelle: Papula Band 2, Kapitel II, Abschnitt 1.1–1.2 (S. 163–173)*

### Formeln & Definitionen

**Periodische Funktion**
Eine Funktion $f(x)$ heisst **periodisch** mit der Periode $p$, wenn gilt:
$$ f(x + p) = f(x) \quad \text{für alle } x $$

**Fourier-Reihe einer periodischen Funktion mit Periode $p = 2\pi$**
$$ f(x) = \frac{a_0}{2} + \sum_{n=1}^{\infty} \left( a_n \cos(nx) + b_n \sin(nx) \right) $$

**Euler-Fourier-Formeln** (Berechnung der Koeffizienten durch Integration über eine volle Periode):

| Koeffizient | Formel | Beschreibung |
| :--- | :--- | :--- |
| $a_0$ | $a_0 = \dfrac{1}{\pi} \displaystyle\int_{0}^{2\pi} f(x) \, dx$ | Doppelter Mittelwert (Gleichanteil) |
| $a_n$ | $a_n = \dfrac{1}{\pi} \displaystyle\int_{0}^{2\pi} f(x) \cos(nx) \, dx$ | Kosinus-Koeffizienten ($n \geq 1$) |
| $b_n$ | $b_n = \dfrac{1}{\pi} \displaystyle\int_{0}^{2\pi} f(x) \sin(nx) \, dx$ | Sinus-Koeffizienten ($n \geq 1$) |

> **Hinweis:** Als Integrationsintervall kann jedes Intervall der Länge $2\pi$ gewählt werden, z.B. $[0, 2\pi]$ oder $[-\pi, \pi]$.

**Dirichlet-Bedingungen** (hinreichend für Konvergenz):
Die Funktion muss im Periodenintervall:
1. absolut integrierbar sein,
2. stetig sein oder nur endlich viele Sprungstellen besitzen,
3. nur endlich viele Extrema besitzen.

An **Sprungstellen** konvergiert die Fourier-Reihe gegen den arithmetischen Mittelwert der links- und rechtsseitigen Grenzwerte.

**Orthogonalitätsrelationen** (Schlüssel zur Herleitung der Koeffizienten):

| Integral | Ergebnis | Bedingung |
| :--- | :--- | :--- |
| $\int_{-\pi}^{\pi} \cos(nx)\cos(mx)\,dx$ | $\pi \cdot \delta_{nm}$ | $= \pi$ für $n=m$, sonst $0$ |
| $\int_{-\pi}^{\pi} \sin(nx)\sin(mx)\,dx$ | $\pi \cdot \delta_{nm}$ | $= \pi$ für $n=m$, sonst $0$ |
| $\int_{-\pi}^{\pi} \cos(nx)\sin(mx)\,dx$ | $0$ | für alle $n, m$ |

### Symmetrieeigenschaften (Vereinfachung!)

| Symmetrie | Eigenschaft | Konsequenz für Fourier-Reihe |
| :--- | :--- | :--- |
| **Gerade Funktion** $f(-x) = f(x)$ | Spiegelsymmetrie an der $y$-Achse | Nur **Kosinus-Glieder**: $b_n = 0$ für alle $n$ |
| **Ungerade Funktion** $f(-x) = -f(x)$ | Punktsymmetrie zum Ursprung | Nur **Sinus-Glieder**: $a_0 = 0$ und $a_n = 0$ für alle $n$ |

> **Prüfungstipp:** Vor dem Rechnen immer die Symmetrie der Funktion prüfen! Damit halbiert sich der Rechenaufwand.

### Beispiel: Rechteckkurve (Papula S. 171–173)

Gegeben:
$$ f(x) = \begin{cases} 1, & 0 \leq x \leq \pi \\ -1, & \pi < x < 2\pi \end{cases} \quad (p = 2\pi) $$

$f(x)$ ist **ungerade** $\Rightarrow$ $a_0 = 0$, $a_n = 0$ (nur Sinus-Glieder).

Berechnung von $b_n$:
$$ b_n = \frac{2}{n\pi} [1 - \cos(n\pi)] $$

Fallunterscheidung mit $\cos(n\pi) = (-1)^n$:
- $n$ **gerade**: $b_{2k} = 0$ (Koeffizienten verschwinden)
- $n$ **ungerade**: $b_{2k-1} = \dfrac{4}{(2k-1)\pi}$

**Ergebnis:**
$$ f(x) = \frac{4}{\pi} \left( \sin x + \frac{1}{3} \sin(3x) + \frac{1}{5} \sin(5x) + \ldots \right) = \frac{4}{\pi} \sum_{k=1}^{\infty} \frac{\sin((2k-1)x)}{2k-1} $$

### Aufgabentypen
- **Fourier-Reihe berechnen:** Koeffizienten $a_0$, $a_n$, $b_n$ über die Integralformeln bestimmen und die Reihe aufschreiben.
- **Symmetrie ausnutzen:** Erkennen, ob nur Sinus- oder nur Kosinus-Glieder auftreten.
- **Näherungsfunktionen bilden:** Die ersten $N$ Glieder der Reihe als Approximation verwenden.

---

## 3. Komplexe Fourier-Reihe
*Quelle: Papula Band 2, Kapitel II, Abschnitt 1.3–1.4 (S. 174–181)*

### Formeln & Definitionen

**Euler-Substitution** (Umschreibung der trigonometrischen Funktionen):
$$ \cos(nx) = \frac{1}{2}\left(e^{jnx} + e^{-jnx}\right) $$
$$ \sin(nx) = \frac{1}{2j}\left(e^{jnx} - e^{-jnx}\right) = -\frac{j}{2}\left(e^{jnx} - e^{-jnx}\right) $$

**Komplexe Fourier-Reihe:**
$$ f(x) = \sum_{n=-\infty}^{\infty} c_n \cdot e^{jnx} $$

**Komplexe Fourier-Koeffizienten** (Integralformel):
$$ c_n = \frac{1}{2\pi} \int_{0}^{2\pi} f(x) \cdot e^{-jnx} \, dx \qquad (n = 0, \pm 1, \pm 2, \ldots) $$

> **Vorteil der komplexen Form:** Die Berechnung ist oft einfacher, da keine trigonometrischen Funktionen im Integranden auftreten – nur die Exponentialfunktion.

### Zusammenhang zwischen reellen und komplexen Koeffizienten

**Von reell nach komplex** ($n \in \mathbb{N}^*$):

| Koeffizient | Umrechnungsformel |
| :--- | :--- |
| $c_0$ | $c_0 = \dfrac{a_0}{2}$ |
| $c_n$ | $c_n = \dfrac{1}{2}(a_n - jb_n)$ |
| $c_{-n}$ | $c_{-n} = c_n^* = \dfrac{1}{2}(a_n + jb_n)$ |

> **Merke:** $c_{-n}$ und $c_n$ sind zueinander **konjugiert komplex**.

**Von komplex nach reell** ($n \in \mathbb{N}^*$):

| Koeffizient | Umrechnungsformel |
| :--- | :--- |
| $a_0$ | $a_0 = 2c_0$ |
| $a_n$ | $a_n = c_n + c_{-n} = c_n + c_n^*$ |
| $b_n$ | $b_n = j(c_n - c_{-n}) = j(c_n - c_n^*)$ |

### Beispiel: Rechteckkurve in komplexer Darstellung (Papula S. 179–181)

Gleiche Funktion wie oben. Aus den reellen Koeffizienten ($a_n = 0$, $b_n = \frac{4}{\pi n}$ für ungerades $n$) folgt:

**1. Lösungsweg (über Umrechnung):**
- $c_0 = 0$ (da $a_0 = 0$)
- $c_n = 0$ für $n$ gerade
- $c_{2k-1} = \frac{1}{2}(0 - j \cdot \frac{4}{\pi(2k-1)}) = -\frac{2j}{\pi} \cdot \frac{1}{2k-1}$ für $n$ ungerade

**2. Lösungsweg (direkt über Integralformel):**

$c_n = \frac{1}{2\pi} \int_0^{2\pi} f(x) \cdot e^{-jnx}\,dx = \frac{1}{2\pi}\left\{\int_0^{\pi} e^{-jnx}\,dx - \int_{\pi}^{2\pi} e^{-jnx}\,dx\right\}$

Nach Auswertung (mit $e^{-jn\pi} = \cos(n\pi) = (-1)^n$ und $e^{-jn2\pi} = 1$):
- $c_{2k} = 0$ (gerades $n$)
- $c_{2k-1} = -\frac{2j}{\pi(2k-1)}$ (ungerades $n$)

Beide Lösungswege führen zum gleichen Ergebnis. ✓

### Aufgabentypen
- **Komplexe Fourier-Koeffizienten berechnen:** Entweder direkt über die Integralformel oder über Umrechnung aus den reellen Koeffizienten.
- **Zwischen reeller und komplexer Form umrechnen:** Umrechnungsformeln sicher anwenden können.

---

## 4. Empfohlene Übungsaufgaben
*(Aus Papula Band 2, Kapitel II, Abschnitt 1, S. 190–191)*

| Nr. | Thema | Kurzbeschreibung | Seite |
| :--- | :--- | :--- | :--- |
| **1)** | Parabelförmiger Impuls | $f(x) = x(2\pi - x) = 2\pi x - x^2$, $0 \leq x \leq 2\pi$. Fourier-Reihe der Parabelbögen-Funktion berechnen. | S. 190 |
| **2)** | Sägezahnfunktion | $f(x) = x$, $0 \leq x < 2\pi$ (Bild II-14). Fourier-Reihe der linearen Sägezahnfunktion bestimmen. | S. 191 |
| **3)** | Betragsfunktion | $f(x) = |x|$, $-\pi \leq x \leq \pi$ (Bild II-15). Fourier-Reihe einer geraden Funktion bestimmen. | S. 191 |
| **4)** | Exponentialfunktion (komplex) | $f(x) = e^x$, $-\pi \leq x \leq \pi$. Fourier-Reihe in **komplexer** Darstellung berechnen und daraus die reelle Form ableiten. | S. 191 |

---

## 5. Lösungen der empfohlenen Aufgaben
*(Lösungswege aus Papula Band 2, S. 722–723)*

### Aufgabe 1) – Parabelförmiger Impuls
$f(x) = 2\pi x - x^2$, $\quad p = 2\pi$

**Koeffizient $a_0$:**
$$ a_0 = \frac{1}{\pi} \int_0^{2\pi} (2\pi x - x^2)\,dx = \frac{1}{\pi}\left[\pi x^2 - \frac{1}{3}x^3\right]_0^{2\pi} = \frac{4}{3}\pi^2 $$

**Koeffizient $a_n$:**
$$ a_n = \frac{1}{\pi} \int_0^{2\pi} (2\pi x - x^2)\cos(nx)\,dx = -\frac{4}{n^2} \quad (n \in \mathbb{N}^*) $$

**Koeffizient $b_n$:**
$b_n = 0$ – $f(x)$ ist eine **gerade** Funktion, daher treten keine Sinus-Glieder auf.

**Ergebnis:**
$$ f(x) = \frac{2}{3}\pi^2 - 4\left(\frac{1}{1^2}\cos x + \frac{1}{2^2}\cos(2x) + \frac{1}{3^2}\cos(3x) + \ldots\right) $$

---

### Aufgabe 2) – Sägezahnfunktion
$f(x) = x$, $\quad 0 \leq x < 2\pi$, $\quad p = 2\pi$

**Koeffizient $a_0$:**
$$ a_0 = \frac{1}{\pi}\int_0^{2\pi} x\,dx = \frac{1}{\pi}\left[\frac{1}{2}x^2\right]_0^{2\pi} = 2\pi $$

**Koeffizient $a_n$:**
$$ a_n = \frac{1}{\pi}\int_0^{2\pi} x\cos(nx)\,dx = 0 \quad (n \in \mathbb{N}^*) $$

**Koeffizient $b_n$:**
$$ b_n = \frac{1}{\pi}\int_0^{2\pi} x\sin(nx)\,dx = -\frac{2}{n} \quad (n \in \mathbb{N}^*) $$

**Ergebnis:**
$$ f(x) = \pi - 2\left(\frac{1}{1}\sin x + \frac{1}{2}\sin(2x) + \frac{1}{3}\sin(3x) + \ldots\right) $$

---

### Aufgabe 3) – Betragsfunktion
$f(x) = |x|$, $\quad -\pi \leq x \leq \pi$ (**gerade** Funktion, Integration von $0$ bis $\pi$, Faktor 2)

**Koeffizient $a_0$:**
$$ a_0 = \frac{1}{\pi}\int_{-\pi}^{\pi} |x|\,dx = \frac{2}{\pi}\int_0^{\pi} x\,dx = \pi $$

**Koeffizient $a_n$:**
$$ a_n = \frac{2}{\pi}\int_0^{\pi} x\cos(nx)\,dx = \frac{2[(-1)^n - 1]}{\pi n^2} = \begin{cases} -\dfrac{4}{\pi n^2}, & n = 1, 3, 5, \ldots \\ 0, & n = 2, 4, 6, \ldots \end{cases} $$

**Koeffizient $b_n$:**
$$ b_n = 0 \quad (\text{gerade Funktion, daher keine Sinus-Glieder}) $$

**Ergebnis:**
$$ f(x) = \frac{\pi}{2} - \frac{4}{\pi}\left(\frac{1}{1^2}\cos x + \frac{1}{3^2}\cos(3x) + \frac{1}{5^2}\cos(5x) + \ldots\right) $$

---

### Aufgabe 4) – Exponentialfunktion (komplexe Darstellung)
$f(x) = e^x$, $\quad -\pi \leq x \leq \pi$, $\quad p = 2\pi$

**Komplexe Koeffizienten $c_n$:**
$$ c_n = \frac{1}{2\pi}\int_{-\pi}^{\pi} e^x \cdot e^{-jnx}\,dx = \frac{1}{2\pi}\int_{-\pi}^{\pi} e^{(1-jn)x}\,dx $$

$$ = \frac{1}{2\pi} \cdot \frac{e^{(1-jn)\pi} - e^{-(1-jn)\pi}}{1 - jn} = (-1)^n \cdot \frac{e^{\pi} - e^{-\pi}}{2\pi} \cdot \frac{1 + jn}{1 + n^2} $$

*(mit $e^{\pm jn\pi} = \cos(n\pi) = (-1)^n$ und Erweiterung mit $(1+jn)$)*

**Komplexe Fourier-Reihe:**
$$ f(x) = \frac{e^{\pi} - e^{-\pi}}{2\pi} \cdot \sum_{n=-\infty}^{\infty} (-1)^n \cdot \frac{1 + jn}{1 + n^2} \cdot e^{jnx} $$

**Umrechnung in die reelle Form:**

$$ a_0 = 2c_0 = \frac{e^{\pi} - e^{-\pi}}{\pi} $$

$$ a_n = (-1)^n \cdot \frac{e^{\pi} - e^{-\pi}}{\pi} \cdot \frac{1}{1 + n^2} $$

$$ b_n = -(-1)^n \cdot \frac{e^{\pi} - e^{-\pi}}{\pi} \cdot \frac{n}{1 + n^2} $$

**Reelle Fourier-Reihe:**
$$ f(x) = \frac{e^{\pi} - e^{-\pi}}{2\pi} + \frac{e^{\pi} - e^{-\pi}}{\pi} \sum_{n=1}^{\infty} (-1)^n \left[\frac{\cos(nx)}{1+n^2} - \frac{n \cdot \sin(nx)}{1+n^2}\right] $$
