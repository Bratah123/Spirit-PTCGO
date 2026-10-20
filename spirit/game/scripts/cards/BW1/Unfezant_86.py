from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import flip_or_nothing
from spirit.game.card_effects.passives_common import apply_protection


async def _fly_success(ctx):
    await ctx.deal_damage()
    await apply_protection(ctx, prevent=True, effects_too=True)


card = PokemonCardDef(
    guid="e8b6140f-26dc-56ed-b8bd-2eabdc09e0b3",
    key="BW1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Unfezant.Name",
    display_name="Unfezant",
    searchable_by=["Unfezant", "Stage 2", "Unfezant"],
    subtypes=["Stage 2"],
    collector_number=86,
    set_code="BW1",
    rarity=Rarities.Rare,
    hp=120,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE2,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=20,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Tranquill.Name",
    family_id=519,
    abilities=[
        Attack(
            title="Fly",
            game_text="Flip a coin. If tails, this attack does nothing. If heads, prevent all effects of attacks, including damage, done to this Pok\u00e9mon during your opponent's next turn.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=50,
            effect=flip_or_nothing(then=_fly_success),
        ),
        Attack(
            title="Cutting Wind",
            cost={PokemonTypes.COLORLESS: 3},
            damage=70,
        ),
    ],
)
