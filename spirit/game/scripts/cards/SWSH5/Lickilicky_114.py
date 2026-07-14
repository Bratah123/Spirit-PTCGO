from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.support_common import opponent_switches


async def selickt(ctx):
    choice = await ctx.choose(
        "Discard the top 3 cards of your deck or discard 3 cards from your hand?",
        ["Discard the top 3 cards of your deck", "Discard 3 cards from your hand"],
        player_id=ctx.opponent_id, use_panel=False,
    )
    if choice == 0:
        await ctx.discard_cards(ctx.deck_top(3, player_id=ctx.opponent_id))
    else:
        await ctx.discard_from_hand(
            3, player_id=ctx.opponent_id, prompt="Discard 3 cards from your hand"
        )


async def pitch(ctx):
    await ctx.deal_damage()
    await opponent_switches(ctx)

card = PokemonCardDef(
    guid="4357a9e4-cfc0-5a15-9da5-a785f1242b83",
    key="SWSH5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Lickilicky.Name",
    display_name="Lickilicky",
    searchable_by=["Lickilicky", "Stage 1", "Lickilicky"],
    subtypes=["Stage 1"],
    collector_number=114,
    set_code="SWSH5",
    rarity=Rarities.Rare,
    hp=140,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=4,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Lickitung.Name",
    family_id=108,
    abilities=[
        Attack(
            title="Selickt",
            game_text="Your opponent chooses to discard the top 3 cards of their deck or to discard 3 cards from their hand.",
            cost={PokemonTypes.COLORLESS: 3},
            effect=selickt,
        ),
        Attack(
            title="Pitch",
            game_text="Your opponent switches their Active Pok\u00e9mon with 1 of their Benched Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 4},
            damage=100,
            effect=pitch,
        ),
    ],
)