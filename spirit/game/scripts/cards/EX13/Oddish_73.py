"""EX13 Holon Phantoms — wired.
"""
from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.ex import (
    blot_heal,
)

card = PokemonCardDef(guid='0576fe51-e38d-5e83-b7ae-376e34c1d9e5', key='EX13', name='com.direwolfdigital.cake.data.archetypes.pokemon.Oddish.Name', display_name='Oddish δ', searchable_by=['Oddish δ', 'Basic', 'Oddish'], subtypes=['Basic'], collector_number=73, set_code='EX13', rarity=Rarities.Common, hp=40, elements=[PokemonTypes.WATER], stage=PokemonStage.BASIC, retreat_cost=1, weakness_type=PokemonTypes.FIRE, family_id=43, abilities=[Attack(title='Tackle', cost={PokemonTypes.COLORLESS: 1}, damage=10), Attack(title='Blot', game_text='Remove 2 damage counters from Oddish.', cost={PokemonTypes.WATER: 1}, damage=10, effect=blot_heal(2))])
