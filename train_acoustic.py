import sys
import os
sys.path.append(os.path.abspath("DiffSinger"))

import os
import yaml
from pathlib import Path

def run_diffsinger_training():
    with open("configs/diffsinger.yaml") as f:
        config = yaml.safe_load(f)

    data_dir = Path(config["data_root"]).name

    os.chdir("DiffSinger")
    os.system(
        f"python tasks/run.py "
        f"--config usr/configs/midi/cascade/opencpop_ds_beta6.yaml "
        f"--exp_name my_csd_training "
        f"--reset"
    )

if __name__ == "__main__":
    run_diffsinger_training()
