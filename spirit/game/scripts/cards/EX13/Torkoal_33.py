"""EX13 Holon Phantoms — wired.
"""
from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.ex import (
    grind_energy,
)

card = PokemonCardDef(guid='61b6b6f5-032e-516b-9622-75b189a32aa1', key='EX13', name='com.direwolfdigital.cake.data.archetypes.pokemon.Torkoal.Name', display_name='Torkoal', searchable_by=['Torkoal', 'Basic', 'Torkoal'], subtypes=['Basic'], collector_number=33, set_code='EX13', rarity=Rarities.Rare, hp=80, elements=[PokemonTypes.FIRE], stage=PokemonStage.BASIC, retreat_cost=2, weakness_type=PokemonTypes.WATER, family_id=324, abilities=[Attack(title='Grind', game_text='Does 10 damage times the amount of Energy attached to Torkoal.', cost={PokemonTypes.COLORLESS: 1}, damage=10, damage_operator='x', effect=grind_energy(10)), Attack(title='Combustion', cost={PokemonTypes.FIRE: 1, PokemonTypes.COLORLESS: 2}, damage=40)])
