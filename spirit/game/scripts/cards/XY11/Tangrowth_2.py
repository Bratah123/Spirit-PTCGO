from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AttrID
from spirit.game.card_effects.attacks_common import flip_bonus


async def _leaf_storm(ctx):
    """80; heal 40 damage from each of your Grass Pokemon."""
    await ctx.deal_damage()
    for p in ctx.my_pokemon_in_play():
        if PokemonTypes.GRASS.value in (p.get_attribute(AttrID.POKEMON_TYPES) or []):
            await ctx.heal(40, p)


card = PokemonCardDef(
    guid="1fdaf0d7-a7bf-5576-978e-a6c10b994df2",
    key="XY11",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Tangrowth.Name",
    display_name="Tangrowth",
    searchable_by=["Tangrowth", "Stage 1", "Tangrowth"],
    subtypes=["Stage 1"],
    collector_number=2,
    set_code="XY11",
    rarity=Rarities.Uncommon,
    hp=130,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=4,
    weakness_type=PokemonTypes.FIRE,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Tangela.Name",
    family_id=114,
    abilities=[
        Attack(
            title="Leaf Storm",
            game_text="Heal 40 damage from each of your Grass Pok\u00e9mon.",
            cost={PokemonTypes.GRASS: 2, PokemonTypes.COLORLESS: 1},
            damage=80,
            effect=_leaf_storm,
        ),
        Attack(
            title="Flog",
            game_text="Flip a coin. If heads, this attack does 30 more damage.",
            cost={PokemonTypes.GRASS: 3, PokemonTypes.COLORLESS: 1},
            damage=110,
            damage_operator="+",
            effect=flip_bonus(30),
        ),
    ],
)