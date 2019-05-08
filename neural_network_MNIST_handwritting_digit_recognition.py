'''
based on :  http://neuralnetworksanddeeplearning.com/chap1.html
'''

import numpy as np
import matplotlib.pyplot as plt

class Network(object):
    def __init__(self, sizes):
        self.num_layers=len(sizes)
        self.sizes=sizes
        # np.random.seed(0)
        self.bias=[np.random.randn(y,1) for y in sizes[1:]] #eg, for sizes=[2,3,1] y = 2,3 in[2,3], so [3,1] then[1,1], bias is yx1
        self.weights=[np.random.randn(y,x) for x, y in zip(sizes[:-1],sizes[1:])]# weights is YxX, x start from 0 and
        #  y start from 1 layer

        #x=input so stopped before last, y=output so start from 2nd column
        #[3,2] then[1,3], zip makes Y and corresponding W the correct pair
        # [2,3,1] then[y,x]=[3,2], =[y,x] since y = output of product
        #Wjk=out j (last layer) with in k nerons (layer before last), a′=σ(wa+b)



    def update_mini_batch(self, mini_batch, eta):
        """Update the network's weights and biases by applying
        gradient descent using backpropagation to a single mini batch.
        The "mini_batch" is a list of tuples "(x, y)", and "eta"
        is the learning rate."""
        #nabla_b, nabla_w are the sum of dC/db_j, dC/dz_jk so initial to zero
        nabla_b=[np.zeros(b.shape) for b in self.bias]
        nabla_w=[np.zeros(w.shape) for w in self.weights]

        for x, y in mini_batch:
            #calculate nable_b, nable_w for single (x, y)
            delta_nabla_b, delta_nabla_w=self.back_prop(x,y)
            #accumute b for each (x, y) in mini batch
            # play the same "in+zip" trick again for each b, w in different nn layers
            # in: loop over nn layers
            # zip: align to make sure nb, dnb at the same layer
            nabla_b=[nb+dnb for nb, dnb in zip(nabla_b, delta_nabla_b)]
            nabla_w = [nw + dnw for nw, dnw in zip(nabla_w, delta_nabla_w)]

        # again "in + zip" trick to pair the weight and its corresponding nabla_weight
        self.weights=[w-(eta/len(mini_batch))*nw for w,nw in zip(self.weights, nabla_w)]
        self.bias = [b - (eta / len(mini_batch))* nb for b, nb in zip(self.bias, nabla_b)]




    def SGD(self,training_data, epochs, mini_batch_size, eta, test_data=None):
        """
        Train the neural network using mini-batch stochastic
        gradient descent.  The "training_data" is a list of tuples
        "(x, y)" representing the training inputs and the desired
        outputs.  The other non-optional parameters are
        self-explanatory.  If "test_data" is provided then the
        network will be evaluated against the test data after each
        epoch, and partial progress printed out.  This is useful for
        tracking progress, but slows things down substantially.
        
        xrange (in Python 2) was renamed range in Python3
        """
        training_data=list(training_data)
        n = len(training_data)
        if test_data:
            test_data=list(test_data)
            n_test=len(test_data)#test data length

        for j in range(epochs):
            # starts by randomly shuffling the training data,
            np.random.shuffle(training_data)
            # partitions it into mini-batches of the appropriate size
            mini_batches=[training_data[k:k+mini_batch_size]
                          for k in range(0,n,mini_batch_size)]
            # for each mini_batch we apply a single step of gradient descent.
            # This is done by the code self.update_mini_batch(mini_batch, eta),
            # which updates the network weights and biases according to
            # a single iteration of gradient descent,
            # using just the training data in mini_batch
            for mini_batch in mini_batches:
                self.update_mini_batch(mini_batch, eta)
            if test_data:
                print("Epoch {}: {}/{} ".format(j,self.evaluate(test_data),n_test))
            else:
                print("Epoch {} completed!".format(j))


    def feedforward(self, a):
        #zip pairs y and corresponding W, till layer before last
        for b,w in zip(self.bias, self.weights):
            # missed the sigmoid function in 1st try so keep having lower successful rates :(
            a=sigmoid(np.dot(w,a)+b)
        return a

    def back_prop(self, x, y):
        """Return a tuple ``(nabla_b, nabla_w)`` representing the
        gradient for the cost function C_x.  ``nabla_b`` and
        ``nabla_w`` are layer-by-layer lists of numpy arrays, similar
        to ``self.biases`` and ``self.weights``."""
        # length for activations = len of layers
        # len of b, w = layers-1
        nabla_b=[np.zeros(b.shape) for b in self.bias] # all b & w are len(shapes)-1 in
        nabla_w=[np.zeros(w.shape) for w in self.weights]
        # feed forward: record all activations ans zs in one forward pass
        activation=x
        # activations=list to store all the activations, layer by layer
        # add input as first activation
        activations = [x]
        zs = []  # list to store all the z vectors, layer by layer
        for b, w in zip(self.bias, self.weights):

            z=np.dot(w, activation)+b
            zs.append(z)
            activation=sigmoid(z)
            activations.append(activation)

        #backward pass
        # calculate delta_L
        delta = self.cost_derivative(activations[-1], y) * sigmoid_prime(zs[-1])
        #calculate w_jk_L, b_j_L
        nabla_b[-1]=delta
        nabla_w[-1]=np.dot(delta, activations[-2].transpose())
        #back propogate delta
        # Note that the variable l in the loop below is used a little
        # differently to the notation in Chapter 2 of the book.  Here,
        # l = 1 means the last layer of neurons, l = 2 is the
        # second-last layer, and so on.  It's a renumbering of the
        # scheme in the book, used here to take advantage of the fact
        # that Python can use negative indices in lists.

        #range(start, stop, step) is misleading function :(, it goes to before stop guess starts from 0
        # followoing = 2,..., self.num_layers-1
        for l in range(2, self.num_layers):
            z=zs[-l]
            sp=sigmoid_prime(z)
            delta=np.dot(self.weights[-l+1].transpose(), delta)*sp #weight.shape=j,k ->transpose=k,j dot delta.shape=j,1
            nabla_b[-l]=delta
            nabla_w[-l]=np.dot(delta, activations[-l-1].transpose()) #dC/dW_jk=a_k*delta_j so a transposed, delta.shape=j,1, a.shape=k,1
        return (nabla_b, nabla_w)

    def evaluate(self, test_data):
        """Return the number of test inputs for which the neural
        network outputs the correct result. Note that the neural
        network's output is assumed to be the index of whichever
        neuron in the final layer has the highest activation."""
        # create a tuple of numbers (position of max bit position)
        #===========================
        #Attention!!! training_data format (784,1), (10,1), validation and test_data format (784,1), int Y
        #  -- y is interger,  instead of vectorized as in training data
        test_results=[(np.argmax(self.feedforward(x)), y) for x, y in test_data]
        return sum(int(x==y) for x,y in test_results)
    def cost_derivative(self,output_activations, y):
        """Return the vector of partial derivatives \partial C_x /
        \partial a for the output activations."""
        return(output_activations-y)

def sigmoid(x):
    """The sigmoid function."""
    return 1/(1+np.exp(-x))

def sigmoid_prime(x):
    """Derivative of the sigmoid function."""
    return sigmoid(x)*(1-sigmoid(x))

#region MNIST
import pickle
import gzip
import  math
def load_data():
    """Return the MNIST data as a tuple containing the training data,
    the validation data, and the test data.
    The ``training_data`` is returned as a tuple with two entries.
    The first entry contains the actual training images.  This is a
    numpy ndarray with 50,000 entries.  Each entry is, in turn, a
    numpy ndarray with 784 values, representing the 28 * 28 = 784
    pixels in a single MNIST image.
    The second entry in the ``training_data`` tuple is a numpy ndarray
    containing 50,000 entries.  Those entries are just the digit
    values (0...9) for the corresponding images contained in the first
    entry of the tuple.
    The ``validation_data`` and ``test_data`` are similar, except
    each contains only 10,000 images.
    This is a nice data format, but for use in neural networks it's
    helpful to modify the format of the ``training_data`` a little.
    That's done in the wrapper function ``load_data_wrapper()``, see
    below.
    """
    f = gzip.open('mnist.pkl.gz', 'rb')
    training_data, validation_data, test_data = pickle.load(f, encoding="latin1")
    f.close()
    return (training_data, validation_data, test_data)

def load_data_wrapper():
    """Return a tuple containing ``(training_data, validation_data,
    test_data)``. Based on ``load_data``, but the format is more
    convenient for use in our implementation of neural networks.
    In particular, ``training_data`` is a list containing 50,000
    2-tuples ``(x, y)``.  ``x`` is a 784-dimensional numpy.ndarray
    containing the input image.  ``y`` is a 10-dimensional
    numpy.ndarray representing the unit vector corresponding to the
    correct digit for ``x``.
    ``validation_data`` and ``test_data`` are lists containing 10,000
    2-tuples ``(x, y)``.  In each case, ``x`` is a 784-dimensional
    numpy.ndarry containing the input image, and ``y`` is the
    corresponding classification, i.e., the digit values (integers)
    corresponding to ``x``.
    Obviously, this means we're using slightly different formats for
    the training data and the validation / test data.  These formats
    turn out to be the most convenient for use in our neural network
    code."""
    tr_d, va_d, te_d = load_data()
    training_inputs = [np.reshape(x, (784, 1)) for x in tr_d[0]]
    training_results = [vectorized_result(y) for y in tr_d[1]]
    training_data = zip(training_inputs, training_results)
    validation_inputs = [np.reshape(x, (784, 1)) for x in va_d[0]]
    validation_data = zip(validation_inputs, va_d[1])
    test_inputs = [np.reshape(x, (784, 1)) for x in te_d[0]]
    test_data = zip(test_inputs, te_d[1])
    return (training_data, validation_data, test_data)

def vectorized_result(j):
    """Return a 10-dimensional unit vector with a 1.0 in the jth
    position and zeroes elsewhere.  This is used to convert a digit
    (0...9) into a corresponding desired output from the neural
    network."""
    e = np.zeros((10, 1))
    e[j] = 1.0
    return e
#endregion MNIST

#region misc test
def test_display(test_data):
    #disply hand writting number
    i = 0
    for x, y in test_data:
        tnp=x.reshape(28, 28)
        #print(1-(np.ceil(x.reshape(28, 28))).astype(int), y)
        print(y)
        i += 1
        if i > 22:
            break
    fig = plt.figure()
    ax = fig.add_subplot(111)
    i = ax.imshow(tnp, interpolation='nearest')
    fig.colorbar(i)
    plt.show()


#endregion

#main 
training_data, validation_data, test_data = load_data_wrapper()
training_data = list(training_data)

#net=Network([784,30,10])
#net.SGD(training_data,30,10,5.0,test_data=test_data)
#net.evaluate(test_data)
test_display(test_data)
#print(sigmoid(1.5))
