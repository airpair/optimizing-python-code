#!/bin/python
from disq import Disque


def read_jobs():
    client = Disque()
    while True:
        job = client.getjob('q', timeout_ms=1)
        if job is None:
            break
        # normally you'd do work here
        client.ackjob(job[1])

read_jobs()
