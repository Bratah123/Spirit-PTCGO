"""DP2 Mysterious Treasures — wired.
"""
from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.attributes import SpecialConditions
from spirit.game.card_effects.attacks_common import condition_attack
from spirit.game.card_effects.dp import (
    concerto_per_kricket,
)

card = PokemonCardDef(guid='35e07c98-96fc-5f2a-9885-f30b202f7240', key='DP2', name='com.direwolfdigital.cake.data.archetypes.pokemon.Kricketune.Name', display_name='Kricketune', searchable_by=['Kricketune', 'Stage 1', 'Kricketune'], subtypes=['Stage 1'], collector_number=27, set_code='DP2', rarity=Rarities.Rare, hp=80, elements=[PokemonTypes.GRASS], stage=PokemonStage.STAGE1, retreat_cost=2, weakness_type=PokemonTypes.FIRE, evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Kricketot.Name', family_id=401, abilities=[Attack(title='Sore Performance', game_text='The Defending Pokémon is now Asleep.', cost={PokemonTypes.COLORLESS: 2}, damage=20, effect=condition_attack(SpecialConditions.ASLEEP)), Attack(title='Concerto', game_text='Does 40 damage plus 10 more damage for each Kricketot and each Kricketune you have in play.', cost={PokemonTypes.GRASS: 2}, damage=40, damage_operator='+', effect=concerto_per_kricket(40, 10))])
