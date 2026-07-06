from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="d5487ebb-78fd-5d16-b182-706c8afd77da",
    key="SWSH45",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.DittoVMAX.Name",
    display_name="Ditto VMAX",
    searchable_by=["Ditto VMAX", "VMAX", "DittoVMAX"],
    subtypes=["VMAX"],
    collector_number=51,
    set_code="SWSH45",
    rarity=Rarities.RareHoloVMAX,
    hp=320,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.VMAX,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.DittoV.Name",
    family_id=132,
    abilities=[
        Attack(
            title="Max Transform",
            game_text="Choose 1 of your opponent's Active Pok\u00e9mon's attacks and use it as this attack.",
            cost={PokemonTypes.COLORLESS: 3},
            effect=unimplemented,
        ),
    ],
)