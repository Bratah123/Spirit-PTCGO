from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="a57b82ca-48a8-5ff7-88d1-9a179268b4cc",
    key="SWSH5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Mienshao.Name",
    display_name="Mienshao",
    searchable_by=["Mienshao", "Stage 1", "Rapid Strike", "Mienshao"],
    subtypes=["Stage 1", "Rapid Strike"],
    collector_number=77,
    set_code="SWSH5",
    rarity=Rarities.Rare,
    hp=90,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Mienfoo.Name",
    family_id=619,
    abilities=[
        Attack(
            title="Pound",
            cost={PokemonTypes.COLORLESS: 1},
            damage=20,
        ),
        Attack(
            title="Spinning Whip",
            game_text="Your opponent's Active Pok\u00e9mon is now Confused. Shuffle this Pok\u00e9mon and all attached cards into your deck.",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 1},
            damage=90,
            effect=unimplemented,
        ),
    ],
)