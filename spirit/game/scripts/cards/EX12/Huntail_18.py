"""STUB: effect not implemented — do not guess mechanics.
Huntail (EX12 #18): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""
from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Activations
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.ex import extra_vs_ex
from spirit.game.card_effects.ex import (
    reactive_generator,
)

card = PokemonCardDef(guid='3ef268be-f2ae-5d0d-a1a2-95776d616c52', key='EX12', name='com.direwolfdigital.cake.data.archetypes.pokemon.Huntail.Name', display_name='Huntail', searchable_by=['Huntail', 'Stage 1', 'Huntail'], subtypes=['Stage 1'], collector_number=18, set_code='EX12', rarity=Rarities.Rare, hp=80, elements=[PokemonTypes.WATER], stage=PokemonStage.STAGE1, retreat_cost=1, weakness_type=PokemonTypes.LIGHTNING, evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Clamperl.Name', family_id=366, abilities=[Ability(title='Reactive Generator', game_text="Once during your turn (before your attack), if Huntail has no React Energy cards attached to it, you may search your deck for a React Energy card and attach it to Huntail. Shuffle your deck afterward. This power can't be used if Huntail is affected by a Special Condition.", ability_type=AbilityTypes.POKE_POWER, effect=reactive_generator(), activation=Activations.ONCE_PER_TURN), Attack(title='Bite Off', game_text='If the Defending Pokémon is Pokémon-ex, this attack does 40 damage plus 30 more damage.', cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 2}, damage=40, damage_operator='+', effect=extra_vs_ex(40, 30))])
