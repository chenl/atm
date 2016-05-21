# -*- coding: utf-8 -*-

"""Account data storage"""

import csv

class Store(object):
    """data store for a data seqence"""

    def __init__(self, filename):
        self.filename = filename

    def save(self, it):
        """Save an iterable into csv"""
        with open(self.filename, 'wb') as db:
            writer = csv.writer(db)
            for item in it:
                writer.writerow(item)

    def load(self):
        """Get an iterable out of csv"""
        with open(self.filename, 'rb') as db:
            reader = csv.reader(db)
            for row in reader:
                yield row

    def __iter__(self):
        return self.load()
