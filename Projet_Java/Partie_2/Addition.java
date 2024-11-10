public class Addition extends Operation {
    public Addition(Expression op1, Expression op2) {
        super(op1, op2);
    }
    
    public double valeur() {
        return this.getOperande1().valeur() + this.getOperande2().valeur();
    }
    
    public String toString() {
        return "(" + this.getOperande1().toString() + " + " + this.getOperande2().toString() + ")";
    }
}