from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import flip_damage, count_energy
from spirit.game.session.passives import effective_retreat_cost

from spirit.game.session.passives import effective_retreat_cost


async def heavy_slam(ctx):
    """200 minus 30 for each Colorless in the Defending Pokémon's Retreat Cost."""
    defender = ctx.defender
    cost = effective_retreat_cost(ctx.board, defender) if defender is not None else 0
    amount = max(0, 200 - 30 * cost)
    if amount > 0:
        await ctx.deal_damage(amount)


card = PokemonCardDef(
    guid="03206966-be57-51e2-b229-a5130ecf4455",
    key="SM2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.AlolanGolem.Name",
    display_name="Alolan Golem",
    searchable_by=["Alolan Golem", "Stage 2", "AlolanGolem"],
    subtypes=["Stage 2"],
    collector_number=42,
    set_code="SM2",
    rarity=Rarities.RareHolo,
    hp=160,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.STAGE2,
    retreat_cost=4,
    weakness_type=PokemonTypes.FIGHTING,
    resistance_type=PokemonTypes.METAL,
    resistance_amount=20,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.AlolanGraveler.Name",
    family_id=74,
    abilities=[
        Attack(
            title="Electromagnetic Rock Wrecker",
            game_text="Flip a coin for each Lightning Energy attached to this Pok\u00e9mon. This attack does 80 damage for each heads.",
            cost={PokemonTypes.LIGHTNING: 1, PokemonTypes.COLORLESS: 2},
            damage=80,
            damage_operator="x",
            effect=flip_damage(coins_from=count_energy('self', PokemonTypes.LIGHTNING), per_heads=80),
        ),
        Attack(
            title="Heavy Slam",
            game_text="This attack does 30 less damage for each Colorless in your opponent's Active Pok\u00e9mon's Retreat Cost.",
            cost={PokemonTypes.LIGHTNING: 1, PokemonTypes.COLORLESS: 3},
            damage=200,
            damage_operator="-",
            effect=heavy_slam,
        ),
    ],
)