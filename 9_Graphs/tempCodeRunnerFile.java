/*
Ausgewählte Probleme aus dem ACM Programming Contest  WS21/22 

Problem:  -
Link:     -

@author   Anton Roesler (anton.roesler@stud.fra-uas.de) 
@version  1.0, dd.mm.2021

Method :  Ad-Hoc 
Status :  Accepted
Runtime:  X.XXX


Leider hat mein Python Program nicht funktioniert, ich kann den Fehler leider nicht finden. Meine Java-Lösung nach der selben Logik funktioniert.
*/


import java.util.Arrays;
import java.util.HashMap;
import java.util.HashSet;
import java.util.Objects;
import java.util.PriorityQueue;
import java.util.Scanner;
import java.util.Set;
import java.math.BigInteger;

public class singlesource {

    public static void main(String[] args) {
        int inf = Integer.MAX_VALUE;

        while(true){

        
        Scanner scan = new Scanner(System.in);

        int n = scan.nextInt();
        int m = scan.nextInt();
        int q = scan.nextInt();
        int s = scan.nextInt();


        if (n==0 && m==0 && q==0 && s==0){
            scan.close();
            return;
        }

        int[] weights = new int[n];
        Arrays.fill(weights, inf);

        HashMap<Integer, HashMap<Integer, Integer>> edges = new HashMap<Integer, HashMap<Integer, Integer>>();

        for (int i = 0; i < m; i++) {
            int u = scan.nextInt();
            int v = scan.nextInt();
            int w = scan.nextInt();
            if(edges.containsKey(u)){
                edges.get(u).put(v, w);
            } else {
                HashMap<Integer, Integer> t = new HashMap<>();
                t.put(v, w);
                edges.put(u, t);
            }
        }
        System.out.println(edges);

        weights[s] = 0;

        PriorityQueue<Integer> queue = new PriorityQueue<>();
        queue.add(9);
        HashMap<Integer, HashSet<Integer>> queueVals = new HashMap<>();
        HashSet<Integer> t= new HashSet<>();
        t.add(s);
        queueVals.put(0, t);

        while (!queue.isEmpty()){
            int cost = queue.poll();
            int idx = qVal(cost, queueVals);
            HashMap<Integer, Integer> ns = edges.get(idx);
            for (int key : ns.keySet()){
                int new_weight = cost + ns.get(key);
                if (weights[key] > new_weight){
                    weights[key] = new_weight;
                    queue.add(new_weight);
                    if (queueVals.containsKey(new_weight)){
                        queueVals.get(new_weight).add(key);
                    } else {
                        HashSet<Integer> t = new HashSet<>();
                        t.add(key);
                        queueVals.put(new_weight, t);
                    }
                }
            }
        }

        for (int i = 0; i < q; i++) {
            int qt = scan.nextInt();
            int r = weights[qt];
            if (r == inf){
                System.out.println("Impossible");
            } else {
                System.out.println(r);
            }
        }
        System.out.println("");

    }

    }

    private static int qVal(int key, HashMap<Integer, HashSet<Integer>> hm){
        int n = hm.get(key).iterator().next();
        hm.remove(n);
        return n;
    }
}
