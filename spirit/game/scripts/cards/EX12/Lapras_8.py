"""STUB: effect not implemented — do not guess mechanics.
Lapras (EX12 #8): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""
from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.ex import (
    support_navigation_on_bench,
)

card = PokemonCardDef(guid='5bd2e035-4a66-5caa-a61d-209ba46b2619', key='EX12', name='com.direwolfdigital.cake.data.archetypes.pokemon.Lapras.Name', display_name='Lapras', searchable_by=['Lapras', 'Basic', 'Lapras'], subtypes=['Basic'], collector_number=8, set_code='EX12', rarity=Rarities.RareHolo, hp=80, elements=[PokemonTypes.WATER], stage=PokemonStage.BASIC, retreat_cost=2, weakness_type=PokemonTypes.LIGHTNING, family_id=131, abilities=[Ability(title='Support Navigation', game_text='Once during your turn, when you put Lapras onto your Bench from your hand, you may search your deck for a Supporter card, show it to your opponent, and put it into your hand. Shuffle your deck afterward.', ability_type=AbilityTypes.POKE_POWER, effect=support_navigation_on_bench(), trigger=Triggers.ON_PLAY), Attack(title='Surf', cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 1}, damage=30)])
