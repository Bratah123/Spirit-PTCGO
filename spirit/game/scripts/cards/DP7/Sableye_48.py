"""STUB: effect not implemented — do not guess mechanics.
Sableye (DP7 #48): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""
from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented, Activations
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.dp import (
    dp7_sableye_48_impersonate,
    dp7_sableye_48_overconfident,
    dp7_sableye_48_overeager_passive,
)

card = PokemonCardDef(guid='ba84cedb-e64a-5f04-98e7-5b96bd6484f7', key='DP7', name='com.direwolfdigital.cake.data.archetypes.pokemon.Sableye.Name', display_name='Sableye', searchable_by=['Sableye', 'Basic', 'Sableye'], subtypes=['Basic'], collector_number=48, set_code='DP7', rarity=Rarities.Uncommon, hp=60, elements=[PokemonTypes.DARKNESS], stage=PokemonStage.BASIC, retreat_cost=1, resistance_type=PokemonTypes.COLORLESS, resistance_amount=20, family_id=302, abilities=[Ability(title='Overeager', game_text="If Sableye is your Active Pokémon at the beginning of the game, you go first. (If each player's Active Pokémon has the Overeager Poké-Body, this power does nothing.)", ability_type=AbilityTypes.POKE_BODY, passive=dp7_sableye_48_overeager_passive(), activation=Activations.ONCE_PER_TURN), Attack(title='Impersonate', game_text='Search your deck for a Supporter card and discard it. Shuffle your deck afterward. Then, use the effect of that card as the effect of this attack.', cost={}, effect=dp7_sableye_48_impersonate()), Attack(title='Overconfident', game_text="If the Defending Pokémon has fewer remaining HP than Sableye, this attack's base damage is 40.", cost={PokemonTypes.DARKNESS: 1}, damage=10, effect=dp7_sableye_48_overconfident())])
