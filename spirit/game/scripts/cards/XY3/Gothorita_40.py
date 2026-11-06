from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities


async def watcheck(ctx):
    """Look at top 5 of opponent's deck; put back in any order."""
    await ctx.reorder_deck_top(
        5,
        player_id=ctx.opponent_id,
        prompt="Rearrange the top cards of your opponent's deck",
    )


card = PokemonCardDef(
    guid="e9086356-8b36-5a01-89e0-eda094726cd0",
    key="XY3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Gothorita.Name",
    display_name="Gothorita",
    searchable_by=["Gothorita", "Stage 1", "Gothorita"],
    subtypes=["Stage 1"],
    collector_number=40,
    set_code="XY3",
    rarity=Rarities.Uncommon,
    hp=80,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Gothita.Name",
    family_id=574,
    abilities=[
        Attack(
            title="Fortunate Eye",
            game_text="Look at the top 5 cards of your opponent's deck and put them back on top of his or her deck in any order.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=watcheck,
        ),
        Attack(
            title="Smack",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
        ),
    ],
)