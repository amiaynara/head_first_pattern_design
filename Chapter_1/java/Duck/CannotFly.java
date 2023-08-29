package duck.FlyBehaviour;

// import QuackBehaviour interface
// import Duck.FlyBehaviour;

public class CannotFly implements FlyBehaviour {
  public void fly() {
    System.out.println("Cannot Fly!");
  };
}
