from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import AttrID, PokemonTypes, PokemonStage, Rarities


async def _leaf_storm(ctx):
    await ctx.deal_damage()
    for pokemon in ctx.my_pokemon_in_play():
        types = pokemon.get_attribute(AttrID.POKEMON_TYPES) or []
        if PokemonTypes.GRASS.value in types:
            await ctx.heal(20, pokemon)


card = PokemonCardDef(
    guid="d171baa9-c86c-555f-a13c-9d5c4e20978f",
    key="BW1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Serperior.Name",
    display_name="Serperior",
    searchable_by=["Serperior", "Stage 2", "Serperior"],
    subtypes=["Stage 2"],
    collector_number=5,
    set_code="BW1",
    rarity=Rarities.RareHolo,
    hp=130,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE2,
    retreat_cost=0,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.WATER,
    resistance_amount=20,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Servine.Name",
    family_id=495,
    abilities=[
        Attack(
            title="Vine Whip",
            cost={PokemonTypes.COLORLESS: 2},
            damage=40,
        ),
        Attack(
            title="Leaf Storm",
            game_text="Heal 20 damage from each of your Grass Pok\u00e9mon.",
            cost={PokemonTypes.GRASS: 2},
            damage=60,
            effect=_leaf_storm,
        ),
    ],
)
