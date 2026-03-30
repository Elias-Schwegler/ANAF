# Prompt: Wöchentliche Zusammenfassung erstellen

Erstelle eine strukturierte Zusammenfassung der Semesterwoche als Markdown-Datei `Zusammenfassung_Woche_XX.md` im jeweiligen Wochenordner. Folge dabei exakt dieser Struktur:

---

## Aufbau

### Header
- Modulname, Dozenten, Quellenangabe (Papula Band + Kapitel)
- Lernziele aus den Folien

### Pro Themenblock (gemäss Folien-Gliederung):

1. **Titel** des Themenblocks (z.B. "Trigonometrische Funktionen")
   - Quellenangabe (Papula Band, Kapitel, Seitenzahlen)

2. **Formeln & Definitionen**
   - Alle relevanten Formeln aus dem Papula aufgelistet
   - Tabellen für Übersichten (z.B. Eigenschaften von Funktionen)
   - Wichtige Werte und Zusammenhänge

3. **Aufgabentypen**
   - Welche Arten von Aufgaben kommen typischerweise?
   - Kurze Beschreibung mit Verweis auf empfohlene Aufgaben

### Nach allen Themenblöcken:

4. **Empfohlene Übungsaufgaben**
   - Tabelle: Aufgabennummer, Thema, Kurzbeschreibung
   - Seitenangaben aus dem Papula

5. **Lösungen der empfohlenen Aufgaben**
   - Vollständige Lösungswege und Ergebnisse
   - Gegliedert nach Aufgabennummer

---

## Prüfungsformat (MEP)

> ⚠️ **WICHTIG: Die Modulendprüfung (MEP) ist zweiteilig!** Dies muss bei der Zusammenfassung berücksichtigt werden.

| | **Teil 1: Ohne Hilfsmittel** | **Teil 2: Mit elektronischen Hilfsmitteln** |
|---|---|---|
| **Erlaubt** | Papier-Unterlagen (Open-Book), Taschenrechner | Laptop mit Maxima, Python, etc. |
| **Nicht erlaubt** | Elektronische Geräte | — |
| **Aufgabentyp** | Formeln anwenden, von Hand rechnen, Konzepte erklären, klassifizieren | Komplexere Aufgaben, die mit CAS/Code in begrenzter Zeit lösbar sind |
| **Vorbereitung** | Formeln & Lösungswege beherrschen, Kochrezepte parat haben | Maxima- & Python-Befehle kennen und schnell eintippen können |

### Konsequenz für die Zusammenfassung:
- **Jede Woche** muss einen Abschnitt **"Maxima & Python – Elektronische Hilfsmittel (MEP Teil 2)"** enthalten
- Dieser Abschnitt enthält **kopierbereite Code-Beispiele** in Maxima und Python für die Themen der Woche
- Fokus auf: **Welche Befehle lösen welche Aufgabentypen?** (nicht theoretische Erklärung des Codes)
- Zusätzlich eine **Kurzreferenz-Tabelle** der wichtigsten Maxima-Befehle pro Woche
- Der Dozent verwendet **wxMaxima** und **Python** im Unterricht – die Zusammenfassung sollte beides abdecken

## Regeln

- **Sprache:** Deutsch
- **Formeln:** LaTeX-Notation ($$...$$) für wichtige Formeln, inline `$(...)$` für kurze Ausdrücke
- **Tabellen:** Für Vergleiche und Übersichten verwenden
- **Trennlinien:** `---` zwischen den Hauptthemen
- **Quellen:** Immer Papula Band, Kapitel und Seitenzahlen angeben
- **Do It Yourself:** Die Aufgaben und Theorie-Referenzen von der letzten Folie ("Do It Yourself") als Grundlage verwenden
- **Inhalt aus dem Papula:** Formeln und Definitionen direkt aus dem Papula extrahieren (PDF lesen), nicht nur von den Folien
- **Prüfungsvorbereitung:** Der Fokus liegt auf dem Verständnis und der Anwendung – nicht nur Auflistung

## Vorgehen

1. Folien der Woche lesen → Themen und Lernziele identifizieren
2. "Do It Yourself" Folie → Theorie-Referenzen und empfohlene Aufgaben notieren
3. Papula-Kapitel extrahieren (PDF-Seiten lesen) → Formeln, Definitionen, Beispiele
4. Übungsaufgaben und Lösungen aus dem Papula extrahieren
5. Vorlesungsnotizen (Screenshots) prüfen und in die Zusammenfassung einbauen
6. **Visualisierungen erstellen** (siehe Abschnitt unten)
7. Zusammenfassung nach obiger Struktur erstellen

---

## Visualisierungen & Graphen

Wo immer es sinnvoll ist, sollen **eigene Graphen/Plots** mit Python (matplotlib) generiert und in die Zusammenfassung eingebettet werden. Das hilft enorm beim Verständnis mathematischer Konzepte.

### Wann Graphen erstellen?
- **Funktionsverläufe** visualisieren (z.B. verschiedene Lösungstypen einer DGL im Vergleich)
- **Vergleiche** zwischen Methoden oder Fällen (z.B. Kriechfall vs. Schwingfall vs. Grenzfall)
- **Numerische vs. analytische** Lösungen gegenüberstellen
- **Konvergenzverhalten** von Reihen, Folgen, Iterationsverfahren
- **Geometrische Interpretationen** (z.B. komplexe Zahlen in der Gaussschen Ebene, Richtungsfelder)

### Wie Graphen erstellen?
1. **Python-Script** mit `matplotlib` direkt im Wochenordner ausführen
2. **PNG-Dateien** mit beschreibendem Namen speichern (z.B. `vergleich_drei_faelle.png`, `schwingfall.png`)
3. In der Zusammenfassung **einbetten** mit `![Beschreibung](dateiname.png)` und einem erklärenden Kursiv-Text darunter
4. **Beschriftung:** Achsenbeschriftung (deutsch), Titel, Legende, Grid
5. **Auflösung:** `dpi=150` für gute Lesbarkeit
6. **Farben:** Konsistente Farbgebung (z.B. blau = Fall 1, rot = Fall 2, grün = Fall 3)

### Zusätzlich: Mermaid-Diagramme
Für **Ablauf-/Entscheidungsdiagramme** (z.B. Lösungsschemata, Fallunterscheidungen) sollen `mermaid`-Codeblöcke direkt im Markdown eingebettet werden. Beispiel: Flussdiagramm für das Lösungsschema einer DGL.

### Was NICHT als Graph?
- Konzepte die bereits als Screenshot aus der Vorlesung vorhanden sind (Duplikate vermeiden)
- Triviale Darstellungen, die keinen Mehrwert gegenüber der Formel bieten

> **Merke:** Generierte Graphen (PNG) werden **committed** (im Gegensatz zu den temporären PDF-Renders). Sie sind ein fester Bestandteil der Zusammenfassung.

---

## Umgang mit PDFs und Bildern

### Papula-PDF (Textbook)
- **Ingestion:** Relevante Seiten des Papula-PDF als Bilder rendern (via Python/fitz) in einen Ordner `papula_images/`. Diese Bilder dienen **nur** zur visuellen Content-Extraction durch den Agenten.
- **Content verwenden, Bilder NICHT committen:** Die Inhalte (Formeln, Definitionen, Beispiele) aus den gerenderten Seiten in LaTeX in die Zusammenfassung übertragen. Die gerenderten Bilder selbst werden **niemals** committed – sie sind in `.gitignore` ausgeschlossen.
- **Seitenoffset:** Der Papula Band 1 hat einen Offset von +23 (Buchseite X = PDF-Seite X+23).

### Folien-PDF (Slides)
- **Ingestion:** Folien-PDF als Bilder rendern in einen Ordner `slides_images/`. Diese dienen nur zur Inhalts-Extraktion.
- **NICHT committen:** Die gerenderten Slide-Bilder sind ebenfalls in `.gitignore` ausgeschlossen.

### Vorlesungsnotizen / Screenshots
- **IMMER committen:** PNG-Screenshots direkt im Wochenordner (z.B. `Taylor_Reihe_Beispiel.png`, `Maxima_polinom.png`) sind handschriftliche Notizen oder CAS-Demonstrationen aus der Vorlesung.
- Diese Screenshots werden in die Zusammenfassung **eingebettet** mit beschreibendem Alt-Text und Erklärungen.
- **Qualitätsprüfung:** Nur Screenshots einbinden, die einen Mehrwert bieten (z.B. visuelle Erklärungen, Schritt-für-Schritt-Herleitungen, Maxima-Plots). Notizen, die zu chaotisch sind oder Inhalte duplizieren, die bereits sauber als LaTeX im Dokument stehen, können weggelassen werden.

### .gitignore Regeln
```
# Automatisch generierte Bilder aus PDFs (nicht committen)
**/papula_images/
**/slides_images/
```

> **Merke:** Lecture screenshots (direkt im Wochenordner) = ✅ committen. Gerenderte PDF-Seiten (in `papula_images/` oder `slides_images/`) = ❌ nicht committen.
