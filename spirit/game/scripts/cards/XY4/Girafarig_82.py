"""STUB: effect not implemented — do not guess mechanics.
Girafarig (XY4 #82): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="48da419f-3215-5cc2-a2e2-65537d72ce96",
    key="XY4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Girafarig.Name",
    display_name="Girafarig",
    searchable_by=["Girafarig", "Basic", "Girafarig"],
    subtypes=["Basic"],
    collector_number=82,
    set_code="XY4",
    rarity=Rarities.Uncommon,
    hp=90,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=203,
    abilities=[
        Attack(
            title="Tackle",
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
        ),
        Attack(
            title="Psybite",
            game_text="If this Pok\u00e9mon has any Psychic Energy attached to it, this attack does 30 more damage.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=50,
            damage_operator="+",
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)