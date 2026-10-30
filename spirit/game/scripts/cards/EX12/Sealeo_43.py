"""STUB: effect not implemented — do not guess mechanics.
Sealeo (EX12 #43): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""
from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Activations
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.ex import (
    power_circulation,
)

card = PokemonCardDef(guid='048b8810-5ef5-55a3-937d-b0d0a13b7be3', key='EX12', name='com.direwolfdigital.cake.data.archetypes.pokemon.Sealeo.Name', display_name='Sealeo', searchable_by=['Sealeo', 'Stage 1', 'Sealeo'], subtypes=['Stage 1'], collector_number=43, set_code='EX12', rarity=Rarities.Uncommon, hp=70, elements=[PokemonTypes.WATER], stage=PokemonStage.STAGE1, retreat_cost=1, weakness_type=PokemonTypes.METAL, evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Spheal.Name', family_id=363, abilities=[Ability(title='Power Circulation', game_text="Once during your turn (before your attack), you may search your discard pile for a basic Energy card, show it to your opponent, and put it on top of your deck. If you do, put 1 damage counter on Sealeo. This power can't be used if Sealeo is affected by a Special Condition.", ability_type=AbilityTypes.POKE_POWER, effect=power_circulation(), activation=Activations.ONCE_PER_TURN), Attack(title='Lunge Out', cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 1}, damage=30)])
