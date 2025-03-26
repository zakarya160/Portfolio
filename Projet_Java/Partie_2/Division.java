public class Division extends Operation {
    
    public Division(Expression op1, Expression op2) {
        super(op1, op2);
    }
     
    /*public double valeur() {
        double operande1 = this.getOperande1().valeur();
        double operande2 = this.getOperande2().valeur();
        if (operande2 == 0.0) {
            System.out.println("\nDivision par zéro impossible.");
            throw new ArithmeticException("Division par zéro");
        }
        return operande1 / operande2;
    }*/

    public double valeur() {
        double operande1 = this.getOperande1().valeur();
        double operande2 = this.getOperande2().valeur();
        try {
            double test = operande1 / operande2;
        }

        catch(ArithmeticException o) {
            System.out.println("\nDivision par zéro impossible.");
            throw o;
        }
        finally { return operande1 / operande2; }
    }
    
    public String toString() {
        return "(" + this.getOperande1().toString() + " / " + this.getOperande2().toString() + ")";
    }
}