from AudioConverter import AudioConverter
from FrequencyConverter import FrequencyConverter
import json

from pydub import AudioSegment

def main():

    # fconverter = FrequencyConverter()
    # aconverter = AudioConverter(fconverter)

    # aconverter.import_directory('../songs/')

    # aconverter.export_store('../output/output_me.json')

    # output = {}

    # output['data'] = list(aconverter.test_spectrum(gamma=0.9, true=False))
    # with open('spectrum.json', 'w') as spectrum_file:
    #     json.dump(output, spectrum_file)

    sound = AudioSegment.from_mp3('../media/dl/Vera Blue - Hold.mp3')
    print(sound)
    sound.export("../media/converted/Vera Blue - Hold.wav", format="wav")

if __name__ == "__main__":
    main()
