"""STUB: effect not implemented — do not guess mechanics.
Voltorb (DP7 #81): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""
from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.dp import outlet_search
from spirit.game.card_effects.dp import (
    dp7_voltorb_81_bouncing_ball,
)

card = PokemonCardDef(guid='7773956e-27da-58e0-9946-48fddc795f89', key='DP7', name='com.direwolfdigital.cake.data.archetypes.pokemon.Voltorb.Name', display_name='Voltorb', searchable_by=['Voltorb', 'Basic', 'Voltorb'], subtypes=['Basic'], collector_number=81, set_code='DP7', rarity=Rarities.Common, hp=60, elements=[PokemonTypes.LIGHTNING], stage=PokemonStage.BASIC, retreat_cost=1, weakness_type=PokemonTypes.FIGHTING, resistance_type=PokemonTypes.METAL, resistance_amount=20, family_id=100, abilities=[Attack(title='Outlet', game_text='Search your deck for a Lightning Energy card, show it to your opponent, and put it into your hand. Shuffle your deck afterward.', cost={PokemonTypes.COLORLESS: 1}, effect=outlet_search()), Attack(title='Bouncing Ball', game_text='Flip a coin. If tails, Voltorb does 10 damage to itself.', cost={PokemonTypes.LIGHTNING: 1}, damage=20, effect=dp7_voltorb_81_bouncing_ball())])
