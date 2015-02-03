# Auhor: Robert Gutierrez
# Obj: Building a Bloom
# Bloom Filter:  A data structure that tells you quickly, wheather 
# an elment might be in the set, or not in the set at all.
# libraries:  [mmh3: a hasing library] [bitarray: create low memorey consuming array]
# input: string 
# output: "we might have your informataion"  or " sorry no data found" 


# create a class Bloom filter:

from bitarray import bitarray
import math 
import mmh3

class Bloom_Filter:
    def __init__(self,array, percantage_postive, size, Hash_count):
        self.size       = size
        self.Barray     = bitarray(size)
        self.Percentage = Percentage_postive
        self.Hash_count = Hash_count
        
        self.Barray.setcall(0) 

    def add(self, string):
        for seed in xrange(self.hash_count):
            total = mmh3.hash(string, seed) % self.size
            return total
    

    def lookup(self, size):
        return



def false_postive_rate(bits_Filter, num_elemt , num_hash):

    #  FPR = ( 1 - e^ ((-num_hash * num_elemt / bits_filter)))^ num_hash

    FPR = ( 1 - math.e**((-num_hash * num_elemt / bits_Filter)))** num_hash
    return FPR
    #  end false_postive_rate

    
def main():

    
    FPR =  false_postive_rate( 100, 40, 5)
    print "Your False Postive is: " , FPR


if __name__=='__main__':
    main()


 
