"""EX13 Holon Phantoms — wired.
"""
from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import flip_bonus
from spirit.game.card_effects.ex import (
    plasma_attach_lightning,
)

card = PokemonCardDef(guid='8b039764-7c23-5f72-afa1-5faa693f43fe', key='EX13', name='com.direwolfdigital.cake.data.archetypes.pokemon.Manectric.Name', display_name='Manectric', searchable_by=['Manectric', 'Stage 1', 'Manectric'], subtypes=['Stage 1'], collector_number=46, set_code='EX13', rarity=Rarities.Uncommon, hp=80, elements=[PokemonTypes.LIGHTNING], stage=PokemonStage.STAGE1, retreat_cost=1, weakness_type=PokemonTypes.FIGHTING, resistance_type=PokemonTypes.METAL, evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Electrike.Name', family_id=309, abilities=[Attack(title='Plasma', game_text='Search your discard pile for a Lightning Energy card and attach it to Manectric.', cost={PokemonTypes.COLORLESS: 1}, damage=20, effect=plasma_attach_lightning()), Attack(title='Quick Blow', game_text='Flip a coin. If heads, this attack does 40 damage plus 20 more damage.', cost={PokemonTypes.LIGHTNING: 1, PokemonTypes.COLORLESS: 2}, damage=40, damage_operator='+', effect=flip_bonus(20))])
