"""STUB: effect not implemented — do not guess mechanics.
Raichu (DP7 #8): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""
from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.dp import (
    cant_attack_next_turn,
    dp7_raichu_8_burst_ball,
    dp7_raichu_8_split_ball,
)

card = PokemonCardDef(guid='d6621965-2d52-51dd-936e-8deffbbf555e', key='DP7', name='com.direwolfdigital.cake.data.archetypes.pokemon.Raichu.Name', display_name='Raichu', searchable_by=['Raichu', 'Stage 1', 'Raichu'], subtypes=['Stage 1'], collector_number=8, set_code='DP7', rarity=Rarities.RareHolo, hp=90, elements=[PokemonTypes.LIGHTNING], stage=PokemonStage.STAGE1, retreat_cost=0, weakness_type=PokemonTypes.FIGHTING, resistance_type=PokemonTypes.METAL, resistance_amount=20, evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Pikachu.Name', family_id=25, abilities=[Attack(title='Slice', game_text="Raichu can't use Slice during your next turn.", cost={}, damage=30, effect=cant_attack_next_turn()), Attack(title='Split Ball', game_text='Move an Energy card attached to Raichu to 1 of your Benched Pokémon.', cost={PokemonTypes.COLORLESS: 3}, damage=50, effect=dp7_raichu_8_split_ball()), Attack(title='Burst Ball', game_text='Discard 3 Energy attached to any of your Pokémon in any way you like.', cost={PokemonTypes.LIGHTNING: 2, PokemonTypes.COLORLESS: 1}, damage=100, effect=dp7_raichu_8_burst_ball())])
