import os
import cv2
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from tensorflow.keras.utils import to_categorical
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.callbacks import ModelCheckpoint
from model import create_model  # Importiere das Modell aus der Datei model.py
from tensorflow.keras.optimizers import Adam


def load_and_preprocess_images(folder, img_size=28):
    images = []
    labels = []

    for letter_folder in os.listdir(folder):
        letter_path = os.path.join(folder, letter_folder)
        if os.path.isdir(letter_path):
            for filename in os.listdir(letter_path):
                filepath = os.path.join(letter_path, filename)
                if os.path.isfile(filepath):
                    image = cv2.imread(filepath, 0)  # Graustufen
                    resized_img = cv2.resize(image, (img_size, img_size))
                    normalized_img = resized_img / 255.0
                    images.append(normalized_img)
                    labels.append(letter_folder)

    images_array = np.array(images)
    label_mapping = {chr(65 + i): i for i in range(26)}  # A-Z -> 0-25
    labels_numeric = np.array([label_mapping[label] for label in labels])
    return images_array, labels_numeric


folder_path = r"C:\Users\adris\OneDrive\Dokumente\HTL\4BHEL\Ki\Alphabet\Buchstaben_ende"
img_size = 28

images_array, labels_array = load_and_preprocess_images(folder_path, img_size)

# Überprüfungen
print(f"Anzahl der Bilder: {len(images_array)}")
print(f"Anzahl der Labels: {len(labels_array)}")
print(f"Bilder Array Shape: {images_array.shape}")
print(f"Labels Array Shape: {labels_array.shape}")

# Beispielbilder anzeigen
plt.figure(figsize=(10, 2))
for i in range(5):
    plt.subplot(1, 5, i + 1)
    plt.imshow(images_array[i], cmap="gray")
    plt.title(f"Label: {labels_array[i]}")
    plt.axis("off")
plt.show()

# Daten anpassen für das Modell
images_array = images_array.reshape(-1, 28, 28, 1).astype('float32')
labels_array = to_categorical(labels_array, num_classes=26)

x_train, x_test, y_train, y_test = train_test_split(images_array, labels_array, test_size=0.2, random_state=42)

model = create_model(input_shape=(28, 28, 1), num_classes=26)
model.compile(optimizer=Adam(), loss='categorical_crossentropy', metrics=['accuracy'])

datagen = ImageDataGenerator(rotation_range=15, width_shift_range=0.2, height_shift_range=0.2, shear_range=0.2,
                             zoom_range=0.2, fill_mode="nearest")
datagen.fit(x_train)

checkpoint = ModelCheckpoint("alphabet_model_best.keras", monitor='val_accuracy', save_best_only=True, mode='max')

history = model.fit(datagen.flow(x_train, y_train, batch_size=32), epochs=35, validation_data=(x_test, y_test),
                    callbacks=[checkpoint])

test_loss, test_acc = model.evaluate(x_test, y_test, verbose=2)
print(f"Test Accuracy: {test_acc * 100:.2f}%")

model.save("alphabet_model.keras")
print("Model saved as alphabet_model.keras")