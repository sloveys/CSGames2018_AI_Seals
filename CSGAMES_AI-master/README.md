# Compétition AI

## Contexte

Votre navette spatiale s'est écrasé sur une planète inconnue. Afin de pouvoir quitter la planète, vous devez récolter des matériaux dans les débris alentours. Malheureusement, vous n'êtes pas les seuls à vous être écrasé. Dépêchez-vous de créer un robot qui ira récolter tout ce que vous pouvez avant qu'il n'en reste plus et que vous soyez pris sur cette planête pour toujours.

### But

Vous devez récolter plus de matériaux que les autres joueurs. Le joueur ayant le plus de points après 1000 tours gagne la partie. Pour faire des points, vous devez récolter les matériaux dans les emplacements sur la carte.
Les points sont attribués uniquement lorsque les matériaux ont été entreposés dans la base.

Si un personnage meurt, il perd tous les matériaux qu'il possédait et va _respawner_ dans sa base après 10 tours.
Si un joueur tue un autre joueur, il vole tous les matériaux de sa victime.

## Déroulement du jeu

À chaque tour, votre robot reçoit les informations suivantes:
1. La carte permettant de visualiser la position des dépôts de matériaux
2. L'information concernant tous les robots, incluant le vôtre.

En utilisant ces informations, vous devez générer une commande indiquant ce que votre robot fera ce tour-ci.

### Carte

La carte que vous recevez ressemble à ceci: 

1111111111122211111111111</br>
1000000000022200000000C01</br>
1000000000002000000000001</br>
1000200011000001100002001</br>
100020J01100J00110J002001</br>
1000200011000001100002001</br>
1C00S00000002000000000001</br>
1000S00000022200000000001</br>
1111111111122211111111111</br>

0 - Sol</br>
1 - Arbre</br>
2 - Eau</br>
J - Dépôts de matériaux</br>
S - Zone dangereuse - le joueur prend entre 5 et 15 de dégâts s'il la traverse.</br>

Les robots ne peuvent pas passer par-dessus les éléments suivants:</br>
1 - Arbre</br>
2 - Eau</br>
Les autres robots</br>
Les bases ennemis</br>

### Informations sur les robots

En plus de la carte, vous recevez l'information suivante sur les robots:

base: L'emplacement de sa base (ligne, colonne)</br>
carrying: Le nombre de matériaux qu'il transporte</br>
health: La vie restante</br>
id: Un identifiant unique</br>
location: La position courante (ligne, colonne)</br>
points: Le nombre de points</br>
spawn: Indique combien de tour il reste avant que le robot _respawn_ (0 = vivant, 1-10 = nombre de tour restant)</br>
status: Le status courant du robot ('alive', 'dead', 'disconnected')</br>

### Dépôts de matériaux

À chaque fois qu'un joueur tente de récolter des matériaux, il a une chance d'en récolter un certain nombre selon une
loi normale propre à chaque emplacement. Cette loi normale a une moyenne pouvant aller de 5 jusqu'à 20 et un écart-type
pouvant aller de 1 jusqu'à 10.

### Base

La base est une zone sécuritaire pour les joueurs. Un joueur peut se soigner à l'intérieur de sa base et il ne peut
pas se faire attaquer par les autres joueurs. Un joueur peut seulement entrer dans sa propre base.

### Précision supplémentaire

Seulement un joueur peut récolter des matériaux d'un emplacement à la fois.</br>
Il n'y a pas de limite à la quantité de matériaux qu'un joueur peut transporter.</br>
Un pathfinder est fourni afin d'accélérer le développement. Par contre, il n'évite pas les zones dangereuses.

### Liste des commandes

1. Attack: Fait une attaque sur une case dans une direction spécifié ('N', 'S', 'E', 'W'). Si un joueur est touché,
celui-ci prend 10 de dégâts. S'il meurt, tout ce qu'il transporte est transféré à l'attaquant.</br>
2. Collect: Peut seulement être utilisé dans les dépôts de matériaux. Permet de récolter des matériaux</br>
3. Idle: Ne rien faire</br>
4. Move: Se déplacer dans la direction spécifiée ('N', 'S', 'E', 'W').</br>
5. Rest: Peut seulement être utilisé dans la base. Permet de récupérer 10 points de vie.</br>
6. Store: Peut seulement être utilisé dans la base. Convertir les matériaux transportés en points.

## Setup

```bash
# Créer un environnement virtuel
python3 -m venv env
source env/bin/activate

# Installer les dépendances
pip install --upgrade pip
pip install -r requirements.txt
```

## Lancer le jeu

Utiliser la commande suivante:

```bash
python3 main.py -m map1 -p BOT1 BOT2
```

Arguments:</br>
-p : Liste des noms des bots en python. Les bots doivent se trouver dans le module src.bot.</br>
-j : Indique que certains bots sont en java (voir section Java).</br>
-m : Nom de la map. Les maps doivent se trouver dans le dossier `maps`.

Vous pouvez ensuite démarrer une ronde en allant à:

http://localhost:5001

## Java

Ajouter [py4j](https://www.py4j.org/install.html#install-instructions) dans les dépendances de votre projet.

Dans le dossier `java`,

1. Modifier le fichier `JavaBotEntryPoint` pour y ajouter votre bot.
2. Démarrer `JavaBotEntryPoint`
3. Lancer le main en python avec l'option `-j`.

## Règles supplémentaires

Vous ne pouvez pas installer de dépendances. Vous avez uniquement le droit d'utiliser ce qui est fourni.

## Remise

Envoyez un seul fichier zip contenant votre bot et tout autre fichier nécessaire à: <br/>
mathieu.carpentier.3@ulaval.ca

Assurez-vous de remettre votre code avant Samedi 11h30 AM.</br>
Assurez-vous que votre courriel contient le nom de votre équipe.

# AI Competition

## Context

Your spaceship has crashed into an unknown planet. To escape, you need to collect materials from the nearby debris. However, you were not the only ones to crash here. You must quickly create a bot that will be able to collect as many materials as possible, before there are is nothing left and you are stuck on this planet forever.

### Goal

Your goal is to collect more materials than the other players. The player with the most points after a 1000 turns wins the game. To gain points, you need to collect materials on the map in the material deposits and store them in your base. Points are only given when the materials are stored.

If a bot dies, it loses all the materials it was carrying and respawns after 10 turns.
If a bot kills another bot, it steals all of the other bot's materials.

## Gameplay

Each turn, your bot will receive the following information:
1. The map
2. Information about all the bots, including your own bot.

Using this information, you need to generate commands to control your bot.

### Map

The map you receive will look like this:

1111111111122211111111111</br>
1000000000022200000000C01</br>
1000000000002000000000001</br>
1000200011000001100002001</br>
100020J01100J00110J002001</br>
1000200011000001100002001</br>
1C00S00000002000000000001</br>
1000S00000022200000000001</br>
1111111111122211111111111</br>

0 - Ground</br>
1 - Tree</br>
2 - Water</br>
J - Material deposit</br>
S - Dangerous zone. Your bot will take between 5 and 15 damage if it crosses one.</br>

The bots cannot traverse the following elements:</br>
1 - Tree</br>
2 - Water</br>
The other bots</br>
An enemy base</br>

### Bot information

In addition to the map, you will receive the following information on each bot.

base: The base location of that bot (line, column)</br>
carrying: How many materials the bot is carrying</br>
health: Health left</br>
id: Unique id</br>
location: The bot location (line, column)</br>
points: Number of points</br>
spawn: How many turns before the bot respawns (0 = alive, 1-10 = turns left)</br>
status: Current bot status ('alive', 'dead', 'disconnected')</br>

### Material deposits

Each time a player attempts to collect materials, the amount a player gets depends on the Gaussian distribution of the deposit. Each deposit has a distribution with a mean ranging from 5 to 20 and a standard deviation ranging from 1 to 10.

### Base

The base of a player is a secure zone for their bot. A bot can heal inside the base and it cannot be attacked by the other bots.

### Additional information

Only one player at a time can collect materials from a deposit.</br>
There is no limit to the amount of materials a bot can carry.</br>
To accelerate the development, a pathfinder is provided. However, this pathfinder will not avoid dangerous zones.

### Command list

1. Attack: Attack in a specific direction ('N', 'S', 'E' 'W'). If a bot is hit, it takes 10 damage. If it dies, the attacker gets everything the bot was carrying.</br>
2. Collect: Can only be used on a material deposit. Collect materials.</br>
3. Idle: Do nothing</br>
4. Move: Move in a specific direciton ('N', 'S', 'E', 'W').</br>
5. Rest: Can only be used inside the base. Heals 10 health.</br>
6. Store: Can only be used in the base. Converts the materials carried into points.

## Setup

```bash
# Create a virtual environment
python3 -m venv env
source env/bin/activate

# Install the dependencies
pip install --upgrade pip
pip install -r requirements.txt
```

## Launch the game

Use the following command:

```bash
python3 main.py -m map1 -p BOT1 BOT2
```

Arguments:</br>
-p : Python bots list. The bots need to be in the `src.bot module`.</br>
-j : Use bots in Java (view Section Java).</br>
-m : Map name. The map needs to be in the folder `maps`.

## Java

Add [py4j](https://www.py4j.org/install.html#install-instructions) to your project dependencies.

In the `java` folder,

1. Add your bot in the `JavaBotEntryPoint` file.
2. Run `JavaBotEntryPoint`
3. Run the python main with `-j`.

## Other rules

You cannot install dependencies. You can only use the ones given in the repository.

## Submission

Submit a single zip file containing your bot and any other necessary file at </br>
mathieu.carpentier.3@ulaval.ca

Make sure to submit before Sat. 11h30 AM.</br>
Make sure to include your team name in the email.
