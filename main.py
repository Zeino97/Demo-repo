import tensorflow as tf


print(f'Number of available GPUs: {tf.config.list_physical_devices("GPU")}')


