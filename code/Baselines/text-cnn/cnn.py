import tensorflow as tf
import numpy as np
# import tensorlayer as tl
# from tensorlayer.models.imagenet_classes import class_names

class Graph:
    def __init__(self, head_size, l2_reg_lambda=3.0,
                 input_len=32, final_len=200, embedding_len=300,
                 lr=5e-4, num_filters=256):


        # Placeholders for input, output and dropout
        self.input_headline__ = tf.compat.v1.placeholder(tf.float64, shape=[None, head_size, embedding_len], name='input_headline')
        self.input_y_ = tf.compat.v1.placeholder(tf.float64, shape=[None, 2], name='input_y')

        self.input_headline_ = tf.reshape(self.input_headline__, [-1, embedding_len])
        self.input_y = tf.reshape(self.input_y_, [-1, 2])

        # transform input data
        W_trans = tf.Variable(tf.compat.v1.truncated_normal([int(embedding_len), int(input_len)],\
                                stddev=0.1, dtype=tf.float64), dtype=tf.float64)
        bias_trans = tf.Variable(tf.constant(0.1, shape=[int(input_len)], dtype=tf.float64), dtype=tf.float64)
        self.input_headline = tf.matmul(self.input_headline_, W_trans) + bias_trans

        self.dropout_keep_prob = tf.compat.v1.placeholder(tf.float64, name='dropout_keep_prob')
        self.batch_size = tf.compat.v1.placeholder(tf.int64, shape=[], name='batch_size')
        self.dtype = tf.float64
        self.filter_sizes = [3, 4]
        self.num_filters = num_filters
        self.final_len = int(final_len)

        # -------------- headline convolution layers --------------
        with tf.compat.v1.variable_scope("convolutions_head", dtype=self.dtype) as scope:
            #  max - pool
            pooled_outputs_head = []
            for filter_size in self.filter_sizes:
                with tf.compat.v1.variable_scope(f"conv-maxpool-{filter_size}-filter-head"):
                    temp = tf.reshape(self.input_headline, [self.batch_size, int(head_size), input_len, 1])
                    conv_h = tf.compat.v1.layers.conv2d(temp, self.num_filters, (filter_size, input_len), activation=tf.nn.relu)
                    pool_h = tf.compat.v1.layers.max_pooling2d(conv_h, (head_size - filter_size + 1, 1), (1, 1))
                    pooled_outputs_head.append(pool_h)

            num_total_filters = self.num_filters * len(self.filter_sizes)
            concat_pooled_head = tf.concat(pooled_outputs_head, 3)
            flat_pooled_head = tf.reshape(concat_pooled_head, [-1, int(num_total_filters)])

            h_dropout_head = tf.compat.v1.layers.dropout(flat_pooled_head, self.dropout_keep_prob)

        with tf.compat.v1.variable_scope("fully-connected_head", dtype=self.dtype) as scope:
            headline_vector = tf.compat.v1.layers.dense(h_dropout_head, self.final_len)


        with tf.compat.v1.name_scope("prediction"):
            vector = tf.concat([headline_vector], 1)
            W = tf.Variable(tf.compat.v1.truncated_normal([self.final_len * 1, 2], stddev=0.1, dtype=tf.float64),
                            dtype=tf.float64)
            bias = tf.Variable(tf.constant(0.1, shape=[2], dtype=tf.float64), dtype=tf.float64)
            y_pre = tf.nn.softmax(tf.matmul(vector, W) + bias)


        with tf.compat.v1.name_scope('loss'):
            self.loss1 = -tf.reduce_mean(tf.reduce_sum(self.input_y * tf.compat.v1.log(y_pre), axis=1))
            self.loss2 = -tf.reduce_mean(tf.reduce_sum(self.input_y * tf.compat.v1.log(self.cos), axis=1))

            alpha = tf.constant(0.5, dtype=tf.float64, name='alpha')
            beta = tf.constant(0.5, dtype=tf.float64, name='beta')

            # self.loss = alpha * self.loss1 + beta * self.loss2
            self.loss = self.loss1
            loss_summary = tf.summary.scalar('loss', self.loss)

            self.train_op = tf.compat.v1.train.AdamOptimizer(lr).minimize(self.loss)

            self.predictions = tf.argmax(y_pre, 1, name='predictions')
            self.correct_prediction = tf.equal(tf.argmax(y_pre, 1), tf.argmax(self.input_y, 1))
            self.accuracy = tf.reduce_mean(tf.cast(self.correct_prediction, "float"), name='accuracy')
            fake_acc_summary = tf.summary.scalar("acc", self.accuracy)

        self.merged = tf.compat.v1.summary.merge_all()



class vggGraph_test:
    def __init__(self, lr=5e-4, num_filters=256, final_len=200):

        # Placeholders for input, output and dropout
        self.input_image = tf.compat.v1.placeholder(tf.float32, shape=[None, 1000], name='input_image')
        self.input_y = tf.compat.v1.placeholder(tf.float32, shape=[None, 2], name='input_y')

        self.dropout_keep_prob = tf.compat.v1.placeholder(tf.float64, name='dropout_keep_prob')
        self.batch_size = tf.compat.v1.placeholder(tf.int64, shape=[], name='batch_size')
        self.dtype = tf.float32
        self.filter_sizes = [3, 4]
        self.num_filters = num_filters
        self.final_len = int(final_len)


        with tf.name_scope("prediction"):
            vector = self.input_image
            W = tf.Variable(tf.compat.v1.truncated_normal([1000, 2], stddev=0.1, dtype=tf.float32),
                            dtype=tf.float32)
            bias = tf.Variable(tf.constant(0.1, shape=[2], dtype=tf.float32), dtype=tf.float32)
            y_pre = tf.nn.softmax(tf.matmul(vector, W) + bias)

        with tf.name_scope('loss'):
            self.loss1 = -tf.reduce_mean(tf.reduce_sum(self.input_y * tf.compat.v1.log(y_pre), axis=1))
            self.loss2 = -tf.reduce_mean(tf.reduce_sum(self.input_y * tf.log(self.cos), axis=1))

            self.loss = 0.6 * self.loss1 + 0.4 * self.loss2
            loss_summary = tf.summary.scalar('loss', self.loss)

            self.train_op = tf.compat.v1.train.AdamOptimizer(lr).minimize(self.loss)

            self.predictions = tf.argmax(y_pre, 1, name='predictions')
            self.correct_prediction = tf.equal(tf.argmax(y_pre, 1), tf.argmax(self.input_y, 1))
            self.accuracy = tf.reduce_mean(tf.cast(self.correct_prediction, "float"), name='accuracy')
            fake_acc_summary = tf.summary.scalar("acc", self.accuracy)

        self.merged = tf.compat.v1.summary.merge_all()