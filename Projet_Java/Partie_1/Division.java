public class Division extends Operation {
    public Division(Nombre op1, Nombre op2) {
        super(op1, op2);
    }
     
    public int valeur() {
        try {
            int test = this.getOperande1().valeur() / this.getOperande2().valeur();
        }

        catch(ArithmeticException o) {
            System.out.println("\nDivision par zéro impossible.");
            throw o;
        }

        finally { return this.getOperande1().valeur() / this.getOperande2().valeur(); }
    }
    
    public String toString() {
        return "(" + this.getOperande1().toString() + " / " + this.getOperande2().toString() + ")";
    }
}