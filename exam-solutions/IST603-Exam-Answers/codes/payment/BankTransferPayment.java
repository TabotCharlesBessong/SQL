/**
 * Class implementing bank transfer payment method.
 */
public class BankTransferPayment implements PaymentMethod {

  private String accountNumber;
  private String bankName;

  /**
   * Constructor to initialize BankTransferPayment.
   * 
   * @param accountNumber The bank account number
   * @param bankName      The name of the bank
   */
  public BankTransferPayment(String accountNumber, String bankName) {
    this.accountNumber = accountNumber;
    this.bankName = bankName;
  }

  /**
   * Implements the pay() method from PaymentMethod interface.
   * Processes payment via bank transfer.
   * 
   * @param amount The amount to be paid
   */
  @Override
  public void pay(double amount) {
    System.out.println("Processing bank transfer payment...");
    System.out.println("Bank: " + bankName);
    System.out.println("Account Number: " + accountNumber);
    System.out.println("Amount: " + amount);
    System.out.println("Payment successful via bank transfer!");
  }
}