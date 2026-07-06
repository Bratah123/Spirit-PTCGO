from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="a805e3bb-4d0e-5a00-ba48-67253452ded6",
    key="SWSH3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Arctovish.Name",
    display_name="Arctovish",
    searchable_by=["Arctovish", "Stage 1", "Arctovish"],
    subtypes=["Stage 1"],
    collector_number=54,
    set_code="SWSH3",
    rarity=Rarities.Rare,
    hp=150,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.LIGHTNING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.RareFossil.Name",
    family_id=883,
    abilities=[
        Attack(
            title="Hard Face",
            game_text="During your opponent's next turn, this Pok\u00e9mon takes 60 less damage from attacks (after applying Weakness and Resistance).",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 2},
            damage=90,
            effect=unimplemented,
        ),
        Attack(
            title="Cold Breath",
            game_text="Your opponent's Active Pok\u00e9mon is now Asleep.",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 3},
            damage=130,
            effect=unimplemented,
        ),
    ],
)