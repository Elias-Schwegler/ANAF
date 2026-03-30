# Recap: Komplexe Zahlen – Übungsaufgaben

> Schnell-Refresher zum Selbst-Durchrechnen. Löse jede Aufgabe zuerst selbst, dann Lösung aufklappen.
> Für Theorie → siehe Abschnitt 0 in `Zusammenfassung_Woche_07.md` oder `../SW 04 - Komplexe Zahlen/Zusammenfassung_Woche_04.md`

---

## 1. Addition & Subtraktion

> **Regel:** Komponentenweise – Realteile zusammen, Imaginärteile zusammen.
> $(a + bi) \pm (c + di) = (a \pm c) + (b \pm d)i$

### Aufgabe 1a

$$z_1 = 3 + 2i, \quad z_2 = -1 + 5i$$

Berechne $z_1 + z_2$ und $z_1 - z_2$.

<details>
<summary>Lösung</summary>

$$z_1 + z_2 = (3 + (-1)) + (2 + 5)i = 2 + 7i$$

$$z_1 - z_2 = (3 - (-1)) + (2 - 5)i = 4 - 3i$$

</details>

### Aufgabe 1b

$$z_1 = -4 + i, \quad z_2 = 2 - 3i, \quad z_3 = -i$$

Berechne $z_1 + z_2 - 2z_3$.

<details>
<summary>Lösung</summary>

Zuerst $2z_3$:

$$2z_3 = 2 \cdot (-i) = -2i$$

Dann zusammen:

$$z_1 + z_2 - 2z_3 = (-4 + i) + (2 - 3i) - (-2i)$$

$$= (-4 + 2) + (1 - 3 + 2)i = -2 + 0i = -2$$

Das Ergebnis ist rein reell!

</details>

---

## 2. Multiplikation

> **Regel:** Ausmultiplizieren wie ein Binom, dann $i^2 = -1$ einsetzen.
> $(a + bi)(c + di) = ac + adi + bci + bdi^2 = (ac - bd) + (ad + bc)i$

### Aufgabe 2a

$$z_1 = 2 + 3i, \quad z_2 = 4 - i$$

Berechne $z_1 \cdot z_2$.

<details>
<summary>Lösung</summary>

$$(2 + 3i)(4 - i)$$

Ausmultiplizieren:

$$= 2 \cdot 4 + 2 \cdot (-i) + 3i \cdot 4 + 3i \cdot (-i)$$

$$= 8 - 2i + 12i - 3i^2$$

$i^2 = -1$ einsetzen:

$$= 8 + 10i - 3(-1) = 8 + 10i + 3 = 11 + 10i$$

</details>

### Aufgabe 2b

$$z = 1 + i$$

Berechne $z^2$ und $z^3$.

<details>
<summary>Lösung</summary>

**$z^2$:**

$$(1 + i)^2 = 1 + 2i + i^2 = 1 + 2i - 1 = 2i$$

**$z^3$:**

$$z^3 = z^2 \cdot z = 2i \cdot (1 + i) = 2i + 2i^2 = 2i - 2 = -2 + 2i$$

</details>

---

## 3. Konjugiert Komplexe & Betrag

> **Konjugiert komplex:** Vorzeichenwechsel beim Imaginärteil: $z^* = a - bi$
> **Betrag:** $|z| = \sqrt{a^2 + b^2}$
> **Wichtige Eigenschaft:** $z \cdot z^* = |z|^2$ (immer reell!)

### Aufgabe 3a

Bestimme $z^*$ und $|z|$ für:

$$z_1 = 3 - 4i, \quad z_2 = -2 + i, \quad z_3 = 5i$$

<details>
<summary>Lösung</summary>

| $z$ | $z^*$ | $\|z\|$ |
|---|---|---|
| $3 - 4i$ | $3 + 4i$ | $\sqrt{9 + 16} = \sqrt{25} = 5$ |
| $-2 + i$ | $-2 - i$ | $\sqrt{4 + 1} = \sqrt{5} \approx 2.24$ |
| $5i$ | $-5i$ | $\sqrt{0 + 25} = 5$ |

</details>

### Aufgabe 3b

Zeige, dass $z \cdot z^* = |z|^2$ für $z = 3 + 4i$.

<details>
<summary>Lösung</summary>

$$z \cdot z^* = (3 + 4i)(3 - 4i) = 9 - 12i + 12i - 16i^2 = 9 + 16 = 25$$

$$|z|^2 = (\sqrt{9 + 16})^2 = 25 \quad ✓$$

</details>

---

## 4. Division

> **Regel:** Zähler und Nenner mit dem **konjugiert Komplexen des Nenners** erweitern.
> Dadurch wird der Nenner reell ($z \cdot z^* = |z|^2$).
>
> $$\frac{z_1}{z_2} = \frac{z_1 \cdot z_2^*}{z_2 \cdot z_2^*} = \frac{z_1 \cdot z_2^*}{|z_2|^2}$$

### Aufgabe 4a

$$\frac{1 + 3i}{2 + i}$$

<details>
<summary>Lösung</summary>

Konjugiert Komplexe des Nenners: $(2 + i)^* = 2 - i$

**Zähler erweitern:**

$$(1 + 3i)(2 - i) = 2 - i + 6i - 3i^2 = 2 + 5i + 3 = 5 + 5i$$

**Nenner erweitern:**

$$(2 + i)(2 - i) = 4 - i^2 = 4 + 1 = 5$$

**Ergebnis:**

$$\frac{5 + 5i}{5} = 1 + i$$

</details>

### Aufgabe 4b

$$\frac{4 - 2i}{1 - 3i}$$

<details>
<summary>Lösung</summary>

Konjugiert Komplexe des Nenners: $(1 - 3i)^* = 1 + 3i$

**Zähler:**

$$(4 - 2i)(1 + 3i) = 4 + 12i - 2i - 6i^2 = 4 + 10i + 6 = 10 + 10i$$

**Nenner:**

$$(1 - 3i)(1 + 3i) = 1 + 9 = 10$$

**Ergebnis:**

$$\frac{10 + 10i}{10} = 1 + i$$

</details>

---

## 5. Polarform & Umrechnung

> **Kartesisch → Polar:** $r = |z| = \sqrt{x^2 + y^2}$, $\varphi = \arctan\!\left(\frac{y}{x}\right)$ (Quadrant beachten!)
> **Polar → Kartesisch:** $x = r\cos\varphi$, $y = r\sin\varphi$
> **Exponentialform:** $z = r \cdot e^{i\varphi}$

### Aufgabe 5a – Kartesisch → Polar

Wandle in Polarform um: $z = 1 + i$

<details>
<summary>Lösung</summary>

$$r = \sqrt{1^2 + 1^2} = \sqrt{2}$$

$$\varphi = \arctan\!\left(\frac{1}{1}\right) = \frac{\pi}{4} = 45°$$

(1. Quadrant, also passt der Winkel direkt.)

$$\boxed{z = \sqrt{2} \cdot e^{i\pi/4}}$$

</details>

### Aufgabe 5b – Polar → Kartesisch

Wandle in kartesische Form um: $z = 4 \cdot e^{i \cdot 2\pi/3}$

<details>
<summary>Lösung</summary>

$$x = 4 \cos\!\left(\frac{2\pi}{3}\right) = 4 \cdot \left(-\frac{1}{2}\right) = -2$$

$$y = 4 \sin\!\left(\frac{2\pi}{3}\right) = 4 \cdot \frac{\sqrt{3}}{2} = 2\sqrt{3}$$

$$\boxed{z = -2 + 2\sqrt{3} \, i \approx -2 + 3.46 \, i}$$

</details>

---

## 6. Multiplikation & Division in Polarform

> **Multiplikation:** Beträge mal, Winkel plus → $r_1 e^{i\varphi_1} \cdot r_2 e^{i\varphi_2} = r_1 r_2 \cdot e^{i(\varphi_1 + \varphi_2)}$
> **Division:** Beträge geteilt, Winkel minus → $\frac{r_1}{r_2} \cdot e^{i(\varphi_1 - \varphi_2)}$

### Aufgabe 6a

$$z_1 = 3 e^{i\pi/6}, \quad z_2 = 2 e^{i\pi/3}$$

Berechne $z_1 \cdot z_2$ und $\frac{z_1}{z_2}$.

<details>
<summary>Lösung</summary>

**Multiplikation:**

$$z_1 \cdot z_2 = 3 \cdot 2 \cdot e^{i(\pi/6 + \pi/3)} = 6 \cdot e^{i \cdot \pi/2} = 6i$$

(Denn $e^{i\pi/2} = \cos(90°) + i\sin(90°) = i$)

**Division:**

$$\frac{z_1}{z_2} = \frac{3}{2} \cdot e^{i(\pi/6 - \pi/3)} = 1.5 \cdot e^{-i\pi/6} = 1.5\left(\cos(-30°) + i\sin(-30°)\right)$$

$$= 1.5 \cdot \left(\frac{\sqrt{3}}{2} - \frac{1}{2}i\right) = \frac{3\sqrt{3}}{4} - \frac{3}{4}i \approx 1.30 - 0.75i$$

</details>

---

## 7. Potenzen & Wurzeln

> **Potenz:** $(r e^{i\varphi})^n = r^n \cdot e^{in\varphi}$
> **Wurzel:** $\sqrt[n]{r} \cdot e^{i \frac{\varphi + 2k\pi}{n}}$ für $k = 0, 1, \ldots, n-1$ → es gibt immer $n$ Lösungen!

### Aufgabe 7a – Potenz

Berechne $(1 + i)^4$.

<details>
<summary>Lösung</summary>

Zuerst in Polarform: $z = 1 + i = \sqrt{2} \cdot e^{i\pi/4}$

Dann potenzieren:

$$z^4 = (\sqrt{2})^4 \cdot e^{i \cdot 4 \cdot \pi/4} = 4 \cdot e^{i\pi} = 4 \cdot (-1) = -4$$

**Probe (kartesisch):**

$$z^2 = (1+i)^2 = 2i$$

$$z^4 = (2i)^2 = 4i^2 = -4 \quad ✓$$

</details>

### Aufgabe 7b – Quadratwurzel

Finde alle Lösungen von $z^2 = -4$.

<details>
<summary>Lösung</summary>

$-4$ in Polarform: $r = 4$, $\varphi = \pi$ → $z = 4 e^{i\pi}$

Wurzelformel ($n = 2$):

$$w_k = \sqrt{4} \cdot e^{i \frac{\pi + 2k\pi}{2}} = 2 \cdot e^{i \frac{\pi + 2k\pi}{2}}$$

**$k = 0$:** $w_0 = 2 e^{i\pi/2} = 2i$

**$k = 1$:** $w_1 = 2 e^{i \cdot 3\pi/2} = -2i$

$$\boxed{z = \pm 2i}$$

**Probe:** $(2i)^2 = 4i^2 = -4$ ✓, $(-2i)^2 = 4i^2 = -4$ ✓

</details>

---

## 8. Die Euler-Formel anwenden (Schlüssel für den Schwingfall!)

> $$e^{i\varphi} = \cos\varphi + i\sin\varphi$$
>
> Damit kann man $e^{(\alpha + i\omega)x}$ in eine **reelle** Form bringen:
> $$e^{(\alpha + i\omega)x} = e^{\alpha x} \cdot (\cos(\omega x) + i\sin(\omega x))$$

### Aufgabe 8a

Schreibe $e^{(-2 + 3i)x}$ in der Form $e^{\alpha x} \cdot (\cos(\omega x) + i\sin(\omega x))$.

<details>
<summary>Lösung</summary>

$$e^{(-2 + 3i)x} = e^{-2x} \cdot e^{3ix} = e^{-2x} \cdot (\cos(3x) + i\sin(3x))$$

Also: $\alpha = -2$ (Dämpfung), $\omega = 3$ (Kreisfrequenz).

</details>

### Aufgabe 8b – Komplette Schwingfall-Anwendung

Die charakteristische Gleichung liefert $\lambda_{1/2} = -1 \pm 2i$.

Bestimme die allgemeine Lösung der DGL.

<details>
<summary>Lösung</summary>

Identifiziere: $\alpha = -1$, $\omega = 2$

Die allgemeine Lösung bei konjugiert komplexen Lösungen ist:

$$y(x) = e^{\alpha x}(C_1 \cos(\omega x) + C_2 \sin(\omega x))$$

Einsetzen:

$$\boxed{y(x) = e^{-x}(C_1 \cos(2x) + C_2 \sin(2x))}$$

</details>

### Aufgabe 8c – Schwingfall mit AWP (Vollständig)

Löse das AWP:

$$y'' + 2y' + 5y = 0, \quad y(0) = 3, \quad y'(0) = -1$$

<details>
<summary>Lösung</summary>

**Schritt 1 – Charakteristische Gleichung:**

$$\lambda^2 + 2\lambda + 5 = 0$$

**Schritt 2 – Diskriminante:**

$$D = 4 - 20 = -16 < 0 \quad \Rightarrow \text{Schwingfall!}$$

**Schritt 3 – Lambda berechnen:**

$$\lambda_{1/2} = \frac{-2 \pm \sqrt{-16}}{2} = \frac{-2 \pm 4i}{2} = -1 \pm 2i$$

Also $\alpha = -1$, $\omega = 2$.

**Schritt 4 – Allgemeine Lösung:**

$$y(x) = e^{-x}(C_1 \cos(2x) + C_2 \sin(2x))$$

**Schritt 5 – Ableitung (Produktregel!):**

$$y'(x) = -e^{-x}(C_1 \cos(2x) + C_2 \sin(2x)) + e^{-x}(-2C_1 \sin(2x) + 2C_2 \cos(2x))$$

**Schritt 6 – Anfangsbedingungen einsetzen:**

$$y(0) = e^0(C_1 \cdot 1 + C_2 \cdot 0) = C_1 = 3$$

$$y'(0) = -C_1 + 2C_2 = -1$$

$$-3 + 2C_2 = -1 \quad \Rightarrow \quad C_2 = 1$$

**Schritt 7 – Spezielle Lösung:**

$$\boxed{y(x) = e^{-x}(3\cos(2x) + \sin(2x))}$$

</details>

---

## Selbstcheck: Kann ich alles?

| Operation | Kann ich ✅ | Muss ich nochmal üben 🔄 |
|---|---|---|
| Addition / Subtraktion | | |
| Multiplikation (ausmultiplizieren, $i^2 = -1$) | | |
| Konjugiert Komplexe bilden | | |
| Betrag berechnen | | |
| Division (konjugiert erweitern) | | |
| Kartesisch ↔ Polar umrechnen | | |
| Multiplikation/Division in Polarform | | |
| Potenzen und Wurzeln | | |
| Euler-Formel anwenden ($e^{i\varphi} = \cos\varphi + i\sin\varphi$) | | |
| Schwingfall komplett lösen | | |
