"""DP3 Secret Wonders — wired.
"""
from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.dp import (
    dp3_breloom_45_drain_punch,
    dp3_breloom_45_homing_uppercut,
)

card = PokemonCardDef(guid='1d57a7f9-40ca-5d89-9d7e-421df5d3c5d8', key='DP3', name='com.direwolfdigital.cake.data.archetypes.pokemon.Breloom.Name', display_name='Breloom', searchable_by=['Breloom', 'Stage 1', 'Breloom'], subtypes=['Stage 1'], collector_number=45, set_code='DP3', rarity=Rarities.Uncommon, hp=100, elements=[PokemonTypes.GRASS], stage=PokemonStage.STAGE1, retreat_cost=2, weakness_type=PokemonTypes.FIRE, evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Shroomish.Name', family_id=285, abilities=[Attack(title='Drain Punch', game_text='Remove from Breloom a number of damage counters equal to the amount of Energy attached to the Defending Pokémon.', cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 1}, damage=40, effect=dp3_breloom_45_drain_punch()), Attack(title='Homing Uppercut', game_text="If the Defending Pokémon's Retreat Cost is 0, this attack does 60 damage plus 60 more damage.", cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 2}, damage=60, damage_operator='+', effect=dp3_breloom_45_homing_uppercut())])
