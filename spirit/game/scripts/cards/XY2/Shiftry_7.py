"""STUB: effect not implemented — do not guess mechanics.
Shiftry (XY2 #7): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="9a2fe570-6e11-58ef-b037-ebc2b0e7d053",
    key="XY2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Shiftry.Name",
    display_name="Shiftry",
    searchable_by=["Shiftry", "Stage 2", "Shiftry"],
    subtypes=["Stage 2"],
    collector_number=7,
    set_code="XY2",
    rarity=Rarities.RareHolo,
    hp=140,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Nuzleaf.Name",
    family_id=273,
    abilities=[
        Ability(
            title="Leaf Draw",
            game_text="Once during your turn (before your attack), you may discard a Grass Energy card from your hand. If you do, draw 3 cards.",
            # STUB: ability effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Deranged Dance",
            game_text="This attack does 20 damage times the number of Benched Pok\u00e9mon (both yours and your opponent's).",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 2},
            damage=20,
            damage_operator="x",
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)