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


