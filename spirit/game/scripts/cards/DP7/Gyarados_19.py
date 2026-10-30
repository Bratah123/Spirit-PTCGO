"""STUB: effect not implemented — do not guess mechanics.
Gyarados (DP7 #19): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""
from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.dp import (
    dp7_gyarados_19_dragon_beat,
    dp7_gyarados_19_tail_revenge,
    dp7_gyarados_19_wreak_havoc,
)

card = PokemonCardDef(guid='87d1997a-eb4a-5332-8f75-d10f8d548394', key='DP7', name='com.direwolfdigital.cake.data.archetypes.pokemon.Gyarados.Name', display_name='Gyarados', searchable_by=['Gyarados', 'Stage 1', 'Gyarados'], subtypes=['Stage 1'], collector_number=19, set_code='DP7', rarity=Rarities.Rare, hp=130, elements=[PokemonTypes.WATER], stage=PokemonStage.STAGE1, retreat_cost=3, weakness_type=PokemonTypes.LIGHTNING, resistance_type=PokemonTypes.FIGHTING, resistance_amount=20, evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Magikarp.Name', family_id=129, abilities=[Attack(title='Tail Revenge', game_text='Does 30 damage times the number of Magikarp in your discard pile.', cost={}, damage=30, damage_operator='x', effect=dp7_gyarados_19_tail_revenge()), Attack(title='Wreak Havoc', game_text="Flip a coin until you get tails. For each heads, discard the top card from your opponent's deck.", cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 1}, damage=40, effect=dp7_gyarados_19_wreak_havoc()), Attack(title='Dragon Beat', game_text="Flip a coin. If heads, discard an Energy card from each of your opponent's Pokémon.", cost={PokemonTypes.WATER: 2, PokemonTypes.COLORLESS: 3}, damage=100, effect=dp7_gyarados_19_dragon_beat())])
