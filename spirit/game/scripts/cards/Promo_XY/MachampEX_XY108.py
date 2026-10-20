from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AttrID


async def _crazy_hammer(ctx):
    """80+; +80 if this Pokemon has a Special Condition, then remove them all."""
    affected = bool(ctx.attacker.get_attribute(AttrID.SPECIAL_CONDITIONS) or [])
    await ctx.deal_damage(ctx.ability.damage + (80 if affected else 0))
    if affected:
        await ctx.cure_all_conditions(ctx.attacker)


card = PokemonCardDef(
    guid="fad59901-27ad-535c-8a78-26899cd0a222",
    key="Promo_XY",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.MachampEX.Name",
    display_name="Machamp-EX",
    searchable_by=["Machamp-EX", "Basic", "EX", "MachampEX"],
    subtypes=["Basic", "EX"],
    collector_number=108,
    set_code="Promo_XY",
    rarity=Rarities.RarePromo,
    hp=180,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=68,
    abilities=[
        Attack(
            title="Steaming Mad",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 1},
            damage=20,
            damage_operator="x",
        ),
        Attack(
            title="Crazy Hammer",
            game_text="If this Pok\u00e9mon is affected by a Special Condition, this attack does 80 more damage. Then, remove all Special Conditions from this Pok\u00e9mon.",
            cost={PokemonTypes.FIGHTING: 2, PokemonTypes.COLORLESS: 1},
            damage=80,
            damage_operator="+",
            effect=_crazy_hammer,
        ),
    ],
)