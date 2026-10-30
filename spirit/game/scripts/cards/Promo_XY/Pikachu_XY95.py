from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import flip_bonus


async def _eat_together(ctx):
    """Heal 30 damage from both Active Pokemon."""
    for p in (ctx.my_active(), ctx.opponent_active()):
        if p is not None:
            await ctx.heal(30, p)


card = PokemonCardDef(
    guid="550acada-7939-5436-b5c7-16e0c743e111",
    key="Promo_XY",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Pikachu.Name",
    display_name="Pikachu",
    searchable_by=["Pikachu", "Basic", "Pikachu"],
    subtypes=["Basic"],
    collector_number=95,
    set_code="Promo_XY",
    rarity=Rarities.RarePromo,
    hp=60,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    resistance_type=PokemonTypes.METAL,
    resistance_amount=20,
    family_id=25,
    abilities=[
        Attack(
            title="Let's Eat Together",
            game_text="Heal 30 damage from both Active Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=_eat_together,
        ),
        Attack(
            title="Quick Attack",
            game_text="Flip a coin. If heads, this attack does 20 more damage.",
            cost={PokemonTypes.LIGHTNING: 1, PokemonTypes.COLORLESS: 1},
            damage=10,
            damage_operator="+",
            effect=flip_bonus(20),
        ),
    ],
)