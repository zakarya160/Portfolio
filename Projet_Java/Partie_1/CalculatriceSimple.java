public class CalculatriceSimple {
    public static void main(String[] args) {

        // Addition

        try {
            Nombre quatre = new Nombre(4);
            Nombre un = new Nombre(1);
            Operation a = new Addition(quatre, un);
            System.out.println("\nAddition : " + a.toString() + " = " + a.valeur()); // doit afficher : (4 + 1) = 5
        }
        catch(Exception o) {
            System.out.println("Exception : " + o);
        }

        // Soustraction

        try {
            Nombre six = new Nombre(6);
            Nombre dix = new Nombre(10);
            Operation s = new Soustraction(dix, six);
            System.out.println("\nSoustraction : " + s.toString() + " = " + s.valeur()); // doit afficher : (10 - 6) = 4
        }
        catch(Exception o) {
            System.out.println("Exception : " + o);
        }

        // Multiplication

        try {
            Nombre neuf = new Nombre(9);
            Nombre trois = new Nombre(3);
            Operation m = new Multiplication(neuf, trois);
            System.out.println("\nMultiplication : " + m.toString() + " = " + m.valeur()); // doit afficher : (9 * 3) = 27
        }
        catch(Exception o) {
            System.out.println("Exception : " + o);
        }

        // Division

        try {
            Nombre huit = new Nombre(8);
            Nombre deux = new Nombre(2);
            Operation d1 = new Division(huit, deux);
            System.out.println("\nDivision n°1 : " + d1.toString() + " = " + d1.valeur()); // doit afficher : (8 / 2) = 4
        }
        catch(Exception o) {
            System.out.println("Exception : " + o);
        }

        // Division par zéro

        try {
            Nombre cinq = new Nombre(5);
            Nombre zero = new Nombre(0);
            Operation d2 = new Division(cinq, zero);
            System.out.println("\nDivision n°2 : " + d2.toString() + " = " + d2.valeur()); // doit afficher le message d'erreur suivant : Division par zéro impossible.
        }
        catch(Exception o) {
            System.out.println("Exception : " + o);
        }
    }
}