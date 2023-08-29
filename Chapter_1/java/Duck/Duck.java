package duck;
// import the Behaviour Classes
// import duck.FlyBehaviour;
// import duck.QuackBehaviour;
import duck.QuackBehaviour.*;
import duck.FlyBehaviour.*;

public class Duck {
  // Changing behaviour that we want to assinged at runtime
  public FlyBehaviour flyBehaviour;
  public QuackBehaviour quackBehaviour;

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

  public void swim() {
    System.out.println("All ducks float, even decoys");
  }
}
