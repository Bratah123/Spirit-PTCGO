"""STUB: effect not implemented — do not guess mechanics.
Dedenne (TwentiethAnn #RC10): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="5f77d765-f855-5fb3-aa4d-fa64d153b253",
    key="TwentiethAnn",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Dedenne.Name",
    display_name="Dedenne",
    searchable_by=["Dedenne", "Basic", "Dedenne"],
    subtypes=["Basic"],
    collector_number=93,
    set_code="TwentiethAnn",
    rarity=Rarities.Uncommon,
    hp=60,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    resistance_type=PokemonTypes.METAL,
    resistance_amount=20,
    family_id=702,
    abilities=[
        Attack(
            title="Rest",
            game_text="Heal 30 damage from this Pok\u00e9mon. This Pok\u00e9mon is now Asleep.",
            cost={PokemonTypes.COLORLESS: 1},
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Pachi",
            game_text="Flip a coin. If heads, this attack does 20 more damage.",
            cost={PokemonTypes.LIGHTNING: 1},
            damage=10,
            damage_operator="+",
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)