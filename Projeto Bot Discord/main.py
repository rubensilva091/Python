import discord
import random
import lista

#Powershell (Comandos para ativar o import do discord no VSCode)
#python3 -m venv bot-env
#bot-env\Scripts\activate.bat
#pip install -U discord.py


TOKEN = ''
rubenID = 167674491504295937

client = discord.Client()

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('boas'):
        msg = 'Mekiee povo {0.author.mention}'.format(message)
        if(message.author.id==rubenID):
            msg = 'Mekieeee, Tu és bravo, quando for grande quero ser como tu {0.author.mention}'.format(message)
        await message.channel.send(msg)

    if message.content.startswith('god' or 'deus'):
        msg = 'aka Ruben Silva {0.author.mention}'.format(message)
        await message.channel.send(msg)
    
    if message.content.startswith('fds' or "fodasse" or "foda-se" or "foda se"):
        msg = 'Não deixes a raiva consumir-te o espírito, lembra-te que existe a Paula Smith {0.author.mention}'.format(message)
        await message.channel.send(msg)

    if message.content.startswith('socrates'):
        deck = lista.listaFF
        randãoo = random.sample(deck,1)
        msg = str(*randãoo) + "{0.author.mention}".format(message)
        await message.channel.send(msg)

    if message.content.startswith('chumbei' or "reprovei" or "vou reprovar"):
        msg =  'Pensa positivo bro, enquanto não for a cadeira da Paula Smith ta safe {0.author.mention}'.format(message)
        await message.channel.send(msg)

    if message.content.startswith('acho que passo' or "tenho de passar" or "ta safe"):
        msg =  'Acredite em milagres, mas não dependa deles. AKA Manel Kant {0.author.mention}'.format(message)
        await message.channel.send(msg)

    if message.content.startswith(".help"):
        msg =  'Sou o Socrates\n.jogar -> Para jogarmos uma beca {0.author.mention}'.format(message)
        await message.channel.send(msg)

    if message.content.startswith(".jogar"):
        msg =  'Tou a configurar ainda, pera uma beca {0.author.mention}'.format(message)
        await message.channel.send(msg)

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

client.run(TOKEN)