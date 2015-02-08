# Auhor: Robert Gutierrez
# Obj: Building a Bloom
# Bloom Filter:  A data structure that tells you quickly, wheather 
# an elment might be in the set, or not in the set at all.
# libraries:  [md5: a cryptic hasing library] [bitarray: create low memorey consuming array]
# input: string 
# output: "we might have your informataion"  or " sorry no data found" 


# create a class Bloom filter:



from bitarray import bitarray
import math 
import mmh3
import hashlib
import md5

class BloomFilter:
    
    def __init__(self, size, num_hash):
        self.size = size        # init number of bits
        self.num_hash = num_hash #  init number of hashes 
        self.bloom_array = bitarray(size) #  make an array with given size
        self.bloom_array.setall(0)       #  bit array starts with all 0's


    def encrypt(self, string):
        crypt = hashlib.sha1()
        crypt.update(string)
        key = crypt.hexdigest() #  gives a hexadecimal number
        key = int(key, 16)      #  convert the number 
        key = key % self.size        #  location in bit array.
        
        return key

    
    def lookup(self, string):
        am_I_here = self.encrypt(string) 
            
        if (self.bloom_array[am_I_here] == 0) :
            return False
            
        else:
            return True
            

    def mark(self, string):
        print string 
        mark_here = self.encrypt(string)
        self.bloom_array[mark_here] = 1
        print "your array has been marked in cell: ", mark_here
            
    


    
def false_postive_rate(bits_Filter, num_elemt , num_hash):
    FPR = ( 1 - math.e**((-num_hash * num_elemt / bits_Filter)))** num_hash
    FPR = round(FPR, 5) * 100

    return FPR

    
def number_of_bits( items_expect , accpt_fpostive):    
    bits_needed  = -items_expect*math.log(accpt_fpostive)/(math.log(2)**2)
    
    return bits_needed


def num_hash_apply(bits_needed,items_expect):
    how_many_hash = (bits_needed / items_expect) * math.log(2)
    
    return how_many_hash

    
    
def main():

    Estimate_Array = 4294967296
    FALSE_POSTIVE  = .01 
    small_list=['hello', 'world' ,'hi', 'down', 'up', 'right', 'left']

    bits_filter = number_of_bits( Estimate_Array, FALSE_POSTIVE)
    bits_filter = math.ceil(bits_filter)
    
    how_many_hash = num_hash_apply( bits_filter, Estimate_Array)
    how_many_hash = math.ceil(how_many_hash)

    bfilter = BloomFilter( Estimate_Array, how_many_hash)

    # This encrypts the small list above
    print bfilter.bloom_array[0]
    
    crypt = hashlib.sha1()
    for words in small_list:
        bfilter.mark(words)




    # SMALL TEST and it RUNNSS !!
    #  Get more Data  clean up and improve if possible 
    
    exist = bfilter.lookup('hel')
    
    if exist == True :
        print 'YAY I exist! '
    else:
        print ' you suck at this >:| '
    
        


        
    print "Estimated items %d\nBits in Array: %.2f\nNumber of Hash Func: %d" %( Estimate_Array, bits_filter, how_many_hash)





    
if __name__=='__main__':
    main()







