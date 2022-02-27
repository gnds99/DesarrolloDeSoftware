
public class CuentaProxy implements Icuenta {
    //private CuentaBanco cuentaReal;
    private Icuenta cuentaReal;

    public CuentaProxy(Icuenta cuentaReal){
        this.cuentaReal = cuentaReal;
    }
     
    @Override
    public Cuenta retirarDinero(Cuenta cuenta, double monto){
        if (cuentaReal == null){ 
            cuentaReal = new CuentaBanco();
             return cuentaReal.retirarDinero(cuenta, monto);
        } else{
            return cuentaReal.retirarDinero(cuenta, monto);
        }
    }

    public Cuenta depositarDinero(Cuenta cuenta, double monto){
        if (cuentaReal == null){
            cuentaReal = new CuentaBanco();
            return cuentaReal.depositarDinero(cuenta, monto);
        }else{
            return cuentaReal.depositarDinero(cuenta, monto);
        }
    }

    public void mostrarSaldo(Cuenta cuenta){
        if(cuentaReal == null){
            cuentaReal = new CuentaBanco();
            cuentaReal.mostrarSaldo(cuenta);
        }else{
            cuentaReal.mostrarSaldo(cuenta);
        }
    }

}
