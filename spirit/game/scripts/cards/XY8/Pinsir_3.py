from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.session.passives import effective_retreat_cost
from spirit.game.card_effects.attacks_common import snipe_attack


async def _iron_crash(ctx):
    """20 more damage for each Colorless in the opponent's Active's Retreat Cost."""
    target = ctx.opponent_active()
    cost = effective_retreat_cost(ctx.board, target) if target is not None else 0
    await ctx.deal_damage(ctx.ability.damage + 20 * cost)


card = PokemonCardDef(
    guid="48cc0d19-2615-564e-91a7-5860dfc7fe90",
    key="XY8",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Pinsir.Name",
    display_name="Pinsir",
    searchable_by=["Pinsir", "Basic", "Pinsir"],
    subtypes=["Basic"],
    collector_number=3,
    set_code="XY8",
    rarity=Rarities.Uncommon,
    hp=100,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    family_id=127,
    abilities=[
        Attack(
            title="Overhead Throw",
            game_text="This attack does 20 damage to 1 of your Benched Pok\u00e9mon. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.GRASS: 1},
            damage=30,
            effect=snipe_attack(20, side='mine', also_base=True),
        ),
        Attack(
            title="Heavy Suplex",
            game_text="This attack does 20 more damage for each Colorless in your opponent's Active Pok\u00e9mon's Retreat Cost.",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 2},
            damage=40,
            damage_operator="+",
            effect=_iron_crash,
        ),
    ],
)