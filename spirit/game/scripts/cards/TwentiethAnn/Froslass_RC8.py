from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import place_counters


async def _drag_along(ctx):
    """Active and Knocked Out by damage from an opponent's attack: flip a coin;
    heads -> the Attacking Pokemon is Knocked Out."""
    attacker = getattr(ctx, "ko_attacker", None)
    if not (getattr(ctx, "ko_from_attack", False) and getattr(ctx, "was_active_at_ko", False)) or attacker is None:
        return
    results = await ctx.flip_coins(1, "Drag Along")
    if results and results[0]:
        await ctx.knock_out(attacker)


card = PokemonCardDef(
    guid="fbf9fe63-7f35-5ec5-851d-9df4a02f6707",
    key="TwentiethAnn",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Froslass.Name",
    display_name="Froslass",
    searchable_by=["Froslass", "Stage 1", "Froslass"],
    subtypes=["Stage 1"],
    collector_number=91,
    set_code="TwentiethAnn",
    rarity=Rarities.Uncommon,
    hp=90,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.METAL,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Snorunt.Name",
    family_id=361,
    abilities=[
        Ability(
            title="Drag Along",
            game_text="If this Pok\u00e9mon is your Active Pok\u00e9mon and is Knocked Out by damage from an opponent's attack, flip a coin. If heads, the Attacking Pok\u00e9mon is Knocked Out.",
            trigger=Triggers.ON_KNOCKED_OUT,
            effect=_drag_along,
        ),
        Attack(
            title="Snowy Drop",
            game_text="Put 4 damage counters on your opponent's Pok\u00e9mon in any way you like.",
            cost={PokemonTypes.COLORLESS: 3},
            effect=place_counters(4, 'choose_any_opponent'),
        ),
    ],
)