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
