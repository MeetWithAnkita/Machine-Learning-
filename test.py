import os
os.environ['TF_ENABLE_ONEDNN_OPTS'] = '0'
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'  # Suppress warnings and info logs
import tensorflow as tf

hello = tf.constant("Hello World !")
output = hello.numpy()
print(output.decode())