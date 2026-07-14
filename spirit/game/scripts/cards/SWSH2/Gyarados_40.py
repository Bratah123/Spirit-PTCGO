from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities


async def big_storm(ctx):
    await ctx.deal_damage()
    await ctx.discard_stadium()


card = PokemonCardDef(
    guid="ba4d9911-4809-5ca5-82d8-83323dea0e89",
    key="SWSH2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Gyarados.Name",
    display_name="Gyarados",
    searchable_by=["Gyarados", "Stage 1", "Gyarados"],
    subtypes=["Stage 1"],
    collector_number=40,
    set_code="SWSH2",
    rarity=Rarities.RareHolo,
    hp=180,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=4,
    weakness_type=PokemonTypes.LIGHTNING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Magikarp.Name",
    family_id=129,
    abilities=[
        Attack(
            title="Wrack Down",
            cost={PokemonTypes.COLORLESS: 3},
            damage=90,
        ),
        Attack(
            title="Big Storm",
            game_text="Discard any Stadium in play.",
            cost={PokemonTypes.WATER: 2, PokemonTypes.COLORLESS: 3},
            damage=200,
            effect=big_storm,
        ),
    ],
)