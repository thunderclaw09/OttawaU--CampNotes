class Car 
{
    private int MAX_SPEED; //Generally, all caps means that it shouldn't change.
    private String bodyColor; //This is called Camel Case
    private String carMake;
    private String carModel;

    private boolean isRunning;
    private int currentSpeed;

    Car(String bodyColor, String carMake, String carModel, int maxSpeed) //This is a CONSTRUCTOR
    {
        this.MAX_SPEED = maxSpeed; //In Python, they use 'self.MAX_SPEED', but other languages uses 'this'
        this.isRunning = false;
        this.bodyColor = bodyColor;
        this.carMake = carMake;
        this.carModel = carModel;
        this.currentSpeed = 0;
    }

    public void accelerate(int speedIncrease)
    {
        if(isRunning)
        {
            currentSpeed += speedIncrease;
            if(currentSpeed > MAX_SPEED)
            {
                currentSpeed = MAX_SPEED;
                return; //This replaces an else statement and stops the function right here, preventing the error message from just running even when not needed.
            }
            System.err.println("Cannot Accelerate Car When not Running!");
        }
    }

    // (Note that not all are copied over, just one of each example)

    public int getMaxSpeed() //This is a getter. It's the opposite of a setter, though it has the same principle. Basically, it lets us access a private variable.
    {
        return MAX_SPEED;
    }

    public void turnOn(){if(!isRunning) isRunning = true;} //You can also stuff an entire function out on one line, as you can see here.
    public void turnOff(){if(isRunning) isRunning = false;}
}