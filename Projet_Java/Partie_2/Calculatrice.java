public class CalculatriceSimple {
    public static void main(String[] args) {

        ////////// Partie n°1 //////////

        System.out.println("Partie 1 : \n");

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
            Operation d = new Division(huit, deux);
            System.out.println("\nDivision n°1 : " + d.toString() + " = " + d.valeur()); // doit afficher : (8 / 2) = 4
        }
        catch(Exception o) {
            System.out.println("Exception : " + o);
        }

        // Division par zéro

        try {
            Nombre cinq = new Nombre(5);
            Nombre zero = new Nombre(0);
            Operation d1 = new Division(cinq, zero);
            System.out.println("\nDivision n°2 : " + d1.toString() + " = " + d1.valeur()); // doit afficher le message d'erreur suivant : Division par zéro impossible.
        }
        catch(Exception o) {
            System.out.println("Exception : " + o);
        }

        ////////// Partie n°2 //////////
        		
		System.out.println("\n\n\nPartie 2 : \n");
		
		try {
            Expression deux = new Nombre(2); 
            Expression trois = new Nombre(3); 
            Expression dixSept = new Nombre(17); 
            Expression s1 = new Soustraction(dixSept, deux); 
            Expression a1 = new Addition(deux, trois);
            Expression d2 = new Division(s1, a1);
            System.out.println("\nTest n°1 : " + d2.toString() + " = " + d2.valeur()); // doit afficher : ((17 - 2) / (2 + 3)) = 3 
        }
		catch (Exception o) {
			System.out.println("\nException : " + o);
        }
        
		try {
            Expression treize = new Nombre(13);
            Expression vingtDeux = new Nombre(22);
            Expression quaranteHuit = new Nombre(48);
            Expression dix = new Nombre(10);
            Expression onze = new Nombre(11);
            Expression s2 = new Soustraction(onze, treize);
            Expression a2 = new Addition(vingtDeux, s2); 
            Expression d3 = new Division(a2, dix);
            Expression m1 = new Multiplication(d3, quaranteHuit);
            System.out.println("\nTest n°2 : " + m1.toString() + " = " + m1.valeur()); // doit afficher : (((22 + (11 - 13)) / 10) * 48) = 96
        }
        catch (Exception o) {
			System.out.println("\nException : " + o);
		}

		try {
            Expression neuf = new Nombre(9); 
			Expression zero = new Nombre(0); 
			Expression d4 = new Division(neuf, zero);
			System.out.println("\n" + d4.toString() + " = " + d4.valeur()); // doit afficher le message d'erreur suivant : Division par zéro impossible.
		}
		catch (Exception o) {
			System.out.println("\nException : " + o);
		}
		
		try {
            Expression deux = new Nombre(2); 
            Expression trois = new Nombre(3); 
            Expression neuf = new Nombre(9); 
			Expression six = new Nombre(6) ; 
			Expression m2 = new Multiplication(deux, trois) ;
			Expression s3 = new Soustraction(six, m2) ;
			Expression d5 = new Division(neuf, s3) ;
			System.out.println("\n" + d5.toString() + " = " + d5.valeur()); // doit afficher le message d'erreur suivant : Division par zéro impossible.
		}
		catch (Exception o) {
			System.out.println("\nException : " + o);
		}
	}	
}