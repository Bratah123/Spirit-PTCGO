from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.pokemon import in_active_spot
from spirit.game.card_effects.support_common import heal_attack


async def needle_line(ctx):
    """Active Spot only: if damaged by an opponent's attack (even if
    Knocked Out), put 3 damage counters on the Attacking Pokémon."""
    if not in_active_spot(ctx.board, ctx.player_id, ctx.source):
        return
    attacker = ctx.damaged_by
    if attacker is None:
        return
    await ctx.deal_damage(30, target=attacker, apply_modifiers=False, as_counters=True)


card = PokemonCardDef(
    guid="5a993c9c-cb33-5d6c-9e2e-bf88dad4ef6f",
    key="SWSH12",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.ChesnaughtV.Name",
    display_name="Chesnaught V",
    searchable_by=["Chesnaught V", "Basic", "V", "ChesnaughtV"],
    subtypes=["Basic", "V"],
    collector_number=15,
    set_code="SWSH12",
    rarity=Rarities.RareHoloV,
    hp=230,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=4,
    weakness_type=PokemonTypes.FIRE,
    family_id=652,
    abilities=[
        Ability(
            title="Needle Line",
            game_text="If your Active Chesnaught V is damaged by an attack from your opponent's Pok\u00e9mon (even if it is Knocked Out), put 3 damage counters on the Attacking Pok\u00e9mon.",
            trigger=Triggers.ON_DAMAGED_BY_ATTACK,
            effect=needle_line,
        ),
        Attack(
            title="Touchdown",
            game_text="Heal 30 damage from this Pok\u00e9mon.",
            cost={PokemonTypes.GRASS: 2, PokemonTypes.COLORLESS: 1},
            damage=130,
            effect=heal_attack(30),
        ),
    ],
)