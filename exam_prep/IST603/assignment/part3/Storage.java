package exam_prep.IST603.assignment.part3;

/**
 * Generic class Storage<T> that can store and retrieve an object of any type.
 * Demonstrates type-safe storage and how generics prevent type-casting errors at compile time.
 */
public class Storage<T> {
    private T value;

    public void set(T value) {
        this.value = value;
    }

    public T get() {
        return value;
    }

    public static void main(String[] args) {
        // Store an Integer
        Storage<Integer> intStorage = new Storage<>();
        intStorage.set(42);
        Integer n = intStorage.get();  // No cast needed; type is known at compile time
        System.out.println("Integer: " + n);

        // Store a String
        Storage<String> strStorage = new Storage<>();
        strStorage.set("Hello");
        String s = strStorage.get();   // No cast needed
        System.out.println("String: " + s);

        // Generics prevent type-casting errors at compile time:
        // - intStorage.set("wrong");     // COMPILE ERROR: incompatible types
        // - String bad = intStorage.get(); // COMPILE ERROR: incompatible types
        // Without generics (raw type), these would only fail at runtime with ClassCastException.
    }
}
