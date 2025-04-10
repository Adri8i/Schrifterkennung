import tkinter as tk
from tkinter import Canvas, messagebox
import numpy as np
import cv2
from PIL import Image, ImageDraw
import matplotlib.pyplot as plt
from tensorflow.keras.models import load_model

# Modell laden
model = load_model("alphabet_model.keras")
label_mapping = {i: chr(65 + i) for i in range(26)}  # 0-25 -> A-Z

class DrawingApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Buchstaben Erkennung")

        self.canvas = Canvas(root, width=280, height=280, bg="white")
        self.canvas.pack()

        self.button_predict = tk.Button(root, text="Predict", command=self.predict)
        self.button_predict.pack()

        self.button_clear = tk.Button(root, text="Clear", command=self.clear_canvas)
        self.button_clear.pack()

        self.canvas.bind("<B1-Motion>", self.paint)

        self.image = Image.new("L", (280, 280), 255)
        self.draw = ImageDraw.Draw(self.image)

    def paint(self, event):
        x1, y1 = (event.x - 10), (event.y - 10)
        x2, y2 = (event.x + 10), (event.y + 10)
        self.canvas.create_oval(x1, y1, x2, y2, fill="black", width=5)
        self.draw.ellipse([x1, y1, x2, y2], fill="black")

    def clear_canvas(self):
        self.canvas.delete("all")
        self.image = Image.new("L", (280, 280), 255)
        self.draw = ImageDraw.Draw(self.image)

    def predict(self):
        img = self.image.resize((28, 28))  # Größe anpassen
        img = np.array(img) / 255.0  # Normalisieren
        img = np.expand_dims(img, axis=(0, -1))  # Reshape zu (1, 28, 28, 1)

        prediction = model.predict(img)[0]  # Vorhersage holen
        predictions_percent = {label_mapping[i]: round(prediction[i] * 100, 2) for i in range(26)}

        sorted_predictions = sorted(predictions_percent.items(), key=lambda x: x[1], reverse=True)
        letters, percentages = zip(*sorted_predictions)

        # Diagramm erstellen
        plt.figure(figsize=(10, 5))
        plt.bar(letters, percentages, color='blue')
        plt.xlabel("Buchstaben")
        plt.ylabel("Wahrscheinlichkeit (%)")
        plt.title("Vorhersage-Wahrscheinlichkeiten")
        plt.xticks(rotation=45)
        plt.show()

if __name__ == "__main__":
    root = tk.Tk()
    app = DrawingApp(root)
    root.mainloop()
