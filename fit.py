from model import *
from dataset import *
from sklearn.model_selection import train_test_split
from keras.preprocessing.image import ImageDataGenerator
from keras.utils import to_categorical
from history import *

def fit(X, y):
    y = to_categorical(y)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=42)
    data_generator = ImageDataGenerator(
        featurewise_center=False,
        featurewise_std_normalization=False,
        rotation_range=10,
        width_shift_range=0.1,
        height_shift_range=0.1,
        zoom_range=.1,
        horizontal_flip=True)

    history=model.fit_generator(data_generator.flow(X_train, y_train, BATCH_SIZE),
                        steps_per_epoch=len(X_train) / BATCH_SIZE,
                        epochs=EPOCHS, verbose=True,
                        validation_data=(X_test, y_test))

    return history

if __name__ == "__main__":
    try:

        X, y = load_data(categories)
        print('X.shape:', X.shape)
        print('y.shape:', y.shape)
        history=fit(X, y)
        plot_history(history,RESULT_PATH)
        save_history(history,RESULT_PATH)
    finally:
        save_model()
