from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="a75f4e68-8a43-59d1-a037-dc931adaae4a",
    key="SWSH6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.BlazikenVMAX.Name",
    display_name="Blaziken VMAX",
    searchable_by=["Blaziken VMAX", "VMAX", "Rapid Strike", "BlazikenVMAX"],
    subtypes=["VMAX", "Rapid Strike"],
    collector_number=201,
    set_code="SWSH6",
    rarity=Rarities.RareRainbow,
    hp=320,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.VMAX,
    retreat_cost=2,
    weakness_type=PokemonTypes.WATER,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.BlazikenV.Name",
    family_id=257,
    abilities=[
        Attack(
            title="Clutch",
            game_text="During your opponent's next turn, the Defending Pok\u00e9mon can't retreat.",
            cost={PokemonTypes.FIRE: 1},
            damage=60,
            effect=unimplemented,
        ),
        Attack(
            title="Max Blaze",
            game_text="Choose up to 2 of your Benched Rapid Strike Pok\u00e9mon and attach an Energy card from your discard pile to each of them.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=130,
            effect=unimplemented,
        ),
    ],
)