from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AttrID


async def recover(ctx):
    """Discard an Energy from this Pokemon and heal all damage from it."""
    picks = await ctx.discard_energy_from(ctx.source, 1, prompt="Discard an Energy from Frillish")
    if not picks:
        return
    pokemon = ctx.source
    await ctx.heal(ctx.max_hp(pokemon) - pokemon.get_attribute(AttrID.HP, 0), pokemon)


card = PokemonCardDef(
    guid="8e118592-fd9a-5428-8434-5b480f7c206a",
    key="SWSH5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Frillish.Name",
    display_name="Frillish",
    searchable_by=["Frillish", "Basic", "Frillish"],
    subtypes=["Basic"],
    collector_number=41,
    set_code="SWSH5",
    rarity=Rarities.Common,
    hp=80,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.LIGHTNING,
    family_id=592,
    abilities=[
        Attack(
            title="Recover",
            game_text="Discard an Energy from this Pok\u00e9mon and heal all damage from it.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=recover,
        ),
        Attack(
            title="Rain Splash",
            cost={PokemonTypes.WATER: 1},
            damage=10,
        ),
    ],
)