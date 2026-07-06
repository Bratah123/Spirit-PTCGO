from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="afd7e0dc-0016-5628-b109-95f4566ce780",
    key="SWSH5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.FlappleVMAX.Name",
    display_name="Flapple VMAX",
    searchable_by=["Flapple VMAX", "VMAX", "FlappleVMAX"],
    subtypes=["VMAX"],
    collector_number=164,
    set_code="SWSH5",
    rarity=Rarities.RareRainbow,
    hp=320,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.VMAX,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIRE,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.FlappleV.Name",
    family_id=841,
    abilities=[
        Attack(
            title="G-Max Rolling",
            game_text="This attack does 10 less damage for each damage counter on this Pok\u00e9mon.",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 2},
            damage=250,
            damage_operator="-",
            effect=unimplemented,
        ),
    ],
)