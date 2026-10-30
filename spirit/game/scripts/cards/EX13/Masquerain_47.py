"""EX13 Holon Phantoms — wired.
"""
from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import flip_bonus
from spirit.game.card_effects.ex import (
    sweet_scent_heal,
)

card = PokemonCardDef(guid='659646bf-8aa7-5337-994a-919fc1869a9f', key='EX13', name='com.direwolfdigital.cake.data.archetypes.pokemon.Masquerain.Name', display_name='Masquerain', searchable_by=['Masquerain', 'Stage 1', 'Masquerain'], subtypes=['Stage 1'], collector_number=47, set_code='EX13', rarity=Rarities.Uncommon, hp=70, elements=[PokemonTypes.GRASS], stage=PokemonStage.STAGE1, retreat_cost=0, weakness_type=PokemonTypes.FIRE, evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Surskit.Name', family_id=283, abilities=[Attack(title='Sweet Scent', game_text='Remove 2 damage counters from 1 of your Pokémon.', cost={PokemonTypes.COLORLESS: 1}, effect=sweet_scent_heal(2)), Attack(title='Quick Attack', game_text='Flip a coin. If heads, this attack does 30 damage plus 10 more damage.', cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 1}, damage=30, damage_operator='+', effect=flip_bonus(10))])
