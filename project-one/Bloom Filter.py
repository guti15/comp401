# Auhor: Robert Gutierrez
# Obj: Building a Bloom
# Bloom Filter:  A data structure that tells you quickly, wheather 
# an elment might be in the set, or not in the set at all.
# Hash Equation: gi(x) = h1(x) + ih2(x) % m,
# m = bits in array, h = hashfunction, i = number of hashes 
# libraries:  [md5: a cryptic hasing library]
# [bitarray: create low memorey consuming array]
# 
# input: string 
# output: "we might have your informataion"  or " sorry no data found" 


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
        
        # Hash Equation: gi(x) = h1(x) + ih2(x) % m,
        for i in range(self.num_hash):
            location = (key + i * crypt_mmh3) % self.size
            self.bloom_array[location] = True # mark the unique key location

        # end encrypt

    def decrypt(self, string):
        crypt_sha1 = hashlib.sha1()
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
        am_I_here = True
        am_I_here = self.decrypt(string) # create hash key 
            
        if am_I_here == True:
            return True
        
        else:
            return False 
            
        # end lookup

    def mark(self, string):
        mark_here = self.encrypt(string) # create hash key 
        # self.bloom_array[mark_here] = 1  # Mark it with a 1

        # end mark

    
def false_postive_rate(bits_Filter, num_elemt , num_hash):
    FPR = (1 - math.e**((-num_hash * num_elemt / bits_Filter)))** num_hash
    FPR = round(FPR, 5) * 100

    return FPR

    
def number_of_bits( items_expect , accpt_fpostive):    
    bits_needed  = (-items_expect*math.log(accpt_fpostive))/(math.log(2)**2)
    
    return bits_needed


def num_hash_apply(bits_needed,items_expect):
    how_many_hash = (bits_needed / items_expect) * math.log(2)
    
    return how_many_hash

    
    
def main():
    # nips full paper apprx: 1,900,000 words
    Estimate_Array = 2000000   
    FALSE_POSTIVE  = .01        # with a 1% error 

    bits_filter = number_of_bits( Estimate_Array, FALSE_POSTIVE) 
    bits_filter = math.ceil(bits_filter)
    
    how_many_hash = num_hash_apply( bits_filter, Estimate_Array)
    how_many_hash = int(math.ceil(how_many_hash))

    bfilter = BloomFilter( Estimate_Array, how_many_hash) # establish Bloom
    
    read_file = open('./vocab.nips.txt', 'r') #  open the file 

    for words in read_file:     #  read list of words
        words = words.rstrip("\n") # take out return char
        bfilter.mark(words)        #  update the filter by marking it
        
    
    ASK = True    
    while ASK == True:
        find = raw_input("Enter Word: ")
        visited = bfilter.lookup(find)
            
        if visited == True:
            print "It's compleatly possible that it may exist\n"
            ASK = input("To continue press 1, to end press 0 : ")
            
        else:
            print "Sorry no record of such Word.\n"
            ASK = input("To continue press 1, to end press 0 : ")

                
    print "Closing Program..."

        
        

if __name__=='__main__':
    main()

