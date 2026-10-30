from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.pokemon import energy_provides_type


async def _frosty_thunder(ctx):
    """120; with any Lightning Energy attached, 20 to each opposing Benched Pokemon."""
    await ctx.deal_damage()
    if any(energy_provides_type(e, PokemonTypes.LIGHTNING.value) for e in ctx.attached_energies(ctx.attacker)):
        for p in ctx.opponent_bench():
            await ctx.deal_damage(20, target=p, apply_modifiers=False)


card = PokemonCardDef(
    guid="e77c48f4-aa04-5e64-8fec-632fab591288",
    key="Promo_XY",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.BlackKyurem.Name",
    display_name="Black Kyurem",
    searchable_by=["Black Kyurem", "Basic", "BlackKyurem"],
    subtypes=["Basic"],
    collector_number=160,
    set_code="Promo_XY",
    rarity=Rarities.RarePromo,
    hp=130,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.METAL,
    family_id=646,
    abilities=[
        Attack(
            title="Ice Wing",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 2},
            damage=60,
        ),
        Attack(
            title="Frosty Thunder",
            game_text="If this Pok\u00e9mon has any Lightning Energy attached to it, this attack does 20 damage to each of your opponent's Benched Pok\u00e9mon. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.WATER: 2, PokemonTypes.COLORLESS: 2},
            damage=120,
            effect=_frosty_thunder,
        ),
    ],
)