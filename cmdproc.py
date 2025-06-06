#!/usr/bin/env python3
#/*--
#
# Copyright (c) 2025  Frêney Studios
# Copyright (c) 2025  XCMG (XCube Media Group)
#
# Module Name:
#
#	 cmdproc.py
#
# Abstract:
#
#	 Main file for GreenCheck Command Processor (Open-source) 
# 
# - Made in Italy
#
# Author:
#
#	 Marco Panseri (Marx) 17-05-2025
#
# Revision History:
#
#--*/

#
# [SECTIONS]
# [SECTION] - IMPORTS
# [SECTION] - FUNCTIONS
#
#

# [SECTION] - IMPORTS
from transformers import pipeline
import geck_aim
import geck_aim_storage 


# [SECTION] - FUNCTIONS
def process_string(string: str) -> str:
  if string.lower().startswith("@help"):
    response = """Avaiable commands: 
              @help                       - shows this output
              @iseco       "LoremIpsum"   - return if an object is ecologic
              @iseco++     "LoremIpsum"   - return if an object is ecologic, not only with "Yes" or "No" 
              @good4us     "LoremIpsum"   - return if an object is good for us (humans)
              @good4future "LoremIpsum"   - return if an object is good for the future
              @advice      "LoremIpsum"   - should we advice this? Yes/No
              
            IMPORTANT NOTICE: Check are done with zero-shot classification, so they aren't 
                              100% correct!
            
            SENTENCES ADVICES: We Advice to add "Increment"/"Decrement" to sentences that use the object
                               complement

            Frêney Studios - XCMG 
            GreenCheck
            Copyright (c) 2025  Frêney Studios Holdings
            Copyright (c) 2025  XCMG (XCube Media Group)

            Made in Italy      
  """
  elif string.lower().startswith("@iseco")      or \
       string.lower().startswith("@isecologic") or \
       string.lower().startswith("@ecologic")      :
    geck_aim.geck_aim_init()
    response = geck_aim.model_catclas(
        string.lower(),
        geck_aim_storage.iseco_labels,
        hypothesis_template=geck_aim_storage.hypothesis_template_iseco,
        multi_label=True
    )
    response = str(response['labels'][0])
  elif string.lower().startswith("@iseco++")      or \
       string.lower().startswith("@isecologic++") or \
       string.lower().startswith("@ecologic++")      :
    geck_aim.geck_aim_init()
    response = geck_aim.model_catclas(
        string.lower(),
        geck_aim_storage.isecoxx_labels,
        hypothesis_template=geck_aim_storage.hypothesis_template_iseco,
        multi_label=True
    )
    response = str(response['labels'][0])
  elif string.lower().startswith("@isgoodforus")    or \
       string.lower().startswith("@isgood")         or \
       string.lower().startswith("@isgood4us")      or \
       string.lower().startswith("@good4us")           :
    geck_aim.geck_aim_init()
    response = geck_aim.model_catclas(
        string.lower(),
        geck_aim_storage.yn_labels,
        hypothesis_template=geck_aim_storage.hypothesis_template_isgoodforus,
        multi_label=True
    )
    response = str(response['labels'][0])
  elif string.lower().startswith("@isgoodforfuture")    or \
       string.lower().startswith("@isgood4future")         or \
       string.lower().startswith("@isgoodfu")      or \
       string.lower().startswith("@good4future")           :
    geck_aim.geck_aim_init()
    response = geck_aim.model_catclas(
        string.lower(),
        geck_aim_storage.yn_labels,
        hypothesis_template=geck_aim_storage.hypothesis_template_isgoodforfu,
        multi_label=True
    )
    response = str(response['labels'][0])
  elif string.lower().startswith("@advice")    or \
       string.lower().startswith("@advice4us")         or \
       string.lower().startswith("@goodadvice")      or \
       string.lower().startswith("@adv")           :
    geck_aim.geck_aim_init()
    response = geck_aim.model_catclas(
        string.lower(),
        geck_aim_storage.yn_labels,
        hypothesis_template=geck_aim_storage.hypothesis_template_advice,
        multi_label=True
    )
    response = str("Nota che questo comando è soggetto a BuGs, ecco la risposta: " + response['labels'][0])
  return response