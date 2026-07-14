from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Activations
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, SpecialConditions


def _stadium_in_play_condition(board, player_id, pokemon):
    area = board.find_global_area("activeStadium")
    return bool(area and area.children)


async def poisonous_puddle(ctx):
    """Once during your turn, if a Stadium is in play, you may make your
    opponent's Active Pokemon Poisoned."""
    if await ctx.ask_yes_no("Make your opponent's Active Pokémon Poisoned?"):
        await ctx.apply_special_condition(ctx.defender, SpecialConditions.POISONED)


card = PokemonCardDef(
    guid="692befb2-3abb-5fe5-9495-3fc7b3fd90ce",
    key="SWSH2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Garbodor.Name",
    display_name="Garbodor",
    searchable_by=["Garbodor", "Stage 1", "Garbodor"],
    subtypes=["Stage 1"],
    collector_number=118,
    set_code="SWSH2",
    rarity=Rarities.Rare,
    hp=120,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Trubbish.Name",
    family_id=568,
    abilities=[
        Ability(
            title="Poisonous Puddle",
            game_text="Once during your turn, if a Stadium is in play, you may make your opponent's Active Pokémon Poisoned.",
            activation=Activations.ONCE_PER_TURN,
            condition=_stadium_in_play_condition,
            effect=poisonous_puddle,
        ),
        Attack(
            title="Sludge Bomb",
            cost={PokemonTypes.DARKNESS: 1, PokemonTypes.COLORLESS: 2},
            damage=80,
        ),
    ],
)
