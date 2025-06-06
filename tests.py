#!/usr/bin/env python3
#/*--
#
# Copyright (c) 2025  Frêney Studios
# Copyright (c) 2025  XCMG (XCube Media Group)
#
# Module Name:
#
#	 tests.py
#
# Abstract:
#
#	 Main file for GreenCheck' tests (Open-source) 
# 
# - Made in Italy
#
# Author:
#
#	 Marco Panseri (Marx) 30-05-2025
#
# Revision History:
#
#--*/

import geck_aim as aim
from   colorama import Fore
import platform

if __name__ == "__main__":
  print("XCMG/Frêney Studios GreenCheck - Test Suite")
  print("Loading libraries...")

  try:
    import transformers
    import torch 
    import numpy 
  except Exception as e:
    print(Fore.RED + "Error while importing (" + str(e) + ")!" + Fore.RESET)

  print("Listing versions...")
  print("Huggingface/Transformers: " + Fore.MAGENTA + transformers.__version__ + Fore.RESET)
  print("Torch: "                    + Fore.MAGENTA + torch.__version__ + Fore.RESET)
  print("Numpy: "                    + Fore.MAGENTA + numpy.__version__ + Fore.RESET)
  print("Using: "                    + Fore.MAGENTA + platform.python_version() + Fore.RESET)
  print("On: "                       + Fore.MAGENTA + platform.system() + Fore.RESET + " (Built on Linux)")

  print("------------------- [ 1 ] Spixe TESTS ----------------------")
  