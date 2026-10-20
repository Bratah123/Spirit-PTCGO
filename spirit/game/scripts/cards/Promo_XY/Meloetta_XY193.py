from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, SpecialConditions
from spirit.game.card_effects.attacks_common import condition_attack


async def phat_sound(ctx):
    """Flip 3 coins. 10×heads to each of opponent's Pokémon (no W/R on bench)."""
    results = await ctx.flip_coins(3, ctx.ability.title)
    amount = 10 * sum(1 for r in results if r)
    if amount <= 0:
        return
    for p in ctx.opponent_pokemon_in_play():
        await ctx.deal_damage(amount, target=p, apply_modifiers=None)


card = PokemonCardDef(
    guid="c1e74244-e058-5369-a34b-5d87f97e8170",
    key="Promo_XY",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Meloetta.Name",
    display_name="Meloetta",
    searchable_by=["Meloetta", "Basic", "Meloetta"],
    subtypes=["Basic"],
    collector_number=193,
    set_code="Promo_XY",
    rarity=Rarities.RarePromo,
    hp=80,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=648,
    abilities=[
        Attack(
            title="Soprano Wave",
            game_text="Flip 3 coins. This attack does 10 damage times the number of heads to each of your opponent's Pok\u00e9mon. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.PSYCHIC: 1},
            effect=phat_sound,
        ),
        Attack(
            title="Entrancing Melody",
            game_text="Your opponent's Active Pok\u00e9mon is now Confused.",
            cost={PokemonTypes.PSYCHIC: 2},
            damage=30,
            effect=condition_attack(SpecialConditions.CONFUSED),
        ),
    ],
)