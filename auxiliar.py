
my_text = "| Papas | null | walmart | null | 10 | kilogramo | 500 pesos | solo si no cuestan más de 500 pesos |"

my_list = my_text.split("|")[1:-1]

stripped = [s.strip() for s in my_list]

print(stripped)
