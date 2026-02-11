
/**
 * Class representing a tuition payment.
 * Extends the Payment abstract class.
 */

public class TuitionPayment extends Payment {
  /**
   * Constructor to initialize a TuitionPayment object.
   * 
   * @param matricule The student's matriculation number
   * @param amount    The tuition payment amount
   */

   public TuitionPayment(String matricule, double amount){
    super(matricule,amount);
   }

   /**
    * Implements the abstract processPayment() method.
    * Displays a message indicating that tuition payment is being processed.
    */

    @Override
    public void processPayment(){
      System.out.println("Processing tuition payment for matricule: " + matricule);
      System.out.println("Amount paid: " + amount);
    }
}
