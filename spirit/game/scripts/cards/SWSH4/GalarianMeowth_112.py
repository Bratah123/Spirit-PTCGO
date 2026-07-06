from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="b84cff1b-7fa2-5a91-aba0-4e6cc38f1320",
    key="SWSH4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.GalarianMeowth.Name",
    display_name="Galarian Meowth",
    searchable_by=["Galarian Meowth", "Basic", "GalarianMeowth"],
    subtypes=["Basic"],
    collector_number=112,
    set_code="SWSH4",
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.GRASS,
    family_id=52,
    abilities=[
        Attack(
            title="Scratch",
            cost={PokemonTypes.METAL: 1},
            damage=10,
        ),
        Attack(
            title="Fury Swipes",
            game_text="Flip 3 coins. This attack does 20 damage for each heads.",
            cost={PokemonTypes.METAL: 1, PokemonTypes.COLORLESS: 1},
            damage=20,
            damage_operator="x",
            effect=unimplemented,
        ),
    ],
)