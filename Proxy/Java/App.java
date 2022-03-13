public class App {
    public static void main(String arg[]){
        Cuenta debito = new Cuenta(1, "noe", 1000);

        Icuenta cuenta = new CuentaProxy(new CuentaBanco());
        cuenta.mostrarSaldo(debito);
        debito = cuenta.depositarDinero(debito, 500);
        debito = cuenta.retirarDinero(debito, 200);
        cuenta.mostrarSaldo(debito);
    }
}
