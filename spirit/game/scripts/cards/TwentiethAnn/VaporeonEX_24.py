from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.support_common import heal_attack
from spirit.game.card_effects.attacks_common import damage_counters_on


async def _deep_squall(ctx):
    """130 minus 10 for each damage counter on this Pokemon."""
    await ctx.deal_damage(max(0, 130 - 10 * damage_counters_on('self')(ctx)))


card = PokemonCardDef(
    guid="60c67b7c-6637-5555-9abd-b5ed450612bb",
    key="TwentiethAnn",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.VaporeonEX.Name",
    display_name="Vaporeon-EX",
    searchable_by=["Vaporeon-EX", "Basic", "EX", "VaporeonEX"],
    subtypes=["Basic", "EX"],
    collector_number=24,
    set_code="TwentiethAnn",
    rarity=Rarities.RareHoloEX,
    hp=180,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.GRASS,
    family_id=134,
    abilities=[
        Attack(
            title="Bubble Drain",
            game_text="Heal 30 damage from this Pok\u00e9mon.",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
            effect=heal_attack(30),
        ),
        Attack(
            title="Deep Squall",
            game_text="This attack does 130 damage minus 10 damage for each damage counter on this Pok\u00e9mon.",
            cost={PokemonTypes.WATER: 2, PokemonTypes.COLORLESS: 1},
            damage=130,
            damage_operator="-",
            effect=_deep_squall,
        ),
    ],
)