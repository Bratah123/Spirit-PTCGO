from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="deeda815-d569-599f-809f-c0ed2b07c786",
    key="SWSH6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.CelebiVMAX.Name",
    display_name="Celebi VMAX",
    searchable_by=["Celebi VMAX", "VMAX", "CelebiVMAX"],
    subtypes=["VMAX"],
    collector_number=8,
    set_code="SWSH6",
    rarity=Rarities.RareHoloVMAX,
    hp=310,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.VMAX,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.CelebiV.Name",
    family_id=251,
    abilities=[
        Ability(
            title="Curative Forest",
            game_text="Once during your turn, you may heal 20 damage from each of your Grass Pok\u00e9mon.",
            effect=unimplemented,
        ),
        Attack(
            title="Max Plant",
            game_text="Search your deck for up to 2 Pok\u00e9mon, reveal them, and put them into your hand. Then, shuffle your deck.",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 1},
            damage=130,
            effect=unimplemented,
        ),
    ],
)