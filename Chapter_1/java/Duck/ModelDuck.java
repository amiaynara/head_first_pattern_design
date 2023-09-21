import java.io.ObjectInputValidation;

import javax.swing.plaf.synth.SynthSplitPaneUI;

public class ModelDuck extends Duck {
    public ModelDuck() {
        this.flyBehaviour = new CannotFly();
        this.quackBehaviour = new Quack();
    }

    /*
     * display of the duck
     */
    public void display() {
        System.out.println("I am a model duck.");
    }
}
