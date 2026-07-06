from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="e4d729c4-b1b3-58b5-9b65-968cbbb1ac93",
    key="SWSH2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.RillaboomVMAX.Name",
    display_name="Rillaboom VMAX",
    searchable_by=["Rillaboom VMAX", "VMAX", "RillaboomVMAX"],
    subtypes=["VMAX"],
    collector_number=193,
    set_code="SWSH2",
    rarity=Rarities.RareRainbow,
    hp=330,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.VMAX,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIRE,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.RillaboomV.Name",
    family_id=812,
    abilities=[
        Attack(
            title="Scratch",
            cost={PokemonTypes.COLORLESS: 1},
            damage=50,
        ),
        Attack(
            title="Max Beating",
            game_text="You may discard up to 3 Grass Energy from this Pok\u00e9mon. If you do, this attack does 50 more damage for each card you discarded in this way.",
            cost={PokemonTypes.GRASS: 3, PokemonTypes.COLORLESS: 1},
            damage=130,
            damage_operator="+",
            effect=unimplemented,
        ),
    ],
)