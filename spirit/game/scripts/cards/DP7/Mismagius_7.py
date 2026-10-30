"""STUB: effect not implemented — do not guess mechanics.
Mismagius (DP7 #7): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""
from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.dp import (
    dp7_mismagius_7_crash_chant,
    dp7_mismagius_7_horror_chant,
)

card = PokemonCardDef(guid='153b0581-df45-5c60-b6a9-1cbb8f8782f6', key='DP7', name='com.direwolfdigital.cake.data.archetypes.pokemon.Mismagius.Name', display_name='Mismagius', searchable_by=['Mismagius', 'Stage 1', 'Mismagius'], subtypes=['Stage 1'], collector_number=7, set_code='DP7', rarity=Rarities.RareHolo, hp=80, elements=[PokemonTypes.PSYCHIC], stage=PokemonStage.STAGE1, retreat_cost=1, weakness_type=PokemonTypes.DARKNESS, resistance_type=PokemonTypes.COLORLESS, resistance_amount=20, evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Misdreavus.Name', family_id=200, abilities=[Attack(title='Crash Chant', game_text="Choose up to 4 in any combination of Pokémon Tool cards and Technical Machine cards in play (both yours and your opponent's) and discard them. This attack does 20 damage times the number of cards discarded in this way.", cost={}, damage=20, damage_operator='x', effect=dp7_mismagius_7_crash_chant()), Attack(title='Horror Chant', game_text="If your opponent has 4 or more Benched Pokémon, choose 1 of them and return that Pokémon and all cards attached to it to your opponent's hand.", cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 1}, damage=40, effect=dp7_mismagius_7_horror_chant())])
