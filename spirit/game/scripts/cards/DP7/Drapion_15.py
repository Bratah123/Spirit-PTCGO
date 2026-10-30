"""STUB: effect not implemented — do not guess mechanics.
Drapion (DP7 #15): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""
from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.dp import (
    dp7_drapion_15_derail,
    dp7_drapion_15_scorpion_grapple,
)
from spirit.game.card_effects.attacks_common import flip_damage

card = PokemonCardDef(guid='c232469c-ac16-5d7d-9ba3-185da93760fa', key='DP7', name='com.direwolfdigital.cake.data.archetypes.pokemon.Drapion.Name', display_name='Drapion', searchable_by=['Drapion', 'Stage 1', 'Drapion'], subtypes=['Stage 1'], collector_number=15, set_code='DP7', rarity=Rarities.Rare, hp=110, elements=[PokemonTypes.DARKNESS], stage=PokemonStage.STAGE1, retreat_cost=3, weakness_type=PokemonTypes.PSYCHIC, evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Skorupi.Name', family_id=451, abilities=[Attack(title='Scorpion Grapple', game_text="Flip a coin. If heads, the Defending Pokémon is now Paralyzed. If tails, the Defending Pokémon can't retreat during your opponent's next turn.", cost={}, damage=10, effect=dp7_drapion_15_scorpion_grapple()), Attack(title='Cross Poison', game_text='Flip 4 coins. This attack does 20 damage times the number of heads. If 2 or more of them are heads, the Defending Pokémon is now Poisoned.', cost={PokemonTypes.COLORLESS: 2}, damage=20, damage_operator='x', effect=flip_damage(coins=4, per_heads=20)), Attack(title='Derail', game_text='Discard all Special Energy cards attached to the Defending Pokémon.', cost={PokemonTypes.DARKNESS: 2, PokemonTypes.COLORLESS: 1}, damage=60, effect=dp7_drapion_15_derail())])
