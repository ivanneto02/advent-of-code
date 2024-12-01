import java.io.FileInputStream;
import java.io.IOException;
import java.util.ArrayList;
import java.util.Collections;
import java.util.List;
import java.util.Scanner;
import java.io.File; 
import java.util.Map;
import java.util.HashMap;

public class Main {

    public static int part1() {

        try {
            Scanner scanner = new Scanner(new File("main.txt"));

            List<Integer> left = new ArrayList<>();
            List<Integer> right = new ArrayList<>();

            while (scanner.hasNextInt()) {
                int i = scanner.nextInt();
                int j = scanner.nextInt();
                left.add(i);
                right.add(j);
            }


            Collections.sort(left);
            Collections.sort(right);

            int sum = 0;
            for (int b = 0; b < left.size(); b++) {
                sum += Math.abs(left.get(b) - right.get(b));
            }

            return sum;

        }   catch (Exception e) {
            System.out.println(e);
        }

        return 0;

    }

    public static int part2() {

        try {
            Scanner scanner = new Scanner(new File("main.txt"));

            List<Integer> left = new ArrayList<>();
            List<Integer> right = new ArrayList<>();

            while (scanner.hasNextInt()) {
                int i = scanner.nextInt();
                int j = scanner.nextInt();
                left.add(i);
                right.add(j);
            }

            Map<Integer, Integer> list2map = new HashMap<>();

            for (int b = 0; b < right.size(); b++) {
                if (!list2map.containsKey(right.get(b))) {
                    list2map.put(right.get(b), 1);
                }
                else {
                    list2map.put(right.get(b), list2map.get(right.get(b)) + 1);
                }
            }

            int sum = 0;
            for (int b = 0; b < left.size(); b++) {
                if (!list2map.containsKey(left.get(b))) { continue; }
                sum += left.get(b) * list2map.get(left.get(b));
            }

            return sum;

        }   catch (Exception e) {
            System.out.println(e);
        }

        return 0;

    }   
    
    public static void main(String[] args) {

        System.out.println("Part1: " + Integer.toString(part1()));
        System.out.println("Part2: " + Integer.toString(part2()));
    
    }
}