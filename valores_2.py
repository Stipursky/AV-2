custo = float(130)

def soma_imposto(sm):
    global custo
    taxa_imposto = (custo / 100) *15
    soma = custo + taxa_imposto
    return soma