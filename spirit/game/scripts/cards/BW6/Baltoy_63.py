from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities


async def _reverse_spin(ctx):
    """Your opponent shuffles their hand into their deck and draws 4 cards."""
    await ctx.shuffle_into_deck(ctx.hand(ctx.opponent_id), ctx.opponent_id)
    await ctx.draw_cards(4, ctx.opponent_id)


card = PokemonCardDef(
    guid="bc2a7c0f-1eaf-50e8-bc64-6ce870bb4c7f",
    key="BW6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Baltoy.Name",
    display_name="Baltoy",
    searchable_by=["Baltoy", "Basic", "Baltoy"],
    subtypes=["Basic"],
    collector_number=63,
    set_code="BW6",
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.GRASS,
    family_id=343,
    abilities=[
        Attack(
            title="Spinning Attack",
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
        ),
        Attack(
            title="Reverse Spin",
            game_text="Your opponent shuffles his or her hand into his or her deck and draws 4 cards.",
            cost={PokemonTypes.COLORLESS: 2},
            effect=_reverse_spin,
        ),
    ],
)