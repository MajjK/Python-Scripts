from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.optimizers import RMSprop
import tensorflow as tf
import numpy as np
import cv2
import os


def detect_car(img_path):
    car_cascade = cv2.CascadeClassifier('cars.xml')
    img = cv2.imread(img_path)
    img = cv2.resize(img, (400, 400))
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    cars = car_cascade.detectMultiScale(gray, 1.01, 3, minSize=(20, 20))
    if len(cars) == 0:
        return False
    else:
        return True


def predict_image(img_path):
    val_datagen = ImageDataGenerator(rescale=1/255)
    img = tf.keras.preprocessing.image.load_img(img_path, target_size=(200, 200))
    img = tf.keras.preprocessing.image.img_to_array(img)
    img = tf.expand_dims(img, 0)
    img = val_datagen.flow(img, batch_size=1)
    return model.predict(img)


def predict_images_from_folder(testing_folder):
    score = 0
    test_imgs_names = os.listdir(os.path.join(testing_folder))
    for i in range(len(test_imgs_names)):
        test_img_path = testing_folder + "/" + test_imgs_names[i]
        car_detected = detect_car(test_img_path)
        if car_detected:
            prediction = predict_image(test_img_path)
            result = np.argmax(prediction)
            print(test_imgs_names[i], " Color: ", labels[result])
            if labels[result] in test_imgs_names[i]:
                score += 1
        else:
            print(test_imgs_names[i], " No Car")
            if "nocar" in test_imgs_names[i]:
                score += 1
    print("Accuracy: %.2f%%" % ((score / len(test_imgs_names)) * 100))


def train_model(training_folder):
    batch_size = 1
    n_epochs = 20
    tf.random.set_seed(0)
    train_datagen = ImageDataGenerator(rescale=1 / 255)
    train_generator = train_datagen.flow_from_directory(training_folder, target_size=(200, 200),
                                                        batch_size=batch_size, class_mode='categorical')
    total_sample = train_generator.n
    detected_labels = train_generator.class_indices
    detected_labels = {v: k for k, v in detected_labels.items()}

    model = tf.keras.models.Sequential([
        tf.keras.layers.Conv2D(16, (3, 3), activation='relu', input_shape=(200, 200, 3)),
        tf.keras.layers.MaxPooling2D(2, 2),
        tf.keras.layers.Conv2D(32, (3, 3), activation='relu'),
        tf.keras.layers.MaxPooling2D(2, 2),
        tf.keras.layers.Conv2D(64, (3, 3), activation='relu'),
        tf.keras.layers.MaxPooling2D(2, 2),
        tf.keras.layers.Conv2D(64, (3, 3), activation='relu'),
        tf.keras.layers.MaxPooling2D(2, 2),
        tf.keras.layers.Conv2D(64, (3, 3), activation='relu'),
        tf.keras.layers.MaxPooling2D(2, 2),
        tf.keras.layers.Flatten(),
        tf.keras.layers.Dense(128, activation='relu'),
        tf.keras.layers.Dense(6, activation='softmax')
    ])
    model.compile(loss='categorical_crossentropy', optimizer=RMSprop(lr=0.001), metrics=['acc'])
    model.fit(train_generator, steps_per_epoch=int(total_sample / batch_size), epochs=n_epochs, verbose=1)
    model.save('car_classification_model', save_format='h5')
    return model, detected_labels


# Training folder path - it should contain car's photos sorted into appropriate folders e.g. black/blue etc.
train_folder = "cars"
# Testing folder path - it should contain car's photos in a common folder.
# Images names should include car color e.g. black_car_0/yellow_car
test_folder = "cars_test"

if os.path.exists(train_folder):
    model, labels = train_model(train_folder)
else:
    model = tf.keras.models.load_model('car_classification_model')
    labels = {0: 'black', 1: 'blue', 2: 'multi', 3: 'red', 4: 'white', 5: 'yellow'}
predict_images_from_folder(test_folder)
