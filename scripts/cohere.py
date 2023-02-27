import cohere
co = cohere.Client('nidVfcm5xYEyW8etrREYrKmXjcdD65sCGVhxRJOl')
response = co.generate(
  model='large',
  prompt='This program will extract topic information from Titles. Here are some examples:\n\n Title: \nBoris Johnson using a taxpayer-funded jet for an election campaign fits a long history of taking things he didn\'t pay for.\n\nExtracted Topic:\n Politics   \n\nTitle:\nA woman facing eviction from the home that she inherited from her brother in 2007. Turns out her brother was in business with a notorious international criminal Paul Le Roux, who is currently serving 25 years in a New York prison. \n\nExtracted Topic:\nCrime   \n\nTitle:\nMarchÃ© RÃ©sines dans les peintures et revÃªtements 2021 avec les donnÃ©es des meilleurs pays et lâ€™analyse Covid-19, la portÃ©e future, lâ€™estimation de la taille, les revenus, les tendances des prix et les prÃ©visions dâ€™ici 2026.\n\nExtracted Topic\nCOVID   \n\nTitle:\nAI drives data analytics surge, study finds \n\nExtracted Topic:\nTech   \n\nTitle:\nMale arrested for the murder of an elderly female in Cofimvaba â€“ SAPS Crime Report: 2021-09-09 13:22:58 \n\nTitle:\nCrime   7th Anniversary of SCOAN Collapse in Nigeria-SABC News Religion   The construction sector is expected to be boosted by riots and looting repairs \n\nExtracted Topic:\nConstruction   \n\nTitle:\nNews24.com
 Court dismisses attempt by former Eskom CEO to \'punish\' woman for tweet Law   Global and Regional Beta-Carotene Market Research 2020 Report
 Growth Forecast 2025 key players! â€“ DSM â€“ BASF â€“ Allied Biotech â€“ Chr Hansen â€“ LYCORED \n\nExtracted Topic:',
  max_tokens=20,
  temperature=0.5,
  k=0,
  p=1,
  frequency_penalty=0,
  presence_penalty=0,
  stop_sequences=["--"],
  return_likelihoods='NONE')
print('Prediction: {}'.format(response.generations[0].text))