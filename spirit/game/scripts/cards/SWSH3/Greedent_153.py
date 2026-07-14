from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AttrID, TrainerType
from spirit.game.card_effects.support_common import remove_self_from_play

_TOOL_TYPES = (TrainerType.POKEMON_TOOL.value, TrainerType.POKEMON_TOOL_F.value)


def _is_tool_card(card):
    return card.get_attribute(AttrID.TRAINER_TYPE) in _TOOL_TYPES


async def scrape_off(ctx):
    """20. Before doing damage, discard all Pokemon Tools from the opponent's Active."""
    defender = ctx.defender
    if defender is not None and not ctx.effects_blocked(defender):
        tools = [c for c in defender.children if _is_tool_card(c)]
        if tools:
            await ctx.discard_cards(tools)
    await ctx.deal_damage()


card = PokemonCardDef(
    guid="4132812c-deeb-5a84-bd17-c42d61511c63",
    key="SWSH3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Greedent.Name",
    display_name="Greedent",
    searchable_by=["Greedent", "Stage 1", "Greedent"],
    subtypes=["Stage 1"],
    collector_number=153,
    set_code="SWSH3",
    rarity=Rarities.Rare,
    hp=120,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Skwovet.Name",
    family_id=819,
    abilities=[
        Attack(
            title="Scrape Off",
            game_text="Before doing damage, discard all Pok\u00e9mon Tools from your opponent's Active Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=20,
            effect=scrape_off,
        ),
        Attack(
            title="Smack and Run",
            game_text="Put this Pok\u00e9mon and all attached cards into your hand.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=100,
            effect=remove_self_from_play(destination="hand", with_attachments="same"),
        ),
    ],
)