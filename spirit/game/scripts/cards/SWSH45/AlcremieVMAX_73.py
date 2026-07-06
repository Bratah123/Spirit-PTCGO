from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="0d0d5da2-bd80-5a43-a206-743b2d8c18f4",
    key="SWSH45",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.AlcremieVMAX.Name",
    display_name="Alcremie VMAX",
    searchable_by=["Alcremie VMAX", "VMAX", "AlcremieVMAX"],
    subtypes=["VMAX"],
    collector_number=73,
    set_code="SWSH45",
    rarity=Rarities.RareRainbow,
    hp=310,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.VMAX,
    retreat_cost=3,
    weakness_type=PokemonTypes.METAL,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.AlcremieV.Name",
    family_id=869,
    abilities=[
        Attack(
            title="Adornment",
            game_text="For each of your Benched Pok\u00e9mon, search your deck for a Psychic Energy card and attach it to that Pok\u00e9mon. Then, shuffle your deck.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=unimplemented,
        ),
        Attack(
            title="G-Max Whisk",
            game_text="Discard any amount of Energy from your Pok\u00e9mon. This attack does 60 damage for each card you discarded in this way.",
            cost={PokemonTypes.PSYCHIC: 2},
            damage=60,
            damage_operator="x",
            effect=unimplemented,
        ),
    ],
)