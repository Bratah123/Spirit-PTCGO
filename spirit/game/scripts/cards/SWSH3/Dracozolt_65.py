from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="67b6b840-7de3-508d-a4b2-742011564715",
    key="SWSH3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Dracozolt.Name",
    display_name="Dracozolt",
    searchable_by=["Dracozolt", "Stage 1", "Dracozolt"],
    subtypes=["Stage 1"],
    collector_number=65,
    set_code="SWSH3",
    rarity=Rarities.Rare,
    hp=160,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.STAGE1,
    retreat_cost=4,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.RareFossil.Name",
    family_id=880,
    abilities=[
        Attack(
            title="Amping Up",
            game_text="During your next turn, this Pok\u00e9mon's Amping Up attack does 90 more damage (before applying Weakness and Resistance).",
            cost={PokemonTypes.LIGHTNING: 1},
            damage=30,
            effect=unimplemented,
        ),
        Attack(
            title="Giga Impact",
            game_text="During your next turn, this Pok\u00e9mon can't attack.",
            cost={PokemonTypes.COLORLESS: 4},
            damage=200,
            effect=unimplemented,
        ),
    ],
)