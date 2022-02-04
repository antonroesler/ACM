/*  Ausgewählte Probleme aus dem ACM Programming Contest  WS21/22 
*   Problem:  Apaxiaaaaaaaaaaaans!
*   Link:     https://open.kattis.com/problems/apaxiaaans
*
*   @author   Anton Roesler (anton.roesler@stud.fra-uas.de) 
*   @version  1.0, 29.01.2022
*
*   Method :  Ad-Hoc 
*   Status :  Accepted
*   Runtime:  0.00 s
*/


#include <stdio.h>

int main(void) {
    char name[250];
    scanf("%s", name);

    int len = 0;
    while (name[len] != '\0')
        len++;
    
    char last = ' ';
    for (int i = 0; i < len; i++)
    {
        if (name[i] != last)
            printf("%c",name[i]);
        
        last = name[i];
    }
    
    return 0;
}