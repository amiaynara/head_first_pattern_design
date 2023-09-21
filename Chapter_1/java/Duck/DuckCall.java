public class DuckCall {
    // a device that mimics the call of a duck
    // we need a device whose call can be varied during operation
    // we should not need a new device for every type of duck
    QuackBehaviour quackBehaviour;

    public DuckCall() {
        // by default let us give the "normal" quacking sound to the device as well
        this.quackBehaviour = new Quack();
        this.display();
    }

    public void display() {
        System.out.println("I am a DuckCall... not a real duck");
    }
    public void performCall() {
        this.quackBehaviour.quack();
    }

    public void setCallBehaviour(QuackBehaviour cb) {
        // user of the device can change the quacking sound coming out of the device
        // in fact they can choose from (quack, squeak or silent)
        System.out.println("Changing Calling sound");
        this.quackBehaviour = cb;
    }
}
