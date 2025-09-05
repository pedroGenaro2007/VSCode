# a = int(input("lado a: "))
# b = int(input("lado b: "))
# c = int(input("lado c: "))
# if (a < b + c) and (b < a + c) and (c < a + b):
#     if ( a == b) and (b == c):
#         print("triangulo equilatero")
#     else:
#         if (a == b) or (a == c) or (b == c):
#             print("triangulo isosceles")
#         else:
#             print("triangulo escaleno")
# else:
#         print("Não é triangulo")

#ex01
# preço = float(input("digite o preço do produto: "))
# cod = int(input("digite o codigo: "))
# if cod == 1:
#     procedencia = "sul"
#     print(preço)
# elif cod == 2:
#     procedencia = "norte"
# elif cod == 3:
#     procedencia = "leste"
#     print(preço)
# elif cod == 4:
#     procedencia = "oeste"
#     print(preço)
# elif cod == 5 or cod == 6:
#     procedencia = "nordeste"
#     print(preço)
# elif cod == 7 or cod == 8 or cod == 9:
#     procedencia = "sudeste"
#     print(preço)
# elif cod >=10 and cod <=20:
#     procedencia = "centro-oeste"
#     print(preço)
# elif cod >=25 and cod <=30:
#     procedencia ="nordeste"
#     print(preço)
# if cod >=30:
#     print("produto importado")

#ex02
a = int(input("digite o valor de A: "))
b = int(input("digite o valor de B: "))
c = int(input("digite o valor de C: "))

if a > b and a > c:
    # print(f"o maior valor é A")
    if b > c:  
            print(a,b,c)
    elif c > b:
          print(a,c,b)
elif b > a and b > c:
    #   print (f"o maior valor é B: {b}")
      if a > c:
            print(b,c,a)
elif c > a and c > b:
        # print(f"o maior valor é C {c}")
