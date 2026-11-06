from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes, AttrID, TrainerType


def _tools_on(pokemon):
    return [c for c in pokemon.children
            if c.get_attribute(AttrID.TRAINER_TYPE) == TrainerType.POKEMON_TOOL.value]


async def _breakwing(ctx):
    """When you play this Pokemon from your hand to evolve 1 of your Pokemon,
    you may discard all Pokemon Tool cards attached to each of your opponent's Pokemon."""
    tools = [t for p in ctx.opponent_pokemon_in_play() for t in _tools_on(p)]
    if tools and await ctx.ask_yes_no("Discard all Pokémon Tools attached to your opponent's Pokémon?"):
        await ctx.discard_cards(tools)


async def _gaia_crush(ctx):
    """Printed damage; discard any Stadium card in play."""
    await ctx.deal_damage()
    if ctx.stadium_in_play() is not None:
        await ctx.discard_stadium()


card = PokemonCardDef(
    guid="7439e91f-6929-55ff-888c-3b255d54f126",
    key="BW10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Salamence.Name",
    display_name="Salamence",
    searchable_by=["Salamence", "Stage 2", "Salamence"],
    subtypes=["Stage 2"],
    collector_number=64,
    set_code="BW10",
    rarity=Rarities.RareHolo,
    hp=150,
    elements=[PokemonTypes.DRAGON],
    stage=PokemonStage.STAGE2,
    retreat_cost=4,
    weakness_type=PokemonTypes.DRAGON,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Shelgon.Name",
    family_id=371,
    abilities=[
        Ability(
            title="Breakwing",
            game_text="When you play this Pok\u00e9mon from your hand to evolve 1 of your Pok\u00e9mon, you may discard all Pok\u00e9mon Tool cards attached to each of your opponent's Pok\u00e9mon.",
            ability_type=AbilityTypes.POKE_ABILITY,
            trigger=Triggers.ON_EVOLVE,
            effect=_breakwing,
        ),
        Attack(
            title="Gaia Crush",
            game_text="Discard any Stadium card in play.",
            cost={PokemonTypes.FIRE: 1, PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 2},
            damage=100,
            effect=_gaia_crush,
        ),
    ],
)