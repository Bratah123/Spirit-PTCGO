from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="a1be1168-1d52-5c3e-a56e-87c171a4b36b",
    key="SWSH8",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.GalarianDarumaka.Name",
    display_name="Galarian Darumaka",
    searchable_by=["Galarian Darumaka", "Basic", "GalarianDarumaka"],
    subtypes=["Basic"],
    collector_number=71,
    set_code="SWSH8",
    rarity=Rarities.Common,
    hp=80,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.METAL,
    family_id=554,
    abilities=[
        Attack(
            title="Reckless Charge",
            game_text="Flip a coin. If tails, this Pok\u00e9mon also does 10 damage to itself.",
            cost={PokemonTypes.WATER: 1},
            damage=20,
            effect=unimplemented,
        ),
    ],
)