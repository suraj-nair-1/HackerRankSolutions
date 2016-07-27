import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

public class Solution {

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int cases = in.nextInt();
        String que = in.nextLine();
        
        for(int i = 0; i < cases; i++){
            String a = in.nextLine();
            String b = in.nextLine();
            int has = 0;
            for(char c : "abcdefghijklmnopqrstuvwxyz".toCharArray())
            {
                if(a.indexOf(c) > -1 && b.indexOf(c) > -1){
                    has = 1;
                }
            }
            if(has == 0){   
                System.out.println("NO");
            }
            else{
                System.out.println("YES");
            }
        }
    }
}