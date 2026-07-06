from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="743c4a25-d2e0-553f-882b-a16401198f9b",
    key="SWSH6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Kecleon.Name",
    display_name="Kecleon",
    searchable_by=["Kecleon", "Basic", "Rapid Strike", "Kecleon"],
    subtypes=["Basic", "Rapid Strike"],
    collector_number=122,
    set_code="SWSH6",
    rarity=Rarities.Rare,
    hp=90,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=352,
    abilities=[
        Ability(
            title="Chromashift",
            game_text="This Pok\u00e9mon is the same type as any basic Energy attached to it. (If it has 2 or more different types of basic Energy attached, this Pok\u00e9mon is each of those types.)",
            effect=unimplemented,
        ),
        Attack(
            title="Spinning Attack",
            cost={PokemonTypes.COLORLESS: 3},
            damage=90,
        ),
    ],
)