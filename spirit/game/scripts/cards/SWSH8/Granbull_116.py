from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AttrID, TrainerType

_TOOL_TYPES = (TrainerType.POKEMON_TOOL.value, TrainerType.POKEMON_TOOL_F.value)


def _is_tool_card(card):
    return card.get_attribute(AttrID.TRAINER_TYPE) in _TOOL_TYPES


async def dig_up(ctx):
    """On evolve: you may put up to 2 Pokemon Tool cards from your discard pile into your hand."""
    tools = [c for c in ctx.discard_pile() if _is_tool_card(c)]
    if not tools:
        return
    picks = await ctx.choose_cards(
        tools, 2, minimum=0,
        prompt="Choose up to 2 Pokémon Tool cards to put into your hand.",
    )
    await ctx.put_in_hand(picks, reveal=False)


card = PokemonCardDef(
    guid="3a5e5018-64d5-5256-9998-7ca0506ed06c",
    key="SWSH8",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Granbull.Name",
    display_name="Granbull",
    searchable_by=["Granbull", "Stage 1", "Granbull"],
    subtypes=["Stage 1"],
    collector_number=116,
    set_code="SWSH8",
    rarity=Rarities.Rare,
    hp=120,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.METAL,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Snubbull.Name",
    family_id=209,
    abilities=[
        Ability(
            title="Dig Up",
            game_text="When you play this Pok\u00e9mon from your hand to evolve 1 of your Pok\u00e9mon during your turn, you may put up to 2 Pok\u00e9mon Tool cards from your discard pile into your hand.",
            trigger=Triggers.ON_EVOLVE,
            effect=dig_up,
        ),
        Attack(
            title="Bite",
            cost={PokemonTypes.COLORLESS: 3},
            damage=90,
        ),
    ],
)