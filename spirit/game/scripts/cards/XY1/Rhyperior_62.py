"""STUB: effect not implemented — do not guess mechanics.
Rhyperior (XY1 #62): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="c7853afb-a3e6-53c2-af16-bb2024f69964",
    key="XY1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Rhyperior.Name",
    display_name="Rhyperior",
    searchable_by=["Rhyperior", "Stage 2", "Rhyperior"],
    subtypes=["Stage 2"],
    collector_number=62,
    set_code="XY1",
    rarity=Rarities.RareHolo,
    hp=160,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE2,
    retreat_cost=4,
    weakness_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Rhydon.Name",
    family_id=111,
    abilities=[
        Attack(
            title="Rock Black",
            game_text="Flip a coin for each Fighting Energy attached to this Pok\u00e9mon. This attack does 50 damage times the number of heads.",
            cost={PokemonTypes.FIGHTING: 1},
            damage=50,
            damage_operator="x",
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Rock Wrecker",
            game_text="This attack's damage isn't affected by Weakness or Resistance. This Pok\u00e9mon can't attack during your next turn.",
            cost={PokemonTypes.FIGHTING: 2, PokemonTypes.COLORLESS: 2},
            damage=130,
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)