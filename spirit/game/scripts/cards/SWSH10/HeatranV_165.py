from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="1e76d67b-0c8a-5ca0-9fa7-f70306697561",
    key="SWSH10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.HeatranV.Name",
    display_name="Heatran V",
    searchable_by=["Heatran V", "Basic", "V", "HeatranV"],
    subtypes=["Basic", "V"],
    collector_number=165,
    set_code="SWSH10",
    rarity=Rarities.RareUltra,
    hp=220,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.WATER,
    family_id=485,
    abilities=[
        Attack(
            title="Heat Burn",
            game_text="Your opponent's Active Pok\u00e9mon is now Burned.",
            cost={PokemonTypes.FIRE: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
            effect=unimplemented,
        ),
        Attack(
            title="Magma Fall",
            game_text="If you have a Stadium in play, this attack does 90 more damage.",
            cost={PokemonTypes.FIRE: 2, PokemonTypes.COLORLESS: 1},
            damage=90,
            damage_operator="+",
            effect=unimplemented,
        ),
    ],
)