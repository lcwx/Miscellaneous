import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers
import matplotlib.pyplot as plt
import numpy
import pandas as pd


class PrintDot(keras.callbacks.Callback):
    def on_epoch_end(self, epoch, logs):
        if epoch % 100 == 0:
            print('')
        print('.', end='')


def regression(list_X, list_Y, learning_rate=0.001, EPOCHS=200):
    # Data processing
    dataset = []
    for ele in list_X:
        dataset.append([ele])
    train_labels = []
    for ele in list_Y:
        train_labels.append([ele])
    dataset = numpy.array(dataset)
    train_labels = numpy.array(train_labels)

    # Parameters
    learning_rate = learning_rate
    EPOCHS = EPOCHS

    # Network Parameters
    n_hidden_1 = 8
    n_hidden_2 = 16
    n_hidden_3 = 8
    input_shape = 1
    num_classes = 1

    def build_model(input_shape):
        model = keras.Sequential([
            layers.Dense(n_hidden_1, activation=tf.nn.relu,
                         input_shape=[input_shape]),
            layers.Dense(n_hidden_2, activation=tf.nn.relu),
            layers.Dense(n_hidden_3, activation=tf.nn.relu),
            layers.Dense(num_classes)
        ])

        optimizer = tf.train.RMSPropOptimizer(learning_rate)

        model.compile(loss='mse',
                      optimizer=optimizer,
                      metrics=['mae', 'mse'])
        return model

    model = build_model(input_shape)
    model.summary()

    history = model.fit(
        dataset, train_labels,
        epochs=EPOCHS, validation_split=0.2, verbose=0,
        callbacks=[PrintDot()])

    hist = pd.DataFrame(history.history)
    hist['epoch'] = history.epoch
    hist.tail()

    def plot_history(history):
        plt.figure()
        plt.xlabel('Epoch')
        plt.ylabel('Mean Abs Error [MPG]')
        plt.plot(hist['epoch'], hist['mean_absolute_error'],
                 label='Train Error')
        plt.plot(hist['epoch'], hist['val_mean_absolute_error'],
                 label='Val Error')
        plt.legend()
        plt.ylim([0, 5])
        plt.savefig("1.jpg")

        plt.figure()
        plt.xlabel('Epoch')
        plt.ylabel('Mean Square Error [$MPG^2$]')
        plt.plot(hist['epoch'], hist['mean_squared_error'],
                 label='Train Error')
        plt.plot(hist['epoch'], hist['val_mean_squared_error'],
                 label='Val Error')
        plt.legend()
        plt.ylim([0, 20])
        plt.savefig("2.jpg")

    print()
    plot_history(history)

    # example_result = model.predict(dataset_test[:1])
    # print("\nresult:", example_result)
    shape = numpy.shape(dataset)
    output = []
    for i in range((shape[0])):
        result = model.predict(dataset[i:i+1])
        # print(result[0][0])
        r = result[0][0]
        output.append(r)

    # print(output)
    return output


if __name__ == "__main__":

    list_X = [1, 2, 3]
    list_Y = [2, 5, 6]

    regression(list_X, list_Y)
