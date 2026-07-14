from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, SpecialConditions, AttrID, TrainerType
from spirit.game.card_effects.attacks_common import condition_attack

_TOOL_TYPES = (TrainerType.POKEMON_TOOL.value, TrainerType.POKEMON_TOOL_F.value)


def _is_tool_card(card):
    return card.get_attribute(AttrID.TRAINER_TYPE) in _TOOL_TYPES


async def trash_cyclone(ctx):
    """30 damage for each Pokemon Tool card in your discard pile. Then,
    shuffle those cards into your deck."""
    tools = [c for c in ctx.discard_pile() if _is_tool_card(c)]
    await ctx.deal_damage(30 * len(tools))
    if tools:
        await ctx.shuffle_into_deck(tools, ctx.player_id)


card = PokemonCardDef(
    guid="95fe0850-6bb7-5d27-9e62-83d87f517693",
    key="SWSH4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Garbodor.Name",
    display_name="Garbodor",
    searchable_by=["Garbodor", "Stage 1", "Garbodor"],
    subtypes=["Stage 1"],
    collector_number=111,
    set_code="SWSH4",
    rarity=Rarities.Rare,
    hp=120,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Trubbish.Name",
    family_id=568,
    abilities=[
        Attack(
            title="Trash Cyclone",
            game_text="This attack does 30 damage for each Pokémon Tool card in your discard pile. Then, shuffle those cards into your deck.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=30,
            damage_operator="x",
            effect=trash_cyclone,
        ),
        Attack(
            title="Poison Spray",
            game_text="Your opponent's Active Pokémon is now Poisoned.",
            cost={PokemonTypes.DARKNESS: 1, PokemonTypes.COLORLESS: 2},
            damage=80,
            effect=condition_attack(SpecialConditions.POISONED),
        ),
    ],
)
