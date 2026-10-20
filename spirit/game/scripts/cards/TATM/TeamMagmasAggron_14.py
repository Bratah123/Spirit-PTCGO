"""STUB: effect not implemented — do not guess mechanics.
Team Magma's Aggron (TATM #14): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="9cc137d2-308e-5ab1-9eec-0944c6a66bd8",
    key="TATM",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.TeamMagmasAggron.Name",
    display_name="Team Magma's Aggron",
    searchable_by=["Team Magma's Aggron", "Stage 2", "TeamMagmasAggron"],
    subtypes=["Stage 2"],
    collector_number=14,
    set_code="TATM",
    rarity=Rarities.RareHolo,
    hp=140,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE2,
    retreat_cost=4,
    weakness_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.TeamMagmasLairon.Name",
    family_id=304,
    abilities=[
        Attack(
            title="Rock Stomp",
            game_text="Discard as many Fighting Energy attached to your Pok\u00e9mon as you like. This attack does 40 damage times the amount of Fighting Energy you discarded.",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 1},
            damage=40,
            damage_operator="x",
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Boulder Storm",
            game_text="This attack does 20 damage to each of your opponent's Benched Pok\u00e9mon that has any damage counters on it. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.FIGHTING: 3, PokemonTypes.COLORLESS: 1},
            damage=120,
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)