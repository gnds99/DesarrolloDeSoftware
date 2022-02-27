public interface Icuenta {
    Cuenta retirarDinero(Cuenta cuenta, double monto);
    Cuenta depositarDinero(Cuenta cuenta, double monto);
    void mostrarSaldo(Cuenta cuenta);
}
 