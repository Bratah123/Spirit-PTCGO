from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, SpecialConditions
from spirit.game.card_effects.pokemon import in_active_spot
from spirit.game.card_effects.attacks_common import condition_attack


async def rough_skin(ctx):
    """Active only: put 2 damage counters on Attacking Pokemon."""
    if not in_active_spot(ctx.board, ctx.player_id, ctx.source):
        return
    attacker = ctx.damaged_by
    if attacker is None:
        return
    await ctx.deal_damage(20, target=attacker, apply_modifiers=False, as_counters=True)


card = PokemonCardDef(
    guid="3d373731-726e-51cd-828b-15427d8dd7b8",
    key="XY2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Qwilfish.Name",
    display_name="Qwilfish",
    searchable_by=["Qwilfish", "Basic", "Qwilfish"],
    subtypes=["Basic"],
    collector_number=21,
    set_code="XY2",
    rarity=Rarities.Rare,
    hp=80,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.GRASS,
    family_id=211,
    abilities=[
        Ability(
            title="Counterattack Quills",
            game_text="If this Pok\u00e9mon is your Active Pok\u00e9mon and is damaged by an opponent's attack (even if this Pok\u00e9mon is Knocked Out), put 2 damage counters on the Attacking Pok\u00e9mon.",
            trigger=Triggers.ON_DAMAGED_BY_ATTACK,
            effect=rough_skin,
        ),
        Attack(
            title="Poison Sting",
            game_text="Your opponent's Active Pok\u00e9mon is now Poisoned.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
            effect=condition_attack(SpecialConditions.POISONED),
        ),
    ],
)