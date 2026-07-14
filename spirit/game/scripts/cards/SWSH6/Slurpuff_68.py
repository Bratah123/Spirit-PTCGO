from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities


async def follow_the_scent(ctx):
    heads = await ctx.flip_coins(3, "Follow the Scent")
    count = sum(1 for h in heads if h)
    discard = ctx.discard_pile()
    if count <= 0 or not discard:
        return
    picks = await ctx.choose_cards(
        discard, count, minimum=1,
        prompt=f"Choose up to {count} cards from your discard pile to put into your hand.",
    )
    if picks:
        await ctx.put_in_hand(picks, reveal=False)

card = PokemonCardDef(
    guid="c055fdce-d988-5206-aeec-a15fa7e9730f",
    key="SWSH6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Slurpuff.Name",
    display_name="Slurpuff",
    searchable_by=["Slurpuff", "Stage 1", "Slurpuff"],
    subtypes=["Stage 1"],
    collector_number=68,
    set_code="SWSH6",
    rarity=Rarities.Rare,
    hp=110,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.METAL,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Swirlix.Name",
    family_id=684,
    abilities=[
        Attack(
            title="Follow the Scent",
            game_text="Flip 3 coins. Put a number of cards up to the number of heads from your discard pile into your hand.",
            cost={PokemonTypes.COLORLESS: 2},
            effect=follow_the_scent,
        ),
        Attack(
            title="Fairy Wind",
            cost={PokemonTypes.COLORLESS: 3},
            damage=80,
        ),
    ],
)