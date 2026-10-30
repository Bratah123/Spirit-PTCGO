"""DP4 Great Encounters — wired.
"""
from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.dp import (
    dp4_tangela_87_grass_knot,
    dp4_tangela_87_vine_invite,
)

card = PokemonCardDef(guid='ae7a1a9c-6513-58a3-b3b7-f846ab743bbf', key='DP4', name='com.direwolfdigital.cake.data.archetypes.pokemon.Tangela.Name', display_name='Tangela', searchable_by=['Tangela', 'Basic', 'Tangela'], subtypes=['Basic'], collector_number=87, set_code='DP4', rarity=Rarities.Common, hp=70, elements=[PokemonTypes.GRASS], stage=PokemonStage.BASIC, retreat_cost=2, weakness_type=PokemonTypes.FIRE, family_id=114, abilities=[Attack(title='Vine Invite', game_text="Switch 1 of your opponent's Benched Pokémon with 1 of the Defending Pokémon.", cost={PokemonTypes.COLORLESS: 1}, effect=dp4_tangela_87_vine_invite()), Attack(title='Grass Knot', game_text="Does 20 damage plus 10 more damage for each Colorless Energy in the Defending Pokémon's Retreat Cost (after applying effects to the the Retreat Cost).", cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 1}, damage=20, damage_operator='+', effect=dp4_tangela_87_grass_knot())])
