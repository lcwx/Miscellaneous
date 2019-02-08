import tensorflow as tf
# from tensorflow.python.client import device_lib
import numpy as np
import random
import time
import os

os.environ["CUDA_VISIBLE_DEVICES"]="-1"
# print(device_lib.list_local_devices())

matrix1 = np.array([])
matrix2 = np.array([])

for i in range(1000):
    matrix1 = np.append(matrix1, [random.randint(20, 600)
                                  for i in range(1000)])
    matrix2 = np.append(matrix2, [random.randint(1, 500) for i in range(1000)])

matrix1 = matrix1.reshape(100, 100, 100)
matrix2 = matrix2.reshape(100, 100, 100)
# matrix2 = tf.matrix_diag(matrix2)

# print(matrix1)
# print(matrix2)
# with tf.device('/cpu:0'):
with tf.Session() as sess:
    m1 = tf.convert_to_tensor(matrix1)
    m2 = tf.convert_to_tensor(matrix2)
    out_ = tf.matrix_diag(matrix2)
    # print(out_)

    out = tf.multiply(m1, m2)
    t1 = time.clock()
    for i in range(10000):
        # print(sess.run(out))
        # out = tf.multiply(m1, m2)
        # matrix2 = tf.matrix_diag(matrix2)
        sess.run(out)
        # sess.run(out_)
        if i % 1000 == 0:
            print("#############")
    t2 = time.clock()
    t = t2 - t1
    print(t)
    print("Time used: %.3f" % (t))
