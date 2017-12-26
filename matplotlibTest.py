#encoding=utf-8
import numpy as np
import matplotlib as ml
#import scipy
import pandas as pd
#from sklearn.datasets import  load_iris
def main():
    #drive a line
    import matplotlib.pyplot as plt
    x=np.linspace(-np.pi,np.pi,256,endpoint=True)
    c,s=np.cos(x),np.sin(x)
    plt.figure(1)
    plt.plot(x,c)
    plt.plot(x,s)
    plt.grid()
    plt.axis([-1,1,-1,1])
    plt.title("con & sin")

    plt.show()

def andlearn():
    # TODO: Set weight1, weight2, and bias
    weight1 = 9
    weight2 = 12
    bias = -8

    # DON'T CHANGE ANYTHING BELOW
    # Inputs and outputs
    test_inputs = [(0, 0), (0, 1), (1, 0), (1, 1)]
    correct_outputs = [False, False, False, True]
    outputs = []

    # Generate and check output
    for test_input, correct_output in zip(test_inputs, correct_outputs):
        linear_combination = weight1 * test_input[0] + weight2 * test_input[1] + bias
        output = int(linear_combination >= 0)
        is_correct_string = 'Yes' if output == correct_output else 'No'
        outputs.append([test_input[0], test_input[1], linear_combination, output, is_correct_string])

    # Print output
    num_wrong = len([output[4] for output in outputs if output[4] == 'No'])
    output_frame = pd.DataFrame(outputs, columns=['Input 1', '  Input 2', '  Linear Combination', '  Activation Output',
                                                  '  Is Correct'])
    if not num_wrong:
        print('Nice!  You got it all correct.\n')
    else:
        print('You got {} wrong.  Keep trying!\n'.format(num_wrong))
    print(output_frame.to_string(index=False))

def notfeel():
    # TODO: Set weight1, weight2, and bias
    weight1 = 0.0
    weight2 = -0.9
    bias = 0.8

    # DON'T CHANGE ANYTHING BELOW
    # Inputs and outputs
    test_inputs = [(0, 0), (0, 1), (1, 0), (1, 1)]
    correct_outputs = [True, False, True, False]
    outputs = []

    # Generate and check output
    for test_input, correct_output in zip(test_inputs, correct_outputs):

        linear_combination = weight1 * test_input[0] + weight2 * test_input[1] + bias
        print linear_combination >= 0
        output = int(linear_combination >= 0)
        print output
        is_correct_string = 'Yes' if output == correct_output else 'No'
        outputs.append([test_input[0], test_input[1], linear_combination, output, is_correct_string])

    # Print output
    num_wrong = len([output[4] for output in outputs if output[4] == 'No'])
    output_frame = pd.DataFrame(outputs, columns=['Input 1', '  Input 2', '  Linear Combination', '  Activation Output',
                                                  '  Is Correct'])
    if not num_wrong:
        print('Nice!  You got it all correct.\n')
    else:
        print('You got {} wrong.  Keep trying!\n'.format(num_wrong))
    print(output_frame.to_string(index=False))

if __name__ == '__main__':
    notfeel()