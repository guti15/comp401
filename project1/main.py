from BloomFilter import number_of_bits, num_hash_apply,num_hash_apply
from BloomFilter import BloomFilter
import math
#--------------------------------------------------------------------------------
def main():
    
    # nips full paper apprx: 1,900,000 words
    Estimate_Array = 2000000   
    FALSE_POSTIVE  = .01        # with a 1% error
    COUNTER_SKIP = 0            # A counter reset every 3,000 words
    pos_words = []
    neg_words = []

    bits_filter = number_of_bits(Estimate_Array, FALSE_POSTIVE)
    bits_filter = math.ceil(bits_filter) # number is a float, so we round 
    
    how_many_hash = num_hash_apply( bits_filter, Estimate_Array)
    how_many_hash = int(math.ceil(how_many_hash)) # round up
    
    bfilter = BloomFilter( Estimate_Array, how_many_hash)
    read_file = open('./data_set/vocab.nips.txt', 'r') 

    # READ FILE 
    for words in read_file:     # read list of words
        if COUNTER_SKIP!= 100:
            words = words.rstrip("\n") # take out return '\n'
            bfilter.mark(words) # update the filter by marking it
            
            if COUNTER_SKIP ==  99:  
                pos_words.append(words) 
                
            COUNTER_SKIP += 1
            
        else:
            words = words.rstrip("\n") # take out return char
            neg_words.append(words) 
            COUNTER_SKIP = 0    #  Don't add the Word
            print "this word will not be inserted: " , words
            
    # ----------------------------------------------------------------------
    #  Now to Test our data:

    print '\n'
    
    for words in range(20):     # range can only max out at size of array (122)

        piece1 =  "Word in pos array: {0:<15}".format( pos_words[words])
        piece2 = " Found in list: %r " % (bfilter.lookup(pos_words[words]))
    
        piece3 =  "Word in neg array: {0:<15}".format( neg_words[words])
        piece4 = " Found in list: %r " % (bfilter.lookup(neg_words[words]))
        
        print  piece1 + piece2 + "   " + piece3 + piece4

                                
    print "\nProgram Terminated.\n" 
    
if __name__=='__main__':
                                                         
        main()

