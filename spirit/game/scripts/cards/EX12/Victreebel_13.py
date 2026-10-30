"""STUB: effect not implemented — do not guess mechanics.
Victreebel (EX12 #13): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""
from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Activations
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.ex import sleep_poison_sure
from spirit.game.card_effects.ex import (
    nectar_pod_switch_stage2,
    sharp_leaf,
)

card = PokemonCardDef(guid='9108fb3f-c0f0-5ecb-837e-a240e256feda', key='EX12', name='com.direwolfdigital.cake.data.archetypes.pokemon.Victreebel.Name', display_name='Victreebel', searchable_by=['Victreebel', 'Stage 2', 'Victreebel'], subtypes=['Stage 2'], collector_number=13, set_code='EX12', rarity=Rarities.RareHolo, hp=100, elements=[PokemonTypes.GRASS], stage=PokemonStage.STAGE2, retreat_cost=2, weakness_type=PokemonTypes.FIRE, evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Weepinbell.Name', family_id=69, abilities=[Ability(title='Nectar Pod', game_text="Once during your turn (before your attack), you may switch 1 of your opponent's Benched Stage 2 Evolved Pokémon with 1 of the Defending Pokémon. Your opponent chooses the Defending Pokémon to switch. This power can't be used if Victreebel is affected by a Special Condition.", ability_type=AbilityTypes.POKE_POWER, effect=nectar_pod_switch_stage2(), activation=Activations.ONCE_PER_TURN), Attack(title='Sleep Poison', game_text='The Defending Pokémon is now Asleep and Poisoned.', cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 1}, damage=10, effect=sleep_poison_sure()), Attack(title='Sharp Leaf', game_text='Flip a coin. If heads, this attack does 40 damage plus 30 more damage.', cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 2}, damage=40, damage_operator='+', effect=sharp_leaf(40, 30))])
