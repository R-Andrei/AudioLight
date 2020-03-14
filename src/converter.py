class Converter(object):
    def __init__(self):
        self.__gamma = 0.75
        self.__Converter = {
            'default': {
                'min': 10,
                'max': 30000
            },
            'mean': {
                'min': 20,
                'max': 20000
            },
            'mean_weighted': {
                'min': 3000,
                'max': 14000
            },
            'light': {
                'min': 380,
                'max': 750
            }
        }

    def set_gamma(self, gamma=None):
        self.__gamma = gamma if gamma else 0.75

    def test_spectrum(self, gamma=None):
        for frequency in range(self.__Converter['light']['min'], self.__Converter['light']['max']+1):
            r, g, b = self.to_rgb(
                frequency, gamma=gamma if gamma else self.__gamma)
            yield {'r': r, 'g': g, 'b': b}

    def to_rgb(self, frequency, true=False, gamma=None):
        '''This converts a given wavelength of light to an 
        approximate RGB color value. The wavelength must be given
        in nanometers in the range from 380 nm through 750 nm
        (789 THz through 400 THz).

        Based on code by Dan Bruton
        http://www.physics.sfasu.edu/astro/color/spectra.html
        '''

        gamma = gamma if gamma else self.__gamma

        wavelength = float(frequency)
        if not true:
            if wavelength >= 380 and wavelength <= 440:
                R = ((-(wavelength - 440) / (440 - 380))) ** gamma
                G = 0.0
                B = (1.0) ** gamma
            elif wavelength >= 440 and wavelength <= 480:
                R = 0.0
                G = ((wavelength - 440) / (480 - 440)) ** gamma
                B = 1.0
            elif wavelength >= 480 and wavelength <= 530:
                R = 0.0
                G = 1.0
                B = (-(wavelength - 530) / (530 - 480)) ** gamma
            elif wavelength >= 530 and wavelength <= 580:
                R = ((wavelength - 530) / (580 - 530)) ** gamma
                G = 1.0
                B = 0.0
            elif wavelength >= 580 and wavelength <= 700:
                R = 1.0
                G = (-(wavelength - 700) / (700 - 580)) ** gamma
                B = 0.0
            elif wavelength >= 700 and wavelength <= 750:
                attenuation = 0.3 + 0.7 * (750 - wavelength) / (750 - 700)
                R = (1.0 * attenuation) ** gamma
                G = 0.0
                B = 0.0
            else:
                R = 0.0
                G = 0.0
                B = 0.0
            R *= 255
            G *= 255
            B *= 255
        else:
            if wavelength >= 380 and wavelength <= 440:
                attenuation = 0.3 + 0.7 * (wavelength - 380) / (440 - 380)
                R = ((-(wavelength - 440) / (440 - 380)) * attenuation) ** gamma
                G = 0.0
                B = (1.0 * attenuation) ** gamma
            elif wavelength >= 440 and wavelength <= 490:
                R = 0.0
                G = ((wavelength - 440) / (490 - 440)) ** gamma
                B = 1.0
            elif wavelength >= 490 and wavelength <= 510:
                R = 0.0
                G = 1.0
                B = (-(wavelength - 510) / (510 - 490)) ** gamma
            elif wavelength >= 510 and wavelength <= 580:
                R = ((wavelength - 510) / (580 - 510)) ** gamma
                G = 1.0
                B = 0.0
            elif wavelength >= 580 and wavelength <= 645:
                R = 1.0
                G = (-(wavelength - 645) / (645 - 580)) ** gamma
                B = 0.0
            elif wavelength >= 645 and wavelength <= 750:
                attenuation = 0.3 + 0.7 * (750 - wavelength) / (750 - 645)
                R = (1.0 * attenuation) ** gamma
                G = 0.0
                B = 0.0
            else:
                R = 0.0
                G = 0.0
                B = 0.0
            R *= 255
            G *= 255
            B *= 255
        return int(R), int(G), int(B)

    def audio_light(self, origin_frequency, use_spectrum='default', true=True):

        origin_min, origin_max = self.__Converter[use_spectrum]['min'], self.__Converter[use_spectrum]['max']
        if use_spectrum != 'light':
            target_min = self.__Converter['light']['min']
            target_max = self.__Converter['light']['max']
        else:
            target_min = self.__Converter['mean']['min']
            target_max = self.__Converter['mean']['max']

        origin_frequency = origin_min if origin_frequency <= origin_min else origin_max if origin_frequency >= origin_max else origin_frequency

        # if origin_frequency < origin_min or origin_frequency > origin_max:
        #     raise ValueError('Frequency [{}] out of bounds [{}, {}]'.format(
        #         origin_frequency, origin_min, origin_max))

        percentage = (origin_frequency - origin_min)/(origin_max-origin_min)
        if not true:
            if percentage <= 0.29:
                percentage *= (0.9-percentage)
            elif percentage > 0.29 and percentage <= 0.32:
                percentage *= (1.05-percentage)
            elif percentage > 0.32 and percentage <= 0.35:
                percentage *= (1.1-percentage)
            elif percentage > 0.35 and percentage <= 0.35:
                percentage*= (1.25-percentage)
            elif percentage > 0.5 and percentage <= 0.69:
                percentage *= (0.65 + percentage)
            elif percentage > 0.69 and percentage < 0.8:
                percentage *= (0.4 + percentage)
        return int(target_min + (percentage*(target_max-target_min)))
