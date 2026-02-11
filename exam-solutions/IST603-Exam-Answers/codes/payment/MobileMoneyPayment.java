
/**
 * Class implementing mobile money payment
 */

public class MobileMoneyPayment implements PaymentMethod {
  private String phoneNumber;

  /**
   * Constructor to initialize MobileMoneyPayment.
   * 
   * @param phoneNumber The mobile money phone number
   */
  public MobileMoneyPayment(String phoneNumber){
    this.phoneNumber = phoneNumber;
  }

  /**
   * Implements the pay() method from PaymentMethod interface
   * Process payment via mobile money
   * 
   * @param amount The amount to be paid
   */
  @Override
  public void pay(double amount) {
    System.out.println("Processing mobile money payment...");
    System.out.println("Phone Number: " + phoneNumber);
    System.out.println("Amount: " + amount);
    System.out.println("Payment successful via mobile money!");
  }
}
