'''
Python script for generating embeddings on ALICE computing facility
'''

import socket
from time import time
import sys

# Adapted from https://github.com/MeMartijn/FakeNewsDetection
sys.path.append('../')
from data_loader import DataLoader  

if __name__ == '__main__':
    # Get starting time of script
    start_time = time()

    print('Python test started on {}'.format(socket.gethostname()))

    # Initialize data loading module
    data = DataLoader()

    # Get word embeddings
    print('Start loading XLM...')
    embeddings = data.get_xlm()
    print('Finished generating XLM')

    print('Python test finished (running time: {0:.1f}s)'.format(time() - start_time))