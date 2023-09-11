import names
import random 
import time
import tracemalloc


class People():
    def __init__(self, id, name, phone) :
        self.id = id
        self.name = name
        self.phone =phone

    def __str__(self):
        return f"{self.id},{self.name},{self.phone}"
    


def people_list(count):
    result =[]
    id = 0
    while id <= count:
        name = names.get_first_name()
        phone = f"+374-77{random.randint(100000, 999999)}"
        result.append(People(id,name,phone))
        id+=1
    return result

def people_generator(count):
    id =0
    name = names.get_first_name()
    phone = f"+374-77{random.randint(100000, 999999)}"
    yield(People(id,name,phone))
    id+=1



tracemalloc.start()
start = time.time()
# peoples = people_list(10000) 
peoples = people_generator(10000)   
for people in peoples:
    print(people)
print(f"used memory is: {tracemalloc.get_tracemalloc_memory() * 0.000001}  mb")    
end = time.time() 
tracemalloc.stop()    
 
print(f" Time is:  {end - start}") 


# people_list is
# used memory is: 3.44548  mb
# Time is:  6.327702522277832


# people_generator is
# used memory is: 0.008616  mb
# Time is:  0.0008115768432617188