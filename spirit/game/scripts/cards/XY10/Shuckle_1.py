from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, SpecialConditions
from spirit.game.card_effects.attacks_common import condition_attack


async def _hide_a_berry(ctx):
    """Draw 2 cards. Then put a card from your hand on the bottom of your deck."""
    await ctx.draw_cards(2)
    hand = list(ctx.hand())
    if hand:
        pick = await ctx.choose_cards(hand, 1, minimum=1, prompt="Put a card on the bottom of your deck")
        if pick:
            await ctx.put_on_bottom_of_deck(pick[0])


card = PokemonCardDef(
    guid="317702bd-eeea-53a2-800b-9567413fe302",
    key="XY10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Shuckle.Name",
    display_name="Shuckle",
    searchable_by=["Shuckle", "Basic", "Shuckle"],
    subtypes=["Basic"],
    collector_number=1,
    set_code="XY10",
    rarity=Rarities.Uncommon,
    hp=80,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    family_id=213,
    abilities=[
        Attack(
            title="Hide a Berry",
            game_text="Draw 2 cards. Then, put a card from your hand on the bottom of your deck.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=_hide_a_berry,
        ),
        Attack(
            title="Wrap",
            game_text="Flip a coin. If heads, your opponent's Active Pok\u00e9mon is now Paralyzed.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=30,
            effect=condition_attack(SpecialConditions.PARALYZED, flip=True),
        ),
    ],
)