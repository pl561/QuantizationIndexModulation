"""Implementation of QIM method from Data Hiding Codes, Moulin and Koetter, 2005"""

from __future__ import print_function
import sys
import os
HOME = os.environ["HOME"]

import numpy as np


class QIM:
    def __init__(self, delta):
        self.delta = delta

    def embed(self, x, m):
        """
        x is a vector of values to be quantized individually
        m is a binary vector of bits to be embeded
        returns: a quantized vector y
        """
        x = x.astype(float)
        d = self.delta
        y = np.round(x/d) * d + (-1)**(m+1) * d/4.
        return y

    def detect(self, z):
        """
        z is the received vector, potentially modified
        returns: a detected vector z_detected and a detected message m_detected
        """

        shape = z.shape
        z = z.flatten()

        m_detected = np.zeros_like(z, dtype=float)
        z_detected = np.zeros_like(z, dtype=float)

        z0 = self.embed(z, 0)
        z1 = self.embed(z, 1)

        d0 = np.abs(z - z0)
        d1 = np.abs(z - z1)

        gen = zip(range(len(z_detected)), d0, d1)
        for i, dd0, dd1 in gen:
            if dd0 < dd1:
                m_detected[i] = 0
                z_detected[i] = z0[i]
            else:
                m_detected[i] = 1
                z_detected[i] = z1[i]


        z_detected = z_detected.reshape(shape)
        m_detected = m_detected.reshape(shape)
        return z_detected, m_detected.astype(int)

    def random_msg(self, l):
        """
        returns: a random binary sequence of length l
        """
        return np.random.choice((0, 1), l)


def test_qim():
    """
    tests the embed and detect methods of class QIM
    """
    l = 10000 # binary message length
    delta = 8 # quantization step
    qim = QIM(delta)

    while True:
        x = np.random.randint(0, 255, l).astype(float) # host sample


        msg = qim.random_msg(l)
        y = qim.embed(x, msg)
        z_detected, msg_detected = qim.detect(y)

        print(x)
        print(y)
        print(z_detected)

        print(msg)
        print(msg_detected)
        assert np.allclose(msg, msg_detected) # compare the original and detected messages
        assert np.allclose(y, z_detected)     # compare the original and detected vectors


def main():
    test_qim()


if __name__ == "__main__":
    sys.exit(main())
