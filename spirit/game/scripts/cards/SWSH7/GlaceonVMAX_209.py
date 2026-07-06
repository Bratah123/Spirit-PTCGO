from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="f0338b44-0381-5301-983d-e59048561f3d",
    key="SWSH7",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.GlaceonVMAX.Name",
    display_name="Glaceon VMAX",
    searchable_by=["Glaceon VMAX", "VMAX", "GlaceonVMAX"],
    subtypes=["VMAX"],
    collector_number=209,
    set_code="SWSH7",
    rarity=Rarities.RareRainbow,
    hp=310,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.VMAX,
    retreat_cost=2,
    weakness_type=PokemonTypes.METAL,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.GlaceonV.Name",
    family_id=471,
    abilities=[
        Ability(
            title="Crystal Veil",
            game_text="Prevent all damage done to this Pok\u00e9mon by attacks from your opponent's Pok\u00e9mon VMAX, except any Glaceon VMAX.",
            effect=unimplemented,
        ),
        Attack(
            title="Max Icicle",
            game_text="This attack also does 30 damage to 1 of your opponent's Benched Pok\u00e9mon. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 2},
            damage=150,
            effect=unimplemented,
        ),
    ],
)