from scipy.io import wavfile
from matplotlib import pyplot
from os import listdir
import numpy
import json
import re


class AudioConverter(object):
    """
    Docstring
    """

    def __init__(self, converter_instance):

        self.__converter = converter_instance
        self.__wavdata = None
        self.__samples = None
        self.__samplerate = None
        self.__duration = None
        self.__wavdata = None
        self.__average_frequency = None
        self.__converted_frequency = None
        self.__frequencies = None
        self.__ahsl = None
        self.__hsl = None
        self.__store = {}

    def store(self, file, name=None, force=False):
        """
        Docstring
        """
        self.read_file(file)
        refile = re.findall(r'.[\'0-9a-zA-Z\. -]+.wav$', file)
        key = name if name else refile[0][1:-4] if refile else None

        if not force and key in self.__store:
            raise ValueError(
                'File already exists in store. Use force=True if you want to replace it.')

        self.__store[key] = {
            'wavdata': self.__wavdata,
            'samples': self.__samples,
            'samplerate': self.__samplerate,
            'duration': self.__duration,
            'average_frequency': self.__average_frequency,
            'converted_frequency': self.__converted_frequency,
            'frequencies': self.__frequencies,
            'ahsl': self.__ahsl,
            'hsl': self.__hsl
        }
        print('File \'{}\' added to store.'.format(key))

    def read_file(self, file):
        """
        Docstring
        """
        if (file[-4:] != '.wav'):
            raise TypeError(
                'File format not supported. Please use a .wav file!')
        try:
            self.__samplerate, self.__wavdata = wavfile.read(file)
            self.__wavdata = abs(self.__wavdata[(self.__wavdata[:, 0] != 0)])
            self.__samples = self.__wavdata.shape[0]
            self.__duration = int(self.__samples/self.__samplerate)
            self.__average_frequency = int(numpy.mean(self.__wavdata))
            self.__converted_frequency = self.__converter.audio_light(self.__average_frequency, use_spectrum='mean_weighted')
            self.__frequencies = [numpy.mean(self.__wavdata[self.__samplerate*i: self.__samplerate*(i+1)]) for i in range(self.__duration-1)]
            self.__ahsl = self.from_audio(self.__average_frequency)
            self.__hsl = [self.from_audio(frequency, true=True, spectrum='mean', color_spectrum='mean') for frequency in self.__frequencies]
        except Exception as e:
            print(e)
            raise e

    def stored_average_frequency(self, file):
        """
        Docstring
        """
        if file not in self.__store:
            raise KeyError('File \'{}\' not in store.'.format(file))
        return self.__store[file]['average_frequency']

    def stored_duration(self, file):
        """
        Docstring
        """
        if file not in self.__store:
            raise KeyError('File \'{}\' not in store.'.format(file))
        return self.__store[file]['duration']

    def average_frequency(self):
        """
        Docstring
        """
        return self.__average_frequency

    def duration(self):
        """
        Docstring
        """
        return self.__duration

    def from_light(self, frequency):
        """
        Docstring
        """
        return self.__converter.to_rgb(frequency)

    def from_audio(self, frequency, true=False, spectrum='mean_weighted', color_spectrum = None):
        """
        Docstring
        """
        light = self.__converter.audio_light(frequency, use_spectrum=spectrum, true=true)
        r, g, b = self.__converter.to_rgb(light, true=true if not color_spectrum else true if color_spectrum!='mean' else False)
        h, l, s = self.__converter.to_hls(r, g, b)
        return {'h': h, 'l': l, 's': s*0.9}

    def import_directory(self, directory_path):
        """
        Docstring
        """
        for file in [file for file in listdir(directory_path) if file[-4:] == '.wav']:
            self.store('{}{}'.format(directory_path, file))

    def test_spectrum(self, gamma=0.75, true=False):
        return self.__converter.test_spectrum(gamma=gamma, true=true)

    def export_store(self, filename="output.json"):
        """
        Docstring
        """
        output = {}
        output['data'] = [{
            'name': key,
            'duration': values['duration'],
            'average_frequency': values['average_frequency'],
            'converted_frequency': values['converted_frequency'],
            'ahsl': values['ahsl'],
            'hsl': values['hsl']
        } for key, values in self.__store.items()]
        with open(filename, 'w') as exported_file:
            json.dump(output, exported_file)
