"""EX12 Legend Maker — Lileep.
"""
from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.attributes import SpecialConditions
from spirit.game.card_effects.attacks_common import condition_attack
from spirit.game.card_effects.ex import (
    tender_tentacles_heal,
)

card = PokemonCardDef(guid='f5796f15-c54e-5c0e-bdb8-976dd4864bbc', key='EX12', name='com.direwolfdigital.cake.data.archetypes.pokemon.Lileep.Name', display_name='Lileep', searchable_by=['Lileep', 'Stage 1', 'Lileep'], subtypes=['Stage 1'], collector_number=56, set_code='EX12', rarity=Rarities.Common, hp=80, elements=[PokemonTypes.GRASS], stage=PokemonStage.STAGE1, retreat_cost=2, weakness_type=PokemonTypes.FIRE, evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.RootFossil.Name', family_id=345, abilities=[Attack(title='Tender Tentacles', game_text='If Lileep has any React Energy cards attached to it, remove 2 damage counters from Lileep.', cost={PokemonTypes.COLORLESS: 1}, damage=20, effect=tender_tentacles_heal(2)), Attack(title='Confuse Ray', game_text='The Defending Pokémon is now Confused.', cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 1}, damage=20, effect=condition_attack(SpecialConditions.CONFUSED))])
