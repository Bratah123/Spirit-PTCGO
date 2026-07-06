from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="b93d9d2e-8870-5ad7-a687-61d647737357",
    key="SWSH35",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.DrednawVMAX.Name",
    display_name="Drednaw VMAX",
    searchable_by=["Drednaw VMAX", "VMAX", "DrednawVMAX"],
    subtypes=["VMAX"],
    collector_number=75,
    set_code="SWSH35",
    rarity=Rarities.RareRainbow,
    hp=320,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.VMAX,
    retreat_cost=4,
    weakness_type=PokemonTypes.LIGHTNING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.DrednawV.Name",
    family_id=834,
    abilities=[
        Ability(
            title="Solid Shell",
            game_text="This Pok\u00e9mon takes 30 less damage from attacks (after applying Weakness and Resistance).",
            effect=unimplemented,
        ),
        Attack(
            title="G-Max Headbutt",
            game_text="Flip a coin. If heads, this attack does 80 more damage.",
            cost={PokemonTypes.WATER: 2, PokemonTypes.COLORLESS: 1},
            damage=160,
            damage_operator="+",
            effect=unimplemented,
        ),
    ],
)