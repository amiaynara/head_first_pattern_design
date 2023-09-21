// package duck;
// import the Behaviour Classes
// import duck.FlyBehaviour;
// import duck.QuackBehaviour;
// import duck.QuackBehaviour.*;
// import duck.FlyBehaviour.*;

public class Duck {
  // Changing behaviour that we want to assinged at runtime
  public FlyBehaviour flyBehaviour;
  public QuackBehaviour quackBehaviour; // encapsulates a family of algorithms that are interchangeable
  // this duck class HAS-A QuackBehaviour to which it delegates the task of quacking
  /*
  When you put two classes together like this you’re using **composition.**
  Instead of inheriting their behavior, the ducks get their behavior by being
  composed with the right behavior object.
    **Favor composition over inheritance.** 
    Not only does it let you encapsulate a family of algorithms into
  their own set of classes, but it also lets you change behavior at runtime as
  long as the object you’re composing with implements the correct behavior
  interface.
  */ 

  /**
   * 
   */
  //public void display();

  public void performFly() {
    flyBehaviour.fly();
  }

  public void performQuack() {
    quackBehaviour.quack();
  }

  public void setFlyBehaviour(FlyBehaviour fb) {
    flyBehaviour = fb;
  }

  public void setQuackBehaviour(QuackBehaviour qb) {
    quackBehaviour = qb;
  }

  public void swim() {
    System.out.println("All ducks float, even decoys");
  }
}
