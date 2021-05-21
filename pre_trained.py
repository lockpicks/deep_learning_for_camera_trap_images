# https://www.tensorflow.org/api_docs/python/tf/compat/v1/train/import_meta_graph

import tensorflow.compat.v1 as tf

with tf.Session() as sess:
    saver = tf.train.import_meta_graph('./snapshot-55.meta')
    saver.restore(sess, "./snapshot-55")
    train_op = tf.get_collection('train_op')[0]
    print(train_op)
    
    '''
    for step in range(100):
        print("running...")
        sess.run(train_op)
    '''