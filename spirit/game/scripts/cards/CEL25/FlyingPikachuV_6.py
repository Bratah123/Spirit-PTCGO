from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, SpecialConditions
from spirit.game.card_effects.attacks_common import condition_attack, flip_or_nothing
from spirit.game.card_effects.passives_common import apply_protection


async def _fly_success(ctx):
    await ctx.deal_damage()
    await apply_protection(ctx, prevent=True, effects_too=True)


card = PokemonCardDef(
    guid="f13a80b5-f37a-54ae-8277-1ed8c8cc6e15",
    key="CEL25",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.FlyingPikachuV.Name",
    display_name="Flying Pikachu V",
    searchable_by=["Flying Pikachu V", "Basic", "V", "FlyingPikachuV"],
    subtypes=["Basic", "V"],
    collector_number=6,
    set_code="CEL25",
    rarity=Rarities.RareHoloV,
    hp=190,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=0,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    family_id=25,
    abilities=[
        Attack(
            title="Thunder Shock",
            game_text="Flip a coin. If heads, your opponent's Active Pokémon is now Paralyzed.",
            cost={PokemonTypes.LIGHTNING: 1},
            damage=20,
            effect=condition_attack(SpecialConditions.PARALYZED, flip=True),
        ),
        Attack(
            title="Fly",
            game_text="Flip a coin. If tails, this attack does nothing. If heads, during your opponent's next turn, prevent all damage from and effects of attacks done to this Pokémon.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=120,
            effect=flip_or_nothing(then=_fly_success),
        ),
    ],
)
