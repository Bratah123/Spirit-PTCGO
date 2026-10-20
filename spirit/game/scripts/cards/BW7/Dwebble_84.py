from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="381f4d3c-8549-5c3d-bd48-f078e6f0e38e",
    key="BW7",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Dwebble.Name",
    display_name="Dwebble",
    searchable_by=["Dwebble", "Basic", "Dwebble"],
    subtypes=["Basic"],
    collector_number=84,
    set_code="BW7",
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.GRASS,
    family_id=557,
    abilities=[
        Attack(
            title="Flail",
            game_text="Does 10 damage times the number of damage counters on this Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=10,
            damage_operator="x",
            effect=unimplemented,
        ),
    ],
)