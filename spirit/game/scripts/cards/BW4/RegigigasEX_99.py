from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import damage_counters_on, damage_per


async def superpower(ctx):
    """You may do 20 more damage; if you do, this Pokémon does 20 to itself."""
    if await ctx.ask_yes_no(
        "Do 20 more damage? If you do, this Pokémon does 20 damage to itself."
    ):
        await ctx.deal_damage(80)
        await ctx.deal_damage(20, target=ctx.attacker, apply_modifiers=False)
    else:
        await ctx.deal_damage(60)


card = PokemonCardDef(
    guid="9f4abc6a-87ae-5fee-b40a-9d8f0fae55c0",
    key="BW4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.RegigigasEX.Name",
    display_name="Regigigas-EX",
    searchable_by=["Regigigas-EX", "Basic", "EX", "RegigigasEX"],
    subtypes=["Basic", "EX"],
    collector_number=99,
    set_code="BW4",
    rarity=Rarities.RareUltra,
    hp=180,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=4,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=486,
    abilities=[
        Attack(
            title="Giga Power",
            game_text="You may do 20 more damage. If you do, this Pok\u00e9mon does 20 damage to itself.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=60,
            damage_operator="+",
            effect=superpower,
        ),
        Attack(
            title="Raging Hammer",
            game_text="Does 10 more damage for each damage counter on this Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 4},
            damage=50,
            damage_operator="+",
            effect=damage_per(damage_counters_on('self'), 10, base=50),
        ),
    ],
)