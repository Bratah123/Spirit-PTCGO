from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AttrID, SpecialConditions, CLIENT_SPECIAL_CONDITION_NAMES


def _has_cond(p, cond):
    return p is not None and CLIENT_SPECIAL_CONDITION_NAMES[cond] in (p.get_attribute(AttrID.SPECIAL_CONDITIONS) or [])


async def _poison_up(ctx):
    """If the Defending Pokemon is Poisoned, 3 more damage counters on it
    between turns (stacks)."""
    await ctx.deal_damage()
    d = ctx.opponent_active()
    if _has_cond(d, SpecialConditions.POISONED) and not ctx.effects_blocked(d):
        counters = ctx.session.poison_counters
        counters[d.entity_id] = counters.get(d.entity_id, 1) + 3


card = PokemonCardDef(
    guid="56efb058-82be-5268-88bf-30433b7e42ab",
    key="XY11",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Croagunk.Name",
    display_name="Croagunk",
    searchable_by=["Croagunk", "Basic", "Croagunk"],
    subtypes=["Basic"],
    collector_number=58,
    set_code="XY11",
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=453,
    abilities=[
        Attack(
            title="Poison Up",
            game_text="If the Defending Pok\u00e9mon is Poisoned, put 3 more damage counters on that Pok\u00e9mon between turns. This effect can be applied more than once.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=_poison_up,
        ),
    ],
)