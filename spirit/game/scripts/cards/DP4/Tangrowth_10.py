"""DP4 Great Encounters — wired.
"""
from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.dp import (
    dp4_tangrowth_10_power_whip,
    heal_attack,
)

card = PokemonCardDef(guid='cf754676-6887-54cb-8d49-34a423ce9354', key='DP4', name='com.direwolfdigital.cake.data.archetypes.pokemon.Tangrowth.Name', display_name='Tangrowth', searchable_by=['Tangrowth', 'Stage 1', 'Tangrowth'], subtypes=['Stage 1'], collector_number=10, set_code='DP4', rarity=Rarities.RareHolo, hp=110, elements=[PokemonTypes.GRASS], stage=PokemonStage.STAGE1, retreat_cost=2, weakness_type=PokemonTypes.FIRE, resistance_type=PokemonTypes.WATER, resistance_amount=20, evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Tangela.Name', family_id=114, abilities=[Attack(title='Power Whip', game_text="Choose 1 of your opponent's Pokémon. This attack does 10 damage for each basic Energy card attached to Tangrowth to that Pokémon. (Don't apply Weakness and Resistance for Benched Pokémon.)", cost={PokemonTypes.GRASS: 1}, effect=dp4_tangrowth_10_power_whip()), Attack(title='Stick and Absorb', game_text="Remove 3 damage counters from Tangrowth. The Defending Pokémon can't retreat during your opponent's next turn.", cost={PokemonTypes.GRASS: 2, PokemonTypes.COLORLESS: 2}, damage=60, effect=heal_attack(30))])
