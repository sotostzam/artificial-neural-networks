import numpy as np
from random import randrange
import matplotlib.pyplot as plt

class NeuralNetwork:

    # Define the sigmoid function
    def sigmoid(self, x):
        return 1 / (1 + np.exp(-x))

    def sigmoid_derivative(self, x):
         return x * (1 - x)

    # Default Constructor
    def __init__(self, input_nodes, hidden_nodes, output_nodes):
        self.input_nodes  = input_nodes
        self.hidden_nodes = hidden_nodes
        self.output_nodes = output_nodes

        # Randomize weights from input -> hidden and hidden -> output layers
        self.weights_IH = -1 + np.random.rand(self.hidden_nodes, self.input_nodes) * 2
        self.weights_HO = -1 + np.random.rand(self.output_nodes, self.hidden_nodes) * 2

        # Randomize biases from input -> hidden and hidden -> output layers
        self.bias_H = -1 + np.random.rand(self.hidden_nodes, 1) * 2
        self.bias_O = -1 + np.random.rand(self.output_nodes, 1) * 2

        # Define the learning rate
        self.learning_rate = 0.1
        
    # Define Feed forward algorithm
    def feedForward(self, input):
        # Generating the hidden layer
        hidden = np.array(self.weights_IH.dot(input))               # Matrix multiplication between weights of Input to Hidden by the dataset
        hidden = np.add(hidden, self.bias_H)                        # Add the bias to the matrix
        hidden = np.array(list(map(self.sigmoid, hidden)))          # Pass every value of the matrix through the activation function

        # Generating the output layer
        outputs = np.array(self.weights_HO.dot(hidden))              # Matrix multiplication between weights of Hidden to Output by the dataset
        outputs = np.add(outputs, self.bias_O)                       # Add the bias to the matrix
        outputs = np.array(list(map(self.sigmoid, outputs)))         # Pass every value of the matrix through the activation function

        return outputs
        
    # Backpropagation
    def train(self, dataset, targets):
        # Generating the hidden layer
        hidden = np.array(self.weights_IH.dot(dataset))                         # Matrix multiplication between weights of Input to Hidden by the dataset
        hidden = np.add(hidden, self.bias_H)                                    # Add the bias to the matrix
        hidden = np.array(list(map(self.sigmoid, hidden)))                      # Pass every value of the matrix through the activation function

        # Generating the output layer
        outputs = np.array(self.weights_HO.dot(hidden))                         # Matrix multiplication between weights of Hidden to Output by the dataset
        outputs = np.add(outputs, self.bias_O)                                  # Add the bias to the matrix
        outputs = np.array(list(map(self.sigmoid, outputs)))                    # Pass every value of the matrix through the activation function

        # Calculate output layer errors
        output_errors = np.array(targets - outputs)

        # Calculate the gradient of the output layer errors
        gradients = np.array(list(map(self.sigmoid_derivative, outputs)))       # Find the derivative of sigmoid (Already applied - Check sigmoid_derivative function)
        gradients = np.multiply(gradients, output_errors)
        gradients = np.multiply(gradients, self.learning_rate)
        self.bias_O = np.add(self.bias_O, gradients)                            # Adjust the bias

        # Calculate Hidden -> Output Deltas
        weights_HO_D = gradients.dot(hidden.T)                                  # Multiply the gradient vector by the hidden output transposed
        self.weights_HO = np.add(self.weights_HO, weights_HO_D)                 # Add the computed Deltas to the Hidden -> Output weights

        # Calculate hidden layer errors
        hidden_errors = self.weights_HO.T.dot(output_errors)

        # Calculate the gradient of the hidden layer errors
        gradients_hid = np.array(list(map(self.sigmoid_derivative, hidden)))    # Find the derivative of sigmoid (Already applied - Check sigmoid_derivative function)
        gradients_hid = np.multiply(gradients_hid, hidden_errors)
        gradients_hid = np.multiply(gradients_hid, self.learning_rate)
        self.bias_H = np.add(self.bias_H, gradients_hid)                        # Adjust the bias

        # Calculate Input -> Hidden Deltas
        weights_IH_D = gradients_hid.dot(dataset.T)                             # Multiply the gradient vector by the input transposed
        self.weights_IH = np.add(self.weights_IH, weights_IH_D)                 # Add the computed Deltas to the Input -> Hidden weights

        return hidden_errors

    def showWeights(self):
        print("\nInput -> Hidden weights:\n" + str(self.weights_IH))
        print("\nHidden -> Output weights:\n" + str(self.weights_HO))

def train_mlp(epochs = 1000, plot = True, update = 1000):
    # Train the neural network on the data feeding it random values each time
    for i in range(0, epochs + 1):
        randomPick = randrange(4)
        mlp.train(np.array([[test_input[randomPick][0]],[test_input[randomPick][1]]]), targets[randomPick])

        if i % update == 0:
            print("Training... " + str(int((i/epochs)*100)) + " %")
            if plot:  
                # Plotting of classes and the line separating the two
                x_range = np.linspace(-.5, 1.5, endpoint = True)

                #y_intercept_g   = - 1 * (mlp.bias_O[0][0] / mlp.weights_HO[0][1]) - 1 * (mlp.weights_HO[0][0] / mlp.weights_HO[0][1]) * x_range
                y_intercept_1   = - 1 * (mlp.bias_H[0][0] / mlp.weights_IH[0][1]) - 1 * (mlp.weights_IH[0][0] / mlp.weights_IH[0][1]) * x_range
                y_intercept_2   = - 1 * (mlp.bias_H[1][0] / mlp.weights_IH[1][1]) - 1 * (mlp.weights_IH[1][0] / mlp.weights_IH[1][1]) * x_range

                plt.clf()
                plt.title('Neural Network is training...')
                plt.scatter(1, 1, c='red')
                plt.scatter(0, 0, c='red')
                plt.scatter(0, 1, c='blue')
                plt.scatter(1, 0, c='blue')
                #plt.plot(x_range, y_intercept_g, linewidth=1, color='green', label='Output Neuron')
                plt.plot(x_range, y_intercept_1, linewidth=1, color='red',   label='Hidden Neuron 1')
                plt.plot(x_range, y_intercept_2, linewidth=1, color='blue',  label='Hidden Neuron 2')
                plt.fill_between(x = x_range, y1 = y_intercept_1, y2 = y_intercept_2, alpha=.2, color='blue')
                plt.xlim(-.5, 1.5)
                plt.ylim(-.5, 1.5)
                plt.legend(loc='upper right', prop={'size': 8})
                plt.pause(0.01)

# Dataset arrays to train the neural network uppon 
test_input = np.array([[0, 0],
                       [0, 1],
                       [1, 0],
                       [1, 1]])

targets = np.array([[0],
                    [1],
                    [1],
                    [0]])

if __name__ == "__main__":
    # Create a neural network of 2 inputs, 2 hidden, and 1 output nodes
    mlp = NeuralNetwork(2, 2, 1)

    # Train network by passing it the dataset values randomly
    train_mlp(epochs = 50000, plot = True, update = 2000)

    # Let the neural network have a guess
    print("\nXOR Gate check:")
    print(str(test_input[0]) + " -> " + str(mlp.feedForward(np.array([[0], [0]]))[0]))      # Should be number close to 0
    print(str(test_input[1]) + " -> " + str(mlp.feedForward(np.array([[0], [1]]))[0]))      # Should be number close to 1
    print(str(test_input[2]) + " -> " + str(mlp.feedForward(np.array([[1], [0]]))[0]))      # Should be number close to 1
    print(str(test_input[3]) + " -> " + str(mlp.feedForward(np.array([[1], [1]]))[0]))      # Should be number close to 0

    # mlp.showWeights()
    plt.show()