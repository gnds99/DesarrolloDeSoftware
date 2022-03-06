
public class ArmourDecorator extends EnemyDecorator {

    ArmourDecorator(Enemy enemy) {
        super(enemy);
    }

    public int takeDamage()
    {
        return (int) (this.enemy.takeDamage() / 1.5);
    }
    
}
