from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AttrID
from spirit.game.card_effects.attacks_common import bonus_if


async def _flip_discard_defender_energy(ctx):
    """Printed damage; flip a coin. If heads, discard an Energy attached to
    your opponent's Active Pokemon."""
    await ctx.deal_damage()
    results = await ctx.flip_coins(1, ctx.ability.title)
    target = ctx.opponent_active()
    if results and results[0] and target is not None and not ctx.effects_blocked(target):
        await ctx.discard_energy_from(target, 1, minimum=1,
                                      prompt="Choose an Energy to discard")


def _more_hp(ctx):
    d = ctx.opponent_active()
    return d is not None and int(d.get_attribute(AttrID.HP) or 0) > int(ctx.attacker.get_attribute(AttrID.HP) or 0)


card = PokemonCardDef(
    guid="4aac6493-4980-51bc-aec9-86d2c5ca7d99",
    key="XY11",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Primeape.Name",
    display_name="Primeape",
    searchable_by=["Primeape", "Stage 1", "Primeape"],
    subtypes=["Stage 1"],
    collector_number=53,
    set_code="XY11",
    rarity=Rarities.Rare,
    hp=90,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Mankey.Name",
    family_id=56,
    abilities=[
        Attack(
            title="Swagger",
            game_text="Flip a coin. If heads, discard an Energy attached to your opponent's Active Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=20,
            effect=_flip_discard_defender_energy,
        ),
        Attack(
            title="Spirited Throw",
            game_text="If, before doing damage, your opponent's Active Pok\u00e9mon has more remaining HP than this Pok\u00e9mon, this attack does 60 more damage.",
            cost={PokemonTypes.FIGHTING: 2},
            damage=30,
            damage_operator="+",
            effect=bonus_if(_more_hp, 60),
        ),
    ],
)