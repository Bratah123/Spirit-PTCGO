"""EX13 Holon Phantoms — wired.
"""
from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.support_common import draw_attack
from spirit.game.card_effects.ex import (
    dual_aura_weakness_resistance_passive,
)

card = PokemonCardDef(guid='4b8d2917-1fab-5892-97ce-5874cad7a373', key='EX13', name='com.direwolfdigital.cake.data.archetypes.pokemon.Latias.Name', display_name='Latias δ', searchable_by=['Latias δ', 'Basic', 'Latias'], subtypes=['Basic'], collector_number=11, set_code='EX13', rarity=Rarities.RareHolo, hp=70, elements=[PokemonTypes.FIRE], stage=PokemonStage.BASIC, retreat_cost=1, weakness_type=PokemonTypes.COLORLESS, resistance_type=PokemonTypes.PSYCHIC, family_id=380, abilities=[Ability(title='Dual Aura', game_text="As long as you have Latios or Latios ex in play, each player's Evolved Pokémon (excluding Pokémon-ex) can't use any Poké-Bodies.", ability_type=AbilityTypes.POKE_BODY, effect=None, passive=dual_aura_weakness_resistance_passive('Latios')), Attack(title='Spearhead', game_text='Draw a card.', cost={PokemonTypes.COLORLESS: 1}, effect=draw_attack(1)), Attack(title='Dragon Claw', cost={PokemonTypes.FIRE: 1, PokemonTypes.COLORLESS: 2}, damage=40)])
