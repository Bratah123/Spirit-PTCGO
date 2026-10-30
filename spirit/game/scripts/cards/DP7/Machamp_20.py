"""STUB: effect not implemented — do not guess mechanics.
Machamp (DP7 #20): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""
from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.dp import (
    dp7_machamp_20_rage,
    dp7_machamp_20_take_out,
)
from spirit.game.card_effects.attacks_common import flip_damage

card = PokemonCardDef(guid='4c2ca1e0-e07c-5ef5-9200-a766929c71d8', key='DP7', name='com.direwolfdigital.cake.data.archetypes.pokemon.Machamp.Name', display_name='Machamp', searchable_by=['Machamp', 'Stage 2', 'Machamp'], subtypes=['Stage 2'], collector_number=20, set_code='DP7', rarity=Rarities.Rare, hp=130, elements=[PokemonTypes.FIGHTING], stage=PokemonStage.STAGE2, retreat_cost=2, weakness_type=PokemonTypes.PSYCHIC, evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Machoke.Name', family_id=66, abilities=[Attack(title='Take Out', game_text="If the Defending Pokémon isn't an Evolved Pokémon, that Pokémon is Knocked Out instead of damaged by this attack.", cost={PokemonTypes.FIGHTING: 1}, damage=40, effect=dp7_machamp_20_take_out()), Attack(title='Hurricane Punch', game_text='Flip 4 coins. This attack does 30 damage times the number of heads.', cost={PokemonTypes.COLORLESS: 2}, damage=30, damage_operator='x', effect=flip_damage(coins=4, per_heads=30)), Attack(title='Rage', game_text='Does 60 damage plus 10 more damage for each damage counter on Machamp.', cost={PokemonTypes.FIGHTING: 2, PokemonTypes.COLORLESS: 2}, damage=60, damage_operator='+', effect=dp7_machamp_20_rage())])
