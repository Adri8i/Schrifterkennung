Buchstaben Erkennung mit CNN (Convolutional Neural Network)

Projektbeschreibung
Dieses Projekt verwendet ein Convolutional Neural Network (CNN), um handgezeichnete Buchstaben zu erkennen. Die Bilder von Buchstaben A-Z werden verwendet, um ein Modell zu trainieren. Das Modell kann in einer GUI-Anwendung verwendet werden, um gezeichnete Buchstaben zu erkennen und Vorhersagen zu treffen.

Technologien
Python 3.x

TensorFlow 2.x: Für das Erstellen und Trainieren des Modells

OpenCV: Zum Laden und Vorverarbeiten der Bilder

Pillow: Zur Bildbearbeitung und -darstellung

Matplotlib: Für die Anzeige der Vorhersage-Wahrscheinlichkeiten

scikit-learn: Zum Aufteilen der Daten und zur Datenvorverarbeitung

tkinter: Für die GUI-Anwendung

Installation
Repository klonen: Klone dieses Repository oder lade die Dateien herunter.

bash
Kopieren
Bearbeiten
git clone https://github.com/DeinUsername/Projektname.git
Python-Abhängigkeiten installieren: Installiere die erforderlichen Python-Pakete:

bash
Kopieren
Bearbeiten
pip install tensorflow opencv-python pillow matplotlib scikit-learn
Verzeichnisstruktur vorbereiten: Stelle sicher, dass du das Verzeichnis Alphabet mit den entsprechenden Bilddaten hast. Jedes Unterverzeichnis sollte einen Buchstaben (A-Z) repräsentieren.

Verwendung
Modelltraining
Um das Modell zu trainieren, führe das Skript trainKi.py aus. Es wird das CNN-Modell erstellen, es mit den Bildern aus dem Alphabet-Verzeichnis trainieren und das beste Modell speichern.

bash
Kopieren
Bearbeiten
python trainKi.py
Das Modell wird als alphabet_model_best.keras gespeichert.

Benutzeroberfläche
Um die GUI zur Vorhersage von handgezeichneten Buchstaben zu verwenden, führe GUI.py aus:

bash
Kopieren
Bearbeiten
python GUI.py
Du kannst Buchstaben auf einer Zeichenfläche malen und auf "Predict" klicken, um die Vorhersage anzuzeigen. Es wird auch ein Diagramm der Vorhersage-Wahrscheinlichkeiten erstellt.

Modell laden und Vorhersagen treffen
Wenn du das Modell nur verwenden möchtest, ohne es neu zu trainieren, kannst du das gespeicherte Modell direkt laden und Vorhersagen treffen.

python
Kopieren
Bearbeiten
from tensorflow.keras.models import load_model
model = load_model('alphabet_model.keras')
Verzeichnisstruktur
bash
Kopieren
Bearbeiten
/Projektverzeichnis
│
├── GUI.py            # GUI-Anwendung zur Zeichnung und Vorhersage von Buchstaben
├── model.py          # Modell-Definition (CNN)
├── trainKi.py        # Skript zum Training des Modells
└── Alphabet/         # Verzeichnis mit Unterordnern A-Z, die jeweils Bilder des Buchstabens enthalten
Funktionsweise
Modell erstellen: In model.py wird ein CNN-Modell erstellt, das drei Convolutional Layers mit MaxPooling, gefolgt von Dense Layers und einem Dropout Layer zur Vermeidung von Overfitting umfasst.

Training: In trainKi.py werden die Bilddaten aus dem Verzeichnis Alphabet geladen, vorverarbeitet und das Modell wird trainiert. Das Modell wird gespeichert und das beste Modell basierend auf der Validierungsgenauigkeit wird als alphabet_model_best.keras gespeichert.

Vorhersage: In GUI.py kann der Benutzer mit einer grafischen Oberfläche einen Buchstaben zeichnen. Dieser wird auf eine Größe von 28x28 Pixel skaliert und für die Vorhersage ins Modell eingespeist. Das Ergebnis wird in einem Balkendiagramm angezeigt.

Lizenz
Dieses Projekt ist unter der MIT-Lizenz lizenziert.
