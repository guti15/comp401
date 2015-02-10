"""
Auhor: Robert Gutierrez
Obj: Building a Bloom Filter
----------------------------------------
Bloom Filter:  A data structure that tells you quickly, wheather 
an elment might be in the set, or not in the set at all.
---------------------------------------------------------------------------
Hash Equation: gi(x) = h1(x) + ih2(x) % m,
m = bits in array, h = hashfunction, i = number of hashes
---------------------------------------------------------------------------
libraries:  [Hashlib: hashing library]
[bitarray: create low memorey consuming array][mmh3: hasing algorithm]
---------------------------------------------------------------------------
input: reads a file from UCI Machine Learning Repository 
output: "Yes, it exist"  or " sorry no record of word"
---------------------------------------------------------------------------
"""

# create a class Bloom filter:

from bitarray import bitarray
import math 
import mmh3
import hashlib


class BloomFilter:
    
    def __init__(self, size, num_hash):
        self.size = size                  # init number of bits
        self.num_hash = num_hash          #  init number of hashes 
        self.bloom_array = bitarray(size) #  make an array with given size
        self.bloom_array.setall(0) #  bit array starts with all 0's


    def encrypt(self, string):
        crypt_sha1 = hashlib.sha1()
        crypt_sha1.update(string)
        key = crypt_sha1.hexdigest() #  gives a hexadecimal number
        key = int(key, 16)           #  convert the number
        crypt_mmh3 = mmh3.hash128(string)
        
        # Hash Equation: gi(x) = h1(x) + ih2(x) % m
        for i in range(self.num_hash):
            location = (key + i * crypt_mmh3) % self.size
            self.bloom_array[location] = True

        # end encrypt

    def decrypt(self, string):  # simlar to encrypt but this function
        crypt_sha1 = hashlib.sha1() # breaks, by setting its self to False
        crypt_sha1.update(string)
        key = crypt_sha1.hexdigest() #  gives a hexadecimal number
        key = int(key, 16)           #  convert the number
        crypt_mmh3 = mmh3.hash128(string)
    
        for i in range(self.num_hash ):
            
            location = (key + i * crypt_mmh3) % self.size
            if self.bloom_array[location] == False:
                return False    
            
        return True             # return True if found otherwise breaks
    
    
    def lookup(self, string):
        am_I_here = True                 # Assume the function exist
        am_I_here = self.decrypt(string) # create hash key and search
            
        if am_I_here == True:
            return True
        
        else:
            return False 
            
        # end lookup

    def mark(self, string):
        mark_here = self.encrypt(string) # create hash key 

        # end mark
        
# Global Functions that calculate necessary attribute for the best
# Bloom Filter. Number of bits, how many hashes and calculating
# the False Postive Rate
    
def false_postive_rate(bits_Filter, num_elemt , num_hash):
    FPR = (1 - math.e**((-num_hash * num_elemt / bits_Filter)))** num_hash
    FPR = round(FPR, 5) * 100

    return FPR                  #  function calculate the False postive

    
def number_of_bits( items_expect , accpt_fpostive):    
    bits_needed  = (-items_expect*math.log(accpt_fpostive))/(math.log(2)**2)
    
    return bits_needed          # function calculates the number of bits


def num_hash_apply(bits_needed,items_expect):
    how_many_hash = (bits_needed / items_expect) * math.log(2)
    
    return how_many_hash        # calculate how many hash function 

    

