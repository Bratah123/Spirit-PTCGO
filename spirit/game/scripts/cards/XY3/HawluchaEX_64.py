from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.pokemon import in_active_spot
from spirit.game.card_effects.attacks_common import bonus_if


async def rough_skin(ctx):
    """Active only: put 2 damage counters on Attacking Pokemon."""
    if not in_active_spot(ctx.board, ctx.player_id, ctx.source):
        return
    attacker = ctx.damaged_by
    if attacker is None:
        return
    await ctx.deal_damage(20, target=attacker, apply_modifiers=False, as_counters=True)


card = PokemonCardDef(
    guid="118c19a7-bb73-5598-8f15-b732a9510c1d",
    key="XY3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.HawluchaEX.Name",
    display_name="Hawlucha-EX",
    searchable_by=["Hawlucha-EX", "Basic", "EX", "HawluchaEX"],
    subtypes=["Basic", "EX"],
    collector_number=64,
    set_code="XY3",
    rarity=Rarities.RareHoloEX,
    hp=130,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=20,
    family_id=701,
    abilities=[
        Ability(
            title="Counterattack",
            game_text="If this Pok\u00e9mon is your Active Pok\u00e9mon and is damaged by an opponent's attack (even if this Pok\u00e9mon is Knocked Out), put 2 damage counters on the Attacking Pok\u00e9mon.",
            trigger=Triggers.ON_DAMAGED_BY_ATTACK,
            effect=rough_skin,
        ),
        Attack(
            title="Moonsault Stomp",
            game_text="If there is any Stadium card in play, this attack does 40 more damage.",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 2},
            damage=60,
            damage_operator="+",
            effect=bonus_if(lambda ctx: ctx.stadium_in_play() is not None, 40),
        ),
    ],
)