from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities


async def _destiny_burst(ctx):
    """Knocked Out as the Active by damage from an opponent's attack: flip a
    coin; heads -> put 5 damage counters on the Attacking Pokemon."""
    if not ctx.ko_from_attack or ctx.ko_attacker is None:
        return
    active_area = ctx.board.find_player_area(ctx.player_id, "activePokemonArea")
    if active_area is not None and active_area.children:
        return  # was Benched, not Active, when Knocked Out
    results = await ctx.flip_coins(1, "Destiny Burst")
    if results and results[0]:
        await ctx.deal_damage(50, target=ctx.ko_attacker, apply_modifiers=False,
                              is_attack=False, as_counters=True)


card = PokemonCardDef(
    guid="e26087cc-fcf2-5030-b402-1a68f18d72dd",
    key="XY1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Voltorb.Name",
    display_name="Voltorb",
    searchable_by=["Voltorb", "Basic", "Voltorb"],
    subtypes=["Basic"],
    collector_number=44,
    set_code="XY1",
    rarity=Rarities.Common,
    hp=50,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=100,
    abilities=[
        Ability(
            title="Destiny Burst",
            game_text="If this Pok\u00e9mon is your Active Pok\u00e9mon and is Knocked Out by damage from an opponent's attack, flip a coin. If heads, put 5 damage counters on the Attacking Pok\u00e9mon.",
            trigger=Triggers.ON_KNOCKED_OUT,
            effect=_destiny_burst,
        ),
        Attack(
            title="Rollout",
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
        ),
    ],
)