from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, SpecialConditions
from spirit.game.card_effects.attacks_common import condition_attack, flip_or_nothing
from spirit.game.card_effects.passives_common import apply_protection


async def _fly_success(ctx):
    await ctx.deal_damage()
    await apply_protection(ctx, prevent=True, effects_too=True)


card = PokemonCardDef(
    guid="0d4f071a-3819-53f6-9aa3-b1dc8131a04a",
    key="XY12",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.FlyingPikachu.Name",
    display_name="Flying Pikachu",
    searchable_by=["Flying Pikachu", "Basic", "FlyingPikachu"],
    subtypes=["Basic"],
    collector_number=110,
    set_code="XY12",
    rarity=Rarities.RareSecret,
    hp=40,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=20,
    family_id=25,
    abilities=[
        Attack(
            title="Thunder Shock",
            game_text="Flip a coin. If heads, your opponent's Active Pok\u00e9mon is now Paralyzed.",
            cost={PokemonTypes.LIGHTNING: 1},
            damage=10,
            effect=condition_attack(SpecialConditions.PARALYZED, flip=True),
        ),
        Attack(
            title="Fly",
            game_text="Flip a coin. If tails, this attack does nothing. If heads, prevent all effects of attacks, including damage, done to this Pok\u00e9mon during your opponent's next turn.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=30,
            effect=flip_or_nothing(then=_fly_success),
        ),
    ],
)