from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="d0761bfd-6814-5f15-a761-5ebe8261dc99",
    key="SWSH8",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.GreninjaV.Name",
    display_name="Greninja V",
    searchable_by=["Greninja V", "Basic", "V", "GreninjaV"],
    subtypes=["Basic", "V"],
    collector_number=73,
    set_code="SWSH8",
    rarity=Rarities.RareHoloV,
    hp=210,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.LIGHTNING,
    family_id=658,
    abilities=[
        Attack(
            title="Water Drip",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 1},
            damage=40,
        ),
        Attack(
            title="Dancing Shuriken",
            game_text="Flip 3 coins. This attack does 80 damage for each heads.",
            cost={PokemonTypes.WATER: 2, PokemonTypes.COLORLESS: 1},
            damage=80,
            damage_operator="x",
            effect=unimplemented,
        ),
    ],
)