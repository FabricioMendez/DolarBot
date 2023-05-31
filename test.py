dictc =[ {
    "date": "2023-05-31",
    "source": "Oficial",
    "value_sell": 250.00,
    "value_buy": 240.00
  },
  {
    "date": "2023-05-31",
    "source": "Blue",
    "value_sell": 490.00,
    "value_buy": 485.00
  },
  {
    "date": "2023-05-30",
    "source": "Oficial",
    "value_sell": 250.00,
    "value_buy": 240.00
  },
  {
    "date": "2023-05-30",
    "source": "Blue",
    "value_sell": 493.00,
    "value_buy": 488.00
  },
  {
    "date": "2023-05-29",
    "source": "Oficial",
    "value_sell": 249.00,
    "value_buy": 239.00
  },
  {
    "date": "2023-05-29",
    "source": "Blue",
    "value_sell": 492.00,
    "value_buy": 487.00
  },
  {
    "date": "2023-05-26",
    "source": "Oficial",
    "value_sell": 247.00,
    "value_buy": 237.00
  }]

filtered_dicts = list()
for dic in dictc:
    newDic = {"date", dic["date"]}
    filtered_dicts.append(newDic)

print(filtered_dicts)

