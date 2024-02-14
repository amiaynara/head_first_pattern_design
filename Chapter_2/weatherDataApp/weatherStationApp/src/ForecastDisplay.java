public class ForecastDisplay implements ObserverInterface, DisplayInterface {
    public void display() {
        System.out.println("Displaying data");
    }

    public void update() {
        System.out.println("Updating the info...");
    }
}
