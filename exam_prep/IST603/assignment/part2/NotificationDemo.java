package exam_prep.IST603.assignment.part2;

/**
 * Notification interface and implementations using:
 * - Local inner class (inside a method)
 * - Anonymous inner class (in another method)
 * Comments explain when each nested class type is appropriate.
 */

interface Notification {
    void sendMessage();
}

class NotificationDemo {

    /**
     * Uses a LOCAL INNER CLASS implementing Notification.
     * Use a local inner class when you need a named implementation that is
     * only used within a single method and may reference that method's
     * final or effectively final variables.
     */
    void useLocalInnerNotification() {
        final String context = "Local";

        class EmailNotification implements Notification {
            @Override
            public void sendMessage() {
                System.out.println("[Local inner] " + context + " email notification: Your application has been received.");
            }
        }

        Notification n = new EmailNotification();
        n.sendMessage();
    }

    /**
     * Uses an ANONYMOUS INNER CLASS implementing Notification.
     * Use an anonymous inner class when you need a one-off implementation
     * of an interface (or subclass) that is used only once and does not
     * need a name or reuse elsewhere.
     */
    void useAnonymousInnerNotification() {
        Notification n = new Notification() {
            @Override
            public void sendMessage() {
                System.out.println("[Anonymous inner] SMS notification: Your code has been verified.");
            }
        };
        n.sendMessage();
    }

    public static void main(String[] args) {
        NotificationDemo demo = new NotificationDemo();
        demo.useLocalInnerNotification();
        demo.useAnonymousInnerNotification();
    }
}
