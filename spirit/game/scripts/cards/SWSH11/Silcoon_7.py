from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import lock_defender_attacks


async def entangling_string(ctx):
    heads = await ctx.flip_coins(1, "Entangling String")
    if heads[0]:
        lock_defender_attacks(ctx)

card = PokemonCardDef(
    guid="17bf77ac-5e9f-582f-a0a5-87a9695f77a0",
    key="SWSH11",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Silcoon.Name",
    display_name="Silcoon",
    searchable_by=["Silcoon", "Stage 1", "Silcoon"],
    subtypes=["Stage 1"],
    collector_number=7,
    set_code="SWSH11",
    rarity=Rarities.Uncommon,
    hp=80,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIRE,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Wurmple.Name",
    family_id=265,
    abilities=[
        Attack(
            title="Entangling String",
            game_text="Flip a coin. If heads, during your opponent's next turn, the Defending Pok\u00e9mon can't attack.",
            cost={PokemonTypes.GRASS: 1},
            effect=entangling_string,
        ),
        Attack(
            title="Ram",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
        ),
    ],
)