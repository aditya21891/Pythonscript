# A python script to Learn OrderDict from Collections 
from collections import OrderedDict

hero=OrderedDict([(1,'Mahesh'),(2,'Pawan'),(3,'NTR'),])

for num,name in hero.items():
	print(num,name)