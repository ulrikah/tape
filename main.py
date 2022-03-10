import sox
from datetime import datetime


def output_filename() -> str:
    timestamp = int(datetime.now().timestamp())
    return f"bounces/output_{timestamp}.wav"


def play(filepath: str):
    return sox.core.play([filepath])


def process(input_filepath: str, output_filepath: str):
    tfm = sox.Transformer()
    tfm.compand()
    tfm.reverse()
    tfm.flanger(2)
    tfm.speed(0.5)
    tfm.reverb()
    return tfm.build_file(
        input_filepath=input_filepath, output_filepath=output_filepath
    )


def transformer_to_file(tfm: sox.Transformer, output_filepath: str):
    tfm.build_file()


def main():
    input_filepath = "rec_1646943950.wav"
    output_filepath = output_filename()
    if process(input_filepath, output_filepath):
        play(output_filepath)
    else:
        print("Something went wrong building the transform to file")


if __name__ == "__main__":
    main()
