from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import flip_damage
from spirit.game.card_effects.pokemon import energy_provides_type


async def _overspark(ctx):
    """Discard all Lightning Energy from this Pokemon: 50 times the number discarded."""
    pool = [e for e in ctx.attached_energies(ctx.attacker)
            if energy_provides_type(e, PokemonTypes.LIGHTNING.value)]
    if not pool:
        return
    await ctx.discard_cards(pool)
    await ctx.deal_damage(50 * len(pool))


card = PokemonCardDef(
    guid="c8d3348f-6acc-51a2-a039-04ec2a651617",
    key="Promo_XY",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.PikachuEX.Name",
    display_name="Pikachu-EX",
    searchable_by=["Pikachu-EX", "Basic", "EX", "PikachuEX"],
    subtypes=["Basic", "EX"],
    collector_number=84,
    set_code="Promo_XY",
    rarity=Rarities.RarePromo,
    hp=130,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    resistance_type=PokemonTypes.METAL,
    resistance_amount=20,
    family_id=25,
    abilities=[
        Attack(
            title="Iron Tail",
            game_text="Flip a coin until you get tails. This attack does 30 damage times the number of heads.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=30,
            damage_operator="x",
            effect=flip_damage(until_tails=True, per_heads=30),
        ),
        Attack(
            title="Overspark",
            game_text="Discard all Lightning Energy attached to this Pok\u00e9mon. This attack does 50 damage times the number of Energy cards you discarded.",
            cost={PokemonTypes.LIGHTNING: 1, PokemonTypes.COLORLESS: 2},
            damage=50,
            damage_operator="x",
            effect=_overspark,
        ),
    ],
)