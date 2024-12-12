from cat import Cat

def main():
     dramatic_cat = Cat("Black","Black","Brown","dramatic",5,"Shamspear")
     print(dramatic_cat)
     dramatic_cat.speak()
     fake_cat = Cat("Dog","Brown","Blue","too kind",4,"DefCat")
     print(fake_cat)
     fake_cat.speak()

if __name__=='__main__':
     main()