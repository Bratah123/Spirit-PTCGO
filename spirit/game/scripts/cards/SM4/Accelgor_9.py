from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.attributes import AttrID


async def recover(ctx):
    """Discard an Energy from this Pokemon and heal all damage from it."""
    picks = await ctx.discard_energy_from(ctx.source, 1, prompt="Discard an Energy from Frillish")
    if not picks:
        return
    pokemon = ctx.source
    await ctx.heal(ctx.max_hp(pokemon) - pokemon.get_attribute(AttrID.HP, 0), pokemon)


card = PokemonCardDef(
    guid="c530de71-fbff-5f12-bd08-4654d5a873c1",
    key="SM4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Accelgor.Name",
    display_name="Accelgor",
    searchable_by=["Accelgor", "Stage 1", "Accelgor"],
    subtypes=["Stage 1"],
    collector_number=9,
    set_code="SM4",
    rarity=Rarities.Uncommon,
    hp=90,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Shelmet.Name",
    family_id=616,
    abilities=[
        Attack(
            title="Recover",
            game_text="Discard an Energy from this Pok\u00e9mon and heal all damage from it.",
            cost={PokemonTypes.COLORLESS: 1},
            # STUB: attack effect not implemented
            effect=recover,
        ),
        Attack(
            title="Speed Attack",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 1},
            damage=70,
        ),
    ],
)