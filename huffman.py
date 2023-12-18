import numpy as np
import math

# calculate the Bernoulli probability of each codeword
def Bprob(n, p):
    P = np.zeros(pow(2, n))
    for i in range(pow(2, n)):
        one = str(bin(i)).count('1')
        P[i] = pow(p, one) * pow(1-p, n-one)
    return P

# calculate the Poisson probability of each codeword
def Pprob(k, lamda):
    P = np.zeros(k)
    for i in range(k):
        P[i] = pow(lamda, i) * np.exp(-lamda) / math.factorial(i)
    return P

def H(P):
    return np.sum(-P*np.log2(P))

def huffmancode(P):
    P_sort = np.sort(P)
    codebook = [''] * len(P)
    idx = [i for i in range(len(P))]
    while len(idx) > 2:
        # add the two smallest probability
        p_add = P_sort[0] + P_sort[1]
        idx_add = [idx[0], idx[1]]
        idx = idx[2:]
        P_sort = np.sort(np.insert(P_sort[2:], 0, p_add))
        idx_new = np.where(P_sort == p_add)
        idx_new = int(idx_new[0][0])
        idx = idx[:idx_new] + [idx_add] + idx[idx_new:]

    # huffman code
    coding(idx, codebook, '')
    return codebook

def coding(idx, codebook, char):
    if type(idx) != list or len(idx) == 1:
        codebook[idx] = codebook[idx] + char
    else:
        coding(idx[0], codebook, char + '0')
        coding(idx[1], codebook, char + '1')

if __name__ == '__main__':
    n = int(input('input the length of serial:'))
    p = float(input('input [ the probability of 1 ]/[ lamda ]:'))
    P = Pprob(n, p)
    huffcode = huffmancode(P)
    print('Huffman code is:', huffcode)
    print('The average code length is:', np.dot(P, [len(i) for i in huffcode]))
    print('The ideal code length is:', H(P))