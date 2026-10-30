"""STUB: effect not implemented — do not guess mechanics.
Regice ★ (EX12 #90): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""
from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.ex import (
    final_blizzard_bench_all,
    ice_barrier_vs_ex,
)

card = PokemonCardDef(guid='3b19dd80-69cc-503a-8d25-30035854e660', key='EX12', name='com.direwolfdigital.cake.data.archetypes.pokemon.Regice.Name', display_name='Regice ★', searchable_by=['Regice ★', 'Basic', 'Star', 'Regice'], subtypes=['Basic', 'Star'], collector_number=90, set_code='EX12', rarity=Rarities.RareHolo, hp=90, elements=[PokemonTypes.WATER], stage=PokemonStage.BASIC, retreat_cost=3, weakness_type=PokemonTypes.METAL, family_id=378, abilities=[Attack(title='Ice Barrier', game_text="Prevent all effects of an attack, including damage, done to Regice Star by your opponent's Pokémon-ex during your opponent's next turn.", cost={PokemonTypes.WATER: 1}, damage=10, effect=ice_barrier_vs_ex()), Attack(title='Final Blizzard', game_text="If your opponent has only 1 Prize card left and Regice Star is the only Pokémon you have in play, this attack does 30 damage to each of your opponent's Benched Pokémon. (Don't apply Weakness and Resistance for Benched Pokémon.)", cost={PokemonTypes.WATER: 2, PokemonTypes.COLORLESS: 1}, damage=30, effect=final_blizzard_bench_all(30))])
