import sox

INPUT_WAV = "hey.wav"
OUTPUT_WAV = "out.wav"


def main():
    tfm = sox.Transformer()
    tfm.compand()
    tfm.reverse()
    tfm.flanger(2)
    tfm.speed(0.5)
    tfm.reverb()
    tfm.build_file(INPUT_WAV, OUTPUT_WAV)

    # get the output in-memory as a numpy array
    # by default the sample rate will be the same as the input file
    # array_out = tfm.build_array(input_filepath=INPUT_WAV)


if __name__ == "__main__":
    main()
