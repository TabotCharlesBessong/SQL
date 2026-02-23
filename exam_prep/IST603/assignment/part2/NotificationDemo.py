"""
Notification interface and implementations using:
- Local inner class (defined inside a method)
- Anonymous-style inner class (one-off implementation in another method)
Comments explain when each type is appropriate in Python.
"""

from abc import ABC, abstractmethod


class Notification(ABC):
    """Interface: implementers must define send_message()."""

    @abstractmethod
    def send_message(self) -> None:
        ...


class NotificationDemo:
    def use_local_inner_notification(self) -> None:
        """
        Use a LOCAL INNER CLASS when you need a named implementation that is
        only used within a single method and may capture that method's variables.
        """
        context = "Local"  # effectively final; can be used by inner class

        class EmailNotification(Notification):
            def send_message(self) -> None:
                print("[Local inner] Email notification: Your application has been received.")

        n: Notification = EmailNotification()
        n.send_message()

    def use_anonymous_inner_notification(self) -> None:
        """
        Use an ANONYMOUS-STYLE (one-off) inner class when you need a single
        implementation used only once. In Python we still name the class inside
        the method, but it is not reused elsewhere—the analogue of Java's anonymous inner class.
        """
        class SmsNotification(Notification):
            def send_message(self) -> None:
                print("[Anonymous inner] SMS notification: Your code has been verified.")

        n: Notification = SmsNotification()
        n.send_message()


def main() -> None:
    demo = NotificationDemo()
    demo.use_local_inner_notification()
    demo.use_anonymous_inner_notification()


if __name__ == "__main__":
    main()
