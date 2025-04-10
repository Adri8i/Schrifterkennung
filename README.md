# Buchstaben Erkennung mit CNN (Convolutional Neural Network)

Dieses Projekt verwendet ein **Convolutional Neural Network (CNN)**, um handgezeichnete Buchstaben (A-Z) zu erkennen. Es besteht aus drei Hauptmodulen: ein Trainingsskript, ein Modell für die Klassifikation von Buchstaben und eine Benutzeroberfläche zur Zeichnung und Vorhersage von Buchstaben.

## 📦 Technologien

- **Python 3.x**
- **TensorFlow 2.x**: Für das Erstellen und Trainieren des Modells
- **OpenCV**: Zum Laden und Vorverarbeiten der Bilder
- **Pillow**: Zur Bildbearbeitung und -darstellung
- **Matplotlib**: Für die Anzeige der Vorhersage-Wahrscheinlichkeiten
- **scikit-learn**: Zum Aufteilen der Daten und zur Datenvorverarbeitung
- **tkinter**: Für die GUI-Anwendung

## 🚀 Installation

### 1. Repository klonen

Klonen Sie dieses Repository oder laden Sie die Dateien herunter:

git clone https://github.com/Adri8i/Schrifterkennung.git

perl
Kopieren
Bearbeiten

### 2. Python-Abhängigkeiten installieren

Installieren Sie die erforderlichen Python-Pakete:

pip install tensorflow opencv-python pillow matplotlib scikit-learn

markdown
Kopieren
Bearbeiten

### 3. Verzeichnisstruktur vorbereiten

Stellen Sie sicher, dass Sie das Verzeichnis `Alphabet` mit den entsprechenden Bilddaten haben. Jedes Unterverzeichnis sollte einen Buchstaben (A-Z) repräsentieren.

## 💻 Verwendung

### Modelltraining

Um das Modell zu trainieren, führen Sie das Skript `trainKi.py` aus. Es wird das CNN-Modell erstellen, es mit den Bildern aus dem `Alphabet`-Verzeichnis trainieren und das beste Modell speichern:

python trainKi.py

markdown
Kopieren
Bearbeiten

- Das Modell wird als `alphabet_model_best.keras` gespeichert.

### Benutzeroberfläche

Um die GUI zur Vorhersage von handgezeichneten Buchstaben zu verwenden, führen Sie `GUI.py` aus:

python GUI.py

php
Kopieren
Bearbeiten

- Sie können Buchstaben auf einer Zeichenfläche malen und auf "Predict" klicken, um die Vorhersage anzuzeigen. Es wird auch ein Diagramm der Vorhersage-Wahrscheinlichkeiten erstellt.

### Modell laden und Vorhersagen treffen

Wenn Sie das Modell nur verwenden möchten, ohne es neu zu trainieren, können Sie das gespeicherte Modell direkt laden und Vorhersagen treffen:

```python
from tensorflow.keras.models import load_model
model = load_model('alphabet_model.keras')
📂 Verzeichnisstruktur
bash
Kopieren
Bearbeiten
/Projektverzeichnis
│
├── GUI.py            # GUI-Anwendung zur Zeichnung und Vorhersage von Buchstaben
├── model.py          # Modell-Definition (CNN)
├── trainKi.py        # Skript zum Training des Modells
└── Alphabet/         # Verzeichnis mit Unterordnern A-Z, die jeweils Bilder des Buchstabens enthalten
⚙️ Funktionsweise
1. Modell erstellen
In model.py wird ein CNN-Modell erstellt, das drei Convolutional Layers mit MaxPooling, gefolgt von Dense Layers und einem Dropout Layer zur Vermeidung von Overfitting umfasst. Das Modell wird mit der Adam-Optimierung und Sparse Categorical Crossentropy-Verlustfunktion trainiert.

2. Training
In trainKi.py werden die Bilddaten aus dem Verzeichnis Alphabet geladen, vorverarbeitet und das Modell wird trainiert. Der Datensatz wird in Trainings- und Testdaten aufgeteilt. Das Modell wird während des Trainings regelmäßig evaluiert, und das beste Modell basierend auf der Validierungsgenauigkeit wird gespeichert.

3. Vorhersage
In GUI.py kann der Benutzer mit einer grafischen Oberfläche einen Buchstaben zeichnen. Dieser wird auf eine Größe von 28x28 Pixel skaliert und für die Vorhersage ins Modell eingespeist. Das Ergebnis wird in einem Balkendiagramm angezeigt, das die Vorhersage-Wahrscheinlichkeiten für alle 26 Buchstaben darstellt.

📊 Diagramm der Vorhersage
Das Diagramm zeigt die Vorhersage-Wahrscheinlichkeiten für alle Buchstaben A-Z. Die Vorhersage, die das höchste Wahrscheinlichkeitsmaß hat, wird als die wahrscheinlichste Erkennung angezeigt.

📝 Lizenz
Dieses Projekt ist unter der MIT-Lizenz lizenziert.

markdown
Kopieren
Bearbeiten
