

class CalcularSalario:
    def __init__(self, usuario):
        self.usuario = usuario

    def calcular_salario_neto(self):
        salario_bruto = self.usuario.salario_bruto
        impuesto_renta = salario_bruto * 0.15
        seguro_social = salario_bruto * 0.05
        salario_neto = salario_bruto - impuesto_renta - seguro_social
        print(f"Salario bruto: ${salario_bruto:.2f}")
        print(f"Impuesto de renta: ${impuesto_renta:.2f}")
        print(f"Seguro social: ${seguro_social:.2f}")
        print(f"Salario neto: ${salario_neto:.2f}")

