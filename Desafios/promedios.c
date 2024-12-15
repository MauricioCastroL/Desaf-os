// Autor: Mauricio Castro
// Fecha: 13/12/2024
// Objetivo: Calculadora de promedios

#include <stdio.h>

float prom(int x, int *score);
void muestro(float promedio);

int main()
{
    int x;
    
    printf("Ingrese la cantidad de notas: ");
    scanf("%i", &x);

    int score[x];

    for (int i = 0; i < x; i++) //ciclo que pida las notas
    {
        printf("Ingrese nota: ");
        scanf("%i", &score[i]);        
    }

    float promedio = prom(x, score);
    muestro(promedio);

    return 0;
}

float prom(int x, int *score)
{
    int promedio = 0;

    for(int i = 0; i < x; i++)
    {
        promedio += score[i];
    }
    promedio = promedio / (float) x;
    
    return promedio;

}

void muestro(float promedio)
{
    printf("El promedio del alumno es: %f", promedio);
}