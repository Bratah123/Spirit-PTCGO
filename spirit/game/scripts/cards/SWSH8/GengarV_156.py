from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, SpecialConditions
from spirit.game.card_effects.attacks_common import condition_attack


async def pain_explosion(ctx):
    """190 damage; put 3 damage counters on this Pokemon."""
    await ctx.deal_damage()
    await ctx.deal_damage(30, target=ctx.attacker, apply_modifiers=False, as_counters=True)


card = PokemonCardDef(
    guid="775bf90d-367b-5c15-8120-1fc1b29570ec",
    key="SWSH8",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.GengarV.Name",
    display_name="Gengar V",
    searchable_by=["Gengar V", "Basic", "V", "Single Strike", "GengarV"],
    subtypes=["Basic", "V", "Single Strike"],
    collector_number=156,
    set_code="SWSH8",
    rarity=Rarities.RareHoloV,
    hp=210,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=94,
    abilities=[
        Attack(
            title="Dark Slumber",
            game_text="Your opponent's Active Pok\u00e9mon is now Asleep.",
            cost={PokemonTypes.DARKNESS: 2},
            damage=40,
            effect=condition_attack(SpecialConditions.ASLEEP),
        ),
        Attack(
            title="Pain Explosion",
            game_text="Put 3 damage counters on this Pok\u00e9mon.",
            cost={PokemonTypes.DARKNESS: 3},
            damage=190,
            effect=pain_explosion,
        ),
    ],
)