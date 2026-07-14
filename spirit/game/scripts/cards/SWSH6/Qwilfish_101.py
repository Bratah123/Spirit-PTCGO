from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, SpecialConditions
from spirit.game.card_effects.attacks_common import condition_attack


async def bursting_needles(ctx):
    """Active Spot only: if Knocked Out by damage from an opponent's
    attack, put 6 damage counters on the Attacking Pokemon."""
    if not ctx.ko_from_attack:
        return
    active_area = ctx.board.find_player_area(ctx.player_id, "activePokemonArea")
    if active_area is not None and active_area.children:
        return  # was Benched, not Active, when Knocked Out
    attacker = ctx.ko_attacker
    if attacker is None:
        return
    await ctx.deal_damage(60, target=attacker, apply_modifiers=False, as_counters=True)


card = PokemonCardDef(
    guid="ccde68b7-8315-5808-9efb-b4ba23242fa8",
    key="SWSH6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Qwilfish.Name",
    display_name="Qwilfish",
    searchable_by=["Qwilfish", "Basic", "Single Strike", "Qwilfish"],
    subtypes=["Basic", "Single Strike"],
    collector_number=101,
    set_code="SWSH6",
    rarity=Rarities.Common,
    hp=90,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=211,
    abilities=[
        Ability(
            title="Bursting Needles",
            game_text="If this Pok\u00e9mon is in the Active Spot and is Knocked Out by damage from an attack from your opponent's Pok\u00e9mon, put 6 damage counters on the Attacking Pok\u00e9mon.",
            trigger=Triggers.ON_KNOCKED_OUT,
            effect=bursting_needles,
        ),
        Attack(
            title="Poison Jab",
            game_text="Your opponent's Active Pok\u00e9mon is now Poisoned.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=30,
            effect=condition_attack(SpecialConditions.POISONED),
        ),
    ],
)