from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import damage_per, count_discard
from spirit.game.session.effects import is_pokemon_card


async def return_effect(ctx):
    """30 damage; you may draw cards until you have 6 cards in your hand."""
    await ctx.deal_damage()
    if await ctx.ask_yes_no("Draw cards until you have 6 cards in your hand?"):
        await ctx.draw_until(6)


card = PokemonCardDef(
    guid="3405e964-9005-5d8f-a219-84d09660d31c",
    key="XY7",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Vespiquen.Name",
    display_name="Vespiquen",
    searchable_by=["Vespiquen", "Stage 1", "Vespiquen"],
    subtypes=["Stage 1"],
    collector_number=10,
    set_code="XY7",
    rarity=Rarities.Uncommon,
    hp=90,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=0,
    weakness_type=PokemonTypes.FIRE,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Combee.Name",
    family_id=415,
    abilities=[
        Attack(
            title="Intelligence Gathering",
            game_text="You may draw cards until you have 6 cards in your hand.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
            effect=return_effect,
        ),
        Attack(
            title="Bee Revenge",
            game_text="This attack does 10 more damage for each Pok\u00e9mon in your discard pile.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
            damage_operator="+",
            effect=damage_per(count_discard('mine', is_pokemon_card), 10, base=20),
        ),
    ],
)