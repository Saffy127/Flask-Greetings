import numpy as np

class NeuralNetwork:
    def __init__(self, input_nodes, hidden_nodes, output_nodes):
        self.input_nodes = input_nodes
        self.hidden_nodes = hidden_nodes
        self.output_nodes = output_nodes
        
        self.weights_ih = np.random.randn(hidden_nodes, input_nodes)
        self.weights_ho = np.random.randn(output_nodes, hidden_nodes)
        self.bias_h = np.random.randn(hidden_nodes, 1)
        self.bias_o = np.random.randn(output_nodes, 1)
        
        self.learning_rate = 0.1

    def sigmoid(self, x):
        return 1 / (1 + np.exp(-x))

    def sigmoid_derivative(self, x):
        return x * (1 - x)

    def feedforward(self, inputs):
        inputs = np.array(inputs).reshape(-1, 1)
        hidden = np.dot(self.weights_ih, inputs) + self.bias_h
        hidden_activated = self.sigmoid(hidden)
        output = np.dot(self.weights_ho, hidden_activated) + self.bias_o
        output_activated = self.sigmoid(output)

        return output_activated

    def train(self, inputs, targets):
        inputs = np.array(inputs).reshape(-1, 1)
        targets = np.array(targets).reshape(-1, 1)

        hidden = np.dot(self.weights_ih, inputs) + self.bias_h
        hidden_activated = self.sigmoid(hidden)
        output = np.dot(self.weights_ho, hidden_activated) + self.bias_o
        output_activated = self.sigmoid(output)

        output_errors = targets - output_activated
        output_gradient = self.sigmoid_derivative(output_activated)
        output_deltas = output_errors * output_gradient

        hidden_errors = np.dot(self.weights_ho.T, output_deltas)
        hidden_gradient = self.sigmoid_derivative(hidden_activated)
        hidden_deltas = hidden_errors * hidden_gradient

        self.weights_ho += self.learning_rate * np.dot(output_deltas, hidden_activated.T)
        self.weights_ih += self.learning_rate * np.dot(hidden_deltas, inputs.T)

        self.bias_o += self.learning_rate * output_deltas
        self.bias_h += self.learning_rate * hidden_deltas

# XOR problem dataset
inputs = [
    [0, 0],
    [0, 1],
    [1, 0],
    [1, 1]
]
targets = [
    [0],
    [1],
    [1],
    [0]
]

# Create and train the neural network
nn = NeuralNetwork(2, 2, 1)
epochs = 10000

for epoch in range(epochs):
    for i in range(len(inputs)):
        nn.train(inputs[i], targets[i])

# Test the neural network
for i in range(len(inputs)):
    print(f"Input: {inputs[i]} -> Output: {nn.feedforward(inputs[i])}")
