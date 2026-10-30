"""DP4 Great Encounters — wired.
"""
from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.dp import (
    dp4_treecko_90_energy_ball,
    heal_attack,
)

card = PokemonCardDef(guid='8eb16a66-f686-51a7-8cb5-64668cc8439e', key='DP4', name='com.direwolfdigital.cake.data.archetypes.pokemon.Treecko.Name', display_name='Treecko', searchable_by=['Treecko', 'Basic', 'Treecko'], subtypes=['Basic'], collector_number=90, set_code='DP4', rarity=Rarities.Common, hp=50, elements=[PokemonTypes.GRASS], stage=PokemonStage.BASIC, retreat_cost=1, weakness_type=PokemonTypes.FIRE, resistance_type=PokemonTypes.WATER, resistance_amount=20, family_id=252, abilities=[Attack(title='Energy Ball', game_text="Does 10 damage plus 10 more damage for each Energy attached to Treecko but not used to pay for this attack's Energy cost. You can't add more than 20 damage in this way.", cost={PokemonTypes.COLORLESS: 1}, damage=10, damage_operator='+', effect=dp4_treecko_90_energy_ball()), Attack(title='Absorb', game_text='Remove 1 damage counter from Treecko.', cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 1}, damage=20, effect=heal_attack(10))])
