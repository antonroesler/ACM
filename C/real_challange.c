/*  Ausgewählte Probleme aus dem ACM Programming Contest  WS21/22 
*   Problem:  A Real Challenge
*   Link:     https://open.kattis.com/problems/areal

*   @author   Anton Roesler (anton.roesler@stud.fra-uas.de) 
*   @version  1.0, 29.01.2022
*
*   Method :  Ad-Hoc 
*   Status :  Accepted
*   Runtime:  0.00 s
*/

#include <stdio.h>
#include <math.h>

int main(void) {
    long long n;
    double result;
    scanf("%lld", &n);
    result = 4*sqrt(n);
    printf("%.8f\n", result);
    return 0;
}