from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import AttrID, PokemonTypes, PokemonStage, Rarities, TrainerType


def _is_tool_card(card):
    return card.get_attribute(AttrID.TRAINER_TYPE) in (
        TrainerType.POKEMON_TOOL.value, TrainerType.POKEMON_TOOL_F.value)


async def ditch_and_shake(ctx):
    """Discard any number of Pokemon Tool cards from hand; 50 damage each."""
    picks = await ctx.discard_from_hand(
        len(ctx.hand()), minimum=0, predicate=_is_tool_card,
        prompt="Discard any number of Pokémon Tool cards from your hand.",
    )
    await ctx.deal_damage(50 * len(picks))


card = PokemonCardDef(
    guid="a8756632-c300-52e6-90f9-6098398f810a",
    key="SWSH8",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Maractus.Name",
    display_name="Maractus",
    searchable_by=["Maractus", "Basic", "Maractus"],
    subtypes=["Basic"],
    collector_number=12,
    set_code="SWSH8",
    rarity=Rarities.Rare,
    hp=110,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    family_id=556,
    abilities=[
        Attack(
            title="Peck",
            cost={PokemonTypes.GRASS: 1},
            damage=20,
        ),
        Attack(
            title="Ditch and Shake",
            game_text="Discard any number of Pok\u00e9mon Tool cards from your hand. This attack does 50 damage for each card you discarded in this way.",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 1},
            damage=50,
            damage_operator="x",
            effect=ditch_and_shake,
        ),
    ],
)