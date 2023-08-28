# let us first get to the existing implementation
'''
Principles
1. Separate things that change or might change from thing that don't.
2. Program to supertype or interface (*not* to implementation)
'''

#supertype
class FlyBehaviour:

  def fly():
    '''
    abstract method that must be implemented by the class that decides to implemnt FlyBehaviour
    '''
    pass


# flybehaviour implmentors
class FlyWithWings(FlyBehaviour):
  '''Specific implementation of FlyBehaviour'''

  def fly():
    '''implementation of flying with wings'''
    print('Flapping wings to fly high in the sky...')

class NoFly(FlyBehaviour):
  '''Specific implementation of FlyBehaviour'''

  def fly():
    '''implementation of flying with wings'''
    print('I cannot fly!')

class FlyWithRocketPower(FlyBehaviour):
  '''Rocket-powered implementation of FlyBehaviour'''

  def fly():
    print('Flying at super-speed... using Rocket power')

#supertype 2
class QuackBehaviour():
  '''Abstract class'''
  def quack():
    pass


# implementations
class Quack(QuackBehaviour):
  '''Quack implementation'''

  def quack():
    print('Quack! Quack! Quack!')
    

class Squeak(QuackBehaviour):
  '''Quack implementation'''

  def quack():
    print('Squeak! Squeak! Squeak!')


class MuteQuack(QuackBehaviour):
  '''Quack implementation'''

  def quack():
    print('..... silence')



'''
1 Using our new design, what would you do if you needed to add rocket-powered
flying to the SimUDuck app?
'''
'''
A new requirement as come along; hmm... I see. 
Looks like a new behaviour. But also just a light thinking about it reveals that
this is a behaviour that we had already predicted (not exactly, but to some extent). 
We already have this "FlyBehaviour" supertype/interface
'''

'''
2 Can you think of a class that might want to use the Quack behavior that isn’t a
duck?
'''
'''
Honestly, looks like very random. By having all the implementation have we not made the
QuackBehaviour, very duck specific or if we are being very generous, it looks like very
much attached to a bird. i mean an Elephant cannot use QuackBehaviour!
'''

# so far how does our implementation look

# we  have a Duck class

class Duck():
  '''A parent duck class'''

  # behaviours (those which are likely to change)
  def __init__(self):
    # in java it would have been something like this:
    # QuackBehaviour quackBehaviour (interface variable)
    self.quack_behaviour = QuackBehaviour()  # interface variable
    self.fly_behaviour = FlyBehaviour()
  
  # the behaviour that will change, we **delegate** that task of implementation
  # to corresponding behavour class's method
  # and since interfaces are contracts that must be implemented, it becomes **compulsory**
  # for that behaviour class to implement the behaviour
  def perform_fly():
    '''method responsible to make the duck fly'''
    self.fly_behaviour().fly()

  def perform_quack():
    '''method responsible to make the duck fly'''
    self.quack_behaviour().quack() # what happens on perform_quack will depend on the self.quack_behaviour's implementation of quacking


  # methods/behaviours which are less likely to vary across Duck types
  def swim():
    ''' method that is responsible to maket ducks swim'''
    print('implementation of swim behaviour')

  def display():
    ''' method that is responsible to pressent ducks'''
    print('implementation of appearance of duck')


# so let us say if the team comes up with a new type of Duck -> MallardDuck
class MallardDuck(Duck):
  '''Mallard duck inherits from the general Duck'''

  def __init__(self):
    # this is the quack_behaviour that was declared in the Duck class (with python it is not very clear)
    # quackBehaviour = new Quack() # in java (Quack behaviour will be assigned to behaviour reference variable that was declared in Duck constructor
    self.quack_behaviour = Quack()  # out of all the quacking behaviours [Quack, Squeak, Mute], we *chose* Quack
    self.fly_behaviour = FlyWithWings()  # out of all the available fly behaviour we *chose* FlyWithWings

  def display():
    '''method to implement display'''
    print('method to swim')


# problem: Should we should **NOT** code to implementation, something that we actually ended up doing in the constructor!
# instantiating Quack class object in the constructorA

### difficult to have interface type in python ###


'''
Take a moment and think about how you would implement a duck so that its
behavior could change at runtime.
'''
''' does that mean: if a duck was initialized with quacking could be changed to squeaking?'''
class DynamicDuck(Duck):
  
  '''
  def set_quacking(quack_type):
    ' a method to assign various behaviuor at run time to a duck'
    if quack_type == 'quack':
      self.quack_behaviour = new Quack();
    elif quack_type == 'squeak':
      self.quack_behaviour = new Squeak();
    elif quack_type == 'mute':
      self.quack_behaviour = new Mute();
  '''

  # for python also we could do something like: 
  def set_quacking(quacking_behaviour_interface_obj):
    self.quacking_behaviour = quacking_behaviour_interface_obj

      
  # or may in java
  # argument is interface type
  '''
  public void setQuacking(QuackBehaviour quackBehavoiur) {
    this.quackBehavour = new quackBehaviour;
  }
  '''



'''if this means that how to dynamically set the quacking behaviour at the time of creation of duck obj'''
class NewDuck(Duck):
  
  def __init__(self, quack_type):
    '''constructor'''
    if quack_type == 'squeak':
      #quackBehaviour = new Squeak(); //(quackBehaviour is a reference variable of 'interface type')
      self.quack_behaviour = Squeak()
    else:
      # quackBehaviour = new Quack();
      self.quack_behaviour = Quack()
  # above can also be written in java
   


####### Testing #######

class DuckSimulator():
  '''class to simulate the existing ducks'''

  def main():
    mallard_duck = MallardDuck()
    mallard_duck.perform_fly()
    mallard_duck.perform_quack()
    
    ## dynamic ducI
    model_duck = DynamicDuck()
    model_duck.perform_quack()  # would just quack
    model_duck.set_quacking(Squeak())
    model_duck.perform_quack()  # would not start 'squeaking' instead



