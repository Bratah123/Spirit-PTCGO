"""STUB: effect not implemented — do not guess mechanics.
Swellow (XY1 #103): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="e46b37c3-8309-518d-bf51-d2c9859b28dd",
    key="XY1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Swellow.Name",
    display_name="Swellow",
    searchable_by=["Swellow", "Stage 1", "Swellow"],
    subtypes=["Stage 1"],
    collector_number=103,
    set_code="XY1",
    rarity=Rarities.Rare,
    hp=90,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Taillow.Name",
    family_id=276,
    abilities=[
        Ability(
            title="Drive Off",
            game_text="Once during your turn (before your attack), you may have your opponent switch his or her Active Pok\u00e9mon with 1 of his or her Benched Pok\u00e9mon.",
            # STUB: ability effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Wing Attack",
            cost={PokemonTypes.COLORLESS: 3},
            damage=60,
        ),
    ],
)