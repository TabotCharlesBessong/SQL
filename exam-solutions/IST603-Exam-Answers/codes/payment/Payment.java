
public abstract class Payment {

  /**
   * The student's matriculation number (Student ID)
   */
  protected String matricule;

  /**
   * The amount to be paid
   */
  protected double amount;

  /**
   * Constructor to initialize a payment object
   * @param maticule The student matriculation number
   * @param amount The payment amount
   */

  public Payment(String matricule, double amount){
    this.matricule = matricule;
    this.amount = amount;
  }

  /**
   * Abstract method to print the payment receipt
   * Must be implemented by subclasses to define specific payment processing logic
   */
  public abstract void processPayment();

  /**
   * Concrete method to print the payment receipt
   * Displayts the matriculation and the amount
   */

  public void printReceipt(){
    System.out.println("=== PAYMENT RECEIPT ===");
    System.out.println("Matriculation: " + matricule);
    System.out.println("Amount Paid: " + amount);
    System.out.println("=====================");
  }

  /**
   * Getter method for matricule
   * 
   * @return The student's matriculation number
   */
  public String getMatricule(){
    return matricule;
  }

  /**
     * Getter method for amount.
     * 
     * @return The payment amount
     */
    public double getAmount() {
      return amount;
    }
}