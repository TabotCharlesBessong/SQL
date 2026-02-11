public class Main {
  public static void main(String[] args){
    System.out.println("=== UNIVERSITY E-PAYMENT MANAGEMENT SYSTEM===\n");

    // Create payment objects (polymorphism with payment references)
    Payment tuitionPayment = new TuitionPayment("SC25P089", 50000);
    Payment hostelPayment = new TuitionPayment("SC25P089", 12000);

    // Create payment method objects
    PaymentMethod mobileMoney = new MobileMoneyPayment("+237670203775");
    PaymentMethod bankTransfer = new BankTransferPayment("000011112222333","UBA");

    // Demonstrate payment processing
    System.out.println("--- Processing Tuition Payment ---");
    tuitionPayment.processPayment();
    tuitionPayment.printReceipt();

    System.out.println("\n--- Processing Hostel Payment ---");
    hostelPayment.processPayment();
    hostelPayment.printReceipt();

    // Demonstrate payment methods
    System.out.println("\n--- Using Mobile Money Payment Method ---");
    mobileMoney.pay(50000.0);

    System.out.println("\n--- Using Bank Transfer Payment Method ---");
    bankTransfer.pay(30000.0);

    // Demonstrate polymorphism: Using Payment reference
    System.out.println("\n--- Polymorphism Example: Payment Reference ---");
    Payment[] payments = {
        new TuitionPayment("ST2024003", 45000.0),
        new HostelPayment("ST2024004", 25000.0)
    };

    for (Payment payment : payments) {
      payment.processPayment();
      payment.printReceipt();
      System.out.println();
    }

    // Demonstrate polymorphism: Using PaymentMethod reference
    System.out.println("--- Polymorphism Example: PaymentMethod Reference ---");
    PaymentMethod[] methods = {
        new MobileMoneyPayment("+237699876543"),
        new BankTransferPayment("9876543210", "UBA Bank")
    };

    for (PaymentMethod method : methods) {
      method.pay(10000.0);
      System.out.println();
    }
  }
}
