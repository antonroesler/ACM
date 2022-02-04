/*  Ausgewählte Probleme aus dem ACM Programming Contest  WS21/22 
*   Problem:  Goat Rope
*   Link:     https://open.kattis.com/problems/goatrope

*   @author   Anton Roesler (anton.roesler@stud.fra-uas.de) 
*   @version  1.0, 04.02.2022
*
*   Method :  Ad-Hoc 
*   Status :  Accepted
*   Runtime:  0.00 s
*/

#include <stdio.h>
#include <math.h>
#include <stdlib.h>

double max(double, double);
double _abs(double);


int main() {
    int x,y,x1,y1,x2,y2;
    scanf("%d %d %d %d %d %d", &x,&y,&x1,&y1,&x2,&y2);

    int width = x2-x1;
    int height = y2-y1;
    double cx = (x1+x2)/2.0;
    double cy = (y1+y2)/2.0;

    double dx = max(_abs(x - cx) - width / 2.0, 0);
    double dy = max(_abs(y - cy) - height / 2.0, 0);

    printf("%.6lf\n", sqrt(dx * dx + dy * dy));

    return 0;
}

double max(double a, double b) { 
    if (a>b)
        return a;
    return b;
}

double _abs(double a) {
    if (a<0)
        return a*-1;
    return a;
}