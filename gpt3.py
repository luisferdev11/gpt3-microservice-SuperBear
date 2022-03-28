import openai
import os
from dotenv import load_dotenv

load_dotenv()
print(os.getenv("OPENAI_API_KEY"))


openai.api_key = os.getenv("OPENAI_API_KEY")


def generate_response(user_input: str) -> list:
    """
    Toma el entrenamiento previamente generado en el playground y devuelve los valores de los atributos indicados
    """

    response = openai.Completion.create(
        engine="text-ada-001",
        prompt=f"A table summarizing the attributes of a purchase:\n\nUn kilo de arroz Verde Valle de walmart\n\n| Nombre | Marca | Supermercado | Departamento | Cantidad | Unidad | Precio | Anotaciones |\n\n| Arroz | Verde Valle | Walmart | null | 1 | kilogramo | null | null |\n\n2 kilos de frijoles La costeña de Costco\n\n| Nombre | Marca | Supermercado | Departamento | Cantidad | Unidad | Precio | Anotaciones |\n\n| Frijoles | La costeña | Costco | null | 2 | kilogramo | null | null |\n\nComprar 10 pesos de epazote del mercado de la esquina\n\n| Nombre | Marca | Supermercado | Departamento | Cantidad | Unidad | Precio | Anotaciones |\n\n| Epazote | null | mercado | null | 10 | pesos | 10 pesos | del mercado de la esquina |\n\n5 litros de leche alpura deslactosada de walmart\n\n| Nombre | Marca | Supermercado | Departamento | Cantidad | Unidad | Precio | Anotaciones |\n\n| Leche | Alpura | Walmart | Lácteos | 5 | litros | null | deslactosada |\n\nIr a comprar 10 refrescos chaparritas de 10 pesos al seven-eleven\n\n| Nombre | Marca | Supermercado | Departamento | Cantidad | Unidad | Precio | Anotaciones |\n\n| Refrescos | Chaparritas | seven-eleven | null | 10 | pieza | 10 pesos | al seven-eleven |\n\n50 paquetes de papas sabritas del mercado de la esquina\n\n| Nombre | Marca | Supermercado | Departamento | Cantidad | Unidad | Precio | Anotaciones |\n\n| Papas | Sabritas | mercado | null | 50 | paquete | null | del mercado de la esquina |\n\nComprar 100 gramos de kush con el compita de la calle\n\n| Nombre | Marca | Supermercado | Departamento | Cantidad | Unidad | Precio | Anotaciones |\n\n| Kush | null | compita de la calle | Cannabis | 100 | gramo | null | null |\n\n{user_input}",
        temperature=0.7,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )

    # Response limpia para su uso
    return [s.strip() for s in response.choices[0].text[95::].split("|")[1:-1]]


# prueba1 = generate_response(
#     "Ir a comprar 10 kilos de papa a walmart solo si no cuestan más de 500 pesos")

# print(prueba1)
