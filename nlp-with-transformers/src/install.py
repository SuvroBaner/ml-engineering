"""
    This file will install all the dependenies to run the DL models.
"""

import subprocess
import sys

# sys.modules it returns the name of the Python modules that the current shell has imported
# when running from colab "google.colab" module gets improted by the shell automatically
is_colab = "google.colab" in sys.modules

torch_to_cuda = {"1.10.0": "cu113",
                "1.9.0": "cu111",
                "1.9.1": "cu111"}

def install_requirements(
    is_classification: bool = False, ):

    """ Installs the required packages """
    print("⏳ Installing base requirements ...")
    cmd = ["python3", "-m", "pip", "install", "-r", "requirements.txt"]
    process_install = subprocess.run(cmd, stdout = subprocess.PIPE, stderr = subprocess.PIPE)
    if process_install.returncode == 0:
        print("✅ Base requirements installed!")
    else:
        raise Exception("😭 Failed to install base requirements", process_install.stderr)

    if is_classification:
        transformers_cmd = "python3 -m pip install transformers==4.13.0".split()
        process_scatter = subprocess.run(
                            transformers_cmd,
                            stdout = subprocess.PIPE,
                            stderr = subprocess.PIPE
        )

