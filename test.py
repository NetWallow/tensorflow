from __future__ import print_function
import tensorflow as tf
import numpy as np
"""
#create data
x_data=np.random.rand(100).astype(np.float32)
y_data=x_data*0.1 + 0.3

## structure start ##
Weight=tf.Variable(tf.random_uniform([1], -1.0, 1.0))
biases=tf.Variable(tf.zeros(1))

y=Weight*x_data + biases

loss = tf.reduce_mean(tf.square(y-y_data))
optimizer = tf.train.GradientDescentOptimizer(0.5)

train=optimizer.minimize(loss)
## structure end ##

sess = tf.Session()

if int((tf.__version__).split('.')[1])<12 and int ((tf.__version__).split('.')[0])<1:
    init = tf.initialize_all_variables()
else:
    init=tf.global_variables_initializer()

sess.run(init)

for step in range(201):
    sess.run(train)
    if step % 20 == 0:
        print(step, sess.run(Weight), sess.run(biases))
"""
matrix1 = tf.constant([[3,3]])
matrix2 = tf.constant([[2],
                       [2]])

product = tf.matmul(matrix1, matrix2)

# method 1
sess = tf.Session()
result=sess.run(product)
print(result)
sess.close()

# method 2
with tf.Session() as sess:
    result2 = sess.run(product)
    print(result2)
