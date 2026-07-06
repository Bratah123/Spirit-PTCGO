from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="9b68348a-12cb-5936-b9a1-3edcc850455b",
    key="SWSH7",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Feebas.Name",
    display_name="Feebas",
    searchable_by=["Feebas", "Basic", "Rapid Strike", "Feebas"],
    subtypes=["Basic", "Rapid Strike"],
    collector_number=37,
    set_code="SWSH7",
    rarity=Rarities.Common,
    hp=30,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    family_id=349,
    abilities=[
        Attack(
            title="Flail Around",
            game_text="Flip 3 coins. This attack does 10 damage for each heads.",
            cost={PokemonTypes.WATER: 1},
            damage=10,
            damage_operator="x",
            effect=unimplemented,
        ),
    ],
)