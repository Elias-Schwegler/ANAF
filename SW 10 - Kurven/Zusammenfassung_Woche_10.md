# Zusammenfassung Woche 10 – Kurven

**Modul:** Fortgeschrittene Analysis (ANA-F)
**Dozenten:** Ron Porath, Joachim Wirth
**Datum:** 20. April 2026
**Quelle:** Papula Band 3, Kapitel I.1 „Ebene und räumliche Kurven", Seiten 1–31
**Übungen:** Papula Band 3, Übungsaufgaben zu Abschnitt 1, **Aufgaben 1–11, Seiten 230–232**
**Lösungen:** Papula Band 3, Seiten 750–753
**Format:** „Do It Yourself" – Selbststudium aus dem Papula, plus Unterrichtsnotizen

---

## Lernziele (aus den Folien)

Zu **ebenen Kurven** und **Raumkurven** folgende Grössen berechnen können:

- **Tangenten-** und **Hauptnormalenvektor**
- **Bogenlänge**
- ~~Krümmung~~ (im Unterricht gestrichen – nicht Teil dieser Woche!)

### Themen
- Darstellung von Kurven
- Ableitung von Kurven: Tangenten-, Geschwindigkeits- und Beschleunigungsvektor
- Bogenlänge
- Hauptnormale

---

# 1. Definition einer Kurve

> Eine **Kurve ist eine Funktion des Ortes nach Zeit.**

Eine Kurve in der Ebene ist eine vektorwertige Funktion

$$\boxed{\vec{c}\,(t) = \begin{pmatrix} x(t) \\ y(t) \end{pmatrix}, \qquad \vec{c}:[a,b] \to \mathbb{R}^2, \quad t \mapsto \vec{c}\,(t)}$$

Der **Parameter** $t$ ist typischerweise die Zeit. Für jeden Zeitpunkt $t$ erhält man einen **Ortsvektor** zu einem Punkt der Kurve.

## 1.1 Drei Darstellungen desselben Kurvenpunktes

```
          y
          ↑
        3 +- - - * P(3|3)    ← Punktdarstellung
          |     /|
          |    / |
          |   /  |               Vektordarstellung: (3, 3)ᵀ
          |  /← Vektor           Komponentendarstellung: x(t)=3, y(t)=3
          | /|
          |/ |
        0 +--+------------→ x
          0  3
       Anfangspunkt
```

| Darstellung | Notation | Bemerkung |
|---|---|---|
| **Punktdarstellung** | $P(3 \mid 3)$ | Statische Sicht: Wo ist der Punkt? |
| **Vektordarstellung** | $\begin{pmatrix}3\\3\end{pmatrix}$ | Richtung + Länge vom Ursprung |
| **Parameterdarstellung** | $\vec{c}(t) = \begin{pmatrix}x(t)\\y(t)\end{pmatrix}$ | Dynamische Sicht: Kurve „entsteht" mit $t$ |

> 💡 **Vektor** = mathematisches Objekt mit **Richtung und Länge**.

## 1.2 Beispiel: Ein Lemniskaten-ähnlicher Pfad

$$\vec{c}\,(t) = \begin{pmatrix} t^2 - 1 \\ t - t^3 \end{pmatrix}, \qquad t \in \left[-\tfrac{5}{4}, \tfrac{5}{4}\right]$$

Dies ist Beispiel 1 „Alpha" aus dem Python-Notebook `kurven.ipynb`. Die Kurve hat die Form eines liegenden $\alpha$ (oder einer verdrehten Acht).

---

# 2. Standardbeispiele von Kurven

## 2.1 Kreis

> 🔗 **Rückbezug zu SW 01 (Trigonometrie):** Am Einheitskreis haben wir gelernt, dass jeder Punkt durch $(\cos t, \sin t)$ parametrisiert wird. Das ist **direkt** eine Kurve!
> 🔗 **Rückbezug zu SW 04 (Komplexe Zahlen):** $z(t) = r e^{it} = r(\cos t + i\sin t)$ beschreibt denselben Kreis in der komplexen Ebene. Die Kurve $\vec{c}(t) = (\text{Re}(z(t)), \text{Im}(z(t)))$ ist identisch zur Parametrisierung unten.

Ein Kreis mit Mittelpunkt $(5, 3)$ und Radius $r$:

$$\boxed{\vec{c}\,(t) = \begin{pmatrix} 5 + r\cos(t) \\ 3 + r\sin(t) \end{pmatrix}, \qquad t \in [0, 2\pi]}$$

```
         y
         ↑
      4 -+           ●---●
         |         ●      ●
      3 -+--------●        ●    ← Mittelpunkt (5, 3), r = 1
         |         ●      ●
      2 -+           ●---●      (r·cos(t), r·sin(t)) + Verschiebung
         |
      0 -+----+----+----+----+---→ x
              3    4    5    6
```

**Python (aus `kurven.ipynb`):**
```python
def Kreis(t):
    x = 5 + np.cos(t)
    y = 3 + np.sin(t)
    return np.array([x, y])

InteractCurve(Kreis, -4*np.pi, 4*np.pi)
```

## 2.2 Funktionsgraph als Kurve

Jede Funktion $y = f(x)$ kann als Kurve $\vec{c}(x) = \begin{pmatrix} x \\ f(x) \end{pmatrix}$ aufgefasst werden:

$$\vec{c}\,(x) = \begin{pmatrix} x \\ f(x) \end{pmatrix} \quad \text{(Parameter = } x\text{)}$$

```
         y
         ↑    f(x)
         |     \    /
      f(x)+- - -●  /     ← (x | f(x)) ist Kurvenpunkt
         |       \/
         |       /\
         |      /  \
         +-----+----+----→ x
               x
```

## 2.3 Anwendung: Schiefer Wurf (Ballistik)

> 🔗 **Rückbezug zu SW 06 (DGL I):** Der schiefe Wurf ist die **Lösung einer Differentialgleichung 2. Ordnung** $\ddot{\vec{r}} = \vec{g}$. Zweimalige Integration (mit Anfangsbedingungen) liefert die Wurfparabel – eine Kurve!
> 🔗 **Rückbezug zu SW 07 (DGL II):** Die **Phasenraumdarstellung** $(x(t), \dot{x}(t))$ eines harmonischen Oszillators ist genau das gleiche Konzept: eine Kurve in $\mathbb{R}^2$, parametrisiert durch die Zeit $t$.

Für einen Körper, der unter Winkel $\alpha$ mit Anfangsgeschwindigkeit $v_0$ geworfen wird:

Ausgangspunkt ist Newton:
$$a = \ddot{s} = -g \quad \Rightarrow \quad v = \dot{s} = -gt + v_0 \quad \Rightarrow \quad s = -\tfrac{1}{2}g t^2 + v_0 t + s_0$$

In Komponenten:

$$\boxed{\vec{r}(t) = \begin{pmatrix} v_0 \cos(\alpha) \cdot t + x_0 \\ v_0 \sin(\alpha) \cdot t - \tfrac{1}{2}g t^2 + y_0 \end{pmatrix}}$$

```
         y
         ↑                  ●
         |              ●       ●
         |           ●             ●
      y₀-+--- ↗                      ●   ← Bahn = Kurve r(t)
         |  v₀  ↑ y(t)
         |↗   |
         +---+----------+-----→ x
         x₀  x(t)
```

→ **Merke:** Eine Kurve entsteht oft aus einem physikalischen Vorgang (Bewegung). Position, Geschwindigkeit, Beschleunigung sind **Ableitungen** der Kurve.

---

# 3. Vektor-Werkzeuge (Wiederholung)

| Operation | Formel | Ergebnis |
|---|---|---|
| **Skalarprodukt** | $\vec{w} \cdot \vec{z} = \|\vec{w}\| \cdot \|\vec{z}\| \cdot \cos(\alpha)$ | Skalar |
| **Orthogonalitätstest** | $\vec{w} \cdot \vec{z} = 0$ | $\Leftrightarrow$ $\vec{w} \perp \vec{z}$ |
| **Vektorprodukt** (3D) | $\vec{w} \times \vec{z}$ | Vektor **senkrecht** auf beiden |
| **Betrag (Länge)** | $\|\vec{w}\| = \sqrt{w_x^2 + w_y^2}$ | Skalar |

Das Vektorprodukt in 3D:
$$\vec{w} \times \vec{z} = \begin{pmatrix} w_y z_z - w_z z_y \\ -(w_x z_z - w_z z_x) \\ w_x z_y - w_y z_x \end{pmatrix}$$

> 💡 Für die Bogenlänge brauchen wir nur **Betrag**. Für Orthogonalität (Tangente ⊥ Normale) brauchen wir das **Skalarprodukt**.

---

# 4. Ableitung von Kurven

## 4.1 Herleitung: Der Geschwindigkeitsvektor als Grenzwert

> 🔗 **Rückbezug zu SW 02 (Grenzwerte):** Die Definition der Ableitung als Grenzwert der Sekante ist **exakt dasselbe** wie in SW 02 für skalare Funktionen. Der einzige Unterschied: Jetzt ist der Grenzwert ein **Vektor** (komponentenweise!). Die ε-δ-Logik funktioniert komponentenweise.
> 🔗 **Rückbezug zu SW 03 (Potenzreihen):** Auch dort hat man "gliedweise" abgeleitet – hier leiten wir "komponentenweise" ab. Gleiches Prinzip auf unterschiedlicher Struktur.

Ähnlich wie bei einer skalaren Funktion bildet man den **Differenzenquotient** (die **Sekante**) zwischen zwei Kurvenpunkten:

```
            P(t+Δt) - P(t)
 Sekante =  ─────────────        (roter Pfeil → blauer Pfeil)
                 Δt

              P(t+Δt)
               ●
              ╱ ← Sekante (blau)
       P(t) ●
           ╱
     ċ(t)↗    (Grenzwert → Tangente, grün)
         ╱
     ───●─────────→ x
```

Im Grenzwert $\Delta t \to 0$:

$$\boxed{\dot{\vec{c}}(t) = \lim_{\Delta t \to 0} \frac{\vec{c}(t+\Delta t) - \vec{c}(t)}{\Delta t} = \frac{d\vec{c}(t)}{dt}}$$

→ Der **Geschwindigkeitsvektor** $\dot{\vec{c}}(t)$ ist die **erste Ableitung** der Kurve. Er zeigt immer **tangential** zur Kurve.

## 4.2 Praktisch: Komponentenweise ableiten

> 💡 **Goldene Regel:** Man leitet jede Komponente **separat** ab.

$$\vec{c}(t) = \begin{pmatrix} x(t) \\ y(t) \end{pmatrix} \quad \Longrightarrow \quad \dot{\vec{c}}(t) = \begin{pmatrix} \dot{x}(t) \\ \dot{y}(t) \end{pmatrix}, \quad \ddot{\vec{c}}(t) = \begin{pmatrix} \ddot{x}(t) \\ \ddot{y}(t) \end{pmatrix}$$

## 4.3 Beispiel (aus dem Unterricht)

Gegeben: $\vec{c}(t) = \begin{pmatrix} t^3 \\ 2t^2 \end{pmatrix}$

$$\dot{\vec{c}}(t) = \begin{pmatrix} 3t^2 \\ 4t \end{pmatrix}, \qquad \ddot{\vec{c}}(t) = \begin{pmatrix} 6t \\ 4 \end{pmatrix}$$

Einsetzen von $t = 1$:

| Grösse | Wert |
|---|---|
| Ortsvektor $\vec{c}(1)$ | $\begin{pmatrix} 1 \\ 2 \end{pmatrix}$ |
| Geschwindigkeitsvektor $\dot{\vec{c}}(1)$ | $\begin{pmatrix} 3 \\ 4 \end{pmatrix}$ |
| Beschleunigungsvektor $\ddot{\vec{c}}(1)$ | $\begin{pmatrix} 6 \\ 4 \end{pmatrix}$ |

## 4.4 Schiefer Wurf – die drei Vektoren

| Vektor | Formel | Bedeutung |
|---|---|---|
| **Ortsvektor** $\vec{r}(t)$ | $\begin{pmatrix} v_0 \cos(\alpha) \cdot t + x_0 \\ v_0 \sin(\alpha) \cdot t - \tfrac{1}{2}g t^2 + y_0 \end{pmatrix}$ | Position zur Zeit $t$ |
| **Geschwindigkeitsvektor** $\dot{\vec{r}}(t)$ | $\begin{pmatrix} v_0 \cos(\alpha) \\ v_0 \sin(\alpha) - g t \end{pmatrix}$ | Richtung + Tempo (tangential!) |
| **Beschleunigungsvektor** $\ddot{\vec{r}}(t)$ | $\begin{pmatrix} 0 \\ -g \end{pmatrix}$ | konstant, nach unten (Gravitation) |

> ⚠️ Beachte: Die Beschleunigung zeigt **immer** senkrecht nach unten. Das ist konsistent mit der Annahme „freier Fall, keine Luftreibung".

---

# 5. Bogenlänge

Die **Bogenlänge** ist die **gestreckte Länge** der Kurve zwischen zwei Parameterwerten $a$ und $b$.

## 5.1 Herleitung (Pythagoras im Unendlichkleinen)

Für einen infinitesimalen Bogen $\Delta s$ gilt näherungsweise:

```
                       Δs   Δy
                       /|
                      / |
                     /  |
                    /___|
                     Δx           Pythagoras: (Δs)² ≈ (Δx)² + (Δy)²
```

Im Grenzwert:

$$ds^2 = dx^2 + dy^2 \quad \Longrightarrow \quad \frac{ds^2}{dt^2} = \frac{dx^2}{dt^2} + \frac{dy^2}{dt^2}$$

Daraus folgt:

$$\frac{ds}{dt} = \sqrt{\dot{x}(t)^2 + \dot{y}(t)^2} = |\dot{\vec{c}}(t)|$$

Die **Bogenlänge** erhält man durch Integration:

$$\boxed{L = \int_a^b \sqrt{\dot{x}(t)^2 + \dot{y}(t)^2} \, dt = \int_a^b |\dot{\vec{c}}(t)| \, dt}$$

> 💡 **Merkhilfe:** Bogenlänge = Integral über den **Betrag der Geschwindigkeit** („Strecke = Geschwindigkeit × Zeit", infinitesimal aufsummiert).

## 5.2 Beispiel: Zykloide (aus dem Unterricht)

> 🔗 **Rückbezug zu SW 01 (Trigonometrie):** Wir nutzen die **Halbwinkel-Identität** $1 - \cos(t) = 2\sin^2(t/2)$ – direkt aus der Formelsammlung von SW 01! Ohne die funktioniert das Zykloid-Integral nicht.


Eine **Zykloide** entsteht, wenn man einen Punkt auf einem abrollenden Kreis (Radius $R$) verfolgt – wie einen Nagel in einem rollenden Rad:

$$\vec{r}(t) = R \begin{pmatrix} t - \sin(t) \\ 1 - \cos(t) \end{pmatrix}$$

```
         y
         ↑    ●●●         ●●●
        2R-  ●   ●       ●   ●
         |  ●     ●     ●     ●
         | ●       ●   ●       ●       ← Zykloide
         |●         ● ●         ●
      0  +●---------●----------●------→ x
           0        πR         2πR
```

**Schritt 1:** Ableitung

$$\dot{\vec{r}}(t) = R \begin{pmatrix} 1 - \cos(t) \\ \sin(t) \end{pmatrix}$$

**Schritt 2:** Quadrat des Betrags

$$|\dot{\vec{r}}(t)|^2 = R^2\left((1-\cos(t))^2 + \sin^2(t)\right) = R^2\left(1 - 2\cos(t) + \underbrace{\cos^2(t) + \sin^2(t)}_{=1}\right) = R^2(2 - 2\cos(t))$$

**Schritt 3:** Integration über einen vollen Bogen ($t \in [0, 2\pi]$)

$$L = \int_0^{2\pi} \sqrt{R^2 (2 - 2\cos(t))} \, dt = \sqrt{2}\,R \int_0^{2\pi} \sqrt{1 - \cos(t)} \, dt$$

Mit der Identität $1 - \cos(t) = 2\sin^2(t/2)$ folgt:

$$\boxed{L = 8R}$$

> 🎯 **Schönes Resultat:** Der Umfang eines Zykloidenbogens ist exakt **8 × Radius** des rollenden Rades. Das war ein überraschendes Ergebnis zu Newtons Zeit!

---

# 6. Tangenten- und Hauptnormalenvektor

## 6.1 Tangentenvektor

```
              ĉ(t) ← Tangenten-Einheitsvektor
             /
            /  ● c(t) ── ċ(t) ──→ ← Tangentenvektor
           /  ╱
          / ╱       Kurve
         ╱         (violett)
        ╱
        ↓ n(t) ← Hauptnormalenvektor
```

| Vektor | Formel | Eigenschaft |
|---|---|---|
| **Tangentenvektor** | $\dot{\vec{c}}(t)$ | zeigt in Bewegungsrichtung; Länge = Geschwindigkeit |
| **Tangenten-Einheitsvektor** $\hat{t}(t)$ | $\displaystyle \frac{\dot{\vec{c}}(t)}{\|\dot{\vec{c}}(t)\|}$ | gleiche Richtung, Länge 1 |
| **Hauptnormalenvektor** $\vec{n}(t)$ | $\displaystyle \frac{d}{dt} \hat{t}(t) = \frac{d}{dt}\!\left(\frac{\dot{\vec{c}}(t)}{\|\dot{\vec{c}}(t)\|}\right)$ | steht **senkrecht** zur Tangente |

> 💡 **Geometrische Idee:** Der Tangenten-Einheitsvektor $\hat{t}(t)$ hat konstante Länge 1, ändert aber seine **Richtung**, wenn sich die Kurve krümmt. Diese Richtungsänderung wird durch den Hauptnormalenvektor erfasst.

> ⚠️ **Achtung:** Einfach nur $\ddot{\vec{c}}(t)$ zu nehmen ist **nicht** der Hauptnormalenvektor! Man muss den **Einheitsvektor** $\hat{t}(t) = \dot{\vec{c}}/|\dot{\vec{c}}|$ differenzieren, nicht $\dot{\vec{c}}$ selbst.

## 6.2 Orthogonalität (Sanity Check)

Da $\hat{t}(t)$ konstante Länge 1 hat, gilt $\hat{t}(t) \cdot \hat{t}(t) = 1$. Ableitung nach $t$:

$$2 \, \hat{t}(t) \cdot \frac{d\hat{t}}{dt} = 0 \quad \Longrightarrow \quad \hat{t}(t) \cdot \vec{n}(t) = 0$$

→ **Hauptnormale steht immer senkrecht zur Tangente.** ✅

---

# 7. Zusammenfassung der zentralen Formeln

> Diese Tabelle ist die Formelsammlung für die Prüfung!

| Grösse | Formel (ebene Kurve) |
|---|---|
| **Kurve** | $\vec{c}(t) = \begin{pmatrix} x(t) \\ y(t) \end{pmatrix}$ |
| **Tangentenvektor** | $\dot{\vec{c}}(t) = \begin{pmatrix} \dot{x}(t) \\ \dot{y}(t) \end{pmatrix}$ |
| **Beschleunigungsvektor** | $\ddot{\vec{c}}(t) = \begin{pmatrix} \ddot{x}(t) \\ \ddot{y}(t) \end{pmatrix}$ |
| **Betrag (Tempo)** | $\|\dot{\vec{c}}(t)\| = \sqrt{\dot{x}(t)^2 + \dot{y}(t)^2}$ |
| **Tangenten-Einheitsvektor** | $\hat{t}(t) = \dot{\vec{c}}(t) / \|\dot{\vec{c}}(t)\|$ |
| **Hauptnormalenvektor** | $\vec{n}(t) = \dfrac{d\hat{t}(t)}{dt}$ |
| **Bogenlänge** | $L = \displaystyle\int_a^b \|\dot{\vec{c}}(t)\| \, dt$ |

Für **Raumkurven** (3D) ersetzt man einfach $(x, y)$ durch $(x, y, z)$:

$$\|\dot{\vec{c}}(t)\| = \sqrt{\dot{x}(t)^2 + \dot{y}(t)^2 + \dot{z}(t)^2}$$

---

# 8. Übungen (Papula Band 3, S. 230–232)

> **„Do It Yourself"** – Aufgaben **1 bis 11**. Lösungen auf den Seiten 750–753.

## Empfohlener Fahrplan

| Priorität | Aufgabenthemen (typisch) | Konzept |
|---|---|---|
| 🟢 Warmup | 1–3 | Kurven parametrisieren, Punkte berechnen |
| 🟡 Kernstoff | 4–7 | Tangentenvektor, Bogenlänge |
| 🔴 Herausforderung | 8–11 | Raumkurven, Hauptnormale, Anwendungen |

## Python-Aufgaben (Jupyter-Notebook)

Im Archiv `ana-f-sw-10.zip` liegen zwei Notebooks:

- **`kurven.ipynb`** – Interaktive Darstellung von Kurven (inkl. Kreis, Alpha-Kurve $c_1(t) = (t^2-1, t-t^3)$, Schiefer Wurf)
- **`kruemmungskreis.ipynb`** – Krümmungskreis (wird erst nächste Woche behandelt, Krümmung wurde gestrichen!)

**Beispiel aus `kurven.ipynb`:**
```python
def Alpha(t):
    x = t**2 - 1
    y = t - t**3
    return np.array([x, y])

InteractCurve(Alpha, -5/4, 5/4)
```

## Maxima-Aufgaben

Im gleichen Archiv unter `Maxima/`:
- `inf-poly.wxmx` – Infinitesimale Betrachtung eines Polynoms
- `umparametrisierung.wxmx` – Wie man eine Kurve umparametrisiert (gleiche Bahn, anderer Parameter)

---

# 9. Prüfungsrelevante Hinweise

## Typische Aufgabentypen

1. **Kurve parametrisieren** – Kreis, Gerade, Funktionsgraph
2. **Tangenten- und Normalenvektor an einer Stelle** berechnen
3. **Bogenlänge berechnen** – oft als bestimmtes Integral
4. **Anwendung: Schiefer Wurf** – gegebene $v_0, \alpha$ → Flugweite, maximale Höhe

## Fallen und Tipps

> ⚠️ **Falle 1:** Der Geschwindigkeitsvektor $\dot{\vec{c}}(t)$ ist **nicht automatisch Einheitsvektor**! Wenn du den Tangenten-**Einheits**-vektor $\hat{t}$ brauchst, **teile durch den Betrag**.

> ⚠️ **Falle 2:** Bogenlänge-Integrale sind oft **unangenehm**. Wenn der Integrand ein Ausdruck der Form $\sqrt{2 - 2\cos(t)}$ ist → halbe-Winkel-Identität $1 - \cos(t) = 2\sin^2(t/2)$ anwenden!

> ⚠️ **Falle 3:** Bei Raumkurven ($\mathbb{R}^3$) nicht die $z$-Komponente beim Ableiten/Betrag vergessen.

> ⚠️ **Falle 4:** Im Skalarprodukt $\vec{w} \cdot \vec{z} = 0$ bedeutet **senkrecht**. Das ist der Test, ob Tangente und Normale wirklich orthogonal sind.

## Merksätze

- **Kurve ist eine Funktion der Zeit**, kein statisches Gebilde.
- **Ableitung = komponentenweise** – einfach für jede Koordinate einzeln.
- **Tangentenvektor** zeigt in Bewegungsrichtung, **Normalenvektor** zeigt „zur Innenseite" der Krümmung.
- Die **Bogenlänge** ist das Integral über den Betrag der Geschwindigkeit.
- **Krümmung kommt nächste Woche** – diese Woche ignorieren (wurde im Unterricht gestrichen!).

---

# 10. Rückbezug & Ausblick

Diese Woche zieht **alle bisherigen Themen** des Semesters zusammen – Kurven sind das Bindeglied zwischen Trigonometrie, komplexen Zahlen, Fourier-Analyse, DGL und Hyperbelfunktionen.

| Woche | Thema | Konkrete Verbindung zu SW 10 |
|---|---|---|
| **SW 01** | Trigonometrie | **Direkt verwendet!** (a) Die Kreisparametrisierung $(\cos t, \sin t)$ stammt 1:1 aus SW 01. (b) Die Halbwinkel-Identität $1 - \cos t = 2\sin^2(t/2)$ ist der Schlüssel zum Zykloid-Bogenlänge-Integral → $L = 8R$. (c) Der trigonometrische Pythagoras $\cos^2 t + \sin^2 t = 1$ wird beim Vereinfachen von Tangentenbeträgen dauernd gebraucht. |
| **SW 02** | Folgen, Reihen, Grenzwerte | **Definition der Ableitung.** $\dot{\vec{c}}(t) = \lim_{\Delta t \to 0} \frac{\vec{c}(t+\Delta t) - \vec{c}(t)}{\Delta t}$ ist wörtlich dieselbe Formel wie bei skalaren Funktionen – jetzt nur für Vektoren komponentenweise. |
| **SW 03** | Potenzreihen | "Komponentenweise ableiten" ist das vektorielle Gegenstück zum "gliedweise ableiten" von Potenzreihen. Reihenableitung $\to$ Vektorableitung. |
| **SW 04** | Komplexe Zahlen | **Alternative Darstellung derselben Kurve!** $z(t) = x(t) + iy(t)$ in $\mathbb{C}$ entspricht $\vec{c}(t) = (x(t), y(t))^T$ in $\mathbb{R}^2$. Der Kreis $z = re^{it}$ ist Parametrisierung via Polarform. |
| **SW 05** | Newton, Fourier | Fourier-Reihe $z(t) = \sum c_k e^{ikt}$ ist eine **Überlagerung vieler Kreisbewegungen** – jeweils eine Kurve! Das Rechteck-Signal aus SW 05 ist die Summe vieler parametrisierter Kreise. |
| **SW 06** | Differentialgleichungen I | **Schiefer Wurf = Lösung einer DGL!** $\ddot{\vec{r}}(t) = \begin{pmatrix}0\\-g\end{pmatrix}$ ist eine Vektor-DGL 2. Ordnung. Zweimalige Integration (wie in SW 06 geübt) ergibt die Wurfparabel. |
| **SW 07** | Differentialgleichungen II | Lösungen $x(t) = A\cos(\omega t) + B\sin(\omega t)$ des harmonischen Oszillators parametrisieren eine **Ellipse** im Phasenraum $(x, \dot{x})$. Jede DGL 2. Ordnung erzeugt eine Kurve! |
| **SW 09** | Hyperbelfunktionen | **Hyperbel als Kurve:** $\vec{c}(t) = (\cosh t, \sinh t)$. Der hyperbolische Pythagoras $\cosh^2 t - \sinh^2 t = 1$ beweist, dass diese Kurve tatsächlich auf der Hyperbel $x^2 - y^2 = 1$ liegt. Die **Kettenlinie** $y = \cosh x$ als Funktionsgraph-Kurve: Bogenlänge mit den Formeln aus SW 10 ausrechnen! |
| *(Ausblick SW 11)* | **Krümmung** | Heute bewusst ausgespart (im Unterricht durchgestrichen!). Nächste Woche: Krümmungsformel $\kappa(t) = \frac{|\dot{x}\ddot{y} - \dot{y}\ddot{x}|}{(\dot{x}^2+\dot{y}^2)^{3/2}}$, Krümmungskreis (Schmiegkreis), Radius $\rho = 1/\kappa$. Das Notebook `kruemmungskreis.ipynb` liegt schon bereit! |

## 🎯 Das grosse Bild

Die gesamte bisherige ANA-F-Theorie ist in dieser Woche **konkret anwendbar**:

```
   SW 01 Trig      SW 02 Grenzwert      SW 03 Reihen
       │                  │                   │
       └──── cos, sin ────┼─── Ableitung ─────┘
                          │
                    ┌─────▼─────┐
   SW 04 Komplex ──►│ SW 10:    │◄── SW 09 Hyperbel
                    │  KURVEN   │
   SW 05 Fourier ──►│ (Synthese)│◄── SW 06/07 DGL
                    └─────┬─────┘
                          │
                          ▼
                    Nächste Woche:
                    Krümmung, Schmiegkreis
```

---

## 📝 Check-Liste vor der Prüfung

- [ ] Kann ich eine Kurve parametrisieren (Kreis, Gerade, Funktionsgraph)?
- [ ] Kann ich den Tangentenvektor $\dot{\vec{c}}(t)$ berechnen?
- [ ] Kann ich den Betrag $|\dot{\vec{c}}(t)|$ korrekt vereinfachen?
- [ ] Weiss ich, dass der Tangenten-**Einheits**-vektor noch durch $|\dot{\vec{c}}|$ geteilt werden muss?
- [ ] Kann ich die Bogenlänge-Formel herleiten (Pythagoras)?
- [ ] Beherrsche ich das Zykloid-Beispiel ($L = 8R$)?
- [ ] Erkenne ich den Hauptnormalenvektor als Ableitung des Einheitstangentenvektors?
- [ ] Habe ich mindestens Aufgaben 1–7 aus Papula Band 3 gelöst?
