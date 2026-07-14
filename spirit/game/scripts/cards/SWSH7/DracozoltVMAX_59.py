from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities


async def spark_trap_retaliate(ctx):
    """During your opponent's next turn, if this Pokémon is damaged by an
    attack (even if it is Knocked Out), put 12 damage counters on the
    Attacking Pokémon."""
    if not ctx.attack_used_last_turn(title="Spark Trap", entity=ctx.source):
        return
    attacker = ctx.damaged_by
    if attacker is None:
        return
    await ctx.deal_damage(120, target=attacker, apply_modifiers=False, as_counters=True)


card = PokemonCardDef(
    guid="5b7b04b5-a3c5-5ccd-ba18-94478c957ca6",
    key="SWSH7",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.DracozoltVMAX.Name",
    display_name="Dracozolt VMAX",
    searchable_by=["Dracozolt VMAX", "VMAX", "DracozoltVMAX"],
    subtypes=["VMAX"],
    collector_number=59,
    set_code="SWSH7",
    rarity=Rarities.RareHoloVMAX,
    hp=330,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.VMAX,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.DracozoltV.Name",
    family_id=880,
    abilities=[
        Attack(
            title="Spark Trap",
            game_text="During your opponent's next turn, if this Pok\u00e9mon is damaged by an attack (even if it is Knocked Out), put 12 damage counters on the Attacking Pok\u00e9mon.",
            cost={PokemonTypes.LIGHTNING: 1},
            damage=60,
        ),
        Ability(
            title="Spark Trap",
            game_text="During your opponent's next turn, if this Pok\u00e9mon is damaged by an attack (even if it is Knocked Out), put 12 damage counters on the Attacking Pok\u00e9mon.",
            trigger=Triggers.ON_DAMAGED_BY_ATTACK,
            effect=spark_trap_retaliate,
        ),
        Attack(
            title="Max Impact",
            cost={PokemonTypes.LIGHTNING: 1, PokemonTypes.COLORLESS: 3},
            damage=200,
        ),
    ],
)