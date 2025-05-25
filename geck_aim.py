#!/usr/bin/env python3
#/*--
#
# Copyright (c) 2025  Frêney Studios
# Copyright (c) 2025  XCMG (XCube Media Group)
#
# Module Name:
#
#	 geck_aim.py
#
# Abstract:
#
#	GreenCheck Artificial Intelligence Models
#   Manager (Based on the Infinity one) (Open-source) 
# 
# - Made in Italy
#
# Author:
#
#	 Marco Panseri (Marx) 23-05-2025
#
# Revision History:
#


print("GECK_AIm started")
from transformers import pipeline 


model_name_catclas      = "MoritzLaurer/deberta-v3-large-zeroshot-v2.0"
model_catclas = None 

@staticmethod
def geck_aim_init():
    """ aim_init: loads AI models """
    global model_catclas, model_senclas

    ## VAR CHECK ##

    # Load the DeBERTa model for zero-shot text classification
    model_catclas = pipeline(model=model_name_catclas)