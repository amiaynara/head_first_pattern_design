public interface SubjectInterface {
    // subject specific methods
    void registerObserver(Observer observer);
    void removeObserver(Observer observer);
    void notifyObserver();

    // hook
    void measurementChange();

//    // methods that define the states of the weather objects
//    void getTemperature();
//    void getPressure();
//    void getHumidity();

}
