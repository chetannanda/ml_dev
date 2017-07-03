# This program explains the basics of tensor flow library
# This implement computational graph for addition of two numbers

# @ author - Chetan Nanda 

import tensorflow as tf

# Create two placeholders
a = tf.placeholder(tf.int32)
b = tf.placeholder(tf.int32)

# Define node for addition
adder = tf.add(a, b)

# Define a node for initializer
init = tf.initialize_all_variables()

# Create a new session and run the computation graaph
with tf.Session() as sess:
    # Run the init node
    sess.run(init)

    # Run the adder node, with values in placeholder
    print 'Adder output', sess.run(adder, feed_dict={a: 5, b: 12})

sess.close()
