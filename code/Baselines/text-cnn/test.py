import tensorflow as tf
import numpy as np
from sklearn.model_selection import train_test_split
# import xlwt
import json

def test(x_test_head, y_test, model):

    checkpoint_file = model

    graph = tf.Graph()
    with graph.as_default():
        session_conf = tf.compat.v1.ConfigProto(
            allow_soft_placement=True,
            log_device_placement=False)
        sess = tf.compat.v1.Session(config=session_conf)

        with sess.as_default():
            # Initialize all variables
            sess.run(tf.compat.v1.global_variables_initializer())

            saver = tf.compat.v1.train.import_meta_graph("{}.meta".format(checkpoint_file))
            saver.restore(sess, checkpoint_file)

            predictions = graph.get_operation_by_name("loss/predictions").outputs[0]
            accuracy = graph.get_operation_by_name("loss/accuracy").outputs[0]
            input_head = graph.get_operation_by_name("input_headline").outputs[0]
            input_y = graph.get_operation_by_name("input_y").outputs[0]

            dropout_keep_prob = graph.get_operation_by_name("dropout_keep_prob").outputs[0]
            batch_size = graph.get_operation_by_name("batch_size").outputs[0]


            all_predictions_fake, acc_fake  = \
                sess.run([predictions, accuracy], feed_dict={input_head: x_test_head,
                                                            input_y: y_test,
                                                            dropout_keep_prob: 1.0,
                                                            batch_size: len(y_test)})

            predictionss_click = tf.convert_to_tensor(all_predictions_fake)
            actuals_click = tf.argmax(y_test, 1)

            #  ----------------------------------------------------------------

            # for clickbait detection
            actuals = actuals_click
            predictionss = predictionss_click

            ones_like_actuals = tf.ones_like(actuals)
            zeros_like_actuals = tf.zeros_like(actuals)
            ones_like_predictions = tf.ones_like(predictionss)
            zeros_like_predictions = tf.zeros_like(predictionss)

            tp_op = tf.reduce_sum(
                tf.cast(
                    tf.logical_and(
                        tf.equal(actuals, ones_like_actuals),
                        tf.equal(predictionss, ones_like_predictions)
                    ),
                    "float"
                )
            )

            tn_op = tf.reduce_sum(
                tf.cast(
                    tf.logical_and(
                        tf.equal(actuals, zeros_like_actuals),
                        tf.equal(predictionss, zeros_like_predictions)
                    ),
                    "float"
                )
            )

            fp_op = tf.reduce_sum(
                tf.cast(
                    tf.logical_and(
                        tf.equal(actuals, zeros_like_actuals),
                        tf.equal(predictionss, ones_like_predictions)
                    ),
                    "float"
                )
            )

            fn_op = tf.reduce_sum(
                tf.cast(
                    tf.logical_and(
                        tf.equal(actuals, ones_like_actuals),
                        tf.equal(predictionss, zeros_like_predictions)
                    ),
                    "float"
                )
            )

            tp, tn, fp, fn = sess.run([tp_op, tn_op, fp_op, fn_op])


            tpr = float(tp) / (float(tp) + float(fn) + 1e-4)

            accuracy = (float(tp) + float(tn)) / (float(tp) + float(fp) + float(fn) + float(tn))
            print('Clickbait: ')
            print('ACC. = ' + str(accuracy))

            precision = float(tp) / (float(tp) + float(fp) + 1e-4)
            print('precision = ' + str(precision))

            recall = tpr
            print('recall = ' + str(recall))

            f1_score = (2 * (precision * recall)) / (precision + recall + 1e-4)
            print('f1_score = ' + str(f1_score))

            print('tp:' + str(tp))
            print("tn: " + str(tn))
            print('fp:' + str(fp))
            print("fn: " + str(fn))

            return [accuracy, precision, recall, f1_score, tp, tn, fp, fn, all_predictions_fake]


if __name__ == '__main__':
    print('===============================================')
    print('load vectors and labels ... ')

    with open('～/text-cnn/dic_embedding.json', 'r') as f:
        dic = json.load(f)

    x_head = []
    y = []
    y_single = []
    key_list = []
    for key, value in dic.items():
        tmp = []
        tmp = [float(i) for j in value['title'] for i in j]
        tmp = np.array(tmp).reshape((-1, 300))
        x_head.append(tmp)


        if value['reliability'] == '1':
            y.append([1, 0])
            y_single.append(1)
        else:
            y.append([0, 1])
            y_single.append(0)
        key_list.append(key)


    x_head = np.array(x_head)
    y = np.array(y)
    y_single = np.array(y_single)


    outdir = '～/text-cnn'
    key_list = np.array(key_list)

    print('split training set and test set ... ')
    x_head_train, x_head_test, y_train, y_test = train_test_split(x_head, y, test_size=0.2, random_state=4)

    key_train, key_test, y_single_train, y_single_test = train_test_split(key_list, y_single, test_size=0.2, random_state=4)



    modelfolder = '～/text-cnn/ckp/'

    print('===============================================')
    print('test......')

    dic_all = {}

    ''' TO FIND OUT THE CKP WITH THE BEST PERFORMANCE '''
    for i in range(1, 63):

        ckp_index = 10 * i
        model = modelfolder + str(ckp_index)
        print('test model : ' + model)
        acc, pre, rec, f1, tp, tn, fp, fn, all_predictions_fake = test(x_head_test, x_body_test, x_image_test, y_test, model)
        
        tmp = {}
        tmp['acc'] = str(acc)
        tmp['pre'] = str(pre)
        tmp['rec'] = str(rec)
        tmp['f1'] = str(f1)
        tmp['tp'] = str(tp)
        tmp['tn'] = str(tn)
        tmp['fp'] = str(fp)
        tmp['fn'] = str(fn)
        tmp['ground'] = y_test.tolist()
        tmp['prediction'] = all_predictions_fake.tolist()

        dic_all[str(ckp_index)] = tmp

    with open('～/text-cnn/prediction_result_simple_text.json', 'w') as f:
        json.dump(dic_all, f)