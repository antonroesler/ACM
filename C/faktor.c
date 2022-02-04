/*  Ausgewählte Probleme aus dem ACM Programming Contest  WS21/22 
*   Problem:  Faktor
*   Link:     https://open.kattis.com/problems/faktor

*   @author   Anton Roesler (anton.roesler@stud.fra-uas.de) 
*   @version  1.0, 30.01.2022
*
*   Method :  Ad-Hoc 
*   Status :  Accepted
*   Runtime:  0.00 s
*/
#include <stdio.h>

int main()
{
    int p, i;
    scanf("%d %d", &p, &i);
    printf("%d", p * (i - 1) + 1);
}