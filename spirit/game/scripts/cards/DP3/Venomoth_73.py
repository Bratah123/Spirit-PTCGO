"""STUB: effect not implemented — do not guess mechanics.
Venomoth (DP3 #73): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes

card = PokemonCardDef(
    guid="04df4de4-24b0-5f84-b34a-3fb272329334",
    key="DP3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Venomoth.Name",
    display_name="Venomoth",
    searchable_by=["Venomoth", "Stage 1", "Venomoth"],
    subtypes=["Stage 1"],
    collector_number=73,
    set_code="DP3",
    rarity=Rarities.Uncommon,
    hp=80,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=20,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Venonat.Name",
    family_id=48,
    abilities=[
        Ability(
            title="Dangerous Scales",
            game_text="If Venomoth is your Active Pok\u00e9mon and is damaged by an opponent's attack (even if Venomoth is Knocked Out), the Attacking Pok\u00e9mon is now Asleep and Poisoned.",
            ability_type=AbilityTypes.POKE_BODY,
            # STUB: ability effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Disturbance Dive",
            game_text="Prevent all effects of an attack, excluding damage, done to Venomoth during your opponent's next turn.",
            cost={PokemonTypes.GRASS: 2},
            damage=50,
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)