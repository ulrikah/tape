import sox
from datetime import datetime
from random import random, randint, uniform

random_bool = lambda: bool(randint(0, 2))


def output_filename() -> str:
    timestamp = str(datetime.now().timestamp()).replace(".", "")
    return f"bounces/output_{timestamp}.wav"


def play(filepaths):
    return sox.core.play(filepaths)


def process(input_filepath: str, output_filepath: str) -> bool:
    """
    Applies various effects from the sox library and
    returns an audio file.

    All sox features: http://sox.sourceforge.net/Docs/Features
    """

    tfm = sox.Transformer()
    tfm.compand()
    if random_bool():
        tfm.reverse()
    tfm.flanger(randint(0, 30))

    speed = uniform(2.0, 3.0)
    tfm.speed(factor=speed)
    tfm.tempo(max(0.1, 0.25 / speed), quick=True)

    n_echos = randint(1, 7)
    delays = [randint(5, 200) for _ in range(n_echos)]
    decays = [0.4 for _ in range(n_echos)]
    tfm.echo(n_echos=n_echos, delays=delays, decays=decays)

    tfm.pitch(n_semitones=randint(-3, 3))
    tfm.reverb(reverberance=randint(20, 90), wet_only=random_bool())

    return tfm.build_file(
        input_filepath=input_filepath, output_filepath=output_filepath
    )


def transformer_to_file(tfm: sox.Transformer, output_filepath: str):
    tfm.build_file()


def main():
    input_filepath = "bounces/rec_1646943950.wav"
    output_filepaths = []
    for i in range(10):
        output_filepath = output_filename()
        if process(input_filepath, output_filepath):
            output_filepaths.append(output_filepath)
    play(output_filepaths)


if __name__ == "__main__":
    main()
