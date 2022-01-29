
import time
from functools import lru_cache
@lru_cache(maxsize=4)
def score(n):                    #lru cache
    time.sleep(3)
    return n
print( "110/1")
score(3)
print("200/2")
score(3)
print("300/2")