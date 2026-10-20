from spirit.game.data_utils import PokemonCardDef, Ability, Activations
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.trainers import is_basic_energy_card


def _transfer_condition(board, player_id, pokemon=None):
    mine = list(board.pokemon_in_play(player_id))
    return len(mine) > 1 and any(is_basic_energy_card(c) for p in mine for c in p.children)


async def _hyper_transfer(ctx):
    """Move a basic Energy from 1 of your Pokemon to another of your Pokemon."""
    mine = ctx.my_pokemon_in_play()
    await ctx.move_energy_freely(mine, mine, predicate=is_basic_energy_card, max_count=1)


card = PokemonCardDef(
    guid="ee6534f9-9946-519d-ad86-4aa20a8280e1",
    key="XY9",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.GolduckBREAK.Name",
    display_name="Golduck BREAK",
    searchable_by=["Golduck BREAK", "BREAK", "GolduckBREAK"],
    subtypes=["BREAK"],
    collector_number=18,
    set_code="XY9",
    rarity=Rarities.Rare,
    hp=140,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BREAK,
    retreat_cost=0,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Golduck.Name",
    family_id=54,
    abilities=[
        Ability(
            title="Hyper Transfer",
            game_text="As often as you like during your turn (before your attack), you may move a basic Energy from 1 of your Pok\u00e9mon to another of your Pok\u00e9mon.",
            activation=Activations.UNLIMITED,
            condition=_transfer_condition,
            effect=_hyper_transfer,
        ),
    ],
)