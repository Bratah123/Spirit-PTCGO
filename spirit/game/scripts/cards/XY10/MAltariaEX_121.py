from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.session.effects import is_special_energy


async def _mist_purge(ctx):
    """100+; with any Special Energy attached: 30 more and heal 30 from each of your Pokemon."""
    special = any(is_special_energy(e) for e in ctx.attached_energies(ctx.attacker))
    await ctx.deal_damage(ctx.ability.damage + (30 if special else 0))
    if special:
        for p in ctx.my_pokemon_in_play():
            await ctx.heal(30, p)


card = PokemonCardDef(
    guid="125ba607-173f-5658-95be-0e7e87653894",
    key="XY10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.MAltariaEX.Name",
    display_name="M Altaria-EX",
    searchable_by=["M Altaria-EX", "MEGA", "EX", "MAltariaEX"],
    subtypes=["MEGA", "EX"],
    collector_number=121,
    set_code="XY10",
    rarity=Rarities.RareUltra,
    hp=220,
    elements=[PokemonTypes.FAIRY],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.METAL,
    resistance_type=PokemonTypes.DARKNESS,
    resistance_amount=20,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.AltariaEX.Name",
    family_id=334,
    abilities=[
        Attack(
            title="Mist Purge",
            game_text="If this Pok\u00e9mon has any Special Energy attached to it, this attack does 30 more damage and heal 30 damage from each of your Pok\u00e9mon.",
            cost={PokemonTypes.FAIRY: 1, PokemonTypes.COLORLESS: 2},
            damage=100,
            damage_operator="+",
            effect=_mist_purge,
        ),
    ],
)