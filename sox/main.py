from datetime import datetime
from random import random, randint, uniform
import sys

import sox
import numpy as np

SAMPLE_RATE = 44100
INT16 = np.int16

random_bool = lambda: bool(randint(0, 2))


def sox_transformer():
    tfm = sox.Transformer()
    tfm.set_globals(verbosity=1)
    return tfm

def timestamped_filename() -> str:
    timestamp = str(datetime.now().timestamp()).replace(".", "")
    return f"bounces/output_{timestamp}.wav"

def process(input_filepath: str) -> np.ndarray:
    """
    Applies various effects from the sox library and
    returns an audio file.

    All sox features: http://sox.sourceforge.net/Docs/Features
    """

    tfm = sox_transformer()
    tfm.compand()
    # if random_bool():
    #     tfm.reverse()
    tfm.flanger(randint(0, 30))

    # speed = uniform(0.5, 3.0)
    speed = 0.5
    tfm.speed(factor=speed)
    tfm.tempo(max(0.1, 0.25 / speed), quick=True)

    n_echos = randint(1, 7)
    delays = [randint(5, 200) for _ in range(n_echos)]
    decays = [0.4 for _ in range(n_echos)]
    tfm.echo(n_echos=n_echos, delays=delays, decays=decays)

    tfm.pitch(n_semitones=randint(-3, 3))
    tfm.reverb(reverberance=randint(20, 90), wet_only=random_bool())

    return tfm.build_array(
        input_filepath=input_filepath
    )
   
def sum_tracks(tracks: np.ndarray) -> np.ndarray:
    return np.sum(pad_tracks(tracks), axis=0, dtype=INT16)

def tracks_to_file(tracks: np.ndarray, filename : str) -> bool:
    tfm = sox_transformer()
    return tfm.build(output_filepath = filename, input_array=tracks, sample_rate_in=SAMPLE_RATE)

def add_list_of_tracks(tracks):
    min_length = min(len(l) for l in tracks)
    return np.asarray([t[:min_length] for t in tracks], dtype=INT16)[:,:min_length]

def pad_tracks(M):
    """Appends the minimal required amount of zeroes at the end of each 
     array in the jagged array `M`, such that `M` looses its jagedness."""

    maxlen = max(len(r) for r in M)
    n_audio_channels = 2
    Z = np.zeros((len(M), maxlen, n_audio_channels))
    for enu, row in enumerate(M):
        Z[enu, :len(row)] += row 
    return Z

def main():
    input_filepath = "/Users/ulrikah/Music/tape/tidal/samples/presloops/ULTRAFLANGE.wav"
    # input_filepath = "/Users/ulrikah/Music/tape/tidal/samples/presperc/K LAP P 23 15 39.wav"
    # input_filepath = sys.argv[-1]
    n_iters = 1
    output_arrays = add_list_of_tracks([process(input_filepath) for i in range(n_iters)])
    output_filename = timestamped_filename()
    if tracks_to_file(sum_tracks(output_arrays), output_filename):
        sox.core.play([output_filename])
    else:
        print("Something went wrong rendering")

if __name__ == "__main__":
    main()
