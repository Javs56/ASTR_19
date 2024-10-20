#Write a Python program that declares a class describing your favorite animal. 
#Have the data members of the class represent the following physical parameters of the animal: length of the arms (float), 
#length of the legs (float), number of eyes (int), does it have a tail? (bool), is it furry? (bool). 
#Write an initialization function that sets the values of the data members when an instance of the class is created. 
#Write a member function of the class to print out and describe the data members representing the physical characteristics 
#of the animal.

class animal:
    def print(self):
        print(f'My animal has arms of length {self.arm_length}, legs of length {self.leg_length}, and {self.num_eyes} eyes')
        print(f'Does it have a tail? {self.has_tail}. Is it furry? {self.is_furry}.')
    def __init__(self,arm,leg,eyes,tail,furry):
        self.arm_length = arm
        self.leg_length = leg
        self.num_eyes = eyes
        self.has_tail = tail
        self.is_furry = furry


def main():
    arm_length = 3.7
    leg_length = 7.0
    num_eyes = 2
    has_tail = True
    is_furry = True
    
    mypet = animal(arm = arm_length, leg=leg_length, eyes=num_eyes,tail=has_tail, furry=is_furry)
    
    mypet.print()
    
if __name__=="__main__":
    main()
