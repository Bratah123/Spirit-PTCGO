from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="0578032a-4bc3-5a3b-b1f4-3e5f0e7c8444",
    key="BW7",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Mienshao.Name",
    display_name="Mienshao",
    searchable_by=["Mienshao", "Stage 1", "Mienshao"],
    subtypes=["Stage 1"],
    collector_number=88,
    set_code="BW7",
    rarity=Rarities.Uncommon,
    hp=90,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Mienfoo.Name",
    family_id=619,
    abilities=[
        Attack(
            title="Knock Off",
            game_text="Discard a random card from your opponent's hand.",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 1},
            damage=20,
            effect=unimplemented,
        ),
        Attack(
            title="Double Whip",
            game_text="Flip 2 coins. This attack does 70 damage times the number of heads.",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 2},
            damage=70,
            damage_operator="x",
            effect=unimplemented,
        ),
    ],
)