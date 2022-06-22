import tensorflow as tf
import sys
import numpy as np
import pdb
import os
from datetime import datetime
import subprocess
from Include.TrainAndTest.create_tf_record import *
import tensorflow.contrib.slim as slim
'''
checkpoint_path=os.path.join('C:/Users/73136/Desktop/models/best_models_204_0.8875.ckpt')
reader=pywrap_tensorflow.NewCheckpointReader(checkpoint_path)
var_to_shape_map=reader.get_variable_to_shape_map()
for key in var_to_shape_map:
    a=reader.get_tensor(key)
    print( 'tensor_name: ',key)
    print("a.shape:%s"%[a.shape])
'''
def net_evaluation(sess,val_images_batch,val_labels_batch,val_nums):
    val_max_steps = int(val_nums / 16)
    print(val_max_steps)
    val_losses = []
    val_accs = []
    val_x, val_y = sess.run([val_images_batch, val_labels_batch])
    print('labels:',val_y)
    #print('labels:', val_y)
        # val_loss = sess.run(loss, feed_dict={x: val_x, y: val_y, keep_prob: 1.0})
        # val_acc = sess.run(accuracy,feed_dict={x: val_x, y: val_y, keep_prob: 1.0})
    val_loss,val_acc = sess.run([loss,accuracy], feed_dict={input_images: val_x, input_labels: val_y, keep_prob:1.0, is_training: False})
    val_losses.append(val_loss)
    val_accs.append(val_acc)
    mean_loss = np.array(val_losses, dtype=np.float32).mean()
    mean_acc = np.array(val_accs, dtype=np.float32).mean()
    return mean_loss, mean_acc

def predict_Origin_V3(path):
    with tf.Session() as sess:
        new_saver = tf.train.import_meta_graph('C:/Users/Administrator/PycharmProjects/Detection/Include/models/Origin/best_models_763_0.8900.ckpt.meta')
        new_saver.restore(sess, tf.train.latest_checkpoint('C:/Users/Administrator/PycharmProjects/Detection/Include/models/Origin'))
        print(sess.run('InceptionV3/AuxLogits/Conv2d_1b_1x1/weights:0'))

        val_record_file = path+'/val256.tfrecords'
        val_images, val_labels = read_records(val_record_file, 256, 256, type='normalization')
        print(val_images, val_labels)
        val_images_batch, val_labels_batch = get_batch_images(val_images, val_labels,
                                                              batch_size=16, labels_nums=2,
                                                              one_hot=True, shuffle=False)
        print(val_images_batch, val_labels_batch)
        mean_loss, mean_acc = net_evaluation(sess,val_images_batch, val_labels_batch, 16)
        return(mean_acc)

def predict_LBP_V3(path):
    with tf.Session() as sess:
        new_saver = tf.train.import_meta_graph('C:/Users/Administrator/PycharmProjects/Detection/Include/models/LBP/best_models_1159_1.0000.ckpt.meta')
        new_saver.restore(sess, tf.train.latest_checkpoint('C:/Users/Administrator/PycharmProjects/Detection/Include/models/LBP'))
        print(sess.run('InceptionV3/AuxLogits/Conv2d_1b_1x1/weights:0'))

        val_record_file = path+'/val256.tfrecords'
        val_images, val_labels = read_records(val_record_file, 256, 256, type='normalization')
        print(val_images, val_labels)
        val_images_batch, val_labels_batch = get_batch_images(val_images, val_labels,
                                                              batch_size=16, labels_nums=2,
                                                              one_hot=True, shuffle=False)
        print(val_images_batch, val_labels_batch)
        mean_loss, mean_acc = net_evaluation(sess,val_images_batch, val_labels_batch, 16)
        return(mean_acc)

def predict_Hog_V3(path):
    with tf.Session() as sess:
        new_saver = tf.train.import_meta_graph('C:/Users/Administrator/PycharmProjects/Detection/Include/models/HOG/best_models_1082_0.8700.ckpt.meta')
        new_saver.restore(sess, tf.train.latest_checkpoint('C:/Users/Administrator/PycharmProjects/Detection/Include/models/HOG'))
        print(sess.run('InceptionV3/AuxLogits/Conv2d_1b_1x1/weights:0'))

        val_record_file = path+'/val256.tfrecords'
        val_images, val_labels = read_records(val_record_file, 256, 256, type='normalization')
        print(val_images, val_labels)
        val_images_batch, val_labels_batch = get_batch_images(val_images, val_labels,
                                                              batch_size=16, labels_nums=2,
                                                              one_hot=True, shuffle=False)
        print(val_images_batch, val_labels_batch)
        mean_loss, mean_acc = net_evaluation(sess,val_images_batch, val_labels_batch, 16)
        return(mean_acc)

def predict_Harr_V3(path):
    with tf.Session() as sess:
        new_saver = tf.train.import_meta_graph('C:/Users/Administrator/PycharmProjects/Detection/Include/models/Harr/best_models_1157_0.8600.ckpt.meta')
        new_saver.restore(sess, tf.train.latest_checkpoint('C:/Users/Administrator/PycharmProjects/Detection/Include/models/Harr'))
        print(sess.run('InceptionV3/AuxLogits/Conv2d_1b_1x1/weights:0'))

        val_record_file = path+'/val256.tfrecords'
        val_images, val_labels = read_records(val_record_file, 256, 256, type='normalization')
        print(val_images, val_labels)
        val_images_batch, val_labels_batch = get_batch_images(val_images, val_labels,
                                                              batch_size=16, labels_nums=2,
                                                              one_hot=True, shuffle=False)
        print(val_images_batch, val_labels_batch)
        mean_loss, mean_acc = net_evaluation(sess,val_images_batch, val_labels_batch, 16)
        return(mean_acc)

def predict_Origin_V1(path):
    with tf.Session() as sess:
        new_saver = tf.train.import_meta_graph('C:/Users/Administrator/PycharmProjects/Detection/Include/models/Harr/best_models_1029_0.9200.ckpt.meta')
        new_saver.restore(sess, tf.train.latest_checkpoint('C:/Users/Administrator/PycharmProjects/Detection/Include/models_v1/Origin'))
        print(sess.run('InceptionV1/AuxLogits/Conv2d_1b_1x1/weights:0'))

        val_record_file = path+'/val256.tfrecords'
        val_images, val_labels = read_records(val_record_file, 256, 256, type='normalization')
        print(val_images, val_labels)
        val_images_batch, val_labels_batch = get_batch_images(val_images, val_labels,
                                                              batch_size=16, labels_nums=2,
                                                              one_hot=True, shuffle=False)
        print(val_images_batch, val_labels_batch)
        mean_loss, mean_acc = net_evaluation(sess,val_images_batch, val_labels_batch, 16)
        return(mean_acc)

def predict_LBP_V1(path):
    with tf.Session() as sess:
        new_saver = tf.train.import_meta_graph('C:/Users/Administrator/PycharmProjects/Detection/Include/models/Harr/best_models_997_0.8300.ckpt.meta')
        new_saver.restore(sess, tf.train.latest_checkpoint('C:/Users/Administrator/PycharmProjects/Detection/Include/models_v1/LBP'))
        print(sess.run('InceptionV1/AuxLogits/Conv2d_1b_1x1/weights:0'))

        val_record_file = path+'/val256.tfrecords'
        val_images, val_labels = read_records(val_record_file, 256, 256, type='normalization')
        print(val_images, val_labels)
        val_images_batch, val_labels_batch = get_batch_images(val_images, val_labels,
                                                              batch_size=16, labels_nums=2,
                                                              one_hot=True, shuffle=False)
        print(val_images_batch, val_labels_batch)
        mean_loss, mean_acc = net_evaluation(sess,val_images_batch, val_labels_batch, 16)
        return(mean_acc)

def predict_Hog_V1(path):
    with tf.Session() as sess:
        new_saver = tf.train.import_meta_graph('C:/Users/Administrator/PycharmProjects/Detection/Include/models/Harr/best_models_1210_0.9000.ckpt.meta')
        new_saver.restore(sess, tf.train.latest_checkpoint('C:/Users/Administrator/PycharmProjects/Detection/Include/models_v1/HOG'))
        print(sess.run('InceptionV1/AuxLogits/Conv2d_1b_1x1/weights:0'))

        val_record_file = path+'/val256.tfrecords'
        val_images, val_labels = read_records(val_record_file, 256, 256, type='normalization')
        print(val_images, val_labels)
        val_images_batch, val_labels_batch = get_batch_images(val_images, val_labels,
                                                              batch_size=16, labels_nums=2,
                                                              one_hot=True, shuffle=False)
        print(val_images_batch, val_labels_batch)
        mean_loss, mean_acc = net_evaluation(sess,val_images_batch, val_labels_batch, 16)
        return(mean_acc)

def predict_Harr_V1(path):
    with tf.Session() as sess:
        new_saver = tf.train.import_meta_graph('C:/Users/Administrator/PycharmProjects/Detection/Include/models/Harr/best_models_1050_0.8800.ckpt.meta')
        new_saver.restore(sess, tf.train.latest_checkpoint('C:/Users/Administrator/PycharmProjects/Detection/Include/models_v1/Harr'))
        print(sess.run('InceptionV1/AuxLogits/Conv2d_1b_1x1/weights:0'))

        val_record_file = path+'/val256.tfrecords'
        val_images, val_labels = read_records(val_record_file, 256, 256, type='normalization')
        print(val_images, val_labels)
        val_images_batch, val_labels_batch = get_batch_images(val_images, val_labels,
                                                              batch_size=16, labels_nums=2,
                                                              one_hot=True, shuffle=False)
        print(val_images_batch, val_labels_batch)
        mean_loss, mean_acc = net_evaluation(sess,val_images_batch, val_labels_batch, 16)
        return(mean_acc)

