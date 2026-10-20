from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, SpecialConditions, AttrID, CLIENT_SPECIAL_CONDITION_NAMES
from spirit.game.card_effects.attacks_common import condition_attack


def _has_cond(p, cond):
    return p is not None and CLIENT_SPECIAL_CONDITION_NAMES[cond] in (p.get_attribute(AttrID.SPECIAL_CONDITIONS) or [])


async def _strange_reaction(ctx):
    """30; if the opponent's Active is Confused, it is now Paralyzed."""
    await ctx.deal_damage()
    d = ctx.opponent_active()
    if _has_cond(d, SpecialConditions.CONFUSED):
        await ctx.apply_special_condition(d, SpecialConditions.PARALYZED)


card = PokemonCardDef(
    guid="3059cb29-cc3c-53ee-af6b-4dd7d027d37e",
    key="XY11",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Amoonguss.Name",
    display_name="Amoonguss",
    searchable_by=["Amoonguss", "Stage 1", "Amoonguss"],
    subtypes=["Stage 1"],
    collector_number=13,
    set_code="XY11",
    rarity=Rarities.Rare,
    hp=90,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Foongus.Name",
    family_id=590,
    abilities=[
        Attack(
            title="Crazy Spore",
            game_text="Your opponent's Active Pok\u00e9mon is now Confused and Poisoned.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=condition_attack(SpecialConditions.CONFUSED, SpecialConditions.POISONED),
        ),
        Attack(
            title="Strange Reaction",
            game_text="If your opponent's Active Pok\u00e9mon is Confused, it is now Paralyzed.",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
            effect=_strange_reaction,
        ),
    ],
)