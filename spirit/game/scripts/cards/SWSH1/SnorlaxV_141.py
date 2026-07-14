from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, SpecialConditions
from spirit.game.card_effects.attacks_common import condition_attack


async def swallow(ctx):
    """Heal from this Pokemon the same amount of damage dealt to the Active."""
    dealt = await ctx.deal_damage()
    if dealt:
        await ctx.heal(dealt, target=ctx.attacker)

card = PokemonCardDef(
    guid="0782209a-a452-56a2-a139-627e4076a465",
    key="SWSH1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.SnorlaxV.Name",
    display_name="Snorlax V",
    searchable_by=["Snorlax V", "Basic", "V", "SnorlaxV"],
    subtypes=["Basic", "V"],
    collector_number=141,
    set_code="SWSH1",
    rarity=Rarities.RareHoloV,
    hp=220,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=4,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=143,
    abilities=[
        Attack(
            title="Swallow",
            game_text="Heal from this Pok\u00e9mon the same amount of damage you did to your opponent's Active Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=60,
            effect=swallow,
        ),
        Attack(
            title="Falling Down",
            game_text="This Pok\u00e9mon is now Asleep.",
            cost={PokemonTypes.COLORLESS: 4},
            damage=170,
            effect=condition_attack(self_conditions=(SpecialConditions.ASLEEP,)),
        ),
    ],
)