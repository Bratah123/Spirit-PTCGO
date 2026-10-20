"""STUB: effect not implemented — do not guess mechanics.
Team Magma's Zangoose (TATM #22): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="832fc007-ff56-594b-9af7-f7b47447eabd",
    key="TATM",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.TeamMagmasZangoose.Name",
    display_name="Team Magma's Zangoose",
    searchable_by=["Team Magma's Zangoose", "Basic", "TeamMagmasZangoose"],
    subtypes=["Basic"],
    collector_number=22,
    set_code="TATM",
    rarity=Rarities.Common,
    hp=90,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=335,
    abilities=[
        Attack(
            title="Call for Family",
            game_text="Search your deck for up to 2 Basic Team Magma Pok\u00e9mon and put them onto your Bench. Shuffle your deck afterward.",
            cost={PokemonTypes.COLORLESS: 1},
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Team Play",
            game_text="This attack does 20 damage times the number of Team Magma Pok\u00e9mon on your Bench.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=20,
            damage_operator="x",
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)