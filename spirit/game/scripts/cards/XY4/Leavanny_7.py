from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AttrID, TrainerType


def _is_tool(card):
    return card.get_attribute(AttrID.TRAINER_TYPE) in (
        TrainerType.POKEMON_TOOL.value, TrainerType.POKEMON_TOOL_F.value)


async def _coordinate(ctx):
    """Up to 2 of your Benched Pokemon without Tools: search your deck for a
    Pokemon Tool for each and attach it. Shuffle."""
    bench = [p for p in ctx.my_bench() if not any(_is_tool(c) for c in p.children)]
    chosen = await ctx.choose_cards(bench, min(2, len(bench)), minimum=0,
                                    prompt="Choose up to 2 Benched Pokémon") if bench else []
    for pokemon in chosen or []:
        picks = await ctx.search_deck(_is_tool, count=1, minimum=0,
                                      prompt="Choose a Pokémon Tool to attach")
        if picks:
            await ctx.attach_tool(picks[0], pokemon)
    await ctx.shuffle_deck()


def _is_grass(pokemon):
    return PokemonTypes.GRASS.value in (pokemon.get_attribute(AttrID.POKEMON_TYPES) or [])


async def _leaf_storm(ctx):
    """70; heal 20 damage from each of your Grass Pokemon."""
    await ctx.deal_damage()
    for p in ctx.my_pokemon_in_play():
        if _is_grass(p):
            await ctx.heal(20, p)


card = PokemonCardDef(
    guid="f005164e-f0fc-5ddc-8674-9d138ffced25",
    key="XY4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Leavanny.Name",
    display_name="Leavanny",
    searchable_by=["Leavanny", "Stage 2", "Leavanny"],
    subtypes=["Stage 2"],
    collector_number=7,
    set_code="XY4",
    rarity=Rarities.Rare,
    hp=130,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE2,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Swadloon.Name",
    family_id=540,
    abilities=[
        Attack(
            title="Coordinate",
            game_text="Choose up to 2 of your Benched Pok\u00e9mon that have no Pok\u00e9mon Tools attached to them. For each of those Pok\u00e9mon, search your deck for a Pok\u00e9mon Tool card, and attach it to that Pok\u00e9mon. Shuffle your deck afterward.",
            cost={PokemonTypes.GRASS: 1},
            effect=_coordinate,
        ),
        Attack(
            title="Leaf Storm",
            game_text="Heal 20 damage from each of your Grass Pok\u00e9mon.",
            cost={PokemonTypes.GRASS: 2, PokemonTypes.COLORLESS: 1},
            damage=70,
            effect=_leaf_storm,
        ),
    ],
)