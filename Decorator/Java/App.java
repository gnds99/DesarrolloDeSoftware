
public class App
{
    public static void main(String args[])
    {
        Enemy enemy = new DifficultEnemy();
        Enemy enemyWithHelmet = new HelmentDecorator(enemy);
        Enemy enemyWithHelmetAndArmour = new ArmourDecorator(enemyWithHelmet);

        int computedDamaged = enemyWithHelmetAndArmour.takeDamage();
        System.out.println(computedDamaged);
    }
}