from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AttrID
from spirit.game.card_effects.attacks_common import place_counters


async def spiteful_magic(ctx):
    """If this Pokemon was at full HP and this attack knocks it out, put 8
    damage counters on the Attacking Pokemon."""
    if ctx.pre_hit_hp != ctx.max_hp(ctx.source):
        return
    if ctx.source.get_attribute(AttrID.HP, 0) > 0:
        return
    if ctx.damaged_by is not None:
        await ctx.deal_damage(80, target=ctx.damaged_by, apply_modifiers=False,
                              as_counters=True)

card = PokemonCardDef(
    guid="2f8c2153-b3e9-5196-9727-d6be25444dfe",
    key="SWSH12",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Mismagius.Name",
    display_name="Mismagius",
    searchable_by=["Mismagius", "Stage 1", "Mismagius"],
    subtypes=["Stage 1"],
    collector_number=64,
    set_code="SWSH12",
    rarity=Rarities.Rare,
    hp=90,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Misdreavus.Name",
    family_id=200,
    abilities=[
        Ability(
            title="Spiteful Magic",
            game_text="If this Pok\u00e9mon has full HP and is Knocked Out by damage from an attack from your opponent's Pok\u00e9mon, put 8 damage counters on the Attacking Pok\u00e9mon.",
            trigger=Triggers.ON_DAMAGED_BY_ATTACK,
            effect=spiteful_magic,
        ),
        Attack(
            title="Eerie Voice",
            game_text="Put 2 damage counters on each of your opponent's Pok\u00e9mon.",
            cost={PokemonTypes.PSYCHIC: 1},
            effect=place_counters(2, "each_opponent"),
        ),
    ],
)