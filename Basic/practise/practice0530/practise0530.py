# -*- coding: utf-8 -*-
"""
Created on Tue May 30 18:07:53 2023

@author: opjoh
"""

import os
import openai

openai.api_key = os.getenv("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")

response = openai.Completion.create(
  model="text-davinci-003",
  prompt="請問要如何考上台中一中？",
  temperature=1,
  max_tokens=256,
  top_p=1,
  frequency_penalty=0,
  presence_penalty=0
)