from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import flip_or_nothing


async def pry(ctx):
    """10 damage. Your opponent reveals their hand."""
    await ctx.deal_damage()
    await ctx.reveal_hand(of_player=ctx.opponent_id)


card = PokemonCardDef(
    guid="11a2367a-4555-50a3-a52b-cf6500b4c064",
    key="Promo_SM",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.DetectivePikachu.Name",
    display_name="Detective Pikachu",
    searchable_by=["Detective Pikachu", "Basic", "DetectivePikachu"],
    subtypes=["Basic"],
    collector_number=170,
    set_code="Promo_SM",
    rarity=Rarities.RarePromo,
    hp=90,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    resistance_type=PokemonTypes.METAL,
    resistance_amount=20,
    family_id=25,
    abilities=[
        Attack(
            title="Scout",
            game_text="Your opponent reveals their hand.",
            cost={PokemonTypes.LIGHTNING: 1},
            effect=pry,
        ),
        Attack(
            title="Surprise Attack",
            game_text="Flip a coin. If tails, this attack does nothing.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=80,
            effect=flip_or_nothing(),
        ),
    ],
)