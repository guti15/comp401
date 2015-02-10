from BloomFilter import number_of_bits, num_hash_apply,num_hash_apply
from BloomFilter import BloomFilter
import math

def main():
    # nips full paper apprx: 1,900,000 words
    Estimate_Array = 2000000   
    FALSE_POSTIVE  = .01        # with a 1% error


    bits_filter = number_of_bits( Estimate_Array, FALSE_POSTIVE) 
    bits_filter = math.ceil(bits_filter) # number is a float, so we round 
    
    how_many_hash = num_hash_apply( bits_filter, Estimate_Array)
    how_many_hash = int(math.ceil(how_many_hash)) # round up

    bfilter = BloomFilter( Estimate_Array, how_many_hash) # establish Bloom
    
    read_file = open('./data_set/vocab.nips.txt', 'r') #  open the file 

    for words in read_file:     #  read list of words
        words = words.rstrip("\n") # take out return char
        bfilter.mark(words)        #  update the filter by marking it
        
    
    ASK = True                  # ask user to search for words
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
