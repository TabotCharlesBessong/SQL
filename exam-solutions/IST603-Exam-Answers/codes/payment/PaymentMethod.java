/**
 * Interface defining the contract for payment methods.
 * Any class implementing this interface must provide a pay() method.
 */
public interface PaymentMethod {

  /**
   * Processes a payment for the given amount.
   * 
   * @param amount The amount to be paid
   */
  void pay(double amount);
}
