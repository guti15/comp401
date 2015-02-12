Senior Seminar
==============
# comp401

Repository for Senior Sem  [comp 401](https://github.com/WheatonWHALE/comp401): Senior Seminar Wheaton college

### Project One: Bloom Filter

![Bloom Filter](http://img3.douban.com/view/note/large/public/p8006482.jpg)

This filter is great on memory, as it test whether or not an item is on the set. The Bloom Filter, searches whether or not an item is on the array, by marking a bit array. Bloom filter usually contain more than one hash functions, marking the Bit array more than once.
The Draw Backs:  This data structure fails to tell us weather the item is in the array, just the possibility that it 'might be' or 'not in the set'.  For more information, and clarity Wikipedia has more detailed information [Bloom Filter](http://en.wikipedia.org/wiki/Bloom_filter). 

#####Functionality
Functionality of Bloom Filter:
* *mark* - reads in a string, which is then _Hashed_ with a unique code
* *lookup* - searches for a string in the Bloom Filter. Checks every possible index
* *number of bits* - Calculates how big the _Bit Array_ should be. Depends on your ideal False Positive.
* *Num hash apply* - Calculate the adequate number of _Hash Functions_
* False postive rate - Calculates the false postive given _bits in filter, number of hashes, number of elements_


#### Complexity Analysis
**Bloom Filter mark:**


**Bloom Filter lookup:**




####Resources Used:
[Wikipedia](http://en.wikipedia.org/wiki/Bloom_filter)
[Python 2.7 documentation](https://docs.python.org/2.7/)
[dev/maverick Blog](http://ilyasterin.com/blog/2010/02/implementing-bloom-filter-with-a-murmur-hash-function.html)









