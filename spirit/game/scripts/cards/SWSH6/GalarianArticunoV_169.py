from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Activations
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, SpecialConditions
from spirit.game.card_effects.attacks_common import condition_attack
from spirit.game.card_effects.support_common import requires_hand


async def reconstitute(ctx):
    """Discard 2 cards from your hand. Once during your turn, you may draw a
    card."""
    await ctx.discard_from_hand(2, prompt="Discard 2 cards to use Reconstitute")
    if await ctx.ask_yes_no("Draw a card?"):
        await ctx.draw_cards(1)


card = PokemonCardDef(
    guid="25585034-455b-5161-9f69-570cf701b499",
    key="SWSH6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.GalarianArticunoV.Name",
    display_name="Galarian Articuno V",
    searchable_by=["Galarian Articuno V", "Basic", "V", "GalarianArticunoV"],
    subtypes=["Basic", "V"],
    collector_number=169,
    set_code="SWSH6",
    rarity=Rarities.RareUltra,
    hp=210,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.FIGHTING,
    family_id=144,
    abilities=[
        Ability(
            title="Reconstitute",
            game_text="You must discard 2 cards from your hand in order to use this Ability. Once during your turn, you may draw a card.",
            activation=Activations.ONCE_PER_TURN,
            condition=requires_hand(n=2),
            effect=reconstitute,
        ),
        Attack(
            title="Psyray",
            game_text="Your opponent's Active Pokémon is now Confused.",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 2},
            damage=110,
            effect=condition_attack(SpecialConditions.CONFUSED),
        ),
    ],
)
