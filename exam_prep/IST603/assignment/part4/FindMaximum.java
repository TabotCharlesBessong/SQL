package exam_prep.IST603.assignment.part4;

/**
 * Generic method findMaximum() with bounded type parameters.
 * Accepts an array of numbers (Integer, Double, etc.) and returns the maximum value.
 */
public class FindMaximum {

    /**
     * Bounded type parameter: T must extend Number and be Comparable with itself,
     * so only numeric types (Integer, Double, Long, etc.) are allowed.
     */
    public static <T extends Number & Comparable<T>> T findMaximum(T[] array) {
        if (array == null || array.length == 0) {
            throw new IllegalArgumentException("Array must not be null or empty");
        }
        T max = array[0];
        for (int i = 1; i < array.length; i++) {
            if (array[i].compareTo(max) > 0) {
                max = array[i];
            }
        }
        return max;
    }

    public static void main(String[] args) {
        Integer[] ints = { 3, 7, 2, 9, 1 };
        System.out.println("Max Integer: " + findMaximum(ints));  // 9

        Double[] doubles = { 3.14, 2.71, 1.41 };
        System.out.println("Max Double: " + findMaximum(doubles));  // 3.14

        Long[] longs = { 100L, 50L, 200L };
        System.out.println("Max Long: " + findMaximum(longs));  // 200
    }
}
