#!/usr/bin/env python3

import matplotlib.pyplot as plt
import typing
import decimal
import datetime
import yaml
from pprint import pprint

class PiValue(typing.NamedTuple):
    label: str
    value: decimal.Decimal
    duration: datetime.timedelta

data = list()

data.append( PiValue("approx", 3.14, 0.0) )

with open("internet.yaml") as f:
    x = yaml.safe_load(f)
    data.append(PiValue("internet", x['value'], x['duration']))
    pprint(x)

for e in data:
    print(e.label, e.value, e.duration)

dur = [ x.duration for x in data]
val = [ x.value for x in data]

plt.plot(dur,val)
plt.show()
