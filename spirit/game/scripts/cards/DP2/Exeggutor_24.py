"""DP2 Mysterious Treasures — wired.
"""
from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.dp import (
    nutritional_support_grass,
    string_bomb,
)

card = PokemonCardDef(guid='3c9e7428-90cf-5766-b0c2-c38410363c61', key='DP2', name='com.direwolfdigital.cake.data.archetypes.pokemon.Exeggutor.Name', display_name='Exeggutor', searchable_by=['Exeggutor', 'Stage 1', 'Exeggutor'], subtypes=['Stage 1'], collector_number=24, set_code='DP2', rarity=Rarities.Rare, hp=90, elements=[PokemonTypes.GRASS], stage=PokemonStage.STAGE1, retreat_cost=2, weakness_type=PokemonTypes.FIRE, evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Exeggcute.Name', family_id=102, abilities=[Attack(title='String Bomb', game_text='Flip a coin for each basic Energy card attached to Exeggutor and to the Defending Pokémon. This attack does 30 damage times the number of heads.', cost={PokemonTypes.COLORLESS: 1}, damage=30, damage_operator='x', effect=string_bomb(30)), Attack(title='Nutritional Support', game_text='Search your deck for up to 2 Grass Energy cards and attach them to any of your Pokémon in any way you like. Shuffle your deck afterward.', cost={PokemonTypes.GRASS: 1}, effect=nutritional_support_grass())])
