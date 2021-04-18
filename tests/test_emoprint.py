from emoprint import __version__
from emoprint import rand_print, nlp_print
from io import StringIO
import sys

class Capturing(list):
    def __enter__(self):
        self._stdout = sys.stdout
        sys.stdout = self._stringio = StringIO()
        return self
    def __exit__(self, *args):
        self.extend(self._stringio.getvalue().splitlines())
        del self._stringio    # free up some memory
        sys.stdout = self._stdout


def test_emoprint():
    with Capturing() as output:
        rand_print("Something")
    assert len(output[0]) == len("Something")+2

def test_nlp_emoprint():
    with Capturing() as output:
        nlp_print("Something")
    assert len(output[0]) == len("Something")+2
