"""STUB: effect not implemented — do not guess mechanics.
Porygon-Z (XY7 #66): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="47bbaaa2-458d-5d97-8b6b-1b95095fa168",
    key="XY7",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.PorygonZ.Name",
    display_name="Porygon-Z",
    searchable_by=["Porygon-Z", "Stage 2", "PorygonZ"],
    subtypes=["Stage 2"],
    collector_number=66,
    set_code="XY7",
    rarity=Rarities.Rare,
    hp=130,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Porygon2.Name",
    family_id=137,
    abilities=[
        Attack(
            title="Cyber Crush",
            game_text="Discard all Special Energy attached to each of your opponent's Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 1},
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Slowing Beam",
            game_text="During your opponent's next turn, the Defending Pok\u00e9mon's attacks cost Colorless more.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=70,
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)