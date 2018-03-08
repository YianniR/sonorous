import tensorflow as tf
import lib.networks as nn
from lib.classes import MusicalPiece
from pandas import *

def main():
    song = MusicalPiece()
    song.load_song('bach/bwv431.mxl')
    #song.load_song('data\Around The World - Chorus.midi')
    song.make_targets(10)

    # now = datetime.utcnow().strftime("%Y%m%d%H%M%S")
    # root_logdir = "tf_logs"
    # logdir = "{}/run-{}/".format(root_logdir, now)
    #
    # tf.reset_default_graph()
    # n_steps   = 28
    # n_inputs  = 127
    # n_neurons = 150
    # n_outputs = 10
    # learning_rate = 0.001
    # batch_size = 100
    #
    # # Height by Width
    # input_ = tf.placeholder('float',[None,n_steps,n_input_nodes]) #784=28x28
    # target = tf.placeholder('float',[None])
    #
    # data = batch_producer()
    # train_x = data.train.inputs
    # train_y = data.train.targets
    # test_x = data.test.inputs
    # test_y = data.test.targets
    #
    # prediction = nn.rnn_model(input_,n_neurons,n_outputs)
    # nn.train(input_,target,prediction,train_x, train_y, test_x, test_y,batch_size,num_epochs)

if __name__ == "__main__":
    main()
