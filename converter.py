#!/usr/bin/env python3

import sys
import wave
import array
from subprocess import call

def convert(filename):

    csv = open(filename, 'r')
    data = csv.read().splitlines()

    rawdata = []

    for i in range(8):
        rawdata.append( array.array('h') )

    for line in data:
        if line:
            fields = line.split(';')
            for i in range(8):
                rawdata[i].append( int(fields[i]) )

    return rawdata

def create_params():

    nchannels = 1
    sampwidth = 2
    framerate = 192000
    nframes = 0
    comptype = 'NONE'
    compname = 0

    params = (nchannels, sampwidth, framerate, nframes, comptype, compname)

    return params

def create_wave(wavename, data):

    wave_object = wave.open(wavename, 'wb')
    wave_object.setparams( create_params() )
    wave_object.writeframes( data.tostring() )
    wave_object.close()


def main(csvfile):
    data = convert(csvfile)

    for i in range(8):
        create_wave(csvfile[:-4] + str(i) + '.wav', data[i])

    call(['soxi', csvfile[:-4] + '0' + '.wav'])


if __name__ == '__main__':
    print( "Path: " + ''.join(sys.argv) )
    main(sys.argv[1])
