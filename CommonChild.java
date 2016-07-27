import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

// Still Too Inefficient to Pass test cases

public class Solution {

    public static Hashtable<ArrayList<String>, ArrayList<String>> tree = new Hashtable<ArrayList<String>, ArrayList<String>>();

    public static void main(String[] args) {
        /* Enter your code here. Read input from STDIN. Print output to STDOUT. Your class should be named Solution. */
        Scanner in = new Scanner(System.in);
        ArrayList<String> a1 = new ArrayList<String>();
        ArrayList<String> a2 = new ArrayList<String>();
        String s1 = in.nextLine();
        String s2 = in.nextLine();
        a1.add(s1);
        a2.add(s2);
        System.out.println(pls(a1, a2, s1.length()));


    }
    public static int pls(ArrayList<String> a, ArrayList<String> b, int n){
        if(n == 0){
            return 0;
        }
        for(int i = 0; i < a.size(); i++){
            if(b.contains(a.get(i))){
                return n;
            }
        }
    
        ArrayList<String> a_children = new ArrayList<String>();
        ArrayList<String> b_children = new ArrayList<String>();
        if(tree.containsKey(a)){
            a_children = tree.get(a);
        }
        else{
            a_children = children(a);
            tree.put(a, a_children);
        }

        if(tree.containsKey(b)){
            b_children = tree.get(b);
        }
        else{
            b_children = children(b);
            tree.put(b, b_children);
        }

        return pls(a_children, b_children, n-1);
    }
    public static ArrayList<String> children(ArrayList<String> b){
        ArrayList<String> a = new ArrayList<String>();
        for(int j = 0; j < b.size(); j++){
            String s = b.get(j);
            for(int i = 0; i < s.length(); i++){
                a.add(s.substring(0, i) + s.substring(i+1));
            }
            
        }
        return a;
    }
}