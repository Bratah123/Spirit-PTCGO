"""DP4 Great Encounters — wired.
"""
from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.ex import may_discard_defender_energy_on_heads
from spirit.game.card_effects.dp import (
    dp4_skarmory_53_steel_wing,
)

card = PokemonCardDef(guid='9940e169-dcb2-5fee-8d23-9a40f437ad97', key='DP4', name='com.direwolfdigital.cake.data.archetypes.pokemon.Skarmory.Name', display_name='Skarmory', searchable_by=['Skarmory', 'Basic', 'Skarmory'], subtypes=['Basic'], collector_number=53, set_code='DP4', rarity=Rarities.Uncommon, hp=70, elements=[PokemonTypes.METAL], stage=PokemonStage.BASIC, retreat_cost=1, weakness_type=PokemonTypes.FIRE, resistance_type=PokemonTypes.PSYCHIC, resistance_amount=20, family_id=227, abilities=[Attack(title='Air Crash', game_text='Flip a coin. If heads, discard an Energy attached to the Defending Pokémon.', cost={PokemonTypes.METAL: 1}, damage=20, effect=may_discard_defender_energy_on_heads()), Attack(title='Steel Wing', game_text="During your opponent's next turn, any damage done to Skarmory by attacks is reduced by 20 (after applying Weakness and Resistance).", cost={PokemonTypes.METAL: 1, PokemonTypes.COLORLESS: 2}, damage=40, effect=dp4_skarmory_53_steel_wing())])
