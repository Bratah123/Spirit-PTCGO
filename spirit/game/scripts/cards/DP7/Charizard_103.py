"""STUB: effect not implemented — do not guess mechanics.
Charizard (DP7 #103): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes

card = PokemonCardDef(
    guid="e99df8b6-08e0-5e0d-a51e-b2cbe059c7e6",
    key="DP7",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Charizard.Name",
    display_name="Charizard",
    searchable_by=["Charizard", "Stage 2", "Charizard"],
    subtypes=["Stage 2"],
    collector_number=103,
    set_code="DP7",
    rarity=Rarities.RareSecret,
    hp=120,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.STAGE2,
    retreat_cost=3,
    weakness_type=PokemonTypes.WATER,
    resistance_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Charmeleon.Name",
    family_id=4,
    abilities=[
        Ability(
            title="Energy Burn",
            game_text="All Energy attached to Charizard are Fire Energy instead of their usual type.",
            ability_type=AbilityTypes.POKE_BODY,
            # STUB: ability effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Fire Spin",
            game_text="Discard 2 Energy attached to Charizard.",
            cost={PokemonTypes.FIRE: 4},
            damage=100,
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)