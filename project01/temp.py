def main()


if  :




    
    
    def mark(self, string):
        mark_here = self.encrypt(string) # create hash key 
        # end mark
        
    def encrypt(self, string):
        crypt_sha1 = hashlib.sha1() # call secure hash algorithm 
        crypt_sha1.update(string)
        key = crypt_sha1.hexdigest() #  gives a hexadecimal number
        key = int(key, 16)           #  convert the number
        
        crypt_mmh3 = mmh3.hash128(string) # second hash function
        
        # Hash Equation: gi(x) = h1(x) + ih2(x) % m
        for i in range(self.num_hash):
            location = (key + i * crypt_mmh3) % self.size
            self.bloom_array[location] = True

        # end encrypt





    def lookup(self, string):
        am_I_here = True                 # Assume the function exist
        am_I_here = self.decrypt(string) # create hash key and search
            
        if am_I_here == True:
            return True
        
        else:
            return False 
            
        # end lookup


    def decrypt(self, string):  # simlar to encrypt
        crypt_sha1 = hashlib.sha1() # secure hash Alg. method use again
        crypt_sha1.update(string)
        key = crypt_sha1.hexdigest() #  gives a hexadecimal number
        key = int(key, 16)           #  convert the number
        
        crypt_mmh3 = mmh3.hash128(string) # second hash algo

        # if this loop fails  once, we can be certain it does not exist
        for i in range(self.num_hash ):
            
            location = (key + i * crypt_mmh3) % self.size
            if self.bloom_array[location] == False: 
                return False    
            
        return True             # return True if found otherwise breaks
    



