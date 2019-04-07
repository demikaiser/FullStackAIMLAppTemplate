from flask import jsonify
import tensorflow as tf


def run():
    hello_world = tf.constant("Hello World from AIML")
    sess = tf.Session()
    result = sess.run(hello_world)

    results = [
        {
            'id': 1,
            'result': result
        }
    ]

    return jsonify({'results': results})
