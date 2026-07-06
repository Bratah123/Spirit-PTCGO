from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="30bbbfb9-8a78-5cfe-8e79-dfd830bfed8b",
    key="SWSH12",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Lopunny.Name",
    display_name="Lopunny",
    searchable_by=["Lopunny", "Stage 1", "Lopunny"],
    subtypes=["Stage 1"],
    collector_number=145,
    set_code="SWSH12",
    rarity=Rarities.Uncommon,
    hp=110,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Buneary.Name",
    family_id=427,
    abilities=[
        Attack(
            title="Smash Kick",
            cost={PokemonTypes.COLORLESS: 1},
            damage=30,
        ),
        Attack(
            title="Double Kick",
            game_text="Flip 2 coins. This attack does 100 damage for each heads.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=100,
            damage_operator="x",
            effect=unimplemented,
        ),
    ],
)