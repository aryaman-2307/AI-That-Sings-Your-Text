import os

def generate_singing(lyrics, midi_file):
    os.chdir("DiffSinger")
    os.system(
        f"python inference/svs/infer.py "
        f"--config ../configs/diffsinger.yaml "
        f"--lyric \"{lyrics}\" "
        f"--midi ../{midi_file} "
        f"--checkpoint checkpoints/acoustic_model.pth "
        f"--output ../outputs/mel.npy"
    )

    os.chdir("../wavenet_vocoder")
    os.system(
        f"python synthesis.py "
        f"--preset ../configs/wavenet.yaml "
        f"--conditional ../outputs/mel.npy "
        f"--checkpoint checkpoints/vocoder_model.pth "
        f"--out ../outputs/generated.wav"
    )

if __name__ == "__main__":
    generate_singing("Sing me a song of AI and dreams", "melody.mid")
