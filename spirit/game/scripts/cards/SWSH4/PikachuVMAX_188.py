from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="d329c902-ea8a-567e-98ba-e38f005a42cc",
    key="SWSH4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.PikachuVMAX.Name",
    display_name="Pikachu VMAX",
    searchable_by=["Pikachu VMAX", "VMAX", "PikachuVMAX"],
    subtypes=["VMAX"],
    collector_number=188,
    set_code="SWSH4",
    rarity=Rarities.RareRainbow,
    hp=310,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.VMAX,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.PikachuV.Name",
    family_id=25,
    abilities=[
        Attack(
            title="G-Max Volt Tackle",
            game_text="You may discard all Energy from this Pok\u00e9mon. If you do, this attack does 150 more damage.",
            cost={PokemonTypes.LIGHTNING: 3},
            damage=120,
            damage_operator="+",
            effect=unimplemented,
        ),
    ],
)