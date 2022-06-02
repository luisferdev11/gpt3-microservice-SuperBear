import openai
import os
from dotenv import load_dotenv

load_dotenv()
# print(os.getenv("OPENAI_API_KEY"))


openai.api_key = os.getenv("OPENAI_API_KEY")


def generate_response(user_input: str) -> list:
    """
    Toma el entrenamiento previamente generado en el playground y devuelve los valores de los atributos indicados
    """

    response = openai.Completion.create(
        engine="text-curie-001",
        prompt=f"A table summarizing the attributes of a purchase:\n\nUn kilo de arroz Verde Valle de walmart\n\n| Nombre | Marca | Supermercado | Departamento | Cantidad | Unidad | Precio | Anotaciones |\n\n| Arroz | Verde Valle | Walmart | null | 1 | kilogramo | null | null |\n\n2 kg de frijoles La costeña de Costco\n\n| Nombre | Marca | Supermercado | Departamento | Cantidad | Unidad | Precio | Anotaciones |\n\n| Frijoles | La costeña | Costco | null | 2 | kilogramo | null | null |\n\nComprar 10 pesos de epazote del mercado de la esquina\n\n| Nombre | Marca | Supermercado | Departamento | Cantidad | Unidad | Precio | Anotaciones |\n\n| Epazote | null | mercado | null | 1 | unidad | 10 | del mercado de la esquina |\n\n5 litros de leche alpura deslactosada de walmart\n\n| Nombre | Marca | Supermercado | Departamento | Cantidad | Unidad | Precio | Anotaciones |\n\n| Leche | Alpura | Walmart | Lácteos | 5 | litros | null | deslactosada |\n\nIr a comprar 15 refrescos chaparritas de 10 pesos al seven-eleven\n\n| Nombre | Marca | Supermercado | Departamento | Cantidad | Unidad | Precio | Anotaciones |\n\n| Refrescos | Chaparritas | seven-eleven | null | 15 | unidad | 10 | al seven-eleven |\n\n50 paquetes de papas sabritas del mercado de la esquina\n\n| Nombre | Marca | Supermercado | Departamento | Cantidad | Unidad | Precio | Anotaciones |\n\n| Papas | Sabritas | mercado | null | 50 | paquete | null | del mercado de la esquina |\n\nComprar 100 gramos de kush con el compita de la calle\n\n| Nombre | Marca | Supermercado | Departamento | Cantidad | Unidad | Precio | Anotaciones |\n\n| Kush | null | compita de la calle | Cannabis | 100 | gramo | null | null |\n\n3 kg de guayaba rosa del costco\n\n| Nombre | Marca | Supermercado | Departamento | Cantidad | Unidad | Precio | Anotaciones |\n\n| Guayaba | null | Costco | Frutas | 3 | kilogramo | null | rosa |\n\n1 litro de jugo de naranja sin azúcar del mercado de la esquina\n\n| Nombre | Marca | Supermercado | Departamento | Cantidad | Unidad | Precio | Anotaciones |\n\n| Jugo de naranja | null | mercado | null | 1 | litro | null | sin azúcar |\n\n2 litros de leche desnatada de la farmacia\n\n| Nombre | Marca | Supermercado | Departamento | Cantidad | Unidad | Precio | Anotaciones |\n\n| Leche | Desnatada | farmacia | Lácteos | 2 | litros | null | null |\n\nUn paquete de salchicas FUD de Aurrera\n\n| Nombre | Marca | Supermercado | Departamento | Cantidad | Unidad | Precio | Anotaciones |\n\n| Salchicas | FUD | Aurrera | null | 1 | paquete | null | null |\n\nTraer del Soriana 3 pelotas de colores\n\n| Nombre | Marca | Supermercado | Departamento | Cantidad | Unidad | Precio | Anotaciones |\n\n| Pelotas de colores | null | Soriana | Jugueteria | 3 | unidad | null | null |\n\nTraer un garrafón de Chedraui\n\n| Nombre | Marca | Supermercado | Departamento | Cantidad | Unidad | Precio | Anotaciones |\n\n| Garrafón | null | Chedraui | Bebidas | 1 | unidad | null | null |\n\n1 kilogramo de arroz negro de Walmart\n\n| Nombre | Marca | Supermercado | Departamento | Cantidad | Unidad | Precio | Anotaciones |\n\n| Arroz negro | null | Walmart | null | 1 | kilogramo | null | null |\n\n15 pesos de tortillas\n\n| Nombre | Marca | Supermercado | Departamento | Cantidad | Unidad | Precio | Anotaciones |\n\n| Tortillas | null | Tortillería | null | 1 | unidad | 15 | null |\n\nPara la despensa necesitamos un bolsa de frijoles bayos marca Aurrera\n\n| Nombre | Marca | Supermercado | Departamento | Cantidad | Unidad | Precio | Anotaciones |\n\n| Bolsa de frijoles | Aurrera | null | null | 1 | Unidad | null | null |\n\nNecesitamos un peluche de PO de $32 de la juguetería del Walmart\n\n| Nombre | Marca | Supermercado | Departamento | Cantidad | Unidad | Precio | Anotaciones |\n\n| Peluche de PO | null | Walmart | Juguetería | 1 | Unidad | 32 | null |\n\nSe ocupan 5 Bolillos del Superama\n\n| Nombre | Marca | Supermercado | Departamento | Cantidad | Unidad | Precio | Anotaciones |\n\n| Bolillo | null | Superama | null | 5 | Unidad | null | null |\n\nUna caja de chocokrispis jumbo del Aurrera\n\n| Nombre | Marca | Supermercado | Departamento | Cantidad | Unidad | Precio | Anotaciones |\n\n| Caja de Chocokrispis | kellog's | Aurrera | null | 1 | Unidad | null | tamaño jumbo |\n\nTraer una torta de jamón del soriana que cueste $50 sin queso ni jitomate\n\n| Nombre | Marca | Supermercado | Departamento | Cantidad | Unidad | Precio | Anotaciones |\n\n| Torta de jamón | null | Soriana | null | 1 | Unidad | 50 | sin queso ni jitomate |\n\nTraer cien kilogramos de papa\n\n| Nombre | Marca | Supermercado | Departamento | Cantidad | Unidad | Precio | Anotaciones |\n\n| Papa | null | null | null | 100 | Kilogramo | null | null |\n\n3 litros de leche conasupo\n\n| Nombre | Marca | Supermercado | Departamento | Cantidad | Unidad | Precio | Anotaciones |\n\n| Leche | conasupo | null | Lácteos | 3 | litros | null | null |\n\n{user_input}",
        temperature=0.5,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )

    # print(response)

    output = [s.strip()
              for s in response.choices[0].text[95::].split("|")[1:-1]]
    # print(output)

    outputLen = len(output)
    # print(outputLen)

    if (outputLen == 7):
        # print("entra en if 7")
        output.append("null")
    elif (outputLen > 8):
        # print("entra en if mas de 8")
        output = output[:8]
    elif (outputLen < 7):
        # print("entra en if de menos 7")
        output = []

    # print(output)

    return output


# prueba1 = generate_response(
#     "Ir a comprar 10 kilos de papa a walmart solo si no cuestan más de 500 pesos")

# print(prueba1)
