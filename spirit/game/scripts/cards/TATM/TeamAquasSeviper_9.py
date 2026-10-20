from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, SpecialConditions, AttrID
from spirit.game.card_effects.attacks_common import condition_attack


def _affected(p):
    return p is not None and bool(p.get_attribute(AttrID.SPECIAL_CONDITIONS))


async def _venom_tail(ctx):
    """30; if the opponent's Active is affected by a Special Condition, discard an Energy attached to it."""
    await ctx.deal_damage()
    d = ctx.opponent_active()
    if _affected(d) and ctx.attached_energies(d) and not ctx.effects_blocked(d):
        await ctx.discard_energy_from(d, 1, minimum=1)


card = PokemonCardDef(
    guid="ba7b8ffa-8af8-54f9-a135-3ec608b2590e",
    key="TATM",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.TeamAquasSeviper.Name",
    display_name="Team Aqua's Seviper",
    searchable_by=["Team Aqua's Seviper", "Basic", "TeamAquasSeviper"],
    subtypes=["Basic"],
    collector_number=9,
    set_code="TATM",
    rarity=Rarities.Common,
    hp=90,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=336,
    abilities=[
        Attack(
            title="Venomous Fang",
            game_text="Flip a coin. If heads, your opponent's Active Pok\u00e9mon is now Poisoned.",
            cost={PokemonTypes.PSYCHIC: 1},
            damage=10,
            effect=condition_attack(SpecialConditions.POISONED, flip=True),
        ),
        Attack(
            title="Venom Tail",
            game_text="If your opponent's Active Pok\u00e9mon is affected by a Special Condition, discard an Energy attached to that Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=30,
            effect=_venom_tail,
        ),
    ],
)