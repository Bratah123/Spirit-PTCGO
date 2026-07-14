from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import has_tool


async def leek_strike(ctx):
    tooled = has_tool(ctx.attacker)
    await ctx.deal_damage(70 + (90 if tooled else 0), ignore_resistance=tooled)


card = PokemonCardDef(
    guid="e64ac4a8-abea-5946-aabb-5a8a8cbecb16",
    key="SWSH6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.GalarianSirfetchd.Name",
    display_name="Galarian Sirfetch'd",
    searchable_by=["Galarian Sirfetch'd", "Stage 1", "Single Strike", "GalarianSirfetchd"],
    subtypes=["Stage 1", "Single Strike"],
    collector_number=79,
    set_code="SWSH6",
    rarity=Rarities.Rare,
    hp=130,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.PSYCHIC,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.GalarianFarfetchd.Name",
    family_id=83,
    abilities=[
        Attack(
            title="Peck",
            cost={PokemonTypes.FIGHTING: 1},
            damage=40,
        ),
        Attack(
            title="Leek Strike",
            game_text="If this Pok\u00e9mon has a Pok\u00e9mon Tool attached, this attack does 90 more damage, and this attack's damage isn't affected by Resistance.",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 2},
            damage=70,
            damage_operator="+",
            effect=leek_strike,
        ),
    ],
)