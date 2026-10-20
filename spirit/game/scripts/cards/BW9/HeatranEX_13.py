from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="a3fe87f5-acaa-57f4-b822-eb3d2bccc6f0",
    key="BW9",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.HeatranEX.Name",
    display_name="Heatran-EX",
    searchable_by=["Heatran-EX", "Basic", "EX", "Team Plasma", "HeatranEX"],
    subtypes=["Basic", "EX", "Team Plasma"],
    collector_number=13,
    set_code="BW9",
    rarity=Rarities.RareHoloEX,
    hp=180,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.WATER,
    family_id=485,
    abilities=[
        Attack(
            title="Heat Boiler",
            game_text="If this Pok\u00e9mon is affected by a Special Condition, this attack does 60 more damage.",
            cost={PokemonTypes.FIRE: 1, PokemonTypes.COLORLESS: 2},
            damage=60,
            damage_operator="+",
            effect=unimplemented,
        ),
        Attack(
            title="Dynamite Press",
            game_text="If this Pok\u00e9mon has any Plasma Energy attached to it, this attack does 10 more damage for each damage counter on the Defending Pok\u00e9mon.",
            cost={PokemonTypes.FIRE: 2, PokemonTypes.COLORLESS: 2},
            damage=80,
            damage_operator="+",
            effect=unimplemented,
        ),
    ],
)