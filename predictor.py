from emojifier import Emojifier
from distutils.util import strtobool

class Predictor(object):

    def __init__(self, **kwars):
        model_path = "/mnt/project/emojifier_model.bin"
        vocab_path = "/mnt/project/emojifier_vocabulary.json"
        self.model = Emojifier(model_path, vocab_path)

    def predict(self, payload):
        text, top_n, emojize = Predictor._get_parameters(payload)
        if not text:
            return None
        return self.model.emojify(text, top_n, emojize)

    @staticmethod
    def _get_parameters(payload):
        print('here', payload)
        text = payload["text"]

        top_n = 5
        if "top_n" in payload:
            top_n = payload["top_n"]
            if top_n.isnumeric():
                top_n = int(top_n)

        emojize = False
        if "emojize" in payload:
            emojize = payload["emojize"]
            if emojize.lower() == "true":
                emojize = True

        print(text, top_n, emojize)

        return text, top_n, emojize