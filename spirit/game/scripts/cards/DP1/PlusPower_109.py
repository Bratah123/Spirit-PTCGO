"""PlusPower (DP1 #109) — attaches as a Pokémon Tool; discard at end of turn."""
from spirit.game.data_utils import PokemonToolCardDef, Ability, Triggers
from spirit.game.attributes import Rarities, AbilityTypes
from spirit.game.card_effects.dp import plus_power_passive

async def _discard_plus_power_eot(ctx):
    """Discard this PlusPower from its holder at end of your turn."""
    src = ctx.source
    if src is None:
        return
    # source may be the tool card or the holder
    holder = src
    tool = None
    children = list(getattr(src, "children", []) or [])
    for c in children:
        dname = c.get_attribute(__import__("spirit.game.attributes", fromlist=["AttrID"]).AttrID.DISPLAY_NAME) or ""
        if "PlusPower" in str(dname) or (c.archetype_id or "").endswith("PlusPower") or "pluspower" in (c.archetype_id or "").lower():
            tool = c
            break
    if tool is None and hasattr(src, "parent") and src.parent is not None:
        # source is the tool itself
        tool = src
        holder = src.parent
    if tool is not None:
        await ctx.discard_cards([tool])


card = PokemonToolCardDef(
    guid="69fd2176-48c0-5434-a271-5c99e13b8ed6",
    key="DP1",
    name="com.direwolfdigital.cake.data.archetypes.trainer.PlusPower.Name",
    display_name="PlusPower",
    searchable_by=["PlusPower", "Pokémon Tool", "Item"],
    subtypes=["Pokémon Tool"],
    collector_number=109,
    set_code="DP1",
    rarity=Rarities.Uncommon,
    passive=plus_power_passive(10),
    granted_abilities=[
        Ability(
            title="PlusPower Discard",
            game_text="Discard this card at the end of your turn.",
            ability_type=AbilityTypes.POKE_BODY,
            trigger=Triggers.END_OF_TURN,
            effect=_discard_plus_power_eot,
        ),
    ],
)
