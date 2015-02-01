# Auhor: Robert Gutierrez
# Obj: Building a Bloom
# Bloom Filter:  A data structure that tells you quickly, wheather an element is in the set.  while being memory efficient.
# create a class Bloom filter:

from bitarray import bitarray
import mmh3

class Bloom_Filter:
    def __init__(self,array, percantage-postive, size, Hash_count):
        self.size       = size
        self.Barray     = bitarray(size)
        self.Percentage = Percentage-postive
        self.Hash_count = Hash_count
        
        self.Barray.setcall(0) 

    def add(self, string):
        for seed in xrange(self.hash_count):
            total = mmh3.hash(string, seed) % self.size 
    

    def lookup(self, size):


        
def main():

     





if __name__=='__main__':
    main()





