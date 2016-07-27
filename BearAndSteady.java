import java.io.*;
import java.util.*;

/*
 * To execute Java, please define "static void main" on a class
 * named Solution.
 *
 * If you need more classes, simply define them inline.
 */

class BearSteady {

  public static int[] counts(String string){
    int[] counts = {0,0,0,0}; // A C G T


    for(int i = 0; i< string.length(); i++){
      switch (string.charAt(i)) {
        case 'A': counts[0] = counts[0]+1;break;
        case 'C': counts[1] = counts[1]+1;break;
        case 'G': counts[2] = counts[2]+1;break;
        case 'T': counts[3] = counts[3]+1;break;
      }

    }
    return counts;
  }

  public static int arrSum(int[] a){
    int sum = 0;
    for (int s: a){
      sum += s;
    }
    return sum;
  }

  public static int[] getNeeded(int[] counts, int n){
    int[] result = new int[counts.length];

    for(int i = 0; i< counts.length; i++){
      if(counts[i] > (n/4)){
        result[i] = counts[i] - (n/4);
      }
      else{
        result[i] = 0;
      }
    }
    return result;
  }

  public static void main(String[] args) {
    Scanner in = new Scanner(System.in);
    int n = Integer.parseInt(in.nextLine());
    String string = in.nextLine();
    //System.out.println(string);

    int[] counts = counts(string);
    //for(int c : counts){
      //  System.out.println(c);
    //}

    int[] needed = getNeeded(counts, n);
      //for(int c : needed){
       // System.out.println(c);
    //}
      
    int j = 0;
    int i = 0;
    int mn = Integer.MAX_VALUE;
    int[] curvals = {0,0,0,0};
    while(i < n || j < n){
        //System.out.println("" + i + ", " + j);
        //for(int c : curvals){
          //System.out.print(" " + c);
        //}
        //System.out.println("");

        Boolean works = true;
        for(int k = 0; k < 4; k++){
            if(curvals[k] < needed[k]){
                works = false;
            }
        }
        if(works){
            mn = Math.min(mn, j-i);
            if(mn == 0){
                break;
            }
            //if(i > 0){
                switch (string.charAt(i)) {
                    case 'A': curvals[0] = curvals[0]-1;break;
                    case 'C': curvals[1] = curvals[1]-1;break;
                    case 'G': curvals[2] = curvals[2]-1;break;
                    case 'T': curvals[3] = curvals[3]-1;break;
                }
            //}
            
            i += 1;
        }
        else if((!works) && j < n){
            switch (string.charAt(j)) {
                case 'A': curvals[0] = curvals[0]+1;break;
                case 'C': curvals[1] = curvals[1]+1;break;
                case 'G': curvals[2] = curvals[2]+1;break;
                case 'T': curvals[3] = curvals[3]+1;break;
            }
            j += 1;
        }
        else{
            break;
        }

   }
   if (mn == Integer.MAX_VALUE){
       System.out.println(0);
   }
   else{
      System.out.println(mn); 
   }
   
 
  }
}

