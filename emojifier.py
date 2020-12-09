#!/usr/bin/env python3
import sys
import os.path
from os import path
import numpy as np
import emoji, json
# https://deepmoji.mit.edu/
from torchmoji.sentence_tokenizer import SentenceTokenizer
from torchmoji.model_def import torchmoji_emojis

# Input arguments
MODEL_PATH = ""
VOCAB_PATH = ""
N_EMOJIS = 5

# Emojis
EMOJIS = ":joy: :unamused: :weary: :sob: :heart_eyes: :pensive: :ok_hand: :blush: :heart: :smirk: :grin: :notes: :flushed: :100: :sleeping: :relieved: :relaxed: :raised_hands: :two_hearts: :expressionless: :sweat_smile: :pray: :confused: :kissing_heart: :heartbeat: :neutral_face: :information_desk_person: :disappointed: :see_no_evil: :tired_face: :v: :sunglasses: :rage: :thumbsup: :cry: :sleepy: :yum: :triumph: :hand: :mask: :clap: :eyes: :gun: :persevere: :smiling_imp: :sweat: :broken_heart: :yellow_heart: :musical_note: :speak_no_evil: :wink: :skull: :confounded: :smile: :stuck_out_tongue_winking_eye: :angry: :no_good: :muscle: :facepunch: :purple_heart: :sparkling_heart: :blue_heart: :grimacing: :sparkles:".split(
    ' ')

"""
Emojifier based on the pre-trained deepmoji model published by MIT. 
"""


class Emojifier:

    def __init__(self, model_path, vocab_path):
        self.model = torchmoji_emojis(model_path)
        with open(vocab_path, 'r') as f:
            self.vocab = json.load(f)
        self.tokenizer = SentenceTokenizer(self.vocab, 30)

    def emojify(self, sentence, top_n=5):
        tokens, _, _ = self.tokenizer.tokenize_sentences([sentence])
        p = self.model(tokens)[0]
        ids = np.argsort(p)[::-1][:top_n]
        emojis = map(lambda x: EMOJIS[x], ids)
        return emoji.emojize(f"{sentence} {' '.join(emojis)}", use_aliases=True)


if __name__ == "__main__":

    if len(sys.argv) < 4:
        print('Usage: python deepmoji.py {MODEL_PATH} {VOCAB_PATH} {SENTENCE}')
        sys.exit()

    MODEL_PATH = sys.argv[1]
    VOCAB_PATH = sys.argv[2]
    if not path.exists(MODEL_PATH):
        print('Model path invalid')
        sys.exit()
    if not path.exists(VOCAB_PATH):
        print('Vocab path invalid')
        sys.exit()

    SENTENCE = sys.argv[3]

    clf = Emojifier(MODEL_PATH, VOCAB_PATH)
    print(clf.emojify(SENTENCE))
