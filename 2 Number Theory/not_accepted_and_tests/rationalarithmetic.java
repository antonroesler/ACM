import java.util.Scanner;
import java.math.BigInteger;
public class rational_arithmetic_java {

public static void main(String[] args) {
Scanner scan = new Scanner(System.in);

int n = scan.nextInt();

for (int i = 0; i < n; i++)
    {
    BigInteger x1 = new BigInteger(scan.next());
    BigInteger y1 = new BigInteger(scan.next());

    String operand = scan.next();

    BigInteger x2 = new BigInteger(scan.next());
    BigInteger y2 = new BigInteger(scan.next());

    BigInteger r1;
    BigInteger r2;

    if (operand.equals("+"))
        {
        r1 = (x1.multiply(y2)).add( x2.multiply(y1));
        r2 = y1.multiply(y2);
        }
    else if (operand.equals("-"))
        {
        r1 = (x1.multiply(y2)).subtract(x2.multiply(y1));
        r2 = y1.multiply(y2);
        }
    else if (operand.equals("*"))
        {
        r1 = x1.multiply(x2);
        r2 = y1.multiply(y2);
        }
    else
        {
        r1 = x1.multiply(y2);
        r2 = y1.multiply(x2);
        }

    BigInteger ggt = r1.gcd(r2);
    r1 = r1.divide(ggt);
    r2 = r2.divide(ggt);

    if (r2.compareTo(BigInteger.ZERO) < 0)
        {
        r2 = r2.negate();
        r1 = r1.negate();
        }

    System.out.println(r1 + " / " + r2);
    }

scan.close();
    }
}
