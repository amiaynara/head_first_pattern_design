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
    quack_behaviour = Quack()  # out of all the quacking behaviours [Quack, Squeak, Mute], we *chose* Quack
    fly_behaviour = FlyWithWings()  # out of all the available fly behaviour we *chose* FlyWithWings
  
  # the behaviour that will change, we **delegate** that task of implementation
  # to corresponding behavour class's method
  # and since interfaces are contracts that must be implemented, it becomes **compulsory**
  # for that behaviour class to implement the behaviour
  def perform_fly():
    '''method responsible to make the duck fly'''
    fly_behaviour().fly()

  def perform_quack():
    '''method responsible to make the duck fly'''
    quack_behaviour().quack() # what happens on perform_quack will depend on the self.quack_behaviour's implementation of quacking


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
    quack_behaviour = Quack()  # out of all the quacking behaviours [Quack, Squeak, Mute], we *chose* Quack
    fly_behaviour = FlyWithWings()  # out of all the available fly behaviour we *chose* FlyWithWings

  def perform_fly():
    '''method responsible to make the duck fly'''
    fly_behaviour().fly()

  def perform_quack():
    '''method responsible to make the duck fly'''
    quack_behaviour().quack() # what happens on perform_quack will depend on the self.quack_behaviour's implementation of quacking

# problem: Should we not always code to 
