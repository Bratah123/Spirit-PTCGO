from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import flip_damage
from spirit.game.session.passives import effective_retreat_cost


async def _shoulder_throw(ctx):
    """80 damage minus 20 for each Colorless in the Defending Pokemon's Retreat Cost."""
    d = ctx.defender
    cost = effective_retreat_cost(ctx.board, d) if d is not None else 0
    amount = 80 - 20 * cost
    if amount > 0:
        await ctx.deal_damage(amount)


card = PokemonCardDef(
    guid="ab3c56d2-0a63-5853-a8e7-47326e1a48d6",
    key="BW10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Throh.Name",
    display_name="Throh",
    searchable_by=["Throh", "Basic", "Throh"],
    subtypes=["Basic"],
    collector_number=51,
    set_code="BW10",
    rarity=Rarities.Common,
    hp=100,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=538,
    abilities=[
        Attack(
            title="Freestyle Strike",
            game_text="Flip 2 coins. This attack does 30 damage times the number of heads.",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
            damage_operator="x",
            effect=flip_damage(coins=2, per_heads=30),
        ),
        Attack(
            title="Shoulder Throw",
            game_text="Does 80 damage minus 20 damage for each Colorless in the Defending Pok\u00e9mon's Retreat Cost.",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 2},
            damage=80,
            damage_operator="-",
            effect=_shoulder_throw,
        ),
    ],
)