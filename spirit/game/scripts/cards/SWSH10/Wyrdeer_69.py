from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Activations
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import bonus_if


async def hurried_gait(ctx):
    """Once during your turn, you may draw a card."""
    if await ctx.ask_yes_no("Draw a card?"):
        await ctx.draw_cards(1)


def _same_hand_size(ctx):
    return ctx.hand_size() == ctx.hand_size(ctx.opponent_id)


card = PokemonCardDef(
    guid="b2d9bd21-030a-5bcd-887e-93db6255c9cb",
    key="SWSH10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Wyrdeer.Name",
    display_name="Wyrdeer",
    searchable_by=["Wyrdeer", "Stage 1", "Wyrdeer"],
    subtypes=["Stage 1"],
    collector_number=69,
    set_code="SWSH10",
    rarity=Rarities.RareHolo,
    hp=140,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Stantler.Name",
    family_id=234,
    abilities=[
        Ability(
            title="Hurried Gait",
            game_text="Once during your turn, you may draw a card.",
            activation=Activations.ONCE_PER_TURN,
            effect=hurried_gait,
        ),
        Attack(
            title="Extrasensory",
            game_text="If you have the same number of cards in your hand as your opponent, this attack does 80 more damage.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=40,
            damage_operator="+",
            effect=bonus_if(_same_hand_size, 80),
        ),
    ],
)