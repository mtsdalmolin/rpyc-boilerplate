import rpyc
from rpyc.utils.server import ThreadedServer


class TFService(rpyc.Service):
  def exposed_train(self):
    import tensorflow as tf
    mnist = tf.keras.datasets.mnist

    (x_train, y_train), (x_test, y_test) = mnist.load_data()
    x_train, x_test = x_train / 255.0, x_test / 255.0

    model = tf.keras.models.Sequential([
      tf.keras.layers.Flatten(input_shape=(28, 28)),
      tf.keras.layers.Dense(128, activation='relu'),
      tf.keras.layers.Dropout(0.2),
      tf.keras.layers.Dense(10, activation='softmax')
    ])

    model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])

    model.fit(x_train, y_train, epochs=5)

    model.save('/tmp/trained_model.h5')
    return 'saved model'

  def exposed_load(self):
    import tensorflow as tf
    loaded_model = tf.keras.models.load_model('/tmp/trained_model.h5')
    loaded_model.summary()
    return 'loaded model'


if __name__ == "__main__":
  rpyc.lib.setup_logger()
  server = ThreadedServer(TFService, port=12345, backlog=10, protocol_config=rpyc.core.protocol.DEFAULT_CONFIG)
  server.start()