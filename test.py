from biosppy import storage
from biosppy.signals import ecg
from biosppy.signals import bvp

# THIS CODE IS MY OWN WORK, IT WAS WRITTEN WITHOUT CONSULTING
# A TUTOR OR CODE WRITTEN BY OTHER STUDENTS - Jie Lin
# Python 3

#coding=utf-8
"""
@version: 1.0
@author: Jie Lin
@Mail: jlin246@emory.edu
@file: test.py
@time: 09/11/2018 12:39am
"""

#the main method
if __name__ == '__main__':
    # load raw ECG signal
    signal, mdata = storage.load_txt('./examples/ecg.txt')

    # process it and plot
    out = ecg.ecg(signal=signal, sampling_rate=1000., show=True)

    # do something interesting to out
