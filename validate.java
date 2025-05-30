// validate.java
public class validate {
    public static void main(String[] args) {
        try {
            String input = args[0];
            if (input.matches("[-+*/]?[0-9]+(\\s+[-+*/]\\s+[0-9]+)?([iI])?")) {
                System.out.println("VALID");
            } else {
                System.out.println("INVALID");
            }
        } catch (Exception e) {
            System.out.println("INVALID");
        }
    }
}
