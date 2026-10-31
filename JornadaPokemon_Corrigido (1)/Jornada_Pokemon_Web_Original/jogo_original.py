import time
import random

# =========================================
# JOGADOR E ESTRUTURAS DE DADOS GLOBAIS
# =========================================

jogador = {
    "nome": "",
    "pokedolares": 3000,
    "inventario": ["pokebola"],
    "vitorias": 0,
    "compras": {},
    "equipe": [],
    "pokemon_guardados": [],
    "ginasios": [],
    "pokedex_capturados": [],
    "historia_concluida": False,
    "treinadores_vencidos": 0,
    "total_capturados": 0
}

cidades = {
    "palet": {
        "casa": ["local seguro"],
        "casa do rival": ["liberar mapa"],
        "laboratorio do prof aok": ["escolha inicial"],
        "rotas": ["rota 1"]
    },
    "viridian": {
        "centro pokemon": ["local seguro"],
        "loja": ["loja"],
        "rotas": ["rota 1", "rota 2", "rota 32", "floresta de viridian"],
        "ginasio": ["blue"]
    },
    "pewter": {
        "centro pokemon": ["local seguro"],
        "loja": ["loja"],
        "rotas": ["rota 3", "rota 4", "caverna de pewter"],
        "ginasio": ["brock"]
    },
    "cerulian": {
        "centro pokemon": ["local seguro"],
        "loja": ["loja"],
        "rotas": ["rota 5", "rota 6", "casa do bill"],
        "ginasio": ["misty"]
    },
    "vermilion": {
        "centro pokemon": ["local seguro"],
        "loja": ["loja"],
        "rotas": ["rota 6", "rota 7", "diglet cave", "ss anne", "usina eletrica", "caverna de gelo", "montanha anber", "ilha antiga", "palacio do ceu", "caverna ancestral"],
        "ginasio": ["surge"]
    },
    "saffron": {
        "centro pokemon": ["local seguro"],
        "loja": ["loja"],
        "rotas": ["rota 8", "silph co"]
    },
    "lavender": {
        "centro pokemon": ["local seguro"],
        "loja": ["loja"],
        "rotas": ["rota 8", "rota maritima 1", "cemiterio pokemon"]
    },
    "celadon": {
        "centro pokemon": ["local seguro"],
        "shopping": ["loja"],
        "rotas": ["rota 9", "rota 10", "covil dos rockets"],
        "ginasio": ["erika"]
    },
    "fuxia": {
        "centro pokemon": ["local seguro"],
        "loja": ["loja"],
        "rotas": ["rota 11", "rota 12", "rota maritima 2", "saffari zone"],
        "ginasio": ["koga"]
    },
    "seafrom": {
        "centro pokemon": ["local seguro"],
        "loja": ["loja"],
        "rotas": ["rota 10", "rota 7", "rota 6", "sylfiscol"],
        "ginasio": ["sabrina"]
    },
    "sinabar": {
        "centro pokemon": ["local seguro"],
        "loja": ["loja"],
        "rotas": ["rota maritima 3", "rota maritima 4", "mansao pokemon"],
        "ginasio": ["blaine"]
    },
    "ilha dos lendarios": {
        "centro pokemon": ["local seguro"],
        "rotas": [
            "bosque de celebi", "lago de suicune", "vulcao de entei",
            "templo de raikou", "pico de articuno", "usina isolada de zapdos",
            "ninho de moltres", "caverna de mewtwo", "santuário de ho-oh",
            "abismo de lugia", "jardim mistico de mew"
        ]
    },
    "rota da vitoria": {
        "centro pokemon": ["local seguro"],
        "loja": ["loja"],
        "rotas": ["victory road"],
        "elites": ["lorelei", "bruno", "agatha", "lance", "red"]
    }
}

ginasios = [
    {"lider": "brock", "pokemons": ["geodude", "onix"]},
    {"lider": "misty", "pokemons": ["staryu", "starmie"]},
    {"lider": "surge", "pokemons": ["voltorb", "pikachu", "raichu"]},
    {"lider": "erika", "pokemons": ["victreebel", "tangela", "vileplume"]},
    {"lider": "koga", "pokemons": ["koffing", "muk", "koffing", "weezing"]},
    {"lider": "sabrina", "pokemons": ["hipno", "kadabra", "mr mime", "alakazam"]},
    {"lider": "blaine", "pokemons": ["growlithe", "ponyta", "rapidash", "arcanine"]},
    {"lider": "blue", "pokemons": ["rhydon", "arcanine", "vileplume", "alakazam", "pigeot", "gyarados"]}
]

POKEMON_ROTAS = {
    "rota 1": ["pidgey", "rattata", "sentret", "hoothoot"],
    "floresta de viridian": ["caterpie", "metapod", "butterfree", "weedle", "kakuna", "beedrill", "pikachu", "ledyba", "spinarak", "paras", "venonat"],
    "rota 2": ["pidgey", "pidgeotto", "rattata", "raticate", "spearow", "fearow", "sentret", "furret"],
    "rota 3": ["spearow", "fearow", "raticate", "primeape", "mankey", "nidoranf", "nidoranm", "ledian"],
    "rota 4": ["sandslash", "sandshrew", "onix", "zubat", "golbat", "ekans", "arbok", "clefairy", "clefable"],
    "caverna de pewter": ["zubat", "golbat", "geodude", "graveler", "onix", "rhyhorn", "rhydon", "clefairy", "paras", "parasect", "machop", "machoke"],
    "rota 5": ["pidgey", "pidgeotto", "rattata", "raticate", "meowth", "persian", "jigglypuff", "wigglytuff", "abra", "kadabra", "bellsprout", "weepinbell"],
    "rota 6": ["pidgey", "pidgeotto", "fearow", "raticate", "psyduck", "golduck", "meowth", "persian", "magnemite", "magneton", "oddish", "gloom", "pikachu", "raichu"],
    "diglett cave": ["diglett", "dugtrio", "geodude", "graveler", "zubat", "golbat"],
    "ss anne": ["tentacool", "tentacruel", "magikarp", "goldeen", "seaking", "krabby", "kingler", "shellder", "horsea", "seadra", "slowpoke", "slowbro", "staryu", "starmie"],
    "rota 7": ["persian", "meowth", "vileplume", "bellsprout", "weepinbell", "victreebel", "rapidash", "ponyta", "eevee", "espeon", "umbreon", "houndour", "houndoom"],
    "rota 8": ["hypno", "drowzee", "gengar", "gastly", "haunter", "dodrio", "doduo", "kadabra", "abra", "murkrow", "misdreavus", "yanma"]
}

POKEMON_ROTAS.update({
    "usina eletrica": ["magnemite", "magneton", "voltorb", "electrode", "electabuzz", "pikachu", "raichu", "mareep", "flaaffy", "ampharos", "elekid"],
    "caverna de gelo": ["swinub", "piloswine", "sneasel", "delibird", "smoochum", "jynx", "lapras", "seel", "dewgong"],
    "montanha anber": ["growlithe", "arcanine", "ponyta", "rapidash", "magmar", "slugma", "magcargo", "houndour", "houndoom", "charmeleon"],
    "ilha antiga": ["togepi", "togetic", "kabuto", "kabutops", "omanyte", "omastar", "aerodactyl"],
    "palacio do ceu": ["aerodactyl", "dragonite", "dragonair", "skarmory", "xatu", "fearow", "pidgeot"],
    "caverna ancestral": ["onix", "steelix", "rhydon", "rhyhorn", "graveler", "golem", "larvitar", "pupitar", "tyranitar", "unown"],
})

# =========================================
# TABELA DE TIPOS
# =========================================

TABELA_TIPOS = {
    "Normal": {"Pedra": 0.5, "Fantasma": 0.0, "Aço": 0.5},
    "Fogo": {"Grama": 2.0, "Gelo": 2.0, "Inseto": 2.0, "Aço": 2.0, "Fogo": 0.5, "Água": 0.5, "Pedra": 0.5, "Dragão": 0.5},
    "Água": {"Fogo": 2.0, "Terra": 2.0, "Pedra": 2.0, "Água": 0.5, "Grama": 0.5, "Dragão": 0.5},
    "Grama": {"Água": 2.0, "Terra": 2.0, "Pedra": 2.0, "Fogo": 0.5, "Grama": 0.5, "Venenoso": 0.5, "Voador": 0.5, "Inseto": 0.5, "Dragão": 0.5, "Aço": 0.5},
    "Elétrico": {"Água": 2.0, "Voador": 2.0, "Elétrico": 0.5, "Grama": 0.5, "Dragão": 0.5, "Terra": 0.0},
    "Gelo": {"Grama": 2.0, "Terra": 2.0, "Voador": 2.0, "Dragão": 2.0, "Fogo": 0.5, "Água": 0.5, "Gelo": 0.5, "Aço": 0.5},
    "Lutador": {"Normal": 2.0, "Gelo": 2.0, "Pedra": 2.0, "Sombrio": 2.0, "Aço": 2.0, "Venenoso": 0.5, "Voador": 0.5, "Psíquico": 0.5, "Inseto": 0.5, "Fada": 0.5, "Fantasma": 0.0},
    "Venenoso": {"Grama": 2.0, "Fada": 2.0, "Venenoso": 0.5, "Terra": 0.5, "Pedra": 0.5, "Fantasma": 0.5, "Aço": 0.0},
    "Terra": {"Fogo": 2.0, "Elétrico": 0.5, "Venenoso": 2.0, "Pedra": 2.0, "Aço": 2.0, "Grama": 0.5, "Inseto": 0.5, "Voador": 0.0},
    "Voador": {"Grama": 2.0, "Lutador": 2.0, "Inseto": 2.0, "Elétrico": 0.5, "Pedra": 0.5, "Aço": 0.5},
    "Psíquico": {"Lutador": 2.0, "Venenoso": 2.0, "Psíquico": 0.5, "Aço": 0.5, "Sombrio": 0.0},
    "Inseto": {"Grama": 2.0, "Psíquico": 2.0, "Sombrio": 2.0, "Fogo": 0.5, "Lutador": 0.5, "Venenoso": 0.5, "Voador": 0.5, "Fantasma": 0.5, "Aço": 0.5, "Fada": 0.5},
    "Pedra": {"Fogo": 2.0, "Gelo": 2.0, "Voador": 2.0, "Inseto": 2.0, "Lutador": 0.5, "Terra": 0.5, "Aço": 0.5},
    "Fantasma": {"Psíquico": 2.0, "Fantasma": 2.0, "Sombrio": 0.5, "Normal": 0.0},
    "Dragão": {"Dragão": 2.0, "Aço": 0.5, "Fada": 0.0},
    "Aço": {"Gelo": 2.0, "Pedra": 2.0, "Fada": 2.0, "Fogo": 0.5, "Água": 0.5, "Elétrico": 0.5, "Aço": 0.5},
    "Sombrio": {"Psíquico": 2.0, "Fantasma": 2.0, "Lutador": 0.5, "Sombrio": 0.5, "Fada": 0.5},
    "Fada": {"Lutador": 2.0, "Dragão": 2.0, "Sombrio": 2.0, "Fogo": 0.5, "Venenoso": 0.5, "Aço": 0.5}
}


def criar_pokemon(nome, tipo, hp, ataque, defesa, ataque_especial, defesa_especial, velocidade, nivel=5, evolui_nivel=None, evolui_para=None, golpes=None):
    return {
        "nome": nome,
        "tipo": tipo,
        "hp": hp,
        "ataque": ataque,
        "defesa": defesa,
        "ataque_especial": ataque_especial,
        "defesa_especial": defesa_especial,
        "velocidade": velocidade,
        "nivel": nivel,
        "evolui_nivel": evolui_nivel,
        "evolui_para": evolui_para,
        "golpes": golpes if golpes else []
    }


# =========================================================
# POKÉDEX COMPLETA — GEN 1 + GEN 2 (251 POKÉMON)
# =========================================================

pokemons = {
    # --- GERAÇÃO 1 (#001 - #151) ---
    "bulbasaur": criar_pokemon("Bulbasaur", "Grama/Venenoso", 45, 49, 49, 65, 65, 45, nivel=5, evolui_nivel=16, evolui_para="Ivysaur"),
    "ivysaur": criar_pokemon("Ivysaur", "Grama/Venenoso", 60, 62, 63, 80, 80, 60, nivel=16, evolui_nivel=32, evolui_para="Venusaur"),
    "venusaur": criar_pokemon("Venusaur", "Grama/Venenoso", 80, 82, 83, 100, 100, 80, nivel=32),

    "charmander": criar_pokemon("Charmander", "Fogo", 39, 52, 43, 60, 50, 65, nivel=5, evolui_nivel=16, evolui_para="Charmeleon"),
    "charmeleon": criar_pokemon("Charmeleon", "Fogo", 58, 64, 58, 80, 65, 80, nivel=16, evolui_nivel=36, evolui_para="Charizard"),
    "charizard": criar_pokemon("Charizard", "Fogo/Voador", 78, 84, 78, 109, 85, 100, nivel=36),

    "squirtle": criar_pokemon("Squirtle", "Água", 44, 48, 65, 50, 64, 43, nivel=5, evolui_nivel=16, evolui_para="Wartortle"),
    "wartortle": criar_pokemon("Wartortle", "Água", 59, 63, 80, 65, 80, 58, nivel=16, evolui_nivel=36, evolui_para="Blastoise"),
    "blastoise": criar_pokemon("Blastoise", "Água", 79, 83, 100, 85, 105, 78, nivel=36),

    "caterpie": criar_pokemon("Caterpie", "Inseto", 45, 30, 35, 20, 20, 45, nivel=4, evolui_nivel=7, evolui_para="Metapod"),
    "metapod": criar_pokemon("Metapod", "Inseto", 50, 20, 55, 25, 25, 30, nivel=7, evolui_nivel=10, evolui_para="Butterfree"),
    "butterfree": criar_pokemon("Butterfree", "Inseto/Voador", 60, 45, 50, 90, 80, 70, nivel=10),

    "weedle": criar_pokemon("Weedle", "Inseto/Venenoso", 40, 35, 30, 20, 20, 50, nivel=4, evolui_nivel=7, evolui_para="Kakuna"),
    "kakuna": criar_pokemon("Kakuna", "Inseto/Venenoso", 45, 25, 50, 25, 25, 35, nivel=7, evolui_nivel=10, evolui_para="Beedrill"),
    "beedrill": criar_pokemon("Beedrill", "Inseto/Venenoso", 65, 90, 40, 45, 80, 75, nivel=10),

    "pidgey": criar_pokemon("Pidgey", "Normal/Voador", 40, 45, 40, 35, 35, 56, nivel=2, evolui_nivel=18, evolui_para="Pidgeotto"),
    "pidgeotto": criar_pokemon("Pidgeotto", "Normal/Voador", 63, 60, 55, 50, 50, 71, nivel=18, evolui_nivel=36, evolui_para="Pidgeot"),
    "pidgeot": criar_pokemon("Pidgeot", "Normal/Voador", 83, 80, 75, 70, 70, 101, nivel=36),

    "rattata": criar_pokemon("Rattata", "Normal", 30, 56, 35, 25, 35, 72, nivel=3, evolui_nivel=20, evolui_para="Raticate"),
    "raticate": criar_pokemon("Raticate", "Normal", 55, 81, 60, 50, 70, 97, nivel=20),

    "spearow": criar_pokemon("Spearow", "Normal/Voador", 40, 60, 30, 31, 31, 70, nivel=3, evolui_nivel=20, evolui_para="Fearow"),
    "fearow": criar_pokemon("Fearow", "Normal/Voador", 65, 90, 65, 61, 61, 100, nivel=20),

    "ekans": criar_pokemon("Ekans", "Venenoso", 35, 60, 44, 40, 54, 55, nivel=3, evolui_nivel=22, evolui_para="Arbok"),
    "arbok": criar_pokemon("Arbok", "Venenoso", 60, 85, 69, 65, 79, 80, nivel=22),

    "pikachu": criar_pokemon("Pikachu", "Elétrico", 35, 55, 40, 50, 50, 90, nivel=5, evolui_para="Raichu"),
    "raichu": criar_pokemon("Raichu", "Elétrico", 60, 90, 55, 90, 80, 110),

    "sandshrew": criar_pokemon("Sandshrew", "Terra", 50, 75, 85, 20, 30, 40, nivel=3, evolui_nivel=22, evolui_para="Sandslash"),
    "sandslash": criar_pokemon("Sandslash", "Terra", 75, 100, 110, 45, 55, 65, nivel=22),

    "nidoranf": criar_pokemon("Nidoran♀", "Venenoso", 55, 47, 52, 40, 40, 41, nivel=3, evolui_nivel=16, evolui_para="Nidorina"),
    "nidorina": criar_pokemon("Nidorina", "Venenoso", 70, 62, 67, 55, 55, 56, nivel=16, evolui_para="Nidoqueen"),
    "nidoqueen": criar_pokemon("Nidoqueen", "Venenoso/Terra", 90, 92, 87, 75, 85, 76),

    "nidoranm": criar_pokemon("Nidoran♂", "Venenoso", 46, 57, 40, 40, 40, 50, nivel=3, evolui_nivel=16, evolui_para="Nidorino"),
    "nidorino": criar_pokemon("Nidorino", "Venenoso", 61, 72, 57, 55, 55, 65, nivel=16, evolui_para="Nidoking"),
    "nidoking": criar_pokemon("Nidoking", "Venenoso/Terra", 81, 102, 77, 85, 75, 85),

    "clefairy": criar_pokemon("Clefairy", "Fada", 70, 45, 48, 60, 65, 35, nivel=5, evolui_para="Clefable"),
    "clefable": criar_pokemon("Clefable", "Fada", 95, 70, 73, 95, 90, 60),

    "vulpix": criar_pokemon("Vulpix", "Fogo", 38, 41, 40, 50, 65, 65, nivel=5, evolui_para="Ninetales"),
    "ninetales": criar_pokemon("Ninetales", "Fogo", 73, 76, 75, 81, 100, 100),

    "jigglypuff": criar_pokemon("Jigglypuff", "Normal/Fada", 115, 45, 20, 45, 25, 20, nivel=5, evolui_para="Wigglytuff"),
    "wigglytuff": criar_pokemon("Wigglytuff", "Normal/Fada", 140, 70, 45, 85, 50, 45),

    "zubat": criar_pokemon("Zubat", "Venenoso/Voador", 40, 45, 35, 30, 40, 55, nivel=3, evolui_nivel=22, evolui_para="Golbat"),
    "golbat": criar_pokemon("Golbat", "Venenoso/Voador", 75, 80, 70, 65, 75, 90, nivel=22, evolui_para="Crobat"),

    "oddish": criar_pokemon("Oddish", "Grama/Venenoso", 45, 50, 55, 75, 65, 30, nivel=5, evolui_nivel=21, evolui_para="Gloom"),
    "gloom": criar_pokemon("Gloom", "Grama/Venenoso", 60, 65, 70, 85, 75, 40, nivel=21, evolui_para="Vileplume"),
    "vileplume": criar_pokemon("Vileplume", "Grama/Venenoso", 75, 80, 85, 110, 90, 50),

    "paras": criar_pokemon("Paras", "Inseto/Grama", 35, 70, 55, 45, 55, 25, nivel=5, evolui_nivel=24, evolui_para="Parasect"),
    "parasect": criar_pokemon("Parasect", "Inseto/Grama", 60, 95, 80, 60, 80, 30),

    "venonat": criar_pokemon("Venonat", "Inseto/Venenoso", 60, 55, 50, 40, 55, 45, nivel=5, evolui_nivel=31, evolui_para="Venomoth"),
    "venomoth": criar_pokemon("Venomoth", "Inseto/Venenoso", 70, 65, 60, 90, 75, 90),

    "diglett": criar_pokemon("Diglett", "Terra", 10, 55, 25, 35, 45, 95, nivel=5, evolui_nivel=26, evolui_para="Dugtrio"),
    "dugtrio": criar_pokemon("Dugtrio", "Terra", 35, 80, 50, 50, 70, 120),

    "meowth": criar_pokemon("Meowth", "Normal", 40, 45, 35, 40, 40, 90, nivel=5, evolui_nivel=28, evolui_para="Persian"),
    "persian": criar_pokemon("Persian", "Normal", 65, 70, 60, 65, 65, 115),

    "psyduck": criar_pokemon("Psyduck", "Água", 50, 52, 48, 65, 50, 55, nivel=5, evolui_nivel=33, evolui_para="Golduck"),
    "golduck": criar_pokemon("Golduck", "Água", 80, 82, 78, 95, 80, 85),

    "mankey": criar_pokemon("Mankey", "Lutador", 40, 80, 35, 35, 45, 70, nivel=5, evolui_nivel=28, evolui_para="Primeape"),
    "primeape": criar_pokemon("Primeape", "Lutador", 65, 105, 60, 60, 70, 95),

    "growlithe": criar_pokemon("Growlithe", "Fogo", 55, 70, 45, 70, 50, 60, nivel=5, evolui_para="Arcanine"),
    "arcanine": criar_pokemon("Arcanine", "Fogo", 90, 110, 80, 100, 80, 95),

    "poliwag": criar_pokemon("Poliwag", "Água", 40, 50, 40, 40, 40, 90, nivel=5, evolui_nivel=25, evolui_para="Poliwhirl"),
    "poliwhirl": criar_pokemon("Poliwhirl", "Água", 65, 65, 65, 50, 50, 90, nivel=25, evolui_para="Poliwrath"),
    "poliwrath": criar_pokemon("Poliwrath", "Água/Lutador", 90, 95, 95, 70, 90, 70),

    "abra": criar_pokemon("Abra", "Psíquico", 25, 20, 15, 105, 55, 90, nivel=5, evolui_nivel=16, evolui_para="Kadabra"),
    "kadabra": criar_pokemon("Kadabra", "Psíquico", 40, 35, 30, 120, 70, 105, nivel=16, evolui_para="Alakazam"),
    "alakazam": criar_pokemon("Alakazam", "Psíquico", 55, 50, 45, 135, 95, 120),

    "machop": criar_pokemon("Machop", "Lutador", 70, 80, 50, 35, 35, 35, nivel=5, evolui_nivel=28, evolui_para="Machoke"),
    "machoke": criar_pokemon("Machoke", "Lutador", 80, 100, 70, 50, 60, 45, nivel=28, evolui_para="Machamp"),
    "machamp": criar_pokemon("Machamp", "Lutador", 90, 130, 80, 65, 85, 55),

    "bellsprout": criar_pokemon("Bellsprout", "Grama/Venenoso", 50, 75, 35, 70, 30, 40, nivel=5, evolui_nivel=21, evolui_para="Weepinbell"),
    "weepinbell": criar_pokemon("Weepinbell", "Grama/Venenoso", 65, 90, 50, 85, 45, 55, nivel=21, evolui_para="Victreebel"),
    "victreebel": criar_pokemon("Victreebel", "Grama/Venenoso", 80, 105, 65, 100, 70, 70),

    "tentacool": criar_pokemon("Tentacool", "Água/Venenoso", 40, 40, 35, 50, 100, 70, nivel=5, evolui_nivel=30, evolui_para="Tentacruel"),
    "tentacruel": criar_pokemon("Tentacruel", "Água/Venenoso", 80, 70, 65, 80, 120, 100),

    "geodude": criar_pokemon("Geodude", "Pedra/Terra", 40, 80, 100, 30, 30, 20, nivel=5, evolui_nivel=25, evolui_para="Graveler"),
    "graveler": criar_pokemon("Graveler", "Pedra/Terra", 55, 95, 115, 45, 45, 35, nivel=25, evolui_para="Golem"),
    "golem": criar_pokemon("Golem", "Pedra/Terra", 80, 120, 130, 55, 65, 45),

    "ponyta": criar_pokemon("Ponyta", "Fogo", 50, 85, 55, 65, 65, 90, nivel=5, evolui_nivel=40, evolui_para="Rapidash"),
    "rapidash": criar_pokemon("Rapidash", "Fogo", 65, 100, 70, 80, 80, 105),

    "slowpoke": criar_pokemon("Slowpoke", "Água/Psíquico", 90, 65, 65, 40, 40, 15, nivel=5, evolui_nivel=37, evolui_para="Slowbro"),
    "slowbro": criar_pokemon("Slowbro", "Água/Psíquico", 95, 75, 110, 100, 80, 30),

    "magnemite": criar_pokemon("Magnemite", "Elétrico/Aço", 25, 35, 70, 95, 55, 45, nivel=5, evolui_nivel=30, evolui_para="Magneton"),
    "magneton": criar_pokemon("Magneton", "Elétrico/Aço", 50, 60, 95, 120, 70, 70),

    "farfetchd": criar_pokemon("Farfetch'd", "Normal/Voador", 52, 90, 55, 58, 62, 60),

    "doduo": criar_pokemon("Doduo", "Normal/Voador", 35, 85, 45, 35, 35, 75, nivel=5, evolui_nivel=31, evolui_para="Dodrio"),
    "dodrio": criar_pokemon("Dodrio", "Normal/Voador", 60, 110, 70, 60, 60, 110),

    "seel": criar_pokemon("Seel", "Água", 65, 45, 55, 45, 70, 45, nivel=5, evolui_nivel=34, evolui_para="Dewgong"),
    "dewgong": criar_pokemon("Dewgong", "Água/Gelo", 90, 70, 80, 70, 95, 70),

    "grimer": criar_pokemon("Grimer", "Venenoso", 80, 80, 50, 40, 50, 25, nivel=5, evolui_nivel=38, evolui_para="Muk"),
    "muk": criar_pokemon("Muk", "Venenoso", 105, 105, 75, 65, 100, 50),

    "shellder": criar_pokemon("Shellder", "Água", 30, 65, 100, 45, 25, 40, nivel=5, evolui_para="Cloyster"),
    "cloyster": criar_pokemon("Cloyster", "Água/Gelo", 50, 95, 180, 85, 45, 70),

    "gastly": criar_pokemon("Gastly", "Fantasma/Venenoso", 30, 35, 30, 100, 35, 80, nivel=5, evolui_nivel=25, evolui_para="Haunter"),
    "haunter": criar_pokemon("Haunter", "Fantasma/Venenoso", 45, 50, 45, 115, 55, 95, nivel=25, evolui_para="Gengar"),
    "gengar": criar_pokemon("Gengar", "Fantasma/Venenoso", 60, 65, 60, 130, 75, 110),

    "onix": criar_pokemon("Onix", "Pedra/Terra", 35, 45, 160, 30, 45, 70),

    "drowzee": criar_pokemon("Drowzee", "Psíquico", 60, 48, 45, 43, 90, 42, nivel=5, evolui_nivel=26, evolui_para="Hypno"),
    "hypno": criar_pokemon("Hypno", "Psíquico", 85, 73, 70, 73, 115, 67),

    "krabby": criar_pokemon("Krabby", "Água", 30, 105, 90, 25, 25, 50, nivel=5, evolui_nivel=28, evolui_para="Kingler"),
    "kingler": criar_pokemon("Kingler", "Água", 55, 130, 115, 50, 50, 75),

    "voltorb": criar_pokemon("Voltorb", "Elétrico", 40, 30, 50, 55, 55, 100, nivel=5, evolui_nivel=30, evolui_para="Electrode"),
    "electrode": criar_pokemon("Electrode", "Elétrico", 60, 50, 70, 80, 80, 150),

    "exeggcute": criar_pokemon("Exeggcute", "Grama/Psíquico", 60, 40, 80, 60, 45, 40, nivel=5, evolui_para="Exeggutor"),
    "exeggutor": criar_pokemon("Exeggutor", "Grama/Psíquico", 95, 95, 85, 125, 65, 55),

    "cubone": criar_pokemon("Cubone", "Terra", 50, 50, 95, 40, 50, 35, nivel=5, evolui_nivel=28, evolui_para="Marowak"),
    "marowak": criar_pokemon("Marowak", "Terra", 60, 80, 110, 50, 80, 45),

    "hitmonlee": criar_pokemon("Hitmonlee", "Lutador", 50, 120, 53, 35, 110, 87),
    "hitmonchan": criar_pokemon("Hitmonchan", "Lutador", 50, 105, 79, 35, 110, 76),

    "lickitung": criar_pokemon("Lickitung", "Normal", 90, 55, 75, 60, 75, 30),

    "koffing": criar_pokemon("Koffing", "Venenoso", 40, 65, 95, 60, 45, 35, nivel=5, evolui_nivel=35, evolui_para="Weezing"),
    "weezing": criar_pokemon("Weezing", "Venenoso", 65, 90, 120, 85, 70, 60),

    "rhyhorn": criar_pokemon("Rhyhorn", "Pedra/Terra", 80, 85, 95, 30, 30, 25, nivel=5, evolui_nivel=42, evolui_para="Rhydon"),
    "rhydon": criar_pokemon("Rhydon", "Pedra/Terra", 105, 130, 120, 45, 45, 40),

    "chansey": criar_pokemon("Chansey", "Normal", 250, 5, 5, 35, 105, 50),

    "tangela": criar_pokemon("Tangela", "Grama", 65, 55, 115, 100, 40, 60),

    "kangaskhan": criar_pokemon("Kangaskhan", "Normal", 105, 95, 80, 40, 80, 90),

    "horsea": criar_pokemon("Horsea", "Água", 30, 40, 70, 70, 25, 60, nivel=5, evolui_nivel=32, evolui_para="Seadra"),
    "seadra": criar_pokemon("Seadra", "Água", 55, 65, 95, 95, 45, 85),

    "goldeen": criar_pokemon("Goldeen", "Água", 45, 67, 60, 35, 50, 63, nivel=5, evolui_nivel=33, evolui_para="Seaking"),
    "seaking": criar_pokemon("Seaking", "Água", 80, 92, 65, 65, 80, 68),

    "staryu": criar_pokemon("Staryu", "Água", 30, 45, 55, 70, 55, 85, nivel=5, evolui_para="Starmie"),
    "starmie": criar_pokemon("Starmie", "Água/Psíquico", 60, 75, 85, 100, 85, 115),

    "mr_mime": criar_pokemon("Mr. Mime", "Psíquico/Fada", 40, 45, 65, 100, 120, 90),

    "scyther": criar_pokemon("Scyther", "Inseto/Voador", 70, 110, 80, 55, 80, 105),

    "jynx": criar_pokemon("Jynx", "Gelo/Psíquico", 65, 50, 35, 115, 95, 95),

    "electabuzz": criar_pokemon("Electabuzz", "Elétrico", 65, 83, 57, 95, 85, 105),

    "magmar": criar_pokemon("Magmar", "Fogo", 65, 95, 57, 100, 85, 93),

    "pinsir": criar_pokemon("Pinsir", "Inseto", 65, 125, 100, 55, 70, 85),

    "tauros": criar_pokemon("Tauros", "Normal", 75, 100, 95, 40, 70, 110),

    "magikarp": criar_pokemon("Magikarp", "Água", 20, 10, 55, 15, 20, 80, nivel=3, evolui_nivel=20, evolui_para="Gyarados"),
    "gyarados": criar_pokemon("Gyarados", "Água/Voador", 95, 125, 79, 60, 100, 81),

    "lapras": criar_pokemon("Lapras", "Água/Gelo", 130, 85, 80, 85, 95, 60),

    "ditto": criar_pokemon("Ditto", "Normal", 48, 48, 48, 48, 48, 48),

    "eevee": criar_pokemon("Eevee", "Normal", 55, 55, 50, 45, 65, 55, nivel=5),
    "vaporeon": criar_pokemon("Vaporeon", "Água", 130, 65, 60, 110, 95, 65),
    "jolteon": criar_pokemon("Jolteon", "Elétrico", 65, 65, 60, 110, 95, 130),
    "flareon": criar_pokemon("Flareon", "Fogo", 65, 130, 60, 95, 110, 65),

    "porygon": criar_pokemon("Porygon", "Normal", 65, 60, 70, 85, 75, 40),

    "omanyte": criar_pokemon("Omanyte", "Pedra/Água", 35, 40, 100, 90, 55, 35, nivel=5, evolui_nivel=40, evolui_para="Omastar"),
    "omastar": criar_pokemon("Omastar", "Pedra/Água", 70, 60, 125, 115, 70, 55),

    "kabuto": criar_pokemon("Kabuto", "Pedra/Água", 30, 80, 90, 55, 45, 55, nivel=5, evolui_nivel=40, evolui_para="Kabutops"),
    "kabutops": criar_pokemon("Kabutops", "Pedra/Água", 60, 115, 105, 65, 70, 80),

    "aerodactyl": criar_pokemon("Aerodactyl", "Pedra/Voador", 80, 105, 65, 60, 75, 130),

    "snorlax": criar_pokemon("Snorlax", "Normal", 160, 110, 65, 65, 110, 30),

    "articuno": criar_pokemon("Articuno", "Gelo/Voador", 90, 85, 100, 95, 125, 85),
    "zapdos": criar_pokemon("Zapdos", "Elétrico/Voador", 90, 90, 85, 125, 90, 100),
    "moltres": criar_pokemon("Moltres", "Fogo/Voador", 90, 100, 90, 125, 85, 90),

    "dratini": criar_pokemon("Dratini", "Dragão", 41, 64, 45, 50, 50, 50, nivel=5, evolui_nivel=30, evolui_para="Dragonair"),
    "dragonair": criar_pokemon("Dragonair", "Dragão", 61, 84, 65, 70, 70, 70, nivel=30, evolui_nivel=55, evolui_para="Dragonite"),
    "dragonite": criar_pokemon("Dragonite", "Dragão/Voador", 91, 134, 95, 100, 100, 80),

    "mewtwo": criar_pokemon("Mewtwo", "Psíquico", 106, 110, 90, 154, 90, 130),
    "mew": criar_pokemon("Mew", "Psíquico", 100, 100, 100, 100, 100, 100),

    # --- GERAÇÃO 2 (#152 - #251) ---
    "chikorita": criar_pokemon("Chikorita", "Grama", 45, 49, 65, 49, 65, 45, nivel=5, evolui_nivel=16, evolui_para="Bayleef"),
    "bayleef": criar_pokemon("Bayleef", "Grama", 60, 62, 80, 63, 80, 60, nivel=16, evolui_nivel=32, evolui_para="Meganium"),
    "meganium": criar_pokemon("Meganium", "Grama", 80, 82, 100, 83, 100, 80, nivel=32),

    "cyndaquil": criar_pokemon("Cyndaquil", "Fogo", 39, 52, 43, 60, 50, 65, nivel=5, evolui_nivel=14, evolui_para="Quilava"),
    "quilava": criar_pokemon("Quilava", "Fogo", 58, 64, 58, 80, 65, 80, nivel=14, evolui_nivel=36, evolui_para="Typhlosion"),
    "typhlosion": criar_pokemon("Typhlosion", "Fogo", 78, 84, 78, 109, 85, 100, nivel=36),

    "totodile": criar_pokemon("Totodile", "Água", 50, 65, 64, 44, 48, 43, nivel=5, evolui_nivel=18, evolui_para="Croconaw"),
    "croconaw": criar_pokemon("Croconaw", "Água", 65, 80, 80, 59, 63, 58, nivel=18, evolui_nivel=30, evolui_para="Feraligatr"),
    "feraligatr": criar_pokemon("Feraligatr", "Água", 85, 105, 100, 79, 83, 78, nivel=30),

    "sentret": criar_pokemon("Sentret", "Normal", 35, 46, 34, 35, 45, 20, nivel=3, evolui_nivel=15, evolui_para="Furret"),
    "furret": criar_pokemon("Furret", "Normal", 85, 76, 64, 45, 55, 90, nivel=15),

    "hoothoot": criar_pokemon("Hoothoot", "Normal/Voador", 60, 30, 30, 36, 56, 50, nivel=5, evolui_nivel=20, evolui_para="Noctowl"),
    "noctowl": criar_pokemon("Noctowl", "Normal/Voador", 100, 50, 50, 76, 96, 70, nivel=20),

    "ledyba": criar_pokemon("Ledyba", "Inseto/Voador", 40, 20, 30, 40, 80, 55, nivel=5, evolui_nivel=18, evolui_para="Ledian"),
    "ledian": criar_pokemon("Ledian", "Inseto/Voador", 55, 35, 50, 55, 110, 85, nivel=18),

    "spinarak": criar_pokemon("Spinarak", "Inseto/Venenoso", 40, 60, 40, 40, 40, 30, nivel=5, evolui_nivel=22, evolui_para="Ariados"),
    "ariados": criar_pokemon("Ariados", "Inseto/Venenoso", 70, 90, 70, 60, 60, 40, nivel=22),

    "crobat": criar_pokemon("Crobat", "Venenoso/Voador", 85, 90, 80, 70, 80, 130),

    "chinchou": criar_pokemon("Chinchou", "Água/Elétrico", 75, 38, 38, 56, 56, 67, nivel=5, evolui_nivel=27, evolui_para="Lanturn"),
    "lanturn": criar_pokemon("Lanturn", "Água/Elétrico", 125, 58, 58, 76, 76, 67, nivel=27),

    "pichu": criar_pokemon("Pichu", "Elétrico", 20, 40, 15, 35, 35, 60, nivel=2, evolui_para="Pikachu"),
    "cleffa": criar_pokemon("Cleffa", "Fada", 50, 25, 28, 45, 55, 15, nivel=2, evolui_para="Clefairy"),
    "igglybuff": criar_pokemon("Igglybuff", "Normal/Fada", 90, 30, 15, 40, 20, 15, nivel=2, evolui_para="Jigglypuff"),

    "togepi": criar_pokemon("Togepi", "Fada", 35, 20, 65, 40, 65, 20, nivel=5, evolui_para="Togetic"),
    "togetic": criar_pokemon("Togetic", "Fada/Voador", 55, 40, 85, 80, 105, 40),

    "natu": criar_pokemon("Natu", "Psíquico/Voador", 40, 50, 45, 70, 45, 70, nivel=5, evolui_nivel=25, evolui_para="Xatu"),
    "xatu": criar_pokemon("Xatu", "Psíquico/Voador", 65, 75, 70, 95, 70, 95, nivel=25),

    "mareep": criar_pokemon("Mareep", "Elétrico", 55, 40, 40, 65, 45, 35, nivel=5, evolui_nivel=15, evolui_para="Flaaffy"),
    "flaaffy": criar_pokemon("Flaaffy", "Elétrico", 70, 55, 55, 80, 60, 45, nivel=15, evolui_nivel=30, evolui_para="Ampharos"),
    "ampharos": criar_pokemon("Ampharos", "Elétrico", 90, 75, 85, 115, 90, 55, nivel=30),

    "bellossom": criar_pokemon("Bellossom", "Grama", 75, 80, 95, 90, 100, 50),

    "marill": criar_pokemon("Marill", "Água/Fada", 70, 20, 50, 20, 50, 40, nivel=5, evolui_nivel=18, evolui_para="Azumarill"),
    "azumarill": criar_pokemon("Azumarill", "Água/Fada", 100, 50, 80, 60, 80, 50, nivel=18),

    "sudowoodo": criar_pokemon("Sudowoodo", "Pedra", 70, 100, 115, 30, 65, 30),

    "politoed": criar_pokemon("Politoed", "Água", 90, 75, 75, 90, 100, 70),

    "hoppip": criar_pokemon("Hoppip", "Grama/Voador", 35, 35, 40, 35, 55, 50, nivel=5, evolui_nivel=18, evolui_para="Skiploom"),
    "skiploom": criar_pokemon("Skiploom", "Grama/Voador", 55, 45, 50, 45, 65, 80, nivel=18, evolui_nivel=27, evolui_para="Jumpluff"),
    "jumpluff": criar_pokemon("Jumpluff", "Grama/Voador", 75, 55, 70, 55, 95, 110, nivel=27),

    "aipom": criar_pokemon("Aipom", "Normal", 55, 70, 55, 40, 55, 85, nivel=5),

    "sunkern": criar_pokemon("Sunkern", "Grama", 30, 30, 30, 30, 30, 30, nivel=5, evolui_para="Sunflora"),
    "sunflora": criar_pokemon("Sunflora", "Grama", 75, 75, 55, 105, 85, 30),

    "yanma": criar_pokemon("Yanma", "Inseto/Voador", 65, 65, 45, 75, 45, 95, nivel=5),

    "wooper": criar_pokemon("Wooper", "Água/Terra", 55, 45, 45, 25, 25, 15, nivel=5, evolui_nivel=20, evolui_para="Quagsire"),
    "quagsire": criar_pokemon("Quagsire", "Água/Terra", 95, 85, 85, 65, 65, 35, nivel=20),

    "espeon": criar_pokemon("Espeon", "Psíquico", 65, 65, 60, 130, 95, 110),
    "umbreon": criar_pokemon("Umbreon", "Sombrio", 95, 65, 110, 60, 130, 65),

    "murkrow": criar_pokemon("Murkrow", "Sombrio/Voador", 60, 85, 42, 85, 42, 91, nivel=5),

    "slowking": criar_pokemon("Slowking", "Água/Psíquico", 95, 75, 80, 100, 110, 30),

    "misdreavus": criar_pokemon("Misdreavus", "Fantasma", 60, 60, 60, 85, 85, 85),

    "unown": criar_pokemon("Unown", "Psíquico", 48, 72, 48, 72, 48, 48),

    "wobbuffet": criar_pokemon("Wobbuffet", "Psíquico", 190, 33, 58, 33, 58, 33),

    "girafarig": criar_pokemon("Girafarig", "Normal/Psíquico", 70, 80, 65, 90, 65, 85),

    "pineco": criar_pokemon("Pineco", "Inseto", 50, 65, 90, 35, 35, 15, nivel=5, evolui_nivel=31, evolui_para="Forretress"),
    "forretress": criar_pokemon("Forretress", "Inseto/Aço", 75, 90, 140, 60, 60, 40, nivel=31),

    "dunsparce": criar_pokemon("Dunsparce", "Normal", 100, 70, 70, 65, 65, 45),

    "gligar": criar_pokemon("Gligar", "Terra/Voador", 65, 75, 105, 35, 65, 85),

    "steelix": criar_pokemon("Steelix", "Aço/Terra", 75, 85, 200, 55, 65, 30),

    "snubbull": criar_pokemon("Snubbull", "Fada", 60, 80, 50, 40, 40, 30, nivel=5, evolui_nivel=23, evolui_para="Granbull"),
    "granbull": criar_pokemon("Granbull", "Fada", 90, 120, 75, 60, 60, 45, nivel=23),

    "qwilfish": criar_pokemon("Qwilfish", "Água/Venenoso", 65, 95, 75, 55, 55, 85),

    "scizor": criar_pokemon("Scizor", "Inseto/Aço", 70, 130, 100, 55, 80, 65),

    "shuckle": criar_pokemon("Shuckle", "Inseto/Pedra", 20, 10, 230, 10, 230, 5),

    "heracross": criar_pokemon("Heracross", "Inseto/Lutador", 80, 125, 75, 40, 95, 85),

    "sneasel": criar_pokemon("Sneasel", "Sombrio/Gelo", 55, 95, 55, 35, 75, 115),

    "teddiursa": criar_pokemon("Teddiursa", "Normal", 60, 80, 50, 50, 50, 40, nivel=5, evolui_nivel=30, evolui_para="Ursaring"),
    "ursaring": criar_pokemon("Ursaring", "Normal", 90, 130, 75, 75, 75, 55, nivel=30),

    "slugma": criar_pokemon("Slugma", "Fogo", 40, 40, 40, 70, 40, 20, nivel=5, evolui_nivel=38, evolui_para="Magcargo"),
    "magcargo": criar_pokemon("Magcargo", "Fogo/Pedra", 50, 50, 120, 80, 80, 30, nivel=38),

    "swinub": criar_pokemon("Swinub", "Gelo/Terra", 50, 50, 40, 30, 30, 50, nivel=5, evolui_nivel=33, evolui_para="Piloswine"),
    "piloswine": criar_pokemon("Piloswine", "Gelo/Terra", 100, 100, 80, 60, 60, 50, nivel=33),

    "corsola": criar_pokemon("Corsola", "Água/Pedra", 55, 55, 85, 65, 85, 35),

    "remoraid": criar_pokemon("Remoraid", "Água", 35, 65, 35, 65, 35, 65, nivel=5, evolui_nivel=25, evolui_para="Octillery"),
    "octillery": criar_pokemon("Octillery", "Água", 75, 105, 75, 105, 75, 45, nivel=25),

    "delibird": criar_pokemon("Delibird", "Gelo/Voador", 45, 55, 45, 65, 45, 75),

    "mantine": criar_pokemon("Mantine", "Água/Voador", 65, 40, 70, 80, 140, 70),

    "skarmory": criar_pokemon("Skarmory", "Aço/Voador", 65, 80, 140, 40, 70, 70),

    "houndour": criar_pokemon("Houndour", "Sombrio/Fogo", 45, 60, 30, 80, 50, 65, nivel=5, evolui_nivel=24, evolui_para="Houndoom"),
    "houndoom": criar_pokemon("Houndoom", "Sombrio/Fogo", 75, 90, 50, 110, 80, 95, nivel=24),

    "kingdra": criar_pokemon("Kingdra", "Água/Dragão", 75, 95, 95, 95, 95, 85),

    "phanpy": criar_pokemon("Phanpy", "Terra", 90, 60, 60, 40, 40, 40, nivel=5, evolui_nivel=25, evolui_para="Donphan"),
    "donphan": criar_pokemon("Donphan", "Terra", 90, 120, 120, 60, 60, 50, nivel=25),

    "porygon2": criar_pokemon("Porygon2", "Normal", 85, 80, 90, 105, 95, 60),

    "stantler": criar_pokemon("Stantler", "Normal", 73, 95, 62, 85, 65, 85),

    "smeargle": criar_pokemon("Smeargle", "Normal", 55, 20, 35, 20, 45, 75),

    "tyrogue": criar_pokemon("Tyrogue", "Lutador", 35, 35, 35, 35, 35, 35, nivel=5, evolui_nivel=20),

    "hitmontop": criar_pokemon("Hitmontop", "Lutador", 50, 95, 95, 35, 110, 70),

    "smoochum": criar_pokemon("Smoochum", "Gelo/Psíquico", 45, 30, 15, 85, 65, 65, nivel=2, evolui_para="Jynx"),

    "elekid": criar_pokemon("Elekid", "Elétrico", 45, 63, 37, 65, 55, 95, nivel=5, evolui_nivel=30, evolui_para="Electabuzz"),

    "magby": criar_pokemon("Magby", "Fogo", 45, 75, 37, 70, 55, 83, nivel=5, evolui_nivel=30, evolui_para="Magmar"),

    "miltank": criar_pokemon("Miltank", "Normal", 95, 80, 105, 40, 70, 100),

    "blissey": criar_pokemon("Blissey", "Normal", 255, 10, 10, 75, 135, 55),

    "raikou": criar_pokemon("Raikou", "Elétrico", 90, 85, 75, 115, 115, 115),
    "entei": criar_pokemon("Entei", "Fogo", 115, 115, 85, 90, 75, 100),
    "suicune": criar_pokemon("Suicune", "Água", 100, 75, 115, 90, 115, 85),

    "larvitar": criar_pokemon("Larvitar", "Pedra/Terra", 50, 64, 50, 45, 50, 41, nivel=5, evolui_nivel=30, evolui_para="Pupitar"),
    "pupitar": criar_pokemon("Pupitar", "Pedra/Terra", 70, 84, 70, 65, 70, 51, nivel=30, evolui_nivel=55, evolui_para="Tyranitar"),
    "tyranitar": criar_pokemon("Tyranitar", "Pedra/Sombrio", 100, 134, 110, 95, 100, 61, nivel=55),

    "lugia": criar_pokemon("Lugia", "Psíquico/Voador", 106, 90, 130, 90, 154, 110),
    "ho_oh": criar_pokemon("Ho-Oh", "Fogo/Voador", 106, 130, 90, 110, 154, 90),
    "celebi": criar_pokemon("Celebi", "Psíquico/Grama", 100, 100, 100, 100, 100, 100)
}

# =========================================
# EVOLUÇÕES
# =========================================

EVOLUCOES_NIVEL = {
    "Eevee": (20, {"Vaporeon", "Jolteon", "Flareon", "Espeon", "Umbreon"}),
    "Pikachu": (30, {"Raichu"}),
    "Clefairy": (25, {"Clefable"}),
    "Nidorina": (30, {"Nidoqueen"}),
    "Nidorino": (30, {"Nidoking"}),
    "Jigglypuff": (25, {"Wigglytuff"}),
    "Gloom": (30, {"Vileplume", "Bellossom"}),
    "Poliwhirl": (30, {"Poliwrath", "Politoed"}),
    "Weepinbell": (30, {"Victreebel"}),
    "Slowpoke": (37, {"Slowbro", "Slowking"}),
    "Onix": (35, {"Steelix"}),
    "Kadabra": (35, {"Alakazam"}),
    "Machoke": (35, {"Machamp"}),
    "Graveler": (35, {"Golem"}),
    "Haunter": (35, {"Gengar"}),
    "Shellder": (30, {"Cloyster"}),
    "Staryu": (30, {"Starmie"}),
    "Bellsprout": (21, {"Weepinbell"}),
    "Oddish": (21, {"Gloom"}),
    "Poliwag": (25, {"Poliwhirl"}),
    "Horsea": (25, {"Seadra"}),
    "Krabby": (28, {"Kingler"}),
    "Exeggcute": (30, {"Exeggutor"}),
    "Magnemite": (30, {"Magneton"}),
    "Voltorb": (30, {"Electrode"}),
    "Diglett": (26, {"Dugtrio"}),
    "Ponyta": (40, {"Rapidash"}),
    "Omanyte": (40, {"Omastar"}),
    "Kabuto": (40, {"Kabutops"}),
    "Dratini": (30, {"Dragonair"}),
    "Dragonair": (55, {"Dragonite"}),
    "Mareep": (15, {"Flaaffy"}),
    "Flaaffy": (30, {"Ampharos"}),
    "Hoppip": (18, {"Skiploom"}),
    "Skiploom": (27, {"Jumpluff"}),
    "Wooper": (20, {"Quagsire"}),
    "Pineco": (31, {"Forretress"}),
    "Teddiursa": (30, {"Ursaring"}),
    "Phanpy": (25, {"Donphan"}),
    "Remoraid": (25, {"Octillery"}),
    "Houndour": (24, {"Houndoom"}),
    "Slugma": (30, {"Magcargo"}),
    "Spearow": (20, {"Fearow"}),
    "Scyther": (35, {"Scizor"}),
    "Seadra": (35, {"Kingdra"}),
    "Porygon": (35, {"Porygon2"}),
    "Chansey": (30, {"Blissey"}),
    "Golbat": (32, {"Crobat"}),
    "Vulpix": (30, {"Ninetales"}),
    "Growlithe": (30, {"Arcanine"}),
    "Togetic": (35, {"Togekiss"}),
    "Sunkern": (20, {"Sunflora"}),
    "Murkrow": (35, {"Honchkrow"}),
    "Misdreavus": (35, {"Mismagius"}),
    "Yanma": (35, {"Yanmega"}),
    "Aipom": (32, {"Ambipom"}),
    "Piloswine": (35, {"Mamoswine"}),
    "Lickitung": (32, {"Lickilicky"}),
    "Tangela": (32, {"Tangrowth"}),
    "Rhydon": (40, {"Rhyperior"}),
    "Electabuzz": (35, {"Electivire"}),
    "Magmar": (35, {"Magmortar"}),
    "Tyrogue": (20, {"Hitmonlee", "Hitmonchan", "Hitmontop"}),
}

RAMOS_EVOLUCAO = {"Eevee": "Espeon", "Gloom": "Vileplume", "Poliwhirl": "Poliwrath", "Slowpoke": "Slowbro", "Tyrogue": "Hitmonlee"}

# =========================================
# FUNÇÕES AUXILIARES
# =========================================

def limpar():
    print("\n" * 3)

def barra_vida(atual, maxima):
    tamanho = 20
    if maxima <= 0:
        maxima = 1
    proporcao = atual / maxima
    cheio = int(proporcao * tamanho)
    return "█" * cheio + "-" * (tamanho - cheio)

def copiar_pokemon(pokemon):
    return pokemon.copy()

_ALIASES_POKEMON = {
    "farfetch_d": "farfetchd",
}

def _normalizar_nome_pokemon(nome):
    if not nome:
        return ""
    nome = nome.strip().lower()
    nome = nome.replace("♀", "f").replace("♂", "m")
    for ch in [".", "'", "’", "-", " "]:
        nome = nome.replace(ch, "_")
    while "__" in nome:
        nome = nome.replace("__", "_")
    chave = nome.strip("_")
    return _ALIASES_POKEMON.get(chave, chave)

def buscar_pokemon(nome):
    chave = _normalizar_nome_pokemon(nome)
    if "pokemons" in globals() and chave in pokemons:
        base = copiar_pokemon(pokemons[chave])
        base["nome"] = base.get("nome", nome.title())
        base["hp_max"] = base.get("hp_max", base.get("hp", 200))
        base["hp"] = base["hp_max"]
        base["speed"] = base.get("speed", base.get("velocidade", 70))
        base["velocidade"] = base["speed"]
        base.setdefault("ataque_especial", base.get("ataque", 70))
        base.setdefault("defesa_especial", base.get("defesa", 60))
        base.setdefault("nivel", 5)
        base.setdefault("evolui_nivel", pokemons[chave].get("evolui_nivel"))
        base.setdefault("evolui_para", pokemons[chave].get("evolui_para"))
        base.setdefault("experiencia", 0)
        base.setdefault("mega_evolution", False)
        base.setdefault("mega_usada", False)
        base.setdefault("golpe_especial", False)
        base.setdefault("golpes", [])
        base.setdefault("habilidade_eevee", base["nome"] == "Eevee")
        return base

    return {
        "nome": nome.replace("_", " ").title(), "tipo": "Normal",
        "hp": 200, "hp_max": 200, "ataque": 70, "defesa": 60,
        "ataque_especial": 70, "defesa_especial": 60,
        "speed": 70, "velocidade": 70, "nivel": 5,
        "mega_evolution": False, "mega_usada": False,
        "golpe_especial": False, "golpes": [], "habilidade_eevee": False
    }

def normalizar_pokemon(pokemon):
    pokemon.setdefault("hp_max", pokemon.get("hp", 200))
    pokemon.setdefault("hp", pokemon["hp_max"])
    pokemon.setdefault("speed", pokemon.get("velocidade", 70))
    pokemon.setdefault("velocidade", pokemon["speed"])
    pokemon.setdefault("ataque", 70)
    pokemon.setdefault("defesa", 60)
    pokemon.setdefault("ataque_especial", pokemon.get("ataque", 70))
    pokemon.setdefault("defesa_especial", pokemon.get("defesa", 60))
    pokemon.setdefault("tipo", "Normal")
    pokemon.setdefault("nivel", 5)
    pokemon.setdefault("experiencia", 0)
    pokemon.setdefault("habilidade_eevee", pokemon.get("nome") == "Eevee")
    pokemon.setdefault("golpe_especial", False)
    pokemon.setdefault("mega_evolution", False)
    pokemon.setdefault("mega_usada", False)
    pokemon.setdefault("golpes", [])
    return pokemon

def escolher_pokemon():
    if not jogador["equipe"]:
        print("\n❌ Você não tem Pokémon na equipe!")
        return None
    print("\nEscolha um Pokémon:")
    for i, p in enumerate(jogador["equipe"]):
        print(f"{i+1} - {p['nome']} (HP: {p['hp']}/{p['hp_max']})")
    try:
        escolha = int(input("> ")) - 1
        if 0 <= escolha < len(jogador["equipe"]):
            return jogador["equipe"][escolha]
    except ValueError:
        pass
    print("\n❌ Escolha inválida!")
    return None

# =========================================
# CÁLCULO DE DANO E VELOCIDADE
# =========================================

def calcular_dano(atacante, defensor):
    dano = atacante["ataque"]
    defesa = defensor["defesa"]
    reducao = defesa / 300
    dano_final = int(dano * (1 - reducao))
    if dano_final < 1:
        dano_final = 1
    return dano_final

def turno_velocidade(pokemon, inimigo):
    if pokemon["speed"] > inimigo["speed"]:
        return "jogador"
    elif pokemon["speed"] < inimigo["speed"]:
        return "inimigo"
    return random.choice(["jogador", "inimigo"])

def calcular_multiplicador_tipo(tipo_ataque, tipo_defensor):
    multiplicador = 1.0
    tipos_ataque = [t.strip().capitalize() for t in tipo_ataque.split("/")]
    tipos_defesa = [t.strip().capitalize() for t in tipo_defensor.split("/")]
    for ataque_tipo in tipos_ataque[:1]:
        for defesa_tipo in tipos_defesa:
            multiplicador *= TABELA_TIPOS.get(ataque_tipo, {}).get(defesa_tipo, 1.0)
    return multiplicador

def aplicar_dano_tipo(atacante, defensor, dano):
    multiplicador = calcular_multiplicador_tipo(
        atacante.get("tipo", "Normal"), defensor.get("tipo", "Normal")
    )
    dano_final = max(0, int(dano * multiplicador))
    if multiplicador > 1:
        print("É super efetivo!")
    elif 0 < multiplicador < 1:
        print("Não é muito efetivo...")
    elif multiplicador == 0:
        print("Não afeta o adversário!")
    return dano_final

def calcular_dano_especial(atacante, defensor):
    ataque = atacante.get("ataque_especial", atacante.get("ataque", 70))
    defesa = defensor.get("defesa_especial", defensor.get("defesa", 60))
    dano = max(1, int(ataque * (1 - defesa / 300)))
    return aplicar_dano_tipo(atacante, defensor, dano)

# =========================================
# MEGA EVOLUÇÃO
# =========================================

def ativar_mega_evolucao(atacante):
    if atacante.get("mega_usada", False):
        print(f"Aviso: {atacante.get('nome', 'Pokémon')} já utilizou a Mega Evolução nesta batalha!")
        return False
    atacante["ataque"] += 20
    atacante["defesa"] += 20
    atacante["speed"] += 20
    atacante["mega_usada"] = True
    print(f"Brilho intenso! {atacante.get('nome', 'Pokémon')} realizou a Mega Evolução! Todos os atributos subiram em 20.")
    return True

# =========================================
# CRIAÇÃO DE PERSONAGEM
# =========================================

def criacao_de_personagem():
    limpar()
    jogador["nome"] = input("Nome do treinador: ").strip() or "Treinador"
    jogador["equipe"] = []
    print(f"\nBem-vindo(a), {jogador['nome']}! Vá ao laboratório do Professor Carvalho em Pallet para escolher seu Pokémon inicial.")
    return jogador

# =========================================
# TRANSFORMAÇÃO DO EEVEE
# =========================================

def transformar_eevee(pokemon):
    if pokemon.get("nome") != "Eevee":
        print("Este Pokémon não é um Eevee e não pode usar esta transformação!")
        return
    print("\n✨ Habilidade especial do Eevee disponível desde o início! Escolha uma transformação:")
    print("1 - Vaporeon (Água)")
    print("2 - Jolteon (Elétrico)")
    print("3 - Flareon (Fogo)")
    print("4 - Espeon (Psíquico)")
    print("5 - Umbreon (Sombrio)")
    escolha = input("Digite o número da evolução desejada: ")
    evolucoes = {
        "1": {"nome": "Vaporeon", "tipo": "água", "hp_bonus": 130, "ataque_bonus": 20, "defesa_bonus": 20},
        "2": {"nome": "Jolteon", "tipo": "elétrico", "hp_bonus": 80, "ataque_bonus": 30, "speed_bonus": 40},
        "3": {"nome": "Flareon", "tipo": "fogo", "hp_bonus": 90, "ataque_bonus": 50, "defesa_bonus": 10},
        "4": {"nome": "Espeon", "tipo": "psíquico", "hp_bonus": 90, "ataque_bonus": 45, "speed_bonus": 30},
        "5": {"nome": "Umbreon", "tipo": "sombrio", "hp_bonus": 150, "defesa_bonus": 50},
    }
    if escolha in evolucoes:
        nova_forma = evolucoes[escolha]
        pokemon["nome"] = nova_forma["nome"]
        pokemon["tipo"] = nova_forma["tipo"]
        pokemon["hp_max"] += nova_forma.get("hp_bonus", 50)
        pokemon["hp"] = pokemon["hp_max"]
        pokemon["ataque"] += nova_forma.get("ataque_bonus", 20)
        pokemon["defesa"] += nova_forma.get("defesa_bonus", 20)
        pokemon["speed"] += nova_forma.get("speed_bonus", 20)
        print(f"\n✨ SUCESSO! O seu Eevee evoluiu instantaneamente para {pokemon['nome']}!")
    else:
        print("Opção inválida! A transformação foi cancelada.")

# =========================================
# EVOLUÇÃO E EXPERIÊNCIA
# =========================================

def evoluir_para_nova_forma(pokemon, nome_novo):
    chave = _normalizar_nome_pokemon(nome_novo)
    base = pokemons.get(chave)
    if not base:
        return False
    hp_antigo_max = max(1, pokemon.get("hp_max", pokemon.get("hp", 1)))
    proporcao_hp = pokemon.get("hp", hp_antigo_max) / hp_antigo_max
    nome_antigo = pokemon["nome"]
    pokemon["nome"] = base["nome"]
    pokemon["tipo"] = base["tipo"]
    for campo in ("ataque", "defesa", "ataque_especial", "defesa_especial"):
        pokemon[campo] = max(pokemon.get(campo, 1), base.get(campo, 1))
    pokemon["hp_max"] = max(hp_antigo_max, base.get("hp", hp_antigo_max))
    pokemon["hp"] = max(1, int(pokemon["hp_max"] * proporcao_hp))
    pokemon["speed"] = max(pokemon.get("speed", 1), base.get("velocidade", 70))
    pokemon["velocidade"] = pokemon["speed"]
    print(f"\n✨ {nome_antigo} evoluiu para {pokemon['nome']}! Seus atributos foram atualizados.")
    return True

def ganhar_experiencia(pokemon, quantidade):
    pokemon = normalizar_pokemon(pokemon)
    pokemon["experiencia"] = pokemon.get("experiencia", 0) + quantidade
    while pokemon.get("nivel", 5) < 100:
        limite = pokemon.get("nivel", 5) * 20
        if pokemon["experiencia"] < limite:
            break
        pokemon["experiencia"] -= limite
        pokemon["nivel"] = pokemon.get("nivel", 5) + 1
        pokemon["hp_max"] = int(pokemon["hp_max"] * 1.04)
        if pokemon.get("hp", 0) > 0:
            pokemon["hp"] = min(pokemon["hp_max"], int(pokemon["hp"] * 1.04) + 1)
        for atributo in ("ataque", "defesa", "ataque_especial", "defesa_especial", "speed"):
            if atributo in pokemon:
                pokemon[atributo] = max(1, int(pokemon[atributo] * 1.025) + 1)
        print(f"⬆️ {pokemon['nome']} subiu para o nível {pokemon['nivel']}!")
        nome_atual = pokemon["nome"]
        dados_base = pokemons.get(_normalizar_nome_pokemon(nome_atual), {})
        nivel_evolucao = dados_base.get("evolui_nivel")
        alvo = dados_base.get("evolui_para")
        if nivel_evolucao and alvo and pokemon["nivel"] >= nivel_evolucao:
            evoluir_para_nova_forma(pokemon, alvo)
        elif nome_atual in EVOLUCOES_NIVEL and pokemon["nivel"] >= EVOLUCOES_NIVEL[nome_atual][0]:
            opcoes = EVOLUCOES_NIVEL[nome_atual][1]
            escolhido = RAMOS_EVOLUCAO.get(nome_atual) or (sorted(opcoes)[0] if opcoes else None)
            if escolhido:
                evoluir_para_nova_forma(pokemon, escolhido)

# =========================================
# COMPLETAR ROTAS
# =========================================

LENDARIOS_EXCLUSIVOS = {"articuno", "zapdos", "moltres", "mewtwo", "mew", "celebi", "raikou", "entei", "suicune", "lugia", "ho_oh"}

# Cada área da Ilha dos Lendários tem um encontro fixo.
LENDARIOS_ILHA = {
    "bosque de celebi": ("celebi", 80),
    "lago de suicune": ("suicune", 80),
    "vulcao de entei": ("entei", 80),
    "templo de raikou": ("raikou", 80),
    "pico de articuno": ("articuno", 80),
    "usina isolada de zapdos": ("zapdos", 80),
    "ninho de moltres": ("moltres", 80),
    "caverna de mewtwo": ("mewtwo", 85),
    "santuário de ho-oh": ("ho_oh", 80),
    "abismo de lugia": ("lugia", 80),
    "jardim mistico de mew": ("mew", 80),
}

def completar_rotas_com_pokemon_restantes():
    usados = {_normalizar_nome_pokemon(nome) for lista in POKEMON_ROTAS.values() for nome in lista}
    rotas_normais = ["rota 1", "floresta de viridian", "rota 3", "rota 4", "rota 5", "rota 6", "rota 7", "rota 8", "rota 9", "rota 10", "rota 11", "rota 12", "rota maritima 1", "rota maritima 2", "rota maritima 3", "rota maritima 4", "saffari zone", "cemiterio pokemon", "mansao pokemon", "victory road"]
    for rota in rotas_normais:
        POKEMON_ROTAS.setdefault(rota, [])
    restantes = [chave for chave in pokemons if chave not in usados and chave not in LENDARIOS_EXCLUSIVOS]
    for i, chave in enumerate(restantes):
        POKEMON_ROTAS[rotas_normais[i % len(rotas_normais)]].append(chave)

completar_rotas_com_pokemon_restantes()

# =========================================
# ITENS
# =========================================

def usar_item(pokemon=None):
    itens = jogador["inventario"]
    if not itens:
        print("Seu inventário está vazio.")
        return False
    print("\n=== INVENTÁRIO ===")
    for i, item in enumerate(itens, 1):
        print(f"{i} - {item}")
    print("0 - Voltar")
    try:
        escolha = int(input("> "))
        if escolha == 0:
            return False
        item = itens[escolha - 1]
    except (ValueError, IndexError):
        print("Escolha inválida.")
        return False

    if item in ("pokebola", "greatball", "ultraball"):
        print("Bolas de captura só podem ser usadas durante uma batalha selvagem.")
        return False

    if item in ("poção", "super poção", "hiper poçao", "hiper poção"):
        alvo = pokemon or escolher_pokemon()
        if not alvo:
            return False
        cura = {"poção": 50, "super poção": 100, "hiper poçao": 200, "hiper poção": 200}[item]
        if alvo["hp"] >= alvo["hp_max"]:
            print(f"{alvo['nome']} já está com HP cheio.")
            return False
        recuperado = min(cura, alvo["hp_max"] - alvo["hp"])
        alvo["hp"] += recuperado
        itens.remove(item)
        print(f"{alvo['nome']} recuperou {recuperado} HP!")
        return True

    if item.lower() in ("max candy", "maxcandy"):
        alvo = pokemon or escolher_pokemon()
        if not alvo:
            return False
        if alvo.get("nivel", 5) >= 100:
            print(f"{alvo['nome']} já está no nível máximo (100).")
            return False
        alvo["nivel"] = min(100, alvo.get("nivel", 5) + 5)
        alvo["hp_max"] = int(alvo["hp_max"] * 1.10)
        alvo["hp"] = alvo["hp_max"]
        for atributo in ("ataque", "defesa", "ataque_especial", "defesa_especial", "speed"):
            if atributo in alvo:
                alvo[atributo] = max(1, int(alvo[atributo] * 1.05) + 1)
        itens.remove(item)
        print(f"🍬 {alvo['nome']} subiu para o nível {alvo['nivel']} e foi curado!")
        return True

    print("Esse item ainda não possui um efeito utilizável.")
    return False

# =========================================
# CAPTURA
# =========================================

def capturar_pokemon(inimigo):
    inventario = jogador["inventario"]
    bolas = [("ultraball", 0.8), ("greatball", 0.5), ("pokebola", 0.2)]
    item_escolhido = None
    chance_base = 0.2
    for item, chance in bolas:
        if item in inventario:
            item_escolhido, chance_base = item, chance
            break
    if not item_escolhido:
        print("Você não tem Pokébolas!")
        return False
    inventario.remove(item_escolhido)
    proporcao = inimigo["hp"] / max(1, inimigo["hp_max"])
    chance = min(0.95, chance_base + (0.35 if proporcao <= 0.2 else 0.15 if proporcao <= 0.5 else 0))
    if random.random() <= chance:
        capturado = normalizar_pokemon(copiar_pokemon(inimigo))
        capturado["hp"] = max(1, capturado["hp"])
        jogador["total_capturados"] = jogador.get("total_capturados", 0) + 1
        if len(jogador["equipe"]) < 6:
            jogador["equipe"].append(capturado)
            print(f"{capturado['nome']} entrou na sua equipe!")
        else:
            jogador.setdefault("pokemon_guardados", []).append(capturado)
            print(f"Sua equipe está cheia! {capturado['nome']} foi enviado automaticamente ao PC.")
        if capturado["nome"] not in jogador["pokedex_capturados"]:
            jogador["pokedex_capturados"].append(capturado["nome"])
        print(f"Você capturou {capturado['nome']}! Total de capturas: {jogador['total_capturados']}/100.")
        if jogador["total_capturados"] >= 100:
            print("🌟 Mew e Celebi agora podem aparecer raramente em qualquer rota!")
        return True
    print(f"{inimigo['nome']} escapou da Pokébola!")
    return False

# =========================================
# BATALHA
# =========================================

def batalha(inimigo, permitir_captura=True):
    inimigo = normalizar_pokemon(copiar_pokemon(inimigo))
    vivos = [p for p in jogador["equipe"] if p.get("hp", 0) > 0]
    if not vivos:
        print("Todos os seus Pokémon estão sem HP. Visite um Centro Pokémon.")
        return False
    pokemon = vivos[0]
    while inimigo["hp"] > 0:
        vivos = [p for p in jogador["equipe"] if p.get("hp", 0) > 0]
        if not vivos:
            print("Todos os seus Pokémon foram derrotados!")
            return False
        if pokemon["hp"] <= 0:
            pokemon = vivos[0]
        limpar()
        print(f"===== BATALHA: {jogador['nome']} =====")
        print(f"{pokemon['nome']} Nv.{pokemon.get('nivel', 5)} | HP {pokemon['hp']}/{pokemon['hp_max']}")
        print(barra_vida(pokemon["hp"], pokemon["hp_max"]))
        print(f"\n{inimigo['nome']} | HP {inimigo['hp']}/{inimigo['hp_max']}")
        print(barra_vida(inimigo["hp"], inimigo["hp_max"]))
        print("\n1 - Atacar\n2 - Golpe especial\n3 - Trocar Pokémon\n4 - Usar item")
        if permitir_captura:
            print("5 - Capturar")
        if pokemon.get("mega_evolution", False) and not pokemon.get("mega_usada", False):
            print("7 - Mega Evolução")
        print("6 - Voltar ao Centro Pokémon")
        op = input("> ").strip()
        if op == "3":
            novo = escolher_pokemon()
            if novo and novo["hp"] > 0:
                pokemon = normalizar_pokemon(novo)
            else:
                print("Não é possível escolher esse Pokémon.")
            continue
        if op == "4":
            usar_item(pokemon)
            continue
        if op == "5" and permitir_captura:
            if capturar_pokemon(inimigo):
                return True
        elif op == "6":
            centro_pokemon()
            print("Você encerrou a batalha e voltou ao Centro Pokémon.")
            return False
        elif op == "7" and pokemon.get("mega_evolution", False) and not pokemon.get("mega_usada", False):
            ativar_mega_evolucao(pokemon)
            dano_inimigo = aplicar_dano_tipo(inimigo, pokemon, calcular_dano(inimigo, pokemon))
            pokemon["hp"] = max(0, pokemon["hp"] - dano_inimigo)
            print(f"{inimigo['nome']} causou {dano_inimigo} de dano!")
            continue
        elif op not in ("1", "2"):
            print("Opção inválida.")
            continue
        else:
            if op == "1":
                dano = aplicar_dano_tipo(pokemon, inimigo, calcular_dano(pokemon, inimigo))
            else:
                dano = calcular_dano_especial(pokemon, inimigo)
            inimigo["hp"] = max(0, inimigo["hp"] - dano)
            print(f"{pokemon['nome']} causou {dano} de dano!")
            if inimigo["hp"] <= 0:
                break
        if inimigo["hp"] > 0:
            dano_inimigo = aplicar_dano_tipo(inimigo, pokemon, calcular_dano(inimigo, pokemon))
            pokemon["hp"] = max(0, pokemon["hp"] - dano_inimigo)
            print(f"{inimigo['nome']} causou {dano_inimigo} de dano!")
            time.sleep(1)
    jogador["vitorias"] += 1
    xp = max(20, inimigo.get("nivel", 5) * 12)
    ganhar_experiencia(pokemon, xp)
    for aliado in jogador["equipe"]:
        if aliado is not pokemon and aliado.get("hp", 0) > 0:
            ganhar_experiencia(aliado, max(5, xp // 4))
    recompensa = max(50, inimigo.get("nivel", 5) * 20)
    jogador["pokedolares"] += recompensa
    print(f"\nVitória! Você recebeu {recompensa} Pokédolares.")
    return True

# =========================================
# CENTRO POKÉMON E PC
# =========================================

def centro_pokemon():
    while True:
        print("\n=== CENTRO POKÉMON ===")
        print("1 - Curar equipe")
        print("2 - Usar PC (guardar/retirar Pokémon)")
        print("0 - Sair do centro")
        op = input("> ").strip()
        if op == "1":
            for pokemon in jogador["equipe"]:
                pokemon["hp"] = pokemon["hp_max"]
                pokemon["mega_usada"] = False
            print("Seus Pokémon foram curados!")
        elif op == "2":
            menu_pc()
        elif op == "0":
            return
        else:
            print("Opção inválida.")

def menu_pc():
    jogador.setdefault("pokemon_guardados", [])
    while True:
        print("\n========== PC POKÉMON ==========")
        print(f"Equipe: {len(jogador['equipe'])}/6 | Pokémon guardados: {len(jogador['pokemon_guardados'])}")
        print("1 - Guardar Pokémon da equipe")
        print("2 - Retirar Pokémon do PC")
        print("3 - Ver Pokémon guardados")
        print("0 - Desligar PC")
        op = input("> ").strip()
        if op == "0":
            return
        elif op == "1":
            if len(jogador["equipe"]) <= 1:
                print("Você precisa manter pelo menos um Pokémon na equipe.")
                continue
            mostrar_equipe()
            try:
                indice = int(input("Qual Pokémon deseja guardar? ")) - 1
                if not 0 <= indice < len(jogador["equipe"]):
                    raise ValueError
            except ValueError:
                print("Escolha inválida.")
                continue
            pokemon = jogador["equipe"].pop(indice)
            jogador["pokemon_guardados"].append(pokemon)
            print(f"{pokemon['nome']} foi guardado no PC.")
        elif op == "2":
            if len(jogador["equipe"]) >= 6:
                print("Sua equipe já tem 6 Pokémon. Guarde um antes de retirar outro.")
                continue
            if not jogador["pokemon_guardados"]:
                print("Não há Pokémon guardados no PC.")
                continue
            print("\n=== POKÉMON GUARDADOS ===")
            for i, pokemon in enumerate(jogador["pokemon_guardados"], 1):
                print(f"{i} - {pokemon['nome']} Nv.{pokemon.get('nivel', 5)} | HP {pokemon.get('hp', 0)}/{pokemon.get('hp_max', 1)}")
            try:
                indice = int(input("Qual Pokémon deseja retirar? ")) - 1
                if not 0 <= indice < len(jogador["pokemon_guardados"]):
                    raise ValueError
            except ValueError:
                print("Escolha inválida.")
                continue
            pokemon = jogador["pokemon_guardados"].pop(indice)
            jogador["equipe"].append(pokemon)
            print(f"{pokemon['nome']} foi transferido para sua equipe.")
        elif op == "3":
            if not jogador["pokemon_guardados"]:
                print("Não há Pokémon guardados no PC.")
            else:
                print("\n=== POKÉMON GUARDADOS ===")
                for i, pokemon in enumerate(jogador["pokemon_guardados"], 1):
                    print(f"{i}. {pokemon['nome']} ({pokemon.get('tipo', 'Normal')}) Nv.{pokemon.get('nivel', 5)} | HP {pokemon.get('hp', 0)}/{pokemon.get('hp_max', 1)}")
        else:
            print("Opção inválida.")

def mostrar_equipe():
    if not jogador["equipe"]:
        print("Sua equipe está vazia.")
        return
    print("\n=== SUA EQUIPE ===")
    for i, p in enumerate(jogador["equipe"], 1):
        print(f"{i}. {p['nome']} ({p.get('tipo', 'Normal')}) Nv.{p.get('nivel', 5)} | HP {p['hp']}/{p['hp_max']} | ATQ {p.get('ataque', 0)} | DEF {p.get('defesa', 0)} | ATQ ESP {p.get('ataque_especial', 0)} | DEF ESP {p.get('defesa_especial', 0)}")

# =========================================
# LOJA
# =========================================

def loja():
    max_candy_vendidos = 0
    while True:
        limpar()
        print("🛒 LOJA")
        print(f"💰 Pokédolares: {jogador['pokedolares']}")
        print("\n1 - Pokébola (300)\n2 - Great Ball (500)\n3 - Ultra Ball (800)")
        print("4 - Poção (200)\n5 - Super Poção (400)\n6 - Hiper Poção (800)")
        print("7 - Mega Evolução (1000)")
        print(f"8 - Max Candy (500) [limite: {max_candy_vendidos}/5 nesta visita]")
        print("9 - Sair")
        op = input("> ")
        if op == "1":
            if jogador["pokedolares"] >= 300:
                jogador["pokedolares"] -= 300
                jogador["inventario"].append("pokebola")
                print("\n🎯 Pokébola comprada!")
            else:
                print("\n❌ Dinheiro insuficiente!")
        elif op == "2":
            if jogador["pokedolares"] >= 500:
                jogador["pokedolares"] -= 500
                jogador["inventario"].append("greatball")
                print("\n🎯 Great Ball comprada!")
            else:
                print("\n❌ Dinheiro insuficiente!")
        elif op == "3":
            if jogador["pokedolares"] >= 800:
                jogador["pokedolares"] -= 800
                jogador["inventario"].append("ultraball")
                print("\n🎯 Ultra Ball comprada!")
            else:
                print("\n❌ Dinheiro insuficiente!")
        elif op == "4":
            if jogador["pokedolares"] >= 200:
                jogador["pokedolares"] -= 200
                jogador["inventario"].append("poção")
                print("\n🧪 Poção comprada!")
            else:
                print("\n❌ Dinheiro insuficiente!")
        elif op == "5":
            if jogador["pokedolares"] >= 400:
                jogador["pokedolares"] -= 400
                jogador["inventario"].append("super poção")
                print("\n🧪 Super Poção comprada!")
            else:
                print("\n❌ Dinheiro insuficiente!")
        elif op == "6":
            if jogador["pokedolares"] >= 800:
                jogador["pokedolares"] -= 800
                jogador["inventario"].append("hiper poção")
                print("\n🧪 Hiper Poção comprada!")
            else:
                print("\n❌ Dinheiro insuficiente!")
        elif op == "7":
            if not jogador["equipe"]:
                print("\n❌ Você não tem Pokémon na equipe!")
                time.sleep(2)
                continue
            print("\nEscolha um Pokémon:")
            for i, pokemon in enumerate(jogador["equipe"]):
                status = "✅" if pokemon.get("mega_evolution", False) else "❌"
                print(f"{i+1} - {pokemon['nome']} | Mega Evolução: {status}")
            try:
                escolha = int(input("> ")) - 1
                pokemon = jogador["equipe"][escolha]
            except (ValueError, IndexError):
                print("\n❌ Escolha inválida!")
                time.sleep(2)
                continue
            if pokemon.get("mega_evolution", False):
                print("\n❌ Esse Pokémon já possui mega evolução!")
            elif jogador["pokedolares"] >= 1000:
                jogador["pokedolares"] -= 1000
                pokemon["mega_evolution"] = True
                print(f"\n🔥 {pokemon['nome']} adquiriu o potencial para a Mega Evolução!")
            else:
                print("\n❌ Pokédolares insuficientes!")
        elif op == "8":
            if max_candy_vendidos >= 5:
                print("\n❌ Limite de Max Candy por visita atingido!")
            elif jogador["pokedolares"] >= 500:
                jogador["pokedolares"] -= 500
                jogador["inventario"].append("max candy")
                max_candy_vendidos += 1
                print("\n🍬 Max Candy comprada!")
            else:
                print("\n❌ Pokédolares insuficientes!")
        elif op == "9":
            break
        else:
            print("Opção inválida!")
        time.sleep(1)

# =========================================
# GINÁSIO
# =========================================

def desafiar_ginasio():
    if len(jogador["ginasios"]) >= len(ginasios):
        print("\n🏆 Você já venceu todos os ginásios! Desafie a Liga em Rota da Vitória.")
        time.sleep(2)
        return
    ginasio = ginasios[len(jogador["ginasios"])]
    print(f"\n🏟️ Líder {ginasio['lider']} te desafiou!")
    time.sleep(2)
    for nome_pokemon in ginasio["pokemons"]:
        inimigo = buscar_pokemon(nome_pokemon)
        for atributo in ("hp", "hp_max", "ataque", "defesa", "ataque_especial", "defesa_especial"):
            if atributo in inimigo:
                inimigo[atributo] = max(1, int(inimigo[atributo] * 0.78))
        inimigo["hp"] = inimigo["hp_max"]
        print(f"\n⚔️ {inimigo['nome']} entrou na batalha!")
        time.sleep(2)
        pokemon = escolher_pokemon()
        if pokemon is None:
            print("\n💀 Você perdeu o desafio do ginásio!")
            time.sleep(2)
            return
        pokemon = normalizar_pokemon(pokemon)
        while inimigo["hp"] > 0 and pokemon["hp"] > 0:
            limpar()
            print(f"===== GINÁSIO - {ginasio['lider'].upper()} =====\n")
            print(f"{pokemon['nome']} | HP: {pokemon['hp']}/{pokemon['hp_max']}")
            print(barra_vida(pokemon['hp'], pokemon['hp_max']))
            print(f"\n{inimigo['nome']} | HP: {inimigo['hp']}/{inimigo['hp_max']}")
            print(barra_vida(inimigo['hp'], inimigo['hp_max']))
            print("\n1 - Atacar\n2 - Trocar Pokémon\n3 - Voltar ao Centro Pokémon (desistir)")
            if pokemon.get("mega_evolution", False) and not pokemon.get("mega_usada", False):
                print("4 - Mega Evolução")
            op = input("> ")
            if op == "1":
                primeiro = turno_velocidade(pokemon, inimigo)
                if primeiro == "jogador":
                    dano = aplicar_dano_tipo(pokemon, inimigo, calcular_dano(pokemon, inimigo))
                    inimigo["hp"] = max(0, inimigo["hp"] - dano)
                    print(f"\n⚡ {pokemon['nome']} atacou primeiro! Causou {dano} de dano!")
                    if inimigo["hp"] <= 0:
                        ganhar_experiencia(pokemon, max(20, inimigo.get("nivel", 5) * 12))
                    else:
                        dano_inimigo = aplicar_dano_tipo(inimigo, pokemon, calcular_dano(inimigo, pokemon))
                        pokemon["hp"] = max(0, pokemon["hp"] - dano_inimigo)
                        print(f"\n💢 {inimigo['nome']} atacou! Causou {dano_inimigo} de dano!")
                else:
                    dano_inimigo = aplicar_dano_tipo(inimigo, pokemon, calcular_dano(inimigo, pokemon))
                    pokemon["hp"] = max(0, pokemon["hp"] - dano_inimigo)
                    print(f"\n⚡ {inimigo['nome']} atacou primeiro! Causou {dano_inimigo} de dano!")
                    if pokemon["hp"] > 0:
                        dano = aplicar_dano_tipo(pokemon, inimigo, calcular_dano(pokemon, inimigo))
                        inimigo["hp"] = max(0, inimigo["hp"] - dano)
                        print(f"\n💢 {pokemon['nome']} atacou! Causou {dano} de dano!")
                        if inimigo["hp"] <= 0:
                            ganhar_experiencia(pokemon, max(20, inimigo.get("nivel", 5) * 12))
            elif op == "2":
                novo_p = escolher_pokemon()
                if novo_p and novo_p["hp"] > 0:
                    pokemon = normalizar_pokemon(novo_p)
                continue
            elif op == "3":
                centro_pokemon()
                print("Você saiu do desafio e voltou ao Centro Pokémon. O ginásio não foi concluído.")
                return
            elif op == "4" and pokemon.get("mega_evolution", False) and not pokemon.get("mega_usada", False):
                ativar_mega_evolucao(pokemon)
                continue
            else:
                print("Opção inválida!")
                continue
            if pokemon["hp"] <= 0:
                print(f"\n💀 {pokemon['nome']} foi derrotado!")
                vivos = [p for p in jogador["equipe"] if p["hp"] > 0]
                if vivos:
                    novo = escolher_pokemon()
                    if novo and novo["hp"] > 0:
                        pokemon = normalizar_pokemon(novo)
                    else:
                        pokemon = vivos[0]
                else:
                    print("\n💀 Você perdeu o desafio do ginásio!")
                    time.sleep(2)
                    return
            time.sleep(2)
    jogador["ginasios"].append(ginasio["lider"])
    print(f"\n🏅 Você venceu o ginásio de {ginasio['lider']}! Insígnia conquistada!")
    time.sleep(3)

# =========================================
# LIGA
# =========================================

def desafiar_elites():
    elites = [
        {"nome": "Lorelei", "pokemons": ["dewgong", "cloyster", "slowbro", "lapras"]},
        {"nome": "Bruno", "pokemons": ["onix", "hitmonchan", "hitmonlee", "machamp"]},
        {"nome": "Agatha", "pokemons": ["gengar", "golbat", "haunter", "arbok"]},
        {"nome": "Lance", "pokemons": ["gyarados", "dragonair", "dragonite", "aerodactyl"]},
        {"nome": "Red", "pokemons": ["pikachu", "charizard", "blastoise", "venusaur", "snorlax"]},
    ]
    print("\n🏆 LIGA POKÉMON — DESAFIO FINAL")
    for elite in elites:
        print(f"\n⚔️ {elite['nome']} te desafiou!")
        time.sleep(2)
        for nome in elite["pokemons"]:
            inimigo = buscar_pokemon(nome)
            inimigo["nivel"] = max(50, inimigo.get("nivel", 5))
            inimigo["hp_max"] = int(inimigo["hp_max"] * 1.5)
            inimigo["hp"] = inimigo["hp_max"]
            if not batalha(inimigo, permitir_captura=False):
                print(f"\n💀 Você foi derrotado por {elite['nome']}!")
                return
        print(f"✅ Você venceu {elite['nome']}!")
    print("\n🎉 PARABÉNS! Você venceu a Liga Pokémon e se tornou CAMPEÃO!")
    jogador["historia_concluida"] = True

# =========================================
# EXPLORAÇÃO
# =========================================

def encontrar_lendario_aleatorio():
    capturados = jogador.get("total_capturados", len(jogador.get("pokedex_capturados", [])))
    chances = [("raikou", 0.012), ("entei", 0.012), ("suicune", 0.012)]
    if capturados >= 100:
        chances.extend([("mew", 0.008), ("celebi", 0.008)])
    for nome, chance in chances:
        if random.random() < chance:
            return nome
    return None

def batalha_treinador(tema="variado"):
    temas = {
        "eletrico": ["magnemite", "voltorb", "pikachu", "electabuzz", "raichu"],
        "gelo": ["swinub", "seel", "dewgong", "jynx", "lapras"],
        "fogo": ["growlithe", "ponyta", "magmar", "rapidash", "arcanine"],
        "variado": ["pidgey", "rattata", "geodude", "oddish", "machop", "psyduck", "gastly"]
    }
    time_nome = random.sample(temas.get(tema, temas["variado"]), k=2)
    print("\n🥊 Um treinador desafiou você para uma batalha!")
    venceu = True
    for nome in time_nome:
        inimigo = buscar_pokemon(nome)
        inimigo["nivel"] = random.randint(10, 24)
        fator = inimigo["nivel"] / max(5, pokemons.get(_normalizar_nome_pokemon(nome), {}).get("nivel", 5))
        inimigo["hp_max"] = max(inimigo.get("hp_max", inimigo.get("hp", 50)), int(inimigo.get("hp", 50) * min(2.2, fator)))
        inimigo["hp"] = inimigo["hp_max"]
        if not batalha(inimigo, permitir_captura=False):
            venceu = False
            break
    if venceu:
        jogador["treinadores_vencidos"] = jogador.get("treinadores_vencidos", 0) + 1
        bonus = 250 + jogador["treinadores_vencidos"] * 25
        jogador["pokedolares"] += bonus
        print(f"Você venceu o treinador e recebeu {bonus} Pokédolares extras!")
    return venceu

def explorar_rota(rota):
    rota = rota.lower().strip()

    # A Ilha dos Lendários só libera encontros após a vitória na Liga.
    if rota in LENDARIOS_ILHA:
        if not jogador.get("historia_concluida", False):
            print("🔒 A Ilha dos Lendários só pode ser explorada depois de concluir a história principal e vencer a Liga Pokémon.")
            return
        nome_lendario, nivel_lendario = LENDARIOS_ILHA[rota]
        inimigo = buscar_pokemon(nome_lendario)
        inimigo["nivel"] = nivel_lendario
        inimigo["hp_max"] = max(inimigo.get("hp_max", 100), nivel_lendario * 8)
        inimigo["hp"] = inimigo["hp_max"]
        print(f"\n✨ Você chegou a {rota.title()} e encontrou {inimigo['nome']} Nv.{nivel_lendario}!")
        batalha(inimigo, permitir_captura=True)
        return

    nomes = POKEMON_ROTAS.get(rota, [])
    if not nomes:
        print("Ainda não há encontros cadastrados para esse local.")
        return
    areas_lendarias_fixas = {"ilha antiga", "palacio do ceu", "caverna ancestral"}
    lendario = None if rota in areas_lendarias_fixas else encontrar_lendario_aleatorio()
    if lendario:
        inimigo = buscar_pokemon(lendario)
        inimigo["nivel"] = 60 if lendario in ("raikou", "entei", "suicune") else 70
        inimigo["hp_max"] = max(inimigo["hp_max"], 350)
        inimigo["hp"] = inimigo["hp_max"]
        print(f"\n✨ Um lendário raro apareceu no mapa: {inimigo['nome']} Nv.{inimigo['nivel']}!")
        batalha(inimigo, permitir_captura=True)
        return
    if random.random() < 0.35:
        tema = "eletrico" if rota == "usina eletrica" else "gelo" if rota == "caverna de gelo" else "fogo" if rota == "montanha anber" else "variado"
        if not batalha_treinador(tema):
            return
    nome = random.choice(nomes)
    if rota == "usina eletrica" and random.random() < 0.10:
        nome, nivel = "zapdos", 60
    elif rota == "caverna de gelo" and random.random() < 0.10:
        nome, nivel = "articuno", 60
    elif rota == "montanha anber" and random.random() < 0.10:
        nome, nivel = "moltres", 60
    elif rota == "ilha antiga":
        nome, nivel = "ho_oh", 80
    elif rota == "palacio do ceu":
        nome, nivel = "lugia", 80
    elif rota == "caverna ancestral":
        nome, nivel = "mewtwo", 80
    else:
        nivel = random.randint(5, 25)
    inimigo = buscar_pokemon(nome)
    inimigo["nivel"] = nivel
    if nivel >= 60:
        inimigo["hp_max"] = max(inimigo["hp_max"], int(nivel * 8))
        inimigo["hp"] = inimigo["hp_max"]
    print(f"\nUm {inimigo['nome']} selvagem apareceu (Nv.{nivel})!")
    batalha(inimigo, permitir_captura=True)

def menu_ss_anne():
    while True:
        print("\n🚢 SS ANNE — EXPEDIÇÕES ESPECIAIS")
        print("1 - Usina elétrica (10% de Zapdos Nv.60)")
        print("2 - Caverna de gelo (10% de Articuno Nv.60)")
        print("3 - Montanha Anber (10% de Moltres Nv.60)")
        print("4 - Ilha antiga (Ho-Oh Nv.80)")
        print("5 - Palácio do céu (Lugia Nv.80)")
        print("6 - Caverna ancestral (Mewtwo Nv.80)")
        print("0 - Voltar a Vermilion")
        op = input("> ").strip()
        locais = {"1": "usina eletrica", "2": "caverna de gelo", "3": "montanha anber", "4": "ilha antiga", "5": "palacio do ceu", "6": "caverna ancestral"}
        if op == "0":
            return
        if op in locais:
            explorar_rota(locais[op])
            input("\nPressione Enter para continuar...")
        else:
            print("Opção inválida.")

# =========================================
# VISITA A LOCAIS
# =========================================

def visitar_local(cidade, local):
    local = local.lower()
    if cidade == "ilha dos lendarios" and not jogador.get("historia_concluida", False):
        print("🔒 A Ilha dos Lendários só pode ser acessada depois de concluir a história principal e vencer a Liga Pokémon.")
        return
    dados = cidades[cidade]
    if local in ("centro pokemon", "casa"):
        centro_pokemon()
    elif local in ("loja", "shopping"):
        loja()
    elif local == "laboratorio do prof aok":
        if not jogador["equipe"]:
            opcoes = ["bulbasaur", "charmander", "squirtle", "eevee"]
            print("Escolha seu inicial:")
            for i, nome in enumerate(opcoes, 1):
                print(f"{i} - {buscar_pokemon(nome)['nome']}")
            try:
                escolhido = opcoes[int(input("> ")) - 1]
            except (ValueError, IndexError):
                print("Escolha inválida.")
                return
            jogador["equipe"] = [normalizar_pokemon(buscar_pokemon(escolhido))]
            jogador["equipe"][0]["habilidade_eevee"] = (jogador["equipe"][0]["nome"] == "Eevee")
            if jogador["equipe"][0]["nome"] not in jogador["pokedex_capturados"]:
                jogador["pokedex_capturados"].append(jogador["equipe"][0]["nome"])
            print(f"Você escolheu {jogador['equipe'][0]['nome']}!")
        else:
            print("Você já escolheu seu Pokémon inicial.")
    elif local == "ginasio":
        desafiar_ginasio()
    elif local in ("rotas", "rota"):
        rotas = dados.get("rotas", [])
        if not rotas:
            print("Não há rotas cadastradas nesta cidade.")
            return
        print("Escolha uma rota/local:")
        for i, nome in enumerate(rotas, 1):
            print(f"{i} - {nome}")
        try:
            rota = rotas[int(input("> ")) - 1].lower()
        except (ValueError, IndexError):
            print("Escolha inválida.")
            return
        if rota == "ss anne":
            menu_ss_anne()
        else:
            explorar_rota(rota)
    elif local == "elites":
        if len(jogador["ginasios"]) < len(ginasios):
            print("Você precisa vencer os 8 ginásios antes de desafiar a Liga!")
            return
        desafiar_elites()
    elif local == "casa do rival":
        print("Você encontrou seu rival! Ele liberou o mapa para você.")
    else:
        print("Você explorou o local, mas não há evento implementado ainda.")

def mostrar_pokedex():
    capturados = jogador.get("pokedex_capturados", [])
    if not capturados:
        print("Sua Pokédex ainda está vazia. Capture Pokémon para registrá-los!")
        return
    print("\n=== POKÉDEX: POKÉMON CAPTURADOS ===")
    for i, nome in enumerate(capturados, 1):
        base = buscar_pokemon(nome)
        print(f"{i}. {nome} | Tipo: {base.get('tipo', 'Normal')}")

def menu_dex():
    while True:
        print("\n====== DEX ======")
        print("1 - Pokédex (capturados)")
        print("2 - Ver equipe")
        print("3 - Abrir inventário")
        print("0 - Voltar")
        op = input("> ").strip()
        if op == "1":
            mostrar_pokedex()
        elif op == "2":
            mostrar_equipe()
        elif op == "3":
            usar_item()
        elif op == "0":
            return
        else:
            print("Opção inválida!")
        input("\nPressione Enter para continuar...")

def menu_cidades():
    cidade = "palet"
    while True:
        limpar()
        print(f"=== JORNADA POKÉMON | Treinador: {jogador['nome']} ===")
        print(f"Cidade atual: {cidade.title()} | Pokédolares: {jogador['pokedolares']}")
        print("1 - Explorar locais da cidade\n2 - Viajar para outra cidade\n3 - Ver equipe")
        print("4 - Dex / Inventário\n5 - Transformar Eevee\n6 - Desafiar ginásio\n7 - Sair")
        op = input("> ").strip()
        if op == "1":
            locais = list(cidades[cidade].keys())
            print("\nLocais disponíveis:")
            for i, local in enumerate(locais, 1):
                print(f"{i} - {local}")
            try:
                local = locais[int(input("> ")) - 1]
            except (ValueError, IndexError):
                print("Local inválido.")
                continue
            visitar_local(cidade, local)
            if len(jogador["ginasios"]) >= len(ginasios) and not jogador.get("historia_concluida", False):
                print("\n🏆 Você venceu todos os ginásios! Agora viaje para 'Rota da Vitória' e vença a Liga Pokémon para concluir a história.")
            input("\nPressione Enter para continuar...")
        elif op == "2":
            nomes = list(cidades.keys())
            for i, nome in enumerate(nomes, 1):
                cadeado = " 🔒 (após zerar o jogo)" if nome == "ilha dos lendarios" and not jogador.get("historia_concluida", False) else ""
                print(f"{i} - {nome.title()}{cadeado}")
            try:
                destino = nomes[int(input("Para qual cidade? > ")) - 1]
                if destino == "ilha dos lendarios" and not jogador.get("historia_concluida", False):
                    print("🔒 A Ilha dos Lendários será liberada após vencer a Liga Pokémon e concluir a história principal.")
                else:
                    cidade = destino
                    if cidade == "ilha dos lendarios":
                        print("\n🏝️ Bem-vindo à Ilha dos Lendários! Cada área abriga um lendário específico.")
            except (ValueError, IndexError):
                print("Cidade inválida.")
        elif op == "3":
            mostrar_equipe()
            input("\nPressione Enter para continuar...")
        elif op == "4":
            menu_dex()
        elif op == "5":
            eevee = next((p for p in jogador["equipe"] if p["nome"] == "Eevee"), None)
            if eevee:
                transformar_eevee(eevee)
            else:
                print("Você não tem um Eevee que possa transformar.")
            input("\nPressione Enter para continuar...")
        elif op == "6":
            desafiar_ginasio()
            input("\nPressione Enter para continuar...")
        elif op == "7":
            print("Obrigado por jogar!")
            break
        else:
            print("Opção inválida.")

def iniciar_jogo():
    limpar()
    criacao_de_personagem()
    for p in jogador["equipe"]:
        normalizar_pokemon(p)
    menu_cidades()

if __name__ == "__main__":
    iniciar_jogo()