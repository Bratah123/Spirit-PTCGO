from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AttrID
from spirit.game.card_effects.passives_common import takes_less_passive


def _fire_or_water(pokemon):
    types = pokemon.get_attribute(AttrID.POKEMON_TYPES) or []
    return PokemonTypes.FIRE.value in types or PokemonTypes.WATER.value in types


async def _primordial_boom(ctx):
    """80+; +40 if you have a Stadium in play; heal 40 from this Pokemon if your opponent has one."""
    stadium = ctx.stadium_in_play()
    mine = stadium is not None and stadium.owning_player_id == ctx.player_id
    await ctx.deal_damage(ctx.ability.damage + (40 if mine else 0))
    if stadium is not None and stadium.owning_player_id == ctx.opponent_id:
        await ctx.heal(40, ctx.attacker)


card = PokemonCardDef(
    guid="6988e9da-fd28-5a5f-aae6-26263ed0d768",
    key="XY8",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Mamoswine.Name",
    display_name="Mamoswine",
    searchable_by=["Mamoswine", "Stage 2", "Mamoswine"],
    subtypes=["Stage 2"],
    collector_number=82,
    set_code="XY8",
    rarity=Rarities.RareHolo,
    hp=160,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE2,
    retreat_cost=4,
    weakness_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Piloswine.Name",
    family_id=220,
    abilities=[
        Ability(
            title="Thick Fat",
            game_text="Any damage done to this Pok\u00e9mon by attacks from your opponent's Fire or Water Pok\u00e9mon is reduced by 30 (after applying Weakness and Resistance).",
            passive=takes_less_passive(30, attacker_pred=_fire_or_water),
        ),
        Attack(
            title="Primordial Boom",
            game_text="If you have a Stadium card in play, this attack does 40 more damage. If your opponent has a Stadium card in play, heal 40 damage from this Pok\u00e9mon.",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 3},
            damage=80,
            damage_operator="+",
            effect=_primordial_boom,
        ),
    ],
)