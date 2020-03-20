from AudioConverter import AudioConverter
from FrequencyConverter import FrequencyConverter
import json

def main():

    fconverter = FrequencyConverter()
    aconverter = AudioConverter(fconverter)

    aconverter.import_directory('songs/')

    aconverter.export_store('output_me.json')

    output = {}

    output['data'] = list(aconverter.test_spectrum(gamma=0.9, true=False))
    with open('spectrum.json', 'w') as spectrum_file:
        json.dump(output, spectrum_file)


if __name__ == "__main__":
    main()
