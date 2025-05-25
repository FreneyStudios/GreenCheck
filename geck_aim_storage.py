#!/usr/bin/env python3
#/*--
#
# Copyright (c) 2025  Frêney Studios
# Copyright (c) 2025  XCMG (XCube Media Group)
#
# Module Name:
#
#	 geck_aim_storage.py
#
# Abstract:
#
#	GreenCheck Artificial Intelligence Models
#   Manager - Hypothesis Templates and Labels
#   Storage
#   (Based on the Infinity one) (Open-source) 
# 
# - Made in Italy
#
# Author:
#
#	 Marco Panseri (Marx) 23-05-2025
#
# Revision History:
#


hypothesis_template_iseco : str        = "This oject is {} ecologic"
yn_labels : list[str] = [
    "Yes",
    "No"
]
iseco_labels : list[str] = yn_labels

isecoxx_labels : list[str] = [
    "Absolutely yes",
    "Yes",
    "Neutral",
    "No",
    "Absolutely not!"
]

hypothesis_template_isgoodforus : str        = "This oject is {} good for humans"
hypothesis_template_isgoodforfu : str        = "This oject is {} good for a better future"
hypothesis_template_advice      : str        = "This oject is {} adviced from us"