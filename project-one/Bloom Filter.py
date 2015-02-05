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
import hashlib
import md5

class BloomFilter:
    
    def __init__(self,array, size, hash_count):
        self.size         = size
        self.bloom_array  = bitarray(size)
        self.hash_count   = hash_count
        self.bloom_array.setcall(0) 

    
    def lookup(self, size):
        return


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

    Estimate_Array = 9999
    FALSE_POSTIVE  = .01 
    small_list=['hello', 'world' ,'hi', 'down', 'up', 'right', 'left']
    
    crypt = hashlib.sha1()
    for words in small_list:
        crypt.update(words)
        print crypt.hexdigest()
        
        
    print '\n'
    
    bits_filter = number_of_bits( Estimate_Array, FALSE_POSTIVE)
    bits_filter = math.ceil(bits_filter)
    
    how_many_hash = num_hash_apply( bits_filter, Estimate_Array)
    how_many_hash = math.ceil( how_many_hash)

    FPR = false_postive_rate(bits_filter, Estimate_Array, how_many_hash)
    
    print "Estimated items %d\nBits in Array: %.2f\nNumber of Hash Func: %d" %( Estimate_Array, bits_filter, how_many_hash)

    print "Your False Postive is: " , FPR, '%'



    
if __name__=='__main__':
    main()
