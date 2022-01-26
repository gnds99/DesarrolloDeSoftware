public class Rectangle implements Shape {
    @Override
    public void draw()
    {
        for(int i = 0; i < 3; i++)
        {
            for(int j = 0; j < 8; j++)
            {
                System.out.print("* ");
            }
            System.out.println("");
        }
    }
    
}
