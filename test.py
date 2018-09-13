from biosppy import storage
from biosppy.signals import ecg
from biosppy.signals import bvp
from biosppy.signals import eda
from biosppy.signals import resp
from biosppy.signals import emg
from multiprocessing import Process

# THIS CODE IS MY OWN WORK, IT WAS WRITTEN WITHOUT CONSULTING
# A TUTOR OR CODE WRITTEN BY OTHER STUDENTS - Jie Lin
# Python 3

#coding=utf-8
"""
@version: 1.1
@author: Jie Lin
@Mail: jlin246@emory.edu
@file: test.py
@time: 09/11/2018 12:39am
@purpose: this is a test file to try out different methods in Bioppy
@code environment: ubuntu 18.01
"""


# plot a graph of ecg
def plotEcg(ecgSignal):

    print();
    # to tell user what should be done if they want to continue
    print("plotting the graph. Close the graph windows to continue in order to continue this program");
    # process it and plot
    # signal is equal to raw ecg data, which is passed from main method
    # the rest parameters are set to default
    ecgGraph = ecg.ecg(signal=ecgSignal);


# plot a graph of bvp
def plotBvp(bvpSignal):

    print();
    # to tell user what should be done if they want to continue
    print("plotting the graph. Close the graph windows to continue in order to continue this program");
    # process it and plot
    # signal is equal to bvp data, which is passed from main method
    # the rest parameters are set to default
    bvpGraph = bvp.bvp(signal=bvpSignal);



# plot a graph of eda
def plotEda(edaSignal):

    print();
    # to tell user what should be done if they want to continue
    print("plotting the graph. Close the graph windows to continue in order to continue this program");
    # process it and plot
    # signal is equal to eda data, which is passed from main method
    # the rest parameters are set to default
    edaGraph = eda.eda(signal=edaSignal);


# plot a graph of resp
def plotResp(respSignal):

    print();
    # to tell user what should be done if they want to continue
    print("plotting the graph. Close the graph windows to continue in order to continue this program");
    # process it and plot
    # signal is equal to resp data, which is passed from main method
    # the rest parameters are set to default
    respGraph = resp.resp(signal=respSignal);


# plot a graph of emg
def plotEmg(emgSignal):

    print();
    # to tell user what should be done if they want to continue
    print("plotting the graph. Close the graph windows to continue in order to continue this program");
    # process it and plot
    # signal is equal to emg data, which is passed from main method
    # the rest parameters are set to default
    emgGraph = emg.emg(signal=emgSignal);


#show two emg plotting, for user to compare them easily
def compareEmgs(emgSignal1, emgSignal2):
    print();

    processEmgPlot1 = Process(target=plotEmg, args=(emgSignal1,));
    processEmgPlot2 = Process(target=plotEmg, args=(emgSignal2,));

    #start processes
    processEmgPlot1.start();
    processEmgPlot2.start();

    #join to main process
    processEmgPlot1.join();
    processEmgPlot2.join();


#the main method
if __name__ == '__main__':
    # load raw ECG signal
    # ecgSignal stores the actual ecg data. ecgMdata stores what is commented in the ect.txt
    ecgSignal, ecgMdata = storage.load_txt('./examples/ecg.txt');
    # load raw bvp signal
    bvpSignal, bvpMdata = storage.load_txt('./examples/bvp.txt');
    # load eda signal
    edaSignal, edaMdata = storage.load_txt('./examples/eda.txt');
    # load resp signal
    respSignal, respMdata = storage.load_txt('./examples/resp.txt');

    # load emg signal
    emgSignal1, emgMdata1 = storage.load_txt('./examples/emg.txt');

    # load emg_1 signal
    emgSignal2, emgMdata2 = storage.load_txt('./examples/emg_1.txt');


    #start multi processing, because I want to see both graphs at the same time
    # processEcgPlot = Process(target=plotEcg, args=(ecgSignal,));
    # processBvpPlot = Process(target=plotBvp, args=(bvpSignal,));
    # processEdaPlot = Process(target=plotEda, args=(edaSignal,));
    # processRespPlot = Process(target=plotResp, args=(respSignal,));
    # processEmgPlot1 = Process(target=plotEmg, args=(emgSignal1,));
    # processEmgPlot2 = Process(target=plotEmg, args=(emgSignal2,));
    # #
    # #
    # # #start threads
    # processEcgPlot.start();
    # processBvpPlot.start();
    # processEdaPlot.start();
    # processRespPlot.start();
    # processEmgPlot1.start();
    # processEmgPlot2.start();
    # #
    # # #join thread to the main thread
    # processEcgPlot.join();
    # processBvpPlot.join();
    # processEdaPlot.join();
    # processRespPlot.join();
    # processEmgPlot1.join();
    # processEmgPlot2.join();

    compareEmgs(emgSignal1,emgSignal2);
