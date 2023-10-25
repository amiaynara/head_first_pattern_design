public class MallardDuck extends Duck {

  public MallardDuck() {
    this.quackBehaviour = new Quack();
    this.flyBehaviour = new FlyWithWings();
  }
  public void display() {
    System.out.println("I am a real mallard duck");
  }
}
