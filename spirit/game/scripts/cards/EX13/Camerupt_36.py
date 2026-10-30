"""EX13 Holon Phantoms — wired.
"""
from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import spread_damage
from spirit.game.card_effects.ex import (
    take_down_recoil,
)

card = PokemonCardDef(guid='aa5387bd-4d2d-5173-a484-3264e478ba1e', key='EX13', name='com.direwolfdigital.cake.data.archetypes.pokemon.Camerupt.Name', display_name='Camerupt', searchable_by=['Camerupt', 'Stage 1', 'Camerupt'], subtypes=['Stage 1'], collector_number=36, set_code='EX13', rarity=Rarities.Uncommon, hp=90, elements=[PokemonTypes.FIRE], stage=PokemonStage.STAGE1, retreat_cost=2, weakness_type=PokemonTypes.WATER, evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Numel.Name', family_id=322, abilities=[Attack(title='Magnitude', game_text="Does 10 damage to each Benched Pokémon (both yours and your opponent's). (Don't apply Weakness and Resistance for Benched Pokémon.)", cost={PokemonTypes.COLORLESS: 2}, damage=20, effect=spread_damage(10, side='both', also_base=True)), Attack(title='Take Down', game_text='Camerupt does 10 damage to itself.', cost={PokemonTypes.FIRE: 1, PokemonTypes.COLORLESS: 2}, damage=60, effect=take_down_recoil(10))])
