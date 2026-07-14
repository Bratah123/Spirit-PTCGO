from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Activations
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AttrID, TrainerType


def _is_pokemon_tool_card(card):
    return card.get_attribute(AttrID.TRAINER_TYPE) in (
        TrainerType.POKEMON_TOOL.value, TrainerType.POKEMON_TOOL_F.value,
    )


async def instant_charge(ctx):
    """Draw 3 cards."""
    await ctx.draw_cards(3)


async def scrap_short(ctx):
    """40. Put any number of Pokémon Tool cards from discard into the Lost Zone; +40 damage per card moved this way."""
    tools = [c for c in ctx.discard_pile() if _is_pokemon_tool_card(c)]
    picks = []
    if tools:
        picks = await ctx.choose_cards(
            tools, len(tools), minimum=0,
            prompt="Put any number of Pokémon Tool cards from your discard pile in the Lost Zone.",
        )
    if picks:
        await ctx.move_to_lost_zone(picks)
    await ctx.deal_damage(40 + 40 * len(picks))


card = PokemonCardDef(
    guid="0c092723-8f2e-5403-9617-2f0369019af6",
    key="SWSH11",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.RotomV.Name",
    display_name="Rotom V",
    searchable_by=["Rotom V", "Basic", "V", "RotomV"],
    subtypes=["Basic", "V"],
    collector_number=58,
    set_code="SWSH11",
    rarity=Rarities.RareHoloV,
    hp=190,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=479,
    abilities=[
        Ability(
            title="Instant Charge",
            game_text="Once during your turn, you may draw 3 cards. If you use this Ability, your turn ends.",
            activation=Activations.ONCE_PER_TURN,
            ends_turn=True,
            effect=instant_charge,
        ),
        Attack(
            title="Scrap Short",
            game_text="Put any number of Pokémon Tool cards from your discard pile in the Lost Zone. This attack does 40 more damage for each card you put in the Lost Zone in this way.",
            cost={PokemonTypes.LIGHTNING: 2},
            damage=40,
            damage_operator="+",
            effect=scrap_short,
        ),
    ],
)
