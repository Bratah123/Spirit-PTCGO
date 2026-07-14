from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, SpecialConditions
from spirit.game.card_effects.attacks_common import condition_attack


async def piercing_strike(ctx):
    """100 damage, ignoring Weakness, Resistance, and any effects on the opponent's Active."""
    await ctx.deal_damage(apply_modifiers=False, ignore_target_effects=True)

card = PokemonCardDef(
    guid="40754ed9-7817-592b-bd8c-c0a307fbb587",
    key="SWSH5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Mawile.Name",
    display_name="Mawile",
    searchable_by=["Mawile", "Basic", "Single Strike", "Mawile"],
    subtypes=["Basic", "Single Strike"],
    collector_number=100,
    set_code="SWSH5",
    rarity=Rarities.Common,
    hp=90,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.GRASS,
    family_id=303,
    abilities=[
        Attack(
            title="Powerful Vise",
            game_text="Flip a coin. If heads, your opponent's Active Pok\u00e9mon is now Paralyzed.",
            cost={PokemonTypes.METAL: 1},
            damage=20,
            effect=condition_attack(SpecialConditions.PARALYZED, flip=True),
        ),
        Attack(
            title="Piercing Strike",
            game_text="This attack's damage isn't affected by Weakness or Resistance, or by any effects on your opponent's Active Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=100,
            effect=piercing_strike,
        ),
    ],
)