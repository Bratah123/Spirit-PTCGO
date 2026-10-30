"""EX13 Holon Phantoms — wired.
"""
from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.attacks_common import flip_bonus
from spirit.game.card_effects.ex import (
    aqua_lift_passive,
)

card = PokemonCardDef(guid='482ca579-8b33-56fe-8957-6e4a66edcf0d', key='EX13', name='com.direwolfdigital.cake.data.archetypes.pokemon.Relicanth.Name', display_name='Relicanth', searchable_by=['Relicanth', 'Basic', 'Relicanth'], subtypes=['Basic'], collector_number=30, set_code='EX13', rarity=Rarities.Rare, hp=70, elements=[PokemonTypes.WATER], stage=PokemonStage.BASIC, retreat_cost=1, weakness_type=PokemonTypes.LIGHTNING, family_id=369, abilities=[Ability(title='Aqua Lift', game_text='If Relicanth has any Water Energy attached to it, the Retreat Cost for Relicanth is 0.', ability_type=AbilityTypes.POKE_BODY, effect=None, passive=aqua_lift_passive()), Attack(title='Knock Away', game_text='Flip a coin. If heads, this attack does 20 damage plus 10 more damage.', cost={PokemonTypes.COLORLESS: 2}, damage=20, damage_operator='+', effect=flip_bonus(10))])
