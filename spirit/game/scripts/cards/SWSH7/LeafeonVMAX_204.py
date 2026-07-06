from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="a6c0a11e-a591-55c5-b2e3-283d849e9298",
    key="SWSH7",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.LeafeonVMAX.Name",
    display_name="Leafeon VMAX",
    searchable_by=["Leafeon VMAX", "VMAX", "LeafeonVMAX"],
    subtypes=["VMAX"],
    collector_number=204,
    set_code="SWSH7",
    rarity=Rarities.RareRainbow,
    hp=310,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.VMAX,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.LeafeonV.Name",
    family_id=470,
    abilities=[
        Attack(
            title="Grass Knot",
            game_text="This attack does 60 damage for each Colorless in your opponent's Active Pok\u00e9mon's Retreat Cost.",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 1},
            damage=60,
            damage_operator="x",
            effect=unimplemented,
        ),
        Attack(
            title="Max Leaf",
            game_text="Heal 30 damage from this Pok\u00e9mon.",
            cost={PokemonTypes.GRASS: 2, PokemonTypes.COLORLESS: 1},
            damage=170,
            effect=unimplemented,
        ),
    ],
)