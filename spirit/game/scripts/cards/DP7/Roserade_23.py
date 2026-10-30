"""STUB: effect not implemented — do not guess mechanics.
Roserade (DP7 #23): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""
from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented, Activations
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.dp import (
    dp7_roserade_23_deep_poison,
    dp7_roserade_23_hidden_poison,
)
from spirit.game.card_effects.attacks_common import snipe_attack

card = PokemonCardDef(guid='d35c0807-299c-5001-9a7d-dde43fcf490e', key='DP7', name='com.direwolfdigital.cake.data.archetypes.pokemon.Roserade.Name', display_name='Roserade', searchable_by=['Roserade', 'Stage 1', 'Roserade'], subtypes=['Stage 1'], collector_number=23, set_code='DP7', rarity=Rarities.Rare, hp=90, elements=[PokemonTypes.PSYCHIC], stage=PokemonStage.STAGE1, retreat_cost=1, weakness_type=PokemonTypes.FIRE, evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Roselia.Name', family_id=315, abilities=[Ability(title='Hidden Poison', game_text="If Roserade is your Active Pokémon and is damaged by an opponent's attack (even if Roserade is Knocked Out), the Defending Pokémon is now Poisoned.", ability_type=AbilityTypes.POKE_BODY, effect=dp7_roserade_23_hidden_poison(), activation=Activations.ONCE_PER_TURN), Attack(title='Bowed Whip', game_text="Choose 1 of your opponent's Pokémon. This attack does 30 damage to that Pokémon. (Don't apply Weakness and Resistance for Benched Pokémon.) Flip a coin. If heads, discard an Energy card attached to that Pokémon.", cost={PokemonTypes.COLORLESS: 2}, effect=snipe_attack(30, pool='bench')), Attack(title='Deep Poison', game_text='If the Defending Pokémon is Poisoned, this attack does 50 damage plus 30 more damage.', cost={PokemonTypes.PSYCHIC: 2, PokemonTypes.COLORLESS: 1}, damage=50, damage_operator='+', effect=dp7_roserade_23_deep_poison())])
