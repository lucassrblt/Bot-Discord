import discord
from discord.ext import commands
import youtube_dl
intents = discord.Intents.all()
intents.messages = True
intents.members = True
intents.typing = True
client = discord.Client(intents=intents)
ytdl = youtube_dl.YoutubeDL()


class Video:
  def __init__(self,link):
      video = ytdl.extract_info(link, download=False)
      video_format = video["formats"][0]
      self.url = video["webpage_url"]
      self.stream_url = video_format["url"]


# Listes et variables utilisées 
jeu = ("GuessWho?")
jeu_lancement = ("!guesswhostart")
jeu_règles = ("!guesswhorules")
jeu_score = ("!guesswhoscore")
jeu_restart = ("!guesswhorestart")
indice1_perso1 = "Ma première apparition dans le Shonen Jump 📚🇯🇵 date de 1997."
indice2_perso1 = "Je suis issu d’un manga 🇯🇵 à succès ⭐️ toujours en cours."
indice3_perso1 = "L’eau 💧 m'affaiblit et je coule 🌊."
indice4_perso1 = "Je parcours les mers avec mon équipage 🏴‍☠️."
indice5_perso1 = "Mon chapeau de paille👒 est connu partout dans le monde."
indice_perso1 = [indice1_perso1,indice2_perso1,indice3_perso1,indice4_perso1,indice5_perso1]
indice1_perso2 = "Le récit du film 🎬🍿 dans lequel j'apparais se déroule entre les années 1950 et 1980 aux Etats-Unis 🇺🇸."
indice2_perso2 = "Je suis nommé 20ème 🎖 plus grand personnage de cinéma de tous les temps."
indice3_perso2 = "Je suis à la fois joueur de football américain 🏈 et soldat 🫡."
indice4_perso2 = "J’ai donné mon nom au film dans lequel j'apparais."
indice5_perso2 = "Je suis interprété 🎥 par Tom Hanks."
indice_perso2 = [indice1_perso2,indice2_perso2,indice3_perso2,indice4_perso2,indice5_perso2]
indice1_perso3 = "Je suis issu d’une série animé américaine très connue."
indice2_perso3 = "J’apparais pour la première fois dans un épisode se nommant Noël mortel 🎄😵."
indice3_perso3 = "Dans cette série connue, je tiens un bar 🍻 dans lequel le personnage principal de la série vient souvent."
indice4_perso3 = "J’ai des excès de violences 😡 ainsi que des envies suicidaires ⚰️."
indice5_perso3 = "Je me fait toujours avoir par les canulars téléphoniques 📞😡 de Bart Simpson."
indice_perso3 = [indice1_perso3,indice2_perso3,indice3_perso3,indice4_perso3,indice5_perso3]
indice1_perso4 = "Dans ce film, j’apparais pour la première fois dans un avion ✈️."
indice2_perso4 = "Mon personnage possède un dédoublement de la personnalité 👬."
indice3_perso4 = "J‘ai créé un club mais la règle numéro 1 est l’interdiction d’en parler."
indice4_perso4 = "La règle numéro 2 de mon club est également l’interdiction d’en parler."
indice5_perso4 = "Je suis jouer 🎥 par Brad Pitt et Edward Norton."
indice_perso4 = [indice1_perso4,indice2_perso4,indice3_perso4,indice4_perso4,indice5_perso4]
indice1_perso5 = "Ma grandeur et ma puissance 💪🏽 ont fait trembler Rome 🏛."
indice2_perso5 = "Mon peuple et moi provenons des côtes d'Afrique du Nord🇹🇳🇲🇦🇩🇿."
indice3_perso5 = "J'ai utilisé des éléphants 🐘🐘 afin de franchir les Alpes 🏔."
indice4_perso5 = "Je suis né à Carthage 🇹🇳 en 247 av J-C 🏛."
indice5_perso5 = "Je suis un grand chef de guerre🤺 carthaginois ayant participé aux guerres puniques ⚔️."
indice_perso5 = [indice1_perso5,indice2_perso5,indice3_perso5,indice4_perso5,indice5_perso5]



@client.event
async def play2(url,channel,client) :
    video = Video(url)
    client = await channel.connect()
    play_song(client, video)

def play_song(client, song):
    source = discord.PCMVolumeTransformer(discord.FFmpegPCMAudio(song.stream_url))

    client.play(source)

  
async def perso1(message) : # Fonction permettant de lancer le premier quizz
    await message.channel.send(f"C'est parti pour le premier **{jeu}**. Voici les trois premiers indices :")
    await message.channel.send("Je suis un personnage  masculin.")  
    await message.channel.send("Je suis un personnage fictif.")
    await message.channel.send("Je suis un personnage extrait d'une oeuvre asiatique.")
    await message.channel.send("Qui suis-je ?")
    async def check(m) : 
        return m.author == message.m.author and message.m.channel == m.channel
    reponse = await client.wait_for("message", check=check)
    error = 0
    i  = 0
    index = 0
    global score
    score = 150
    while "luffy" not in reponse.content.lower() and error < 5 :
      if "!guesswhoscore" in reponse.content.lower() :
        await message.channel.send (f"Votre score est égale à : {score}")
        await message.channel.send("Qui suis-je ?")
        reponse = await client.wait_for("message",check=check)
      else :
        error+=1
        i += 1
        await message.channel.send("Mauvaise réponse !")
        await reponse.add_reaction ("❌")
        await message.channel.send(f"Pour t'aider un peu voici l'indice numéro {i}:")
        await message.channel.send(indice_perso1[index])
        await message.channel.send("Qui suis-je ?")
        index += 1
        score = score - 2
        reponse = await client.wait_for("message",check=check)
    if "luffy" in reponse.content.lower() :
      await message.channel.send("Bien joué !")
      await reponse.add_reaction ("✅")
      await reponse.channel.send ("https://imgur.com/cVXsnMN")
      await message.channel.send(f"Voici le deuxième **{jeu}**.")
    if "luffy" not in reponse.content.lower() and error ==5 :
      await message.channel.send("Mauvaise Réponse")
      await reponse.add_reaction ("❌")
      await message.channel.send("La réponse était Luffy.")
      await message.channel.send("https://imgur.com/InXIbEd")
      await message.channel.send("https://onepiece.fandom.com/fr/wiki/Monkey_D._Luffy")
      await message.channel.send(f"Voici le deuxième **{jeu}**.")
    
    
async def perso2(message) : # Fonction permettant de lancer le deuxième quizz
  global score
  print(score)
  message.content = message.content.lower()
  await message.channel.send(f"C'est parti pour le deuxième **{jeu}**. Voici les trois premiers indices :")
  await message.channel.send("Mon personnage est masculin.")  
  await message.channel.send("Mon personnage est extrait d'un film culte.")
  await message.channel.send("Ce film est apparu dans les années 90.") 
  await message.channel.send("Qui suis-je ?")
  async def check(m) :
      return m.author == message.m.author and message.m.channel == m.channel
  reponse = await client.wait_for("message", check=check)
  error = 0
  i = 0
  index = 0
  while "forest gump" not in reponse.content.lower() and error < 5 and "!guesswhorestart" not in reponse.content.lower() :
    if "!guesswhoscore" in reponse.content.lower() :
      await message.channel.send (f"Votre score est égale à : {score}")
      await message.channel.send("Qui suis-je ?")
      reponse = await client.wait_for("message",check=check)
    else :
      error += 1
      i += 1
      await message.channel.send("Mauvaise réponse !")
      await reponse.add_reaction ("❌")
      await message.channel.send(f"Pour t'aider un peu voici l'indice numéro {i}:")
      await message.channel.send(indice_perso2[index])
      await message.channel.send("Qui suis-je ?")
      reponse = await client.wait_for("message", check=check)
      index += 1
      score -= 4
  if "!guesswhoscore" in reponse.content.lower() :
    await message.channel.send (f"Votre score est égale à : {score}")
    await message.channel.send("Qui suis-je ?")
    reponse = await client.wait_for("message",check=check)
  if "forest gump" in reponse.content.lower():
    await message.channel.send("Bien joué !")
    await reponse.add_reaction ("✅")
    await reponse.channel.send("https://media.giphy.com/media/13bdJQNZ2HpXQk/giphy.gif")
    await message.channel.send(f"Voici le troisième **{jeu}**.")
  if "forest gump" not in  reponse.content.lower() and error == 5 :
    await message.channel.send("Mauvaise réponse !")
    await reponse.add_reaction ("❌")
    await message.channel.send ("La réponse était Forest Gump.")
    await message.channel.send ("https://media.giphy.com/media/JUv9NDR1pXpVSpxI9R/giphy.gif")
    await message.channel.send("https://fr.wikipedia.org/wiki/Forrest_Gump_(personnage)")
    await message.channel.send(f"Voici le troisième **{jeu}**.")


async def perso3(message) : # Fonction permettant de lancer le troisième quizz
  global score
  message.content = message.content.lower()
  await message.channel.send(f"C'est parti pour le troisième **{jeu}**. Voici les trois premiers indices :")
  await message.channel.send("Je suis un personnage de fiction.")  
  await message.channel.send("Je suis un personnage masculin.")
  await message.channel.send("J’apparais dans un dessin animé.") 
  await message.channel.send("Qui suis-je ?")
  async def check(m) : 
      return m.author == message.m.author and message.m.channel == m.channel
  reponse = await client.wait_for("message", check=check)
  error = 0 
  i = 0
  index = 0  
  while "mo" not in reponse.content.lower() and error < 5 :
    if "!guesswhoscore" in reponse.content.lower() : 
      await message.channel.send("Qui suis-je ?")
      await message.channel.send (f"Votre score est égale à : {score}")
      reponse = await client.wait_for("message",check=check)
    else :
      error += 1
      i += 1
      await message.channel.send("Mauvaise réponse !")
      await reponse.add_reaction ("❌")
      await message.channel.send(f"Pour t'aider un peu voici l'indice numéro {i}:")
      await message.channel.send(indice_perso3[index])
      await message.channel.send("Qui suis-je ?")
      reponse = await client.wait_for("message",check=check)
      index += 1
      score -= 6
  if "mo" in reponse.content.lower()  : 
      await message.channel.send("Bien joué !")
      await reponse.add_reaction ("✅")
      await reponse.channel.send("https://media.giphy.com/media/UMRb3OBnZelAQ/giphy.gif")
      await message.channel.send(f"Voici le quatrième **{jeu}**.")
  if "mo" not in reponse.content.lower() and error == 5 :
    await message.channel.send("Mauvaise réponse !")
    await reponse.add_reaction ("❌")
    await message.channel.send ("La réponse était Mo dans les Simpson.")
    await message.channel.send ("https://media.giphy.com/media/3orife65euFUUReNbO/giphy.gif")
    await message.channel.send("https://simpsons.fandom.com/fr/wiki/Moe_Szyslak")
    await message.channel.send(f"Voici le quatrième **{jeu}**.")

async def perso4(message) : # Fonction permettant de lancer le quatrième quizz
  global score
  message.content = message.content.lower()
  await message.channel.send(f"C'est parti pour le quatrième **{jeu}**. Voici les trois premiers indices :")
  await message.channel.send("Je suis personnage est masculin.")  
  await message.channel.send("Je suis un personnage de fiction.")
  await message.channel.send("Je suis issu d’un film culte sorti à la fin des années 90.") 
  await message.channel.send("Qui suis-je ?")
  async def check(m) : 
      return m.author == message.m.author and message.m.channel == m.channel
  reponse = await client.wait_for("message", check=check)
  index = 0
  i = 0 
  error = 0
  while "tyler" not in reponse.content.lower() and error < 5 :
    if "!guesswhoscore" in reponse.content.lower() :
      await message.channel.send (f"Votre score est égale à : {score}")
      await message.channel.send("Qui suis-je ?")
      reponse = await client.wait_for("message",check=check)
    else : 
      error += 1 
      i += 1
      await message.channel.send("Mauvaise réponse !")
      await reponse.add_reaction ("❌")
      await message.channel.send(f"Pour t'aider un peu voici l'indice numéro {i}:")
      await message.channel.send(indice_perso4[index])
      await message.channel.send("Qui suis-je ?")
      reponse = await client.wait_for("message",check=check)
      index += 1
      score -= 8
  if "tyler" in reponse.content.lower() : 
    await message.channel.send("Bien joué !")
    await reponse.add_reaction ("✅")
    await reponse.channel.send("https://media.giphy.com/media/syEfLvksYQnmM/giphy.gif")
    await message.channel.send(f"Voici le cinquième **{jeu}**.")
  if "tyler" not in reponse.content.lower() and error == 5 : 
    await message.channel.send("Mauvaise réponse !")
    await reponse.add_reaction ("❌")
    await message.channel.send ("La réponse était tyler ou pour etre plus precis Tyler Durden.")
    await message.channel.send ("https://media.giphy.com/media/vOH0ku0LFGYzS/giphy.gif")
    await message.channel.send("https://fightclub.fandom.com/wiki/Tyler_Durden")
    await message.channel.send(f"Voici le cinquième **{jeu}**.")


async def perso5(message) : # Fonction permettant de lancer le cinquième quizz
  global score
  message.content = message.content.lower()
  await message.channel.send(f"C'est parti pour le cinquième et dernier **{jeu}**. Voici les trois premiers indices :")
  await message.channel.send("Je suis personnage est masculin.")  
  await message.channel.send("Je suis un personnage réel et historique.")
  await message.channel.send("Je suis issu d’un film culte sorti à la fin des années 90.") 
  await message.channel.send("Je fus un grand général de guerre.")
  await message.channel.send("Qui suis-je ?")
  async def check(m) : 
      return m.author == message.m.author and message.m.channel == m.channel
  reponse = await client.wait_for("message", check=check)
  error = 0 
  index = 0 
  i = 0
  while "hannibal" not in reponse.content.lower() and error < 5 :
    if "!guesswhoscore" in reponse.content :
      await message.channel.send (f"Votre score est égale à : {score}")
      await message.channel.send("Qui suis-je ?")
      reponse = await client.wait_for("message",check=check)
    else :
      error += 1
      i += 1
      await message.channel.send("Mauvaise réponse !")
      await reponse.add_reaction ("❌")
      await message.channel.send(f"Pour t'aider un peu voici l'indice numéro {i} :")
      await message.channel.send (indice_perso5[index])
      await message.channel.send("Qui suis-je ?")
      reponse = await client.wait_for("message",check=check)
      index += 1
      score -= 10
  if "hannibal" in reponse.content.lower() :
      await message.channel.send("Bien joué !")
      await reponse.add_reaction ("✅")
      await reponse.channel.send("https://media.giphy.com/media/nZIntykN1R86A/giphy.gif")
      await message.channel.send(f"Bravo tu as terminé {jeu}, Merci pour ta participation. Si tu veux soutenir les devs de ce jeu fantastique \n https://www.paypal.me/lucasrblt \n https://www.paypal.me/ineedmoneiyy \n https://paypal.me/OZCELIKmelih")
  if "hannibal" not in reponse.content.lower() and error == 5 :  
    await message.channel.send("Mauvaise réponse !")
    await reponse.add_reaction ("❌")
    await message.channel.send("La réponse était Hannibal Barca")
    await message.channel.send ("https://tenor.com/br690.gif")
    await message.channel.send ("https://fr.wikipedia.org/wiki/Hannibal_Barca")
    await message.channel.send(f"Bravo tu as terminé {jeu}, Merci pour ta participation. Ton score est égale à {score} .Si tu veux soutenir les devs de ce jeu fantastique \n https://www.paypal.me/lucasrblt \n https://www.paypal.me/ineedmoneiyy \n https://paypal.me/OZCELIKmelih")
              

@client.event #Indication dans la console
async def on_ready():
    print("Le bot est prêt !")


@client.event  
async def on_member_join(member) : #Envoi un message de bienvenue, permet de présenter le bot 
      general_channel = client.get_channel(1047439547606245500)
      jeu = ("!guesswho") 
      await general_channel.send(member.name + " a rejoint le vaisseau 🛸. Tout le monde lui souhaitent la bienvenue \n ")
      await general_channel.send(f"Si tu veux à un jeu développé avec les fesses 🍑👋, utilise la commande **{jeu}**")

@client.event #Fonction principale
async def on_message(message): 
  if message.author == client.user :
    return
  message.content = message.content.lower()
  jeu = ("GuessWho?")
  jeu_lancement = ("!guesswhostart")
  jeu_règles = ("!guesswhorules")
  jeu_score = ("!guesswhoscore")
  if message.content == ("!guesswho") : 
    await message.channel.send(f"Tu veux jouer à GuessWho? ! Pour connaitre les règles du jeu utilise la commande **{jeu_règles}**, lorsque tu es prêt lance le jeu avec la commande **{jeu_lancement}**")
  if message.content == ("!guesswhorules") :
    await message.channel.send(f"Le but de **{jeu}** est de deviner 5 personnages de pop culture (fictifs ou non) sélectionnés par le bot. A chaque personnage est attribué un niveau de difficulté entre très facile (10 points), facile (20 points), moyen (30 points), difficile (40 points) et très difficile (50 points). En début de partie, 3 affirmations te seront données, tu obtiendras également une banque de points égale à 150 points. A chaque erreur, ta banque de points diminuera et tu obtiendras un indice. Le **{jeu}** s'arrête lorsque tu as deviné le personnage ou après 6 tentatives. A la fin de la partie tu obtiendras un score final sur /150. Tu peux consulter votre solde de points à tout moment au cours de la partie avec la commande **{jeu_score}**. Enfin avant de commencer, branchez ton casque 🎧 et rejoins le salon vocal du serveur pour vivre l’expérience auditive 🎶🎶 de  **{jeu}**")
  if message.content.startswith("!guesswhostart") :
    await play2("https://www.youtube.com/watch?v=LYN6DRDQcjI&t=2s",message.author.voice.channel,client)
    await perso1(message)
    await perso2(message)
    await perso3(message) 
    await perso4(message)
    await perso5(message)




