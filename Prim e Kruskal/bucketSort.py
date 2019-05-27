def insertion_sort(vet):
    for i in range(1, len(vet)):
        aux = vet[i]
        j = i - 1
        while (j >= 0 and aux < vet[j]):
            vet[j + 1] = vet[j]
            j = j - 1
        vet[j + 1] = aux

def bucketSort(vet):
    maior = max(vet)
    tam = len(vet)
    x = maior / tam

    buckets = [[] for _ in range(tam)]
    for i in range(tam):
        j = int(vet[i]/x)
        if j != tam:
            buckets[j].append(vet[i])
        else:
            buckets[tam-1].append(vet[i])

    for i in range(tam):
        insertion_sort(buckets[i])

    resultado = []
    for i in range(tam):
        resultado = resultado + buckets[i]

    return resultado