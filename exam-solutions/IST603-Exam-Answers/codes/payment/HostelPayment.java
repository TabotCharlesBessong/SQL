/**
 * Class representing a hostel payment.
 * Extends the Payment abstract class.
 */
public class HostelPayment extends Payment {

  /**
   * Constructor to initialize a HostelPayment object.
   * 
   * @param matricule The student's matriculation number
   * @param amount    The hostel payment amount
   */
  public HostelPayment(String matricule, double amount) {
    super(matricule, amount);
  }

  /**
   * Implements the abstract processPayment() method.
   * Displays a message indicating that hostel payment is being processed.
   */
  @Override
  public void processPayment() {
    System.out.println("Processing hostel payment for matricule: " + matricule);
    System.out.println("Amount paid: " + amount);
  }
}