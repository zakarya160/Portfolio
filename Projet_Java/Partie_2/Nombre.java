public class Nombre extends Expression {
    private int valeurNombre;
    
    public Nombre(int nb) {
        this.valeurNombre = nb;
    }
    
    public double valeur() {
        return this.valeurNombre;
    }
    
    public String toString() {
        return "" + this.valeurNombre;
    }
}