from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="7fd5c2df-c315-5671-bd24-b18256169dce",
    key="SWSH11",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.RadiantSteelix.Name",
    display_name="Radiant Steelix",
    searchable_by=["Radiant Steelix", "Basic", "Radiant", "RadiantSteelix"],
    subtypes=["Basic", "Radiant"],
    collector_number=124,
    set_code="SWSH11",
    rarity=Rarities.RareRadiant,
    hp=170,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.BASIC,
    retreat_cost=4,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.GRASS,
    family_id=208,
    abilities=[
        Attack(
            title="Energy Stream",
            game_text="Attach up to 2 Metal Energy cards from your discard pile to this Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=20,
            effect=unimplemented,
        ),
        Attack(
            title="Destructive Finish",
            game_text="Discard cards from the top of your deck until only 1 card remains. This attack does 30 more damage for each Energy card you discarded in this way.",
            cost={PokemonTypes.METAL: 2, PokemonTypes.COLORLESS: 1},
            damage=60,
            damage_operator="+",
            effect=unimplemented,
        ),
    ],
)