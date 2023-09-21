//package duck;

//import duck.MallardDuck;

public class DuckSimulator {
  public static void main(String[] args) {
    Duck mallard = new MallardDuck();
    mallard.performFly();
    mallard.performQuack();
    Duck modelDuck = new ModelDuck();
    modelDuck.performFly();

    // Duck call device
    DuckCall duckCall = new DuckCall();
    duckCall.performCall();
    // device user wants to change the sound of the device
    duckCall.setCallBehaviour(new Squeak());
    duckCall.performCall();
  } 
}
