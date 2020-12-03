from pathlib import Path
import simpleaudio
import argparse
from nltk.corpus import cmudict
import re

# import numpy
# import datetime
# ...others?  (only modules that come as standard with Python3 - i.e. so they will be available on a marker's machine)

# A pair of potentially useful classes to start you off (you can change these however you like, or delete them entirely)
class Synth:
    def __init__(self, wav_folder):
        self.diphones = self.load_diphone_data(wav_folder)

    def load_diphone_data(self, wav_folder):

        diphones = {}
        all_diphone_wav_files = (str(item) for item in Path(wav_folder).glob('*.wav') if item.is_file())

        for wav_file in all_diphone_wav_files:
            pass  # delete this line and implement

        return diphones


class Utterance:
    def __init__(self, phrase):
        print(f'Making utterance to synthesise phrase: {phrase}')  # just a hint - can be deleted
        # pass  # delete this and implement
        self.phrase = phrase

    def get_phone_seq(self):
        # pass  # delete this line and implement
        phone_seq = re.sub(r'[^\w\s]', '', self.phrase.lower())
        print("normalise the text: ", phone_seq) #TODO: need a exception character
        prondict = cmudict.dict()
        print(prondict[phone_seq])
        for each in prondict[phone_seq]:
            each.insert(0,'PAU')
            each.append('PAU')
        print(prondict[phone_seq])
        return prondict[phone_seq]


# NOTE: DO NOT CHANGE ANY OF THE ARGPARSE ARGUMENTS - CHANGE NOTHING IN THIS FUNCTION
def process_commandline():
    parser = argparse.ArgumentParser(
        description='A basic text-to-speech app that synthesises speech using diphone concatenation.')

    # basic synthesis arguments
    parser.add_argument('--diphones', default="./diphones",
                        help="Folder containing diphone wavs")
    parser.add_argument('--play', '-p', action="store_true", default=False,
                        help="Play the output audio")
    parser.add_argument('--outfile', '-o', action="store", dest="outfile",
                        help="Save the output audio to a file", default=None)
    parser.add_argument('phrase', nargs='?',
                        help="The phrase to be synthesised")

    # Arguments for extension tasks
    parser.add_argument('--volume', '-v', default=None, type=int,
                        help="An int between 0 and 100 representing the desired volume")
    parser.add_argument('--spell', '-s', action="store_true", default=False,
                        help="Spell the input text instead of pronouncing it normally")
    parser.add_argument('--reverse', '-r', action="store", default=None, choices=['words', 'phones', 'signal'],
                        help="Speak backwards in a mode specified by string argument: 'words', 'phones' or 'signal'")
    parser.add_argument('--fromfile', '-f', action="store", default=None,
                        help="Open file with given name and synthesise all text, which can be multiple sentences.")
    parser.add_argument('--crossfade', '-c', action="store_true", default=False,
                        help="Enable slightly smoother concatenation by cross-fading between diphone units")

    args = parser.parse_args()

    if (args.fromfile and args.phrase) or (not args.fromfile and not args.phrase):
        parser.error('Must supply either a phrase or "--fromfile" to synthesise (but not both)')

    return args


if __name__ == "__main__":
    args = process_commandline()

    utt = Utterance(phrase=args.phrase)
    phone_seq = utt.get_phone_seq()


    print(f'Will load wavs from: {args.diphones}')  # just a clue - can be deleted
    diphone_synth = Synth(wav_folder=args.diphones)

    # out could be a simpleaudio.Audio object which will become your output.
    # you need to modify (or create) out.data to produce the correct synthesis
    out = simpleaudio.Audio(rate=16000)
    print(out.data, type(out.data))  # just a clue - can be deleted