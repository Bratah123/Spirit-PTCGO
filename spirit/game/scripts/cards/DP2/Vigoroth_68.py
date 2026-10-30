"""DP2 Mysterious Treasures — wired.
"""
from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.dp import (
    wakeup_punch,
)
from spirit.game.card_effects.attacks_common import flip_damage

card = PokemonCardDef(guid='0e0e24d7-3e3c-56aa-8483-f8b40944d6a5', key='DP2', name='com.direwolfdigital.cake.data.archetypes.pokemon.Vigoroth.Name', display_name='Vigoroth', searchable_by=['Vigoroth', 'Stage 1', 'Vigoroth'], subtypes=['Stage 1'], collector_number=68, set_code='DP2', rarity=Rarities.Uncommon, hp=80, elements=[PokemonTypes.COLORLESS], stage=PokemonStage.STAGE1, retreat_cost=1, weakness_type=PokemonTypes.FIGHTING, evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Slakoth.Name', family_id=287, abilities=[Attack(title='Wake-up Punch', game_text="If Vigoroth evolved from Slakoth during this turn and Slakoth was Asleep, this attack's base damage is 60 instead of 10.", cost={PokemonTypes.COLORLESS: 1}, damage=10, effect=wakeup_punch(10, 50)), Attack(title='Fury Swipes', game_text='Flip 3 coins. This attack does 30 damage times the number of heads.', cost={PokemonTypes.COLORLESS: 3}, damage=30, damage_operator='x', effect=flip_damage(3, per_heads=30))])
