import abc
import numpy as np

'''
abc - Abstract Base Classes, this module provides the infrastructure for
    defining abstract base classes in Python

numpy - NumPy is a library for the Python programming language, adding support
    for large, multi-dimensional arrays and matrices, along with a large collection
    of high-level mathematical functions to operate on these arrays.
'''


class BaseDetector(object):

    @abc.abstractmethod
    def __init__(self):
        '''
        @abc.abstractmethod : The subclass must define this function
        '''
        pass

    @abc.abstractmethod
    def detect(self, ts, label = None):
        '''
        @abc.abstractmethod : The subclass must define this function
        :param ts: Time series
        :param label: Ignored in unsupervised methods
        :return: Detected result
        '''
        pass