from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import AttrID, PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import flip_bonus


async def _tag_draw(ctx):
    """Shuffle your hand into your deck, draw 4 (8 if Minun is on your Bench)."""
    hand = list(ctx.hand())
    if hand:
        await ctx.shuffle_into_deck(hand)
    else:
        await ctx.shuffle_deck()
    minun = any(p.get_attribute(AttrID.EVOLUTION_LOGIC_NAME) == "Minun" for p in ctx.my_bench())
    await ctx.draw_cards(8 if minun else 4)


card = PokemonCardDef(
    guid="804fc7e2-20f9-5dc1-a541-cc74c68c48ec",
    key="BW5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Plusle.Name",
    display_name="Plusle",
    searchable_by=["Plusle", "Basic", "Plusle"],
    subtypes=["Basic"],
    collector_number=39,
    set_code="BW5",
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=311,
    abilities=[
        Attack(
            title="Tag Draw",
            game_text="Shuffle your hand into your deck. Then, draw 4 cards. If Minun is on your Bench, draw 4 more cards.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=_tag_draw,
        ),
        Attack(
            title="Positive Ion",
            game_text="Flip a coin. If heads, this attack does 10 more damage.",
            cost={PokemonTypes.LIGHTNING: 1},
            damage=20,
            damage_operator="+",
            effect=flip_bonus(10),
        ),
    ],
)