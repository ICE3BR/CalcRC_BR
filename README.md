# CalcRC_BR
Calculadora de taxas do programa brasileiro remessa conforme, que pega o valor do dólar no dia. para fazer os cálculos.
--------------------------
Para usar precisa apenas informar o valor do produto e frete. (Pode incluir o valor total de uma compra com vários produtos e o frete.)
Depois clicar em calcular.
Os resultados serão mostrados logo a baixo.
--------------------------
O processo é relativamente simples.
1- Os valores da compra e do frete são adicionados
2- Pegamos o valor do dolar usando a API do banco central
3- Acontece a soma do produto com o frete e então é convertido em dólar
4- Com esses valores, vai ser decidido quais taxas serão incluídas
5- Se o total for até 50 Dólares será aplicada apenas uma taxa, se passar de 50 Dólares vai ter 2 taxas (=50dol -> 17% // +50dol -> 60%)
6- Depois de fazer os calculos das taxas, vai fazer o calculo também do valor total de tudo em real a ser pago depois de aplicar as taxas. (produto,frete e taxas)
7- No final os valores são mostrados para o usuário. Incluindo a cotação do dólar que foi utilizada
