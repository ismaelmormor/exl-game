
import os

from bs4 import BeautifulSoup
import requests
import pandas as pd
import random
import tabulate
from tabulate import tabulate
import time
import string
import datetime
from datetime import date
from datetime import datetime, timezone


import discord
from discord.ui import Button, View
from discord.ext import commands
from discord import app_commands


import mysql.connector
from mysql.connector import Error

##====================BOT==================##

client = commands.Bot(command_prefix= commands.when_mentioned_or('!'), intents=discord.Intents.all())

##================VARIABLES=================##

contraseña_sql = os.environ['SQL_PASS']

#------RANK A------#
curso_A = 0
cola_A = 0
jugadores_A = []
msg_id_A = 0
cola_members_A=[]
v1_A = 0
v2_A = 0
v3_A = 0
message_A = 0
votaciones_A=[]
elecciones_capis_A = 0
capi1_A = ''
capi2_A = ''
eligiendo_A = ''
team1_A = []
team2_A = []
#------RANK B------#
curso_B = 0
message_B = 0
cola_B = 0
jugadores_B = []
msg_id_B = 0
cola_members_B = []
v1_B = 0
v2_B = 0
v3_B = 0
#------RANK C------#
curso_C = 0
message_C = 0
cola_C = 0
jugadores_C = []
msg_id_C = 0
cola_members_C = []
v1_C = 0
v2_C = 0
v3_C = 0
#------RANK D------#
curso_D = 0
message_D = 0
cola_D = 0
jugadores_D = []
msg_id_D = 0
cola_members_D = []
v1_D = 0
v2_D = 0
v3_D = 0
#------RANK E------#
#------RANK F------#
#------RANK G------#
#------RANK H------#
#------RANK I------#

##==================COMMANDS==================##

@client.command()
async def q(ctx):
    user = ctx.author
    channel = ctx.channel.id
    guild = ctx.message.guild
    ##------------------RANK A-------------------
    
    if channel == 1009611785801834597:
        global curso_A
        global message_A
        global cola_A
        global jugadores_A
        global msg_id_A
        global cola_members_A
        chan_a=client.get_channel(1009611785801834597)
        
        if user not in cola_members_A:
            if curso_A == 0:
                if cola_A < 3:
                    cola_A = cola_A+1
                    embed = discord.Embed(title=f'Hay {cola_A} jugadores en cola', description=f'{user.mention} se unió a la cola', color=0xb000ff)
                    embed.set_footer(text='Powered by Exile Gaming', icon_url='https://imgur.com/IOKfTml.png')
                    await chan_a.send(embed=embed)
                    jugadores_A.append(user.mention)
                    cola_members_A.append(user)
                
                else:
                    if cola_A==3:
                        cola_A = cola_A+1
                        embed = discord.Embed(title=f'Hay {cola_A} jugadores en cola', description=f'{user.mention} se unió a la cola', color=0xb000ff)
                        embed.set_footer(text='Powered by Exile Gaming', icon_url='https://imgur.com/IOKfTml.png')
                        await chan_a.send(embed=embed)
                        jugadores_A.append(user.mention)
                        cola_members_A.append(user)
                        embed1= discord.Embed(title=f'Ya hemos llegado a {cola_A} jugadores!', description='La votación comienza ahora', color=0xb000ff)
                        embed1.add_field(name='Equipos aleatorios', value='Pulsa 1️⃣')
                        embed1.add_field(name='Equipos balanceados', value='Pulsa 2️⃣ (DESHABILITADO)')
                        embed1.add_field(name='Equipos con capitanes', value='Pulsa 3️⃣ (DESHABILITADO)')
                        embed1.set_footer(text='Powered by Exile Gaming', icon_url='https://imgur.com/IOKfTml.png')
                        msg = await ctx.send(f'''{jugadores_A[0]}{jugadores_A[1]}{jugadores_A[2]}{jugadores_A[3]}''', embed=embed1)
                        curso_A = 1
                        await msg.add_reaction('1️⃣')
                        await msg.add_reaction('2️⃣')
                        await msg.add_reaction('3️⃣')
                        i=0
                        while i < 3:
                            try:
                                await cola_members_A[i].send(f'{jugadores_A[i]}, se ha completado la cola. Mira en canal para la votación.')
                            except discord.Forbidden:
                                pass
                            i += 1
                        msg_id_A = msg.id
                        message_A=msg
                        cola_A = 0
                        jugadores_A.clear()
            else:
                return
##============================= rank b================
    if channel == 1009611818265755678:
        global curso_B
        global message_B
        global cola_B
        global jugadores_B
        global msg_id_B
        global cola_members_B
        chan_b=client.get_channel(1009611818265755678)
        if True:
            if curso_B == 0:
                if cola_B < 3:
                    cola_B = cola_B+1
                    embed = discord.Embed(title=f'Hay {cola_B} jugadores en cola', description=f'{user.mention} se unió a la cola', color=0xfa8cff)
                    embed.set_footer(text='Powered by Exile Gaming', icon_url='https://imgur.com/IOKfTml.png')
                    await chan_b.send(embed=embed)
                    jugadores_B.append(user.mention)
                    cola_members_B.append(user)
                else:
                    if cola_B==3:
                        cola_B = cola_B+1
                        embed = discord.Embed(title=f'Hay {cola_B} jugadores en cola', description=f'{user.mention} se unió a la cola', color=0xfa8cff)
                        embed.set_footer(text='Powered by Exile Gaming', icon_url='https://imgur.com/IOKfTml.png')
                        await chan_b.send(embed=embed)
                        jugadores_B.append(user.mention)
                        cola_members_B.append(user)
                        embed1= discord.Embed(title=f'Ya hemos llegado a {cola_B} jugadores!', description='La votación comienza ahora', color=0xfa8cff)
                        embed1.add_field(name='Equipos aleatorios', value='1️⃣')
                        embed1.add_field(name='Equipos balanceados', value='2️⃣')
                        embed1.add_field(name='Equipos con capitanes', value='3️⃣')
                        embed1.set_footer(text='Powered by Exile Gaming', icon_url='https://imgur.com/IOKfTml.png')
                        msg = await ctx.send(f'''{jugadores_B[0]}{jugadores_B[1]}{jugadores_B[2]}{jugadores_B[3]}''', embed=embed1)
                        curso_B = 1
                        cola_members_B.append(client)
                        await msg.add_reaction(emoji='1️⃣')
                        await msg.add_reaction(emoji='2️⃣')
                        await msg.add_reaction(emoji='3️⃣')
                        i=0
                        while i < 3:
                            await cola_members_B[i].send(f'{jugadores_B[i]}, se ha completado la cola. Mira en canal para la votación.')
                            i += 1
                        msg_id_B = msg.id
                        message_B=msg
                        cola_B = 0
                        jugadores_B.clear()
            else:
                return
##==============================RANK C ===================#
    if channel == 1009611839803506809:
        global curso_C
        global message_C
        global cola_C
        global jugadores_C
        global msg_id_C
        global cola_members_C
        chan=client.get_channel(1009611839803506809)
        if user not in cola_members_C:
            if curso_C == 0:
                if cola_C < 3:
                    cola_C = cola_C+1
                    embed = discord.Embed(title=f'Hay {cola_C} jugadores en cola', description=f'{user.mention} se unió a la cola', color=0x2659ff)
                    embed.set_footer(text='Powered by Exile Gaming', icon_url='https://imgur.com/IOKfTml.png')
                    await chan.send(embed=embed)
                    jugadores_C.append(user.mention)
                    cola_members_C.append(user)
                else:
                    if cola_C==3:
                        cola_C = cola_C+1
                        embed = discord.Embed(title=f'Hay {cola_C} jugadores en cola', description=f'{user.mention} se unió a la cola', color=0x2659ff)
                        embed.set_footer(text='Powered by Exile Gaming', icon_url='https://imgur.com/IOKfTml.png')
                        await chan.send(embed=embed)
                        jugadores_C.append(user.mention)
                        cola_members_C.append(user)
                        embed1= discord.Embed(title=f'Ya hemos llegado a {cola_C} jugadores!', description='La votación comienza ahora', color=0x2659ff)
                        embed1.add_field(name='Equipos aleatorios', value='1️⃣')
                        embed1.add_field(name='Equipos balanceados', value='2️⃣')
                        embed1.add_field(name='Equipos con capitanes', value='3️⃣')
                        embed1.set_footer(text='Powered by Exile Gaming', icon_url='https://imgur.com/IOKfTml.png')
                        msg = await ctx.send(f'''{jugadores_C[0]}{jugadores_C[1]}{jugadores_C[2]}{jugadores_C[3]}''', embed=embed1)
                        curso_C = 1
                        cola_members_C.append(client)
                        await msg.add_reaction(emoji='1️⃣')
                        await msg.add_reaction(emoji='2️⃣')
                        await msg.add_reaction(emoji='3️⃣')
                        i=0
                        while i < 3:
                            await cola_members_A[i].send(f'{jugadores_A[i]}, se ha completado la cola. Mira en canal para la votación.')
                            i += 1
                        msg_id_C = msg.id
                        message_C=msg
                        cola_C = 0
                        jugadores_C.clear()
            else:
                return
##==============================RANK D ====================#
    if channel == 1009611859529302046:
        global curso_D
        global message_D
        global cola_D
        global jugadores_D
        global msg_id_D
        global cola_members_D
        chan=client.get_channel(1009611859529302046)
        if user not in cola_members_D:
            if curso_D == 0:
                if cola_D < 3:
                    cola_D = cola_D+1
                    embed = discord.Embed(title=f'Hay {cola_D} jugadores en cola', description=f'{user.mention} se unió a la cola', color=0x18e6ff)
                    embed.set_footer(text='Powered by Exile Gaming', icon_url='https://imgur.com/IOKfTml.png')
                    await chan.send(embed=embed)
                    jugadores_D.append(user.mention)
                    cola_members_D.append(user)
                else:
                    if cola_D==3:
                        cola_D = cola_D+1
                        embed = discord.Embed(title=f'Hay {cola_D} jugadores en cola', description=f'{user.mention} se unió a la cola', color=0x18e6ff)
                        embed.set_footer(text='Powered by Exile Gaming', icon_url='https://imgur.com/IOKfTml.png')
                        await chan.send(embed=embed)
                        jugadores_D.append(user.mention)
                        cola_members_D.append(user)
                        embed1= discord.Embed(title=f'Ya hemos llegado a {cola_D} jugadores!', description='La votación comienza ahora', color=0x18e6ff)
                        embed1.add_field(name='Equipos aleatorios', value='1️⃣')
                        embed1.add_field(name='Equipos balanceados', value='2️⃣')
                        embed1.add_field(name='Equipos con capitanes', value='3️⃣')
                        embed1.set_footer(text='Powered by Exile Gaming', icon_url='https://imgur.com/IOKfTml.png')
                        msg = await ctx.send(f'''{jugadores_D[0]}{jugadores_D[1]}{jugadores_D[2]}{jugadores_D[3]}''', embed=embed1)
                        curso_D = 1
                        cola_members_D.append(client)
                        await msg.add_reaction(emoji='1️⃣')
                        await msg.add_reaction(emoji='2️⃣')
                        await msg.add_reaction(emoji='3️⃣')
                        i=0
                        while i < 3:
                            await cola_members_A[i].send(f'{jugadores_A[i]}, se ha completado la cola. Mira en canal para la votación.')
                            i += 1
                        msg_id_D = msg.id
                        message_D=msg
                        cola_D = 0
                        jugadores_D.clear()
            else:
                return

##============LEAVE==========
@client.command()
async def leave(ctx):
    user = ctx.author
    channel = ctx.channel.id
    if channel == 1009611785801834597:
        global cola_members_A
        global jugadores_A
        global curso_A
        global cola_A
        chan_a=client.get_channel(1009611785801834597)
        if curso_A == 0:
            if user in cola_members_A:
                cola_members_A.remove(user)
                jugadores_A.remove(user.mention)
                cola_A = cola_A-1
                embed = discord.Embed(title=f'Hay {cola_A} jugadores en cola', description=f'{user.mention} abandonó a la cola', color=0xb000ff)
                embed.set_footer(text='Powered by Exile Gaming', icon_url='https://imgur.com/IOKfTml.png')
                await chan_a.send(embed=embed)
        else:
            return
    ##----------RANK B--------------#
    if channel == 1009611818265755678:
        global cola_members_B
        global curso_B
        global cola_B
        chan_b=client.get_channel(1009611818265755678)
        if curso_B == 0:
            if user in cola_members_B:
                cola_members_B.remove(user)
                jugadores_B.remove(user.mention)
                cola_B = cola_B-1
                embed = discord.Embed(title=f'Hay {cola_B} jugadores en cola', description=f'{user.mention} abandonó a la cola', color=0xfa8cff)
                embed.set_footer(text='Powered by Exile Gaming', icon_url='https://imgur.com/IOKfTml.png')
                await chan_b.send(embed=embed)
        else:
            return
    ##--------------RANK C------------#
    if channel == 1009611839803506809:
        global cola_members_C
        global curso_C
        global cola_C
        chan=client.get_channel(1009611839803506809)
        if curso_C == 0:
            if user in cola_members_C:
                cola_members_C.remove(user)
                jugadores_C.remove(user.mention)
                cola_C = cola_C-1
                embed = discord.Embed(title=f'Hay {cola_C} jugadores en cola', description=f'{user.mention} abandonó a la cola', color=0x2659ff)
                embed.set_footer(text='Powered by Exile Gaming', icon_url='https://imgur.com/IOKfTml.png')
                await chan.send(embed=embed)
        else:
            return
    ##-------------RANK D--------------#  
    if channel == 1009611859529302046:
        global cola_members_D
        global curso_D
        global cola_D
        chan_D=client.get_channel(1009611859529302046)
        if curso_D == 0:
            if user in cola_members_D:
                cola_members_D.remove(user)
                jugadores_D.remove(user.mention)
                cola_D = cola_D-1
                embed = discord.Embed(title=f'Hay {cola_D} jugadores en cola', description=f'{user.mention} abandonó a la cola', color=0x18e6ff)
                embed.set_footer(text='Powered by Exile Gaming', icon_url='https://imgur.com/IOKfTml.png')
                await chan_D.send(embed=embed)
        else:
            return


@client.event
async def on_ready():
    await client.change_presence(activity=discord.Game(name="EXL Gaming"))
    print('Hello')
    now = datetime.now(timezone.utc).astimezone()
    dt_string = now.strftime("%B %d, %Y %H:%M:%S")
    print(dt_string)



@client.event
async def on_raw_reaction_add(payload):
    member = payload.member
    emoji = payload.emoji.name
    global msg_id_A
    ##------------------RANK A-----------------#
    if msg_id_A == payload.message_id:
        guild = member.guild
        global curso_A
        global cola_members_A
        global v1_A
        global v2_A
        global v3_A
        global message_A
        global votaciones_A
        if member in cola_members_A:
            if member not in votaciones_A:
                votaciones_A.append(member)
                if emoji=='1️⃣':
                    v1_A = v1_A +1
                if emoji=='2️⃣':
                    v2_A = v2_A +1
                if emoji=='3️⃣':
                    v3_A = v3_A +1
                await message_A.remove_reaction(emoji, member)
                embed2= discord.Embed(title=f'Ya hemos llegado a {cola_A} jugadores!', description='La votación comienza ahora', color=0xb000ff)
                embed2.add_field(name='Equipos aleatorios', value='Pulsa 1️⃣')
                embed2.add_field(name='Equipos balanceados', value='Pulsa 2️⃣ (DESHABILITADO)')
                embed2.add_field(name='Equipos con capitanes', value='Pulsa 3️⃣ (DESHABILITADO)')
                embed2.add_field(name='Votos mandados', value=f'{v1_A+v2_A+v3_A}', inline=False)
                embed2.set_footer(text='Powered by Exile Gaming', icon_url='https://imgur.com/IOKfTml.png')
                await message_A.edit(embed=embed2)
                if v1_A+v2_A+v3_A==4:
                    if v2_A<v1_A>v3_A: 
                        vote_final = 'Aleatorio'
                    if v1_A<v2_A>v3_A:
                        vote_final='Balanceados'
                    if v2_A<v3_A>v1_A:
                        vote_final='Capitanes'
                    if v1_A==2==v2_A:
                        vote_final= random.choice(['Aleatorio', 'Balanceado'])
                    if v2_A==2==v3_A:
                        vote_final= random.choice(['Balanceado', 'Capitanes'])
                    if v1_A==2==v3_A:
                        vote_final= random.choice(['Aleatorio', 'Capitanes'])
                    lobby = lobby_create()
                    embed= discord.Embed(title=f'Por favor uniros a la Lobby#{lobby} en la categoría Rank A', description=f'''Todos losjugadores se deberán unir   antes de que se hagan los equipos.
**Resultado votacioes**: {vote_final}''', color=0xb000ff)
                    chan_a=client.get_channel(1009611785801834597)
                    embed.set_footer(text='Powered by Exile Gaming', icon_url='https://imgur.com/IOKfTml.png')
                    await chan_a.send(f'{cola_members_A[0].mention}{cola_members_A[1].mention}{cola_members_A[2].mention}{cola_members_A[3].mention}', embed=embed)
                    #await msg_id_A.delete()
                    category = discord.utils.get(chan_a.guild.categories, name='Rank A')
                    lobby_chat = await guild.create_voice_channel(f'Lobby#{lobby}', category=category)
                    if vote_final == 'Capitanes':
                        await capitanes(cola_members=cola_members_A, canal=chan_a, rank='A', num_lobby=lobby)
                        v_team1 = await guild.create_voice_channel('- Team 1 -', category=category, user_limit=2)
                        v_team2 = await guild.create_voice_channel('- Team 2 -', category=category, user_limit=2)
                        v_channels(v1= v_team1, v2= v_team2, lobby_chat = lobby_chat, id=lobby)
                    if vote_final == 'Aleatorio':
                        await aleatorio(cola_members=cola_members_A, canal=chan_a, rank='A', num_lobby=lobby)
                        v_team1 = await guild.create_voice_channel('- Team 1 -', category=category, user_limit=2)
                        v_team2 = await guild.create_voice_channel('- Team 2 -', category=category, user_limit=2)
                        v_channels(v1= v_team1, v2= v_team2, lobby_chat = lobby_chat, id=lobby)
                    if vote_final == 'Balanceado':
                        await aleatorio(cola_members=cola_members_A, canal=chan_a, rank='A', num_lobby=lobby)
                        v_team1 = await guild.create_voice_channel('- Team 1 -', category=category, user_limit=2)
                        v_team2 = await guild.create_voice_channel('- Team 2 -', category=category, user_limit=2)
                        v_channels(v1= v_team1, v2= v_team2, lobby_chat = lobby_chat, id=lobby)
                    v1_A=0
                    v2_A=0
                    v3_A=0
                    curso_A = 0
                    msg_id_A = 0
                    votaciones_A.clear()
                    cola_members_A.clear()
            else:
                await message_A.remove_reaction(emoji, member)
        elif member not in cola_members_A:
            return
    ##-------------------RANK B------------------#
    if msg_id_B == payload.message_id:
        guild = member.guild
        global curso_B
        global cola_members_B
        global v1_B
        global v2_B
        global v3_B
        global message_B
        member = payload.member
        emoji = payload.emoji.name
        if member in cola_members_B:
            if emoji=='1️⃣':
                v1_B = v1_B +1
            if emoji=='2️⃣':
                v2_B = v2_B +1
            if emoji=='3️⃣':
                v3_B = v3_B +1
            await message_B.remove_reaction(emoji, member)
            
            if v1_B+v2_B+v3_B==4:
                if v2_B<v1_B>v3_B: 
                    vote_final = 'Aleatorio'
                if v1_B<v2_B>v3_B:
                    vote_final='Balanceados'
                if v2_B<v3_B>v1_B:
                    vote_final='Capitanes'
                if v1_B==2==v2_B:
                    vote_final= random.choice(['Aleatorio', 'Balanceado'])
                if v2_B==2==v3_B:
                    vote_final= random.choice(['Balanceado', 'Capitanes'])
                if v1_B==2==v3_B:
                    vote_final= random.choice(['Aleatorio', 'Capitanes'])
                embed= discord.Embed(title='Por favor uniros a la Lobby#'+' en la categoría Rank B', description=f'''Todos los jugadores se deberán unir en 7 minutos para que los equipos se eligan.
                **Resultado votaciones**: {vote_final}''', color=0xb000ff)
                chan_a=client.get_channel(1009611818265755678)
                embed.set_footer(text='Powered by Exile Gaming', icon_url='https://imgur.com/IOKfTml.png')
                await chan_a.send(f'{cola_members_B[0].mention}{cola_members_B[1].mention}{cola_members_B[2].mention}{cola_members_B[3].mention}', embed=embed)
                lobby = await lobby_create()
                print(lobby)
                await guild.create_voice_channel(f'Lobby {lobby}')
                if vote_final == 'Capitanes':
                    await capitanes(cola_members=cola_members_B, canal=chan_a, rank='B', num_lobby=lobby)
                cola_members_B.clear()
                v1_B=0
                v2_B=0
                v3_B=0
                curso_B = 0
        elif member not in cola_members_B:
            await message_B.remove_reaction(emoji, member)
            print('no está')
            
    ###################################################



@client.command()
async def report(ctx, id, w):
    user = ctx.author
    message = ctx.message
    await message.add_reaction('⏳')
    try:       
        connection = mysql.connector.connect(
            host='sql133.main-hosting.eu',
            user='u789788981_ismael',
            password=contraseña_sql,
            database='u789788981_polarisleague'
        )
        if connection.is_connected():
            #Conectamos
            print('hemos entrado n el inframundo')
            Cursor = connection.cursor()
            Cursor.execute(f"SELECT `ganador` from `rank_partidos` WHERE `id`={id}")
            comparar = Cursor.fetchall()
            x=0
            for row in comparar:
                x = row[0]
            
            if x == '':
                Cursor.execute(f"SELECT * from `rank_partidos` WHERE `id` = {id}")
                comparar = Cursor.fetchall()
                ids = list(comparar[0])
                print(ids)
                if str(user.id) in ids:
                    ganador1 = str(user.id)
                    if ids.index(ganador1) == 1:
                        ganador2= ids[2]
                        perdedor1 = ids[3]
                        perdedor2 = ids[4]
                        g_dato = 0
                        team = 'jugador1_1'
                    if ids.index(ganador1) == 2:
                        ganador2= ids[1]
                        perdedor1 = ids[3]
                        perdedor2 = ids[4]
                        g_dato = 0
                        team = 'jugador1_2'
                    if ids.index(ganador1) == 3:
                        ganador2= ids[4]
                        perdedor1 = ids[2]
                        perdedor2 = ids[1]
                        g_dato = 1
                        team = 'jugador2_1'
                    if ids.index(ganador1) == 4:
                        ganador2= ids[3]
                        perdedor1 = ids[2]
                        perdedor2 = ids[1]
                        g_dato = 1
                        team = 'jugador2_2'
                    Cursor.execute(f"SELECT `elo` FROM `rank_jugadores` WHERE `id_discord`={ganador1}")
                    comparar = Cursor.fetchall()
                    elo = list(comparar[0])
                    elo_ganador1 = int(elo[0])
                    Cursor.execute(f"SELECT `elo` FROM `rank_jugadores` WHERE `id_discord`={ganador2}")
                    comparar = Cursor.fetchall()
                    elo = list(comparar[0])
                    elo_ganador2 = int(elo[0])
                    Cursor.execute(f"SELECT `elo` FROM `rank_jugadores` WHERE `id_discord`={perdedor1}")
                    comparar = Cursor.fetchall()
                    elo = list(comparar[0])
                    elo_perdedor1 = int(elo[0])
                    Cursor.execute(f"SELECT `elo` FROM `rank_jugadores` WHERE `id_discord`={perdedor2}")
                    comparar = Cursor.fetchall()
                    elo = list(comparar[0])
                    elo_perdedor2 = int(elo[0])

                    elo_ganador1 += 15
                    elo_ganador2 += 15
                    elo_perdedor1 -= 12
                    elo_perdedor2 -= 12

                    Cursor.execute(f"UPDATE `rank_jugadores` SET `elo`='{elo_ganador1}' WHERE `id_discord` = {ganador1}")
                    Cursor.execute(f"UPDATE `rank_jugadores` SET `elo`='{elo_ganador2}' WHERE `id_discord` = {ganador2}")
                    Cursor.execute(f"UPDATE `rank_jugadores` SET `elo`='{elo_perdedor1}' WHERE `id_discord` = {perdedor1}")
                    Cursor.execute(f"UPDATE `rank_jugadores` SET `elo`='{elo_perdedor2}' WHERE `id_discord` = {perdedor2}")
                    Cursor.execute(f"UPDATE `rank_partidos` SET `ganador`='{g_dato}' WHERE `{team}` = {ganador1} AND `id` = {id}")

                    

                    Cursor.execute(f"SELECT `v_team1` FROM `rank_partidos` WHERE `id`={id}")
                    comparar = Cursor.fetchall()
                    id_v = list(comparar[0])
                    print(id_v)
                    v_c = client.get_channel(int(id_v[0]))
                    await v_c.delete()

                    Cursor.execute(f"SELECT `v_team2` FROM `rank_partidos` WHERE `id`={id}")
                    comparar = Cursor.fetchall()
                    id_v = list(comparar[0])
                    v_c = client.get_channel(int(id_v[0]))
                    await v_c.delete()

                    Cursor.execute(f"SELECT `v_lobby` FROM `rank_partidos` WHERE `id`={id}")
                    comparar = Cursor.fetchall()
                    id_v = list(comparar[0])
                    v_c = client.get_channel(int(id_v[0]))
                    await v_c.delete()

                    Cursor.execute(f"SELECT `fecha` FROM `rank_partidos` WHERE `id`={id}")
                    comparar = Cursor.fetchall()
                    fecha = list(comparar[0])
                    embed3 = discord.Embed(title=f'Partido {id}', color=0xb000ff)
                    embed3.add_field(name='GANADORES', value=f'<@{ganador1}> & <@{ganador2}>', inline=True)
                    embed3.add_field(name='PERDEDORES', value=f'<@{perdedor1}> & <@{perdedor2}>', inline=False)
                    embed3.set_footer(text=f'{fecha[0]}', icon_url='https://imgur.com/IOKfTml.png')

                    reports = client.get_channel(1009609847001600101)
                    await reports.send(embed=embed3)
                    await message.add_reaction('✅')
                else:
                    print('no está')
                connection.commit()
                Cursor.close()
                connection.close()
            else:
                await message.add_reaction('❌')
    except Error as e:
                print("Error while connecting to MySQL", e)


def comprobacion_compas(jugador1, jugador2):
    try:
        connection = mysql.connector.connect(
            host='sql133.main-hosting.eu',
            user='u789788981_ismael',
            password=contraseña_sql,
            database='u789788981_polarisleague'
        )
        if connection.is_connected():
            #Conectamos
            Cursor = connection.cursor()

            ##-----------JUGADOR 1 ------------

            #ELO------
            Cursor.execute(f"SELECT `elo` from `rank_jugadores` WHERE `id_discord`='{jugador1}'")
            comparar = Cursor.fetchall()
            x=0
            for row in comparar:
                x = row[0]
            elo1 = x
            ##WINS --------------
            Cursor.execute(f"SELECT `id` FROM `rank_partidos` WHERE `jugador1_1`= '{jugador1}' AND `ganador`='0' OR `jugador1_2`= '{jugador1}' AND `ganador`='0' OR `jugador2_1`= '{jugador1}' AND `ganador`='1' OR `jugador2_2`= '{jugador1}' AND `ganador`='1'")
            comparar = Cursor.fetchall()
            x=0
            for row in comparar:
                x += 1
            wins1 = x
            ##LOSES--------
            Cursor.execute(f"SELECT `id` FROM `rank_partidos` WHERE `jugador1_1`= '{jugador1}' AND `ganador`='1' OR `jugador1_2`= '{jugador1}' AND `ganador`='1' OR `jugador2_1`= '{jugador1}' AND `ganador`='0' OR `jugador2_2`= '{jugador1}' AND `ganador`='0'")
            comparar = Cursor.fetchall()
            x=0
            for row in comparar:
                x += 1
            loses1 = x
            partidos_jugados1 = wins1+loses1
            if partidos_jugados1==0:
                wr1 = 0
            else:
                wr1 = 100/partidos_jugados1 * wins1

            ##-----------JUGADOR 2------------

            #ELO------
            Cursor.execute(f"SELECT `elo` from `rank_jugadores` WHERE `id_discord`='{jugador2}'")
            comparar = Cursor.fetchall()
            x=0
            for row in comparar:
                x = row[0]
            elo2 = x
            ##WINS --------------
            Cursor.execute(f"SELECT `id` FROM `rank_partidos` WHERE `jugador1_1`= '{jugador2}' AND `ganador`='0' OR `jugador1_2`= '{jugador2}' AND `ganador`='0' OR `jugador2_1`= '{jugador2}' AND `ganador`='1' OR `jugador2_2`= '{jugador2}' AND `ganador`='1'")
            comparar = Cursor.fetchall()
            x=0
            for row in comparar:
                x += 1
            wins2 = x
            ##LOSES--------
            Cursor.execute(f"SELECT `id` FROM `rank_partidos` WHERE `jugador1_1`= '{jugador2}' AND `ganador`='1' OR `jugador1_2`= '{jugador2}' AND `ganador`='1' OR `jugador2_1`= '{jugador2}' AND `ganador`='0' OR `jugador2_2`= '{jugador2}' AND `ganador`='0'")
            comparar = Cursor.fetchall()
            x=0
            for row in comparar:
                x += 1
            loses2 = x
            partidos_jugados2 = wins2+loses2
            if partidos_jugados2==0:
                wr2 = 0
            else:
                wr2 = 100/partidos_jugados2 * wins2

            return elo1, elo2, wins1, wins2, loses1, loses2, wr1, wr2
    except Error as e:
         print('falla en comprobación de compas')
         print("Error while connecting to MySQL", e)


@client.command()
async def stats(ctx):
    user = ctx.author
    try:
        connection = mysql.connector.connect(
            host='sql133.main-hosting.eu',
            user='u789788981_ismael',
            password=contraseña_sql,
            database='u789788981_polarisleague'
        )
        if connection.is_connected():
            #Conectamos
            Cursor = connection.cursor()
            #ELO------
            Cursor.execute(f"SELECT `elo` from `rank_jugadores` WHERE `id_discord`={user.id}")
            comparar = Cursor.fetchall()
            x=0
            for row in comparar:
                x = row[0]
            elo = x
            ##WINS --------------
            Cursor.execute(f"SELECT `id` FROM `rank_partidos` WHERE `jugador1_1`= '{user.id}' AND `ganador`='0' OR `jugador1_2`= '{user.id}' AND `ganador`='0' OR `jugador2_1`= '{user.id}' AND `ganador`='1' OR `jugador2_2`= '{user.id}' AND `ganador`='1'")
            comparar = Cursor.fetchall()
            x=0
            for row in comparar:
                x += 1
            wins = x
            ##LOSES--------
            Cursor.execute(f"SELECT `id` FROM `rank_partidos` WHERE `jugador1_1`= '{user.id}' AND `ganador`='1' OR `jugador1_2`= '{user.id}' AND `ganador`='1' OR `jugador2_1`= '{user.id}' AND `ganador`='0' OR `jugador2_2`= '{user.id}' AND `ganador`='0'")
            comparar = Cursor.fetchall()
            x=0
            for row in comparar:
                x += 1
            loses = x
            partidos_jugados = wins+loses
            if partidos_jugados==0:
                wr = 0
            else:
                wr = 100/partidos_jugados * wins
            await ctx.reply(f'ELO: {elo} / WINS: {wins} / LOSES: {loses} / WINRATE: {round(wr,1)}%')
    except Error as e:
         print("Error while connecting to MySQL", e)
         await ctx.reply('No estás registrado', mention_author=False)



async def capitanes(cola_members, canal, rank, num_lobby):
    capi1 = random.choice(cola_members)
    cola_members.remove(capi1)
    capi2 = random.choice(cola_members)
    cola_members.remove(capi2)
    eligiendo = random.choice([capi1, capi2])
    embed = discord.Embed(title=f'Lobby#{num_lobby}', description=f'''**Capitán 1**: {capi1}
    **Capitán 2**: {capi2}
    Eligiendo: {eligiendo}''', color=0xb000ff)
    await canal.send(embed=embed)

    stats = list(comprobacion_compas(jugador1=cola_members[0].id, jugador2=cola_members_A[1].id))
    
    #class MyView(View): # Create a class called MyView that subclasses discord.ui.View
    #    team1=[]
    #    team2=[]
    #    elegido = []
    #    no_elegido=[]
    #    @discord.ui.button(label=f"{cola_members[0]}", style=discord.ButtonStyle.primary, emoji="😎") # Create a button with the label "😎 Click me!" with color Blurple
    #    async def button_callback(self, button, interaction):
    #        for child in self.children: # loop through all the children of the view
    #            child.disabled = True # set the button to disabled
    #        button.style = discord.ButtonStyle.green
    #        elegido = cola_members[0]
    #        no_elegido = cola_members[1]
    #        if capi1 == eligiendo:
    #            team1 = [eligiendo, elegido]
    #            team2 = [capi2, no_elegido]
    #        if capi2 == eligiendo:
    #            team1 = [eligiendo, elegido]
    #            team2 = [capi1, no_elegido]
    #        cola_members.clear()
    #        self.team1 = team1
    #        self.team2 = team2
    #        self.elegido = elegido
    #        self.no_elegido = no_elegido
    #        await interaction.response.edit_message(view=self)
    #        await interaction.followup.send(f'Has elegido a {elegido.name} correctamente', ephemeral=True)
#
#
    #    @discord.ui.button(label="Click me2!", style=discord.ButtonStyle.primary, emoji="😎") # Create a button with the label "😎 Click me!" with color Blurple
    #    async def button1_callback(self, button, interaction):
    #        for child in self.children: # loop through all the children of the view
    #            child.disabled = True # set the button to disabled
    #        button.style = discord.ButtonStyle.green
    #        elegido = cola_members[1]
    #        await interaction.respond(content=f'Has elegido a {elegido.name} correctamente', ephemeral=True)
    #        no_elegido = cola_members[0]
    #        if capi1 == eligiendo:
    #            team1 = [eligiendo, elegido]
    #            team2 = [capi2, no_elegido]
    #        if capi2 == eligiendo:
    #            team1 = [eligiendo, elegido]
    #            team2 = [capi1, no_elegido]
    #        cola_members.clear()
    #        self.team1 = team1
    #        self.team2 = team2
    #        self.elegido = elegido
    #        self.no_elegido = no_elegido
    #        await interaction.response.edit_message(view=self)
    #        await interaction.followup.send('You chose the second button') # Send a message when the button is clicked
    #view = MyView()
    #team2 = MyView.team2
    #
    #team1 = MyView.team1
    #elegido = MyView.elegido
    #no_elegido = MyView.no_elegido
    button1 = Button(style=discord.ButtonStyle.primary, label=f'{cola_members[0].name}', custom_id='jugador1')
    button2 = Button(style=discord.ButtonStyle.primary, label=f'{cola_members[1].name}', custom_id='jugador2')
    view = View()
    view.add_item(button1)
    view.add_item(button2)
    await eligiendo.send(f'''Elige a uno de los 2 jugadores:
🅰️ {cola_members[0].name}: ELO: {stats[0]} / WINS: {stats[2]} / LOSES: {stats[4]} / WR: {stats[6]}
🅱️ {cola_members[1].name}: ELO: {stats[1]} / WINS: {stats[3]} / LOSES: {stats[5]} / WR: {stats[7]}''', view=view)
    while True:
        try:
            interaction = await client.wait_for('button_click')
            if interaction.component.id == 'jugador1':
                user = interaction.author
                elegido = cola_members[0]
                await interaction.respond(content=f'Has elegido a {elegido.name} correctamente', ephemeral=True)
                no_elegido = cola_members[1]
                if capi1 == eligiendo:
                    team1 = [eligiendo, elegido]
                    team2 = [capi2, no_elegido]
                if capi2 == eligiendo:
                    team1 = [eligiendo, elegido]
                    team2 = [capi1, no_elegido]
                cola_members.clear()

            if interaction.component.id == 'jugador2':
                user = interaction.author
                elegido = cola_members[1]
                await interaction.respond(content=f'Has elegido a {elegido.name} correctamente', ephemeral=True)
                no_elegido = cola_members[0]
                if capi1 == eligiendo:
                    team1 = [eligiendo, elegido]
                    team2 = [capi2, no_elegido]
                if capi2 == eligiendo:
                    team1 = [eligiendo, elegido]
                    team2 = [capi1, no_elegido]
                cola_members.clear()
            embed2 = discord.Embed(title='Lobby#', description='Ya se han elegido los equipos!', color=0xb000ff)
            embed2.add_field(name='-Team 1-', value=f'{team1[0].mention}, {team1[1].mention}', inline = False)
            embed2.add_field(name='-Team 2-', value=f'{team2[0].mention}, {team2[1].mention}', inline = False)
            embed2.set_footer(text='Powered by Exile Gaming', icon_url='https://imgur.com/IOKfTml.png')
            if rank == 'A':
                canal = client.get_channel(1009611785801834597)
            if rank == 'B':
                canal = client.get_channel(1009611818265755678)
            num_lobby1 = num_lobby
            print(num_lobby, num_lobby1)
            await canal.send(embed=embed2)
            creador = random.choice([eligiendo, elegido, capi2, no_elegido])
            print('aquí estamos')
            pasw = generate_random_password()
            print('La contraseña de generate random pass = '+pasw)
            embed_c = discord.Embed(title='Detalles de Lobby', description=f'**Match ID:** {num_lobby}')
            embed_c.add_field(name='Lobby Name:', value=f'L{num_lobby}', inline = False)
            embed_c.add_field(name='Password:', value=f'{pasw}', inline = False)
            embed_c.add_field(name='Creando:', value=f'{creador}', inline = False)
            embed_c.set_footer(text='Powered by Exile Gaming', icon_url='https://imgur.com/IOKfTml.png')
            await eligiendo.send(embed=embed_c)
            await elegido.send(embed=embed_c)
            await capi2.send(embed=embed_c)
            await no_elegido.send(embed=embed_c)
            try:

                connection = mysql.connector.connect(
                    host='sql133.main-hosting.eu',
                    user='u789788981_ismael',
                    password=contraseña_sql,
                    database='u789788981_polarisleague'
                )
                if connection.is_connected():
                    #Conectamos
                    print('hemos entrado n el inframundo')
                    Cursor = connection.cursor()
                    Cursor.execute(f"UPDATE `rank_partidos` SET `jugador1_1`='{team1[0].id}',`jugador1_2`='{team1[1].id}',`jugador2_1`='{team2[0].id}',`jugador2_2`='{team2[1].id}',`rank`='{rank}' WHERE `id` = {num_lobby}")
                    comparar = Cursor.fetchall()
                    connection.commit()
                    Cursor.close()
                    connection.close()
            except Error as e:
                print('falla en capitanes')
                print("Error while connecting to MySQL", e)

        except:
            print('error')
        


async def aleatorio(cola_members, canal, rank, num_lobby):
    jugador1_1 = random.choice(cola_members)
    cola_members.remove(jugador1_1)
    jugador2_1 = random.choice(cola_members)
    cola_members.remove(jugador2_1)
    team1 = [jugador1_1, jugador2_1]
    team2 = [cola_members[0], cola_members[1]]
    embed2 = discord.Embed(title=f'Lobby#{num_lobby}', description='Ya se han elegido los equipos!', color=0xb000ff)
    embed2.add_field(name='-Team 1-', value=f'{team1[0].mention}, {team1[1].mention}', inline = False)
    embed2.add_field(name='-Team 2-', value=f'{team2[0].mention}, {team2[1].mention}', inline = False)
    embed2.set_footer(text='Powered by Exile Gaming', icon_url='https://imgur.com/IOKfTml.png')
    if rank == 'A':
        canal = client.get_channel(1009611785801834597)
    if rank == 'B':
        canal = client.get_channel(1009611818265755678)
    await canal.send(embed=embed2)

    creador = random.choice([jugador1_1, jugador2_1, cola_members[0], cola_members[1]])
    pasw = generate_random_password()
    embed_c = discord.Embed(title='Detalles de Lobby', description=f'**Match ID:** {num_lobby}')
    embed_c.add_field(name='Lobby Name:', value=f'L{num_lobby}', inline = False)
    embed_c.add_field(name='Password:', value=f'{pasw}', inline = False)
    embed_c.add_field(name='Creando:', value=f'{creador}', inline = False)
    embed_c.set_footer(text='Powered by Exile Gaming', icon_url='https://imgur.com/IOKfTml.png')
    try:
        await jugador1_1.send(embed=embed_c)
    except discord.Forbidden:
        pass
    try:
        await jugador2_1.send(embed=embed_c)
    except discord.Forbidden:
        pass
    try:
        await cola_members[0].send(embed=embed_c)
    except discord.Forbidden:
        pass
    try:
        await cola_members[1].send(embed=embed_c)
    except discord.Forbidden:
        pass


    print(team1[0].id)
    print(num_lobby)
    try:
        connection = mysql.connector.connect(
            host='sql133.main-hosting.eu',
            user='u789788981_ismael',
            password=contraseña_sql,
            database='u789788981_polarisleague'
        )
        if connection.is_connected():
          #Conectamos
          Cursor = connection.cursor()
          Cursor.execute(f"UPDATE `rank_partidos` SET `jugador1_1`= {team1[0].id},`jugador1_2`= {team1[1].id},`jugador2_1`= {team2[0].id},`jugador2_2`={team2[1].id},`rank`='{rank}' WHERE `id`= {num_lobby}")
          print('llegamos aquuuuuí')
    except Error as e:
        print("Error while connecting to MySQL", e)


async def balanceado(cola_members, canal, rank, num_lobby):
    jugador1_1 = random.choice([cola_members])
    cola_members.remove(jugador1_1)
    jugador2_1 = random.choice([cola_members])
    cola_members.remove(jugador2_1)
    team1 = [jugador1_1, jugador2_1]
    team2 = [cola_members[0], cola_members[1]]
    cola_members.clear()
    embed2 = discord.Embed(title='Lobby#', description='Ya se han elegido los equipos!', color=0xb000ff)
    embed2.add_field(name='-Team 1-', value=f'{team1[0].mention}, {team1[1].mention}', inline = False)
    embed2.add_field(name='-Team 2-', value=f'{team2[0].mention}, {team2[1].mention}', inline = False)
    embed2.set_footer(text='Powered by Exile Gaming', icon_url='https://imgur.com/IOKfTml.png')
    if rank == 'A':
        canal = client.get_channel(1009611785801834597)
    if rank == 'B':
        canal = client.get_channel(1009611818265755678)
    await canal.send(embed=embed2)



def generate_random_password():
    caracteres = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','0','1','2','3','4','5','6','7','8','9','!','#','@']

    caracteres_pass = []
    i=0
    while i <6:
        chose = random.choice(caracteres)
        caracteres_pass.append(chose)
        i += 1
    f_password = ''.join(caracteres_pass)
    print(f_password)
    return f_password



def lobby_create():
    now = datetime.now(timezone.utc).astimezone()
    dt_string = now.strftime("%B %d, %Y %H:%M:%S")
    print('hasta aquí llego')
    try:
        connection = mysql.connector.connect(
            host='sql133.main-hosting.eu',
            user='u789788981_ismael',
            password=contraseña_sql,
            database='u789788981_polarisleague'
        )
        if connection.is_connected():
            #Conectamos
            Cursor = connection.cursor()
            Cursor.execute(f"INSERT INTO `rank_partidos`(`id`, `jugador1_1`, `jugador1_2`, `jugador2_1`, `jugador2_2`, `ganador`, `fecha`, `rank`, `v_team1`, `v_team2`, `v_lobby`) VALUES ('[value-1]','[value-2]','[value-3]','[value-4]','[value-5]','','{dt_string}','','[value-9]','[value-10]','[value-11]')")
            comparar = Cursor.fetchall()
            Cursor.execute(f"SELECT `id` from `rank_partidos` ORDER BY `id`")
            comparar = Cursor.fetchall()
            connection.commit()
            Cursor.close()
            connection.close()
            x=0
            for row in comparar:
                x = row[0]
            print(x)
            return x
    except Error as e:
         print('falla en lobby create')
         print("Error while connecting to MySQL", e)


def v_channels(v1, v2, lobby_chat, id):
    try:         
        connection = mysql.connector.connect(
            host='sql133.main-hosting.eu',
            user='u789788981_ismael',
            password=contraseña_sql,
            database='u789788981_polarisleague'
        )
        if connection.is_connected():
            #Conectamos
            print('hemos entrado n el inframundo')
            Cursor = connection.cursor()
            Cursor.execute(f"UPDATE `rank_partidos` SET `v_team1`='{v1.id}',`v_team2`='{v2.id}',`v_lobby`='{lobby_chat.id}' WHERE `id` = {id}")
            connection.commit()
            Cursor.close()
            connection.close()
    except Error as e:
        print("Error while connecting to MySQL", e)   

class MyView2(View): # Create a class called MyView that subclasses discord.ui.View
    @discord.ui.button(label="Click me!", style=discord.ButtonStyle.primary, emoji="😎") # Create a button with the label "😎 Click me!" with color Blurple
    async def button_callback(self, button, interaction):
        for child in self.children: # loop through all the children of the view
            child.disabled = True # set the button to disabled
        button.style = discord.ButtonStyle.green
        await interaction.response.edit_message(view=self)
        await interaction.followup.send('You chose the first button')
        

        
    @discord.ui.button(label="Click me2!", style=discord.ButtonStyle.primary, emoji="😎") # Create a button with the label "😎 Click me!" with color Blurple
    async def button1_callback(self, button, interaction):
        for child in self.children: # loop through all the children of the view
            child.disabled = True # set the button to disabled
        button.style = discord.ButtonStyle.green
        await interaction.response.edit_message(view=self)
        await interaction.followup.send('You chose the second button') # Send a message when the button is clicked
        


@client.command() # Create a slash command
async def button(ctx):
    await ctx.respond("This is a button!", view=MyView2()) # Send a message with our View class that contains the button





@client.add_command(guild_ids=[780485379613523990], name='leaderboards', description='Mira los rankings de tu elo!')
async def leaderboards(ctx, rank):
    user = ctx.author
    print(user.mention)
    try:
        connection = mysql.connector.connect(
            host='sql133.main-hosting.eu',
            user='u789788981_ismael',
            password=contraseña_sql,
            database='u789788981_polarisleague'
        )
        if connection.is_connected():
            #Conectamos
            Cursor = connection.cursor()
            Cursor.execute(f"SELECT `id_discord`, `elo`, `rank` FROM `rank_jugadores` ORDER BY `elo` desc")
            comparar = Cursor.fetchall()
            connection.commit()
            Cursor.close()
            connection.close()
            leaders=[['Nickname','ELO', 'RANK']]
            index = len(comparar)
            i=0
            while i<index:
              leaders.append(list(comparar[i]))
              i+=1
            for x in range(len(leaders)):
              if len(leaders[x][0]) == 18:
                leaders[x][0] = f'<@{leaders[x][0]}>'
            tabla= tabulate(leaders, headers='firstrow', tablefmt='grid', showindex=range(1,i+1))
            embed = discord.Embed(title='Leaderboards', description=tabla)
            await ctx.reply(embed=embed)
    except Error as e:
         print("Error while connecting to MySQL", e)



client.run(os.environ["TOKEN"])

