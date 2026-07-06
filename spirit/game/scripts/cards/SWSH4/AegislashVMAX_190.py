from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="668200e8-a452-554c-a54d-5d6fed80754a",
    key="SWSH4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.AegislashVMAX.Name",
    display_name="Aegislash VMAX",
    searchable_by=["Aegislash VMAX", "VMAX", "AegislashVMAX"],
    subtypes=["VMAX"],
    collector_number=190,
    set_code="SWSH4",
    rarity=Rarities.RareRainbow,
    hp=320,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.VMAX,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.AegislashV.Name",
    family_id=681,
    abilities=[
        Attack(
            title="Max Hack",
            game_text="This attack does 30 more damage for each Prize card you have taken.",
            cost={PokemonTypes.METAL: 2, PokemonTypes.COLORLESS: 1},
            damage=160,
            damage_operator="+",
            effect=unimplemented,
        ),
    ],
)