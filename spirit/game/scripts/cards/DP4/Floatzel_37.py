"""DP4 Great Encounters — wired.
"""
from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.dp import (
    dp4_floatzel_37_agility,
    dp4_floatzel_37_aqua_jet,
)

card = PokemonCardDef(guid='faec3404-d526-586d-acfe-d56441ba6bd2', key='DP4', name='com.direwolfdigital.cake.data.archetypes.pokemon.Floatzel.Name', display_name='Floatzel', searchable_by=['Floatzel', 'Stage 1', 'Floatzel'], subtypes=['Stage 1'], collector_number=37, set_code='DP4', rarity=Rarities.Uncommon, hp=80, elements=[PokemonTypes.WATER], stage=PokemonStage.STAGE1, retreat_cost=1, weakness_type=PokemonTypes.LIGHTNING, evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Buizel.Name', family_id=418, abilities=[Attack(title='Agility', game_text="Flip a coin. If heads, prevent all effects of an attack, including damage, done to Floatzel during your opponent's next turn.", cost={PokemonTypes.COLORLESS: 2}, damage=20, effect=dp4_floatzel_37_agility()), Attack(title='Aqua Jet', game_text="Flip a coin. If heads, this attack does 10 damage to 1 of your opponent's Benched Pokémon. (Don't apply Weakness and Resistance for Benched Pokémon.)", cost={PokemonTypes.WATER: 2, PokemonTypes.COLORLESS: 1}, damage=60, effect=dp4_floatzel_37_aqua_jet())])
