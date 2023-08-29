package duck.MallardDuck;

// import duck class
// import duck.FlyBehaviour.*;
// import duck.QuackBehaviour.*;
import duck.*;
import duck.QuackBehaviour.Quack;
import duck.FlyBehaviour.FlyWithWings;

public class MallardDuck extends Duck {

  public MallardDuck() {
    this.quackBehaviour = new Quack();
    this.flyBehaviour = new FlyWithWings();
  }
  public void display() {
    System.out.println("I am a real mallard duck");
  }
}
