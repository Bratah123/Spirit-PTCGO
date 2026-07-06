from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="bc6e7720-d28f-5f43-9928-c2958ab3cb1b",
    key="SWSH6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Scolipede.Name",
    display_name="Scolipede",
    searchable_by=["Scolipede", "Stage 2", "Scolipede"],
    subtypes=["Stage 2"],
    collector_number=107,
    set_code="SWSH6",
    rarity=Rarities.Rare,
    hp=160,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.STAGE2,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Whirlipede.Name",
    family_id=543,
    abilities=[
        Attack(
            title="Poison Sting",
            game_text="Your opponent's Active Pok\u00e9mon is now Poisoned.",
            cost={PokemonTypes.DARKNESS: 1},
            damage=50,
            effect=unimplemented,
        ),
        Attack(
            title="Venoshock",
            game_text="If your opponent's Active Pok\u00e9mon is Poisoned, this attack does 120 more damage.",
            cost={PokemonTypes.DARKNESS: 1, PokemonTypes.COLORLESS: 2},
            damage=100,
            damage_operator="+",
            effect=unimplemented,
        ),
    ],
)