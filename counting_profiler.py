#!/bin/python
from time import sleep
from disq.rolling_counter import RollingCounter
from itertools import izip, cycle


@profile
def count_incoming():
    # Set the count lifetime really low
    rc = RollingCounter(ttl_secs=0.1)
    for i, _ in izip(cycle('1234567890'), xrange(10000)):
        rc.add(i)

    while rc.max() is not None:
        sleep(0.001)

count_incoming()
