
public class HelmentDecorator extends EnemyDecorator {
    
    HelmentDecorator(Enemy enemy) {
        super(enemy);
    }

    @Override
    public int takeDamage() {
        return this.enemy.takeDamage() / 2;
    }
}
