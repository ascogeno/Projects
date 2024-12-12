from cat import Cat

def main():
    ranger = Cat("American Shorthair","tabby","green","evil",5,"Ranger")
    print(ranger)
    ranger.speak()      
    
    bandit = Cat("American Shorthair","black/white","green","chaotic good",5,"Bandit")
    print(bandit)    
    bandit.speak()    
    
    mellow = Cat("Ragdoll","white","blue","weird",3,"Mellow")
    print(mellow)
    mellow.speak()
    
    stray = Cat()
    print(stray)
    
if __name__=='__main__':
  main()