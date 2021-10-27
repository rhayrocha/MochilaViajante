import datetime #USADO PARA A TEREFA DE MOSTRAR HORA TUAL
import requests #USADO PARA IMPORTAR A BIBLIOTECA DO binance
import discord #IMPORTA A BIBLIOTECA DO DISCORD
from discord.ext import commands, tasks 

bot = commands.Bot("!") #DECLARANDO QUE ! É UM SIMBOLO RESERVADO PARA ATIIVAR AS TEREFAS

@bot.event #ATIVANDO O BOT
async def on_ready(): 
    print(f"Estou Pronto! Estou conectado como {bot.user}")
    #current_time.start() #AO ATIVAR DE TEMPOS EM TEMPOS O BOT VAI ENVIAR A HORA ATUAL

@bot.event
async def on_message(message): 
    if message.author == bot.user: #PARA NÃO DESONSIDERAR O QUE O BOT ESCREVE
        return
    
    if "palavrão" in (message.content): #ANALISA SE DIGITARAM A PALAVRA PALAVRÃO
        await message.channel.send(
            f"Por favor, {message.author.name}, não ofenda os demais usuários!") 

        await message.delete() #DELETA MENSAGEM CONTENDO PALAVRÃO

    if "COTIN" in message.content:
        await message.channel.send(
            f"Por favor, {message.author.name}, Ligue para o ramal 9699")

    await bot.process_commands(message)

@bot.command(name = "oi") #CRIANDO O COMANDO !OI PARA O BOT
async def send_hello(ctx):
    name = ctx.author.name 
    response = "Olá, " + name

    await ctx.send(response)

@bot.command(name = "calcular")
async def calculate_espression(ctx, *expression):
    expression = "".join(expression)
    response =  eval(expression)

    await ctx.send("A resposta é: " + str(response))

@bot.command()
async def binance(ctx, coin, base):
    try:
        response = requests.get("https://api.binace.com/api/v3/ticker/price?symbol={coin.upper()} {base.upper()}")
        data =  response.json
        price = data.get("price")
        if price:
            await ctx.send("O valor do par {coin}/{base} é {price}")
        else:
            await ctx.send("O valor do par {coin}/{base} é Inválido")
    except:
        await ctx.send("Ops... deu algum erro!")
        print(error)

@tasks.loop(hours=1)
async def current_time():
    now = datetime.datetime.now()

    now = now.strftime("%d/%m/%y às %H:%M:%S")

    channel = bot.get_channel(901135318835687467)
    await channel.send("Data atual: " + now)


bot.run( "OTAxNTY2NjA0NDEwNzczNTA1.YXRvVA.3iVop9P18cyLsA8EojWO0jhtFAs ")