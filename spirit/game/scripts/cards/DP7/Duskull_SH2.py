"""STUB: effect not implemented — do not guess mechanics.
Duskull (DP7 #SH2): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""
from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.dp import (
    dp7_duskull_sh2_counting_song,
    dp7_duskull_sh2_night_bind,
)

card = PokemonCardDef(guid='35944af1-e430-5830-91b9-0032529a6193', key='DP7', name='com.direwolfdigital.cake.data.archetypes.pokemon.Duskull.Name', display_name='Duskull', searchable_by=['Duskull', 'Basic', 'Duskull'], subtypes=['Basic'], collector_number=105, set_code='DP7', rarity=Rarities.Rare, hp=60, elements=[PokemonTypes.PSYCHIC], stage=PokemonStage.BASIC, retreat_cost=1, weakness_type=PokemonTypes.DARKNESS, resistance_type=PokemonTypes.COLORLESS, resistance_amount=20, family_id=355, abilities=[Attack(title='Counting Song', game_text='Put up to 3 damage counters on Duskull. Then, put that many damage counters on the Defending Pokémon.', cost={}, effect=dp7_duskull_sh2_counting_song()), Attack(title='Ram', cost={PokemonTypes.PSYCHIC: 1}, damage=10), Attack(title='Night Bind', game_text="Flip a coin. If heads, your opponent can't attach any Energy cards from his or her hand to the Active Pokémon during his or her next turn.", cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 1}, damage=20, effect=dp7_duskull_sh2_night_bind())])
