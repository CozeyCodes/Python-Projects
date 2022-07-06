class school:
    
    numstu = 0
    
    @classmethod
    def count(cls):
        cls.numstu +=1
        print(f"{cls.numstu} PERSON HAS BEEN ADDED!")


p = 5
while p > 0:
    p -=1 
    school.count()
