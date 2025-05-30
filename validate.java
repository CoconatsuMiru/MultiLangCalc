import java.util.regex.*;

public class validate {
    public static void main(String[] args) {
        if (args.length != 1) {
            System.out.println("INVALID");
            return;
        }

        String input = args[0].trim();

        // Pattern allows: number [operator] number (operator can be + - * / ^)
        Pattern pattern = Pattern.compile("^\\s*\\d+\\s*([+\\-*/^])\\s*\\d+\\s*$");

        Matcher matcher = pattern.matcher(input);
        if (matcher.matches()) {
            System.out.println("VALID");
        } else {
            System.out.println("INVALID");
        }
    }
}
