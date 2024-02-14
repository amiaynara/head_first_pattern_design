import java.util.ArrayList;

public class WeatherData implements SubjectInterface {
    private ArrayList<Observer> observers;
    private float temperature;
    private float pressure;
    private float humidity;

    @Override
    public void registerObserver(Observer observer) {
        this.observers.add(observer);
    }

    @Override
    public void removeObserver(Observer observer) {
        // get the index of the observer
        int indexOfObserver = this.observers.indexOf(observer);
        if (i >= 0) {
            this.observers.remove(indexOfObserver);
        }
    }

    @Override
    public void notifyObserver() {
        for (Observer observer : observers) {
            observer.update(this.temperature, this.pressure, this.humidity);
        }
    }

    @Override
    public void measurementChange() {
        this.notifyObserver();
    }

    public float getTemperature() {
        return this.temperature;
    }

    public float getPressure() {
        return this.pressure;
    }

    public float getHumidity() {
        return this.humidity;
    }

    public void setMeasurements(float temperature, float pressure, float humidity) {
        this.temperature = temperature;
        this.pressure = pressure;
        this.humidity = humidity;
        this.measurementChange();
    }

}
