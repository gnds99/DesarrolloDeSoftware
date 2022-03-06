
public abstract class EnemyDecorator implements Enemy {
    
    protected Enemy enemy;

    EnemyDecorator( Enemy enemy){
        this.enemy = enemy;
    }

    @Override
    public int takeDamage() {
        return this.enemy.takeDamage();
    }
}
