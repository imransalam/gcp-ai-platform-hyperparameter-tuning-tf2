
import argparse
import hypertune
import tensorflow as tf

# LOAD DATASET
dataset = tf.keras.datasets.boston_housing
(x_train, y_train), (x_val, y_val) = dataset.load_data()


class LinearRegression(tf.keras.Model): # Subclass from tf.keras.model
    def __init__(self): # Define All your Variables Here. And other configurations
        super(LinearRegression, self).__init__()
        self.dense = tf.keras.layers.Dense(1)
    
    def call(self, x): # Use the variables defined here.... this is forward prop
        return self.dense(x)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Input parameters need to be Specified for hypertuning')
    parser.add_argument('--epochs', default=10, type=int, help='Number of Epochs Specified')
    parser.add_argument('--lr', default=0.003, type=float, help='Learning rate parameter')
    args = parser.parse_args()
    epochs = args.epochs
    lr = args.lr

    model = LinearRegression()
    adam = tf.keras.optimizers.Adam(learning_rate=lr)
    model.compile(loss='mse', optimizer=adam)
    model.fit(x_train, y_train, epochs=epochs, verbose=0)
    loss = model.evaluate(x_val, y_val) / x_val.shape[0]
    print(loss)

    hpt = hypertune.HyperTune()
    hpt.report_hyperparameter_tuning_metric(hyperparameter_metric_tag='loss', metric_value=loss, global_step=epochs)