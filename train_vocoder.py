import yaml
import os

def run_wavenet_training():
    with open("configs/wavenet.yaml") as f:
        config = yaml.safe_load(f)

    os.chdir("wavenet_vocoder/egs/mulaw256")
    os.system(f"./run.sh --db-root ../../{config['data_root']}")

if __name__ == "__main__":
    run_wavenet_training()
