from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Activations
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.pokemon import is_energy_card, energy_provides_type


def _is_fairy_energy(card):
    return is_energy_card(card) and energy_provides_type(card, PokemonTypes.FAIRY.value)


def _fairy_transfer_condition(board, player_id, pokemon=None):
    mine = board.pokemon_in_play(player_id)
    return len(mine) >= 2 and any(_is_fairy_energy(c) for p in mine for c in p.children)


async def _fairy_transfer(ctx):
    """Move a Fairy Energy attached to 1 of your Pokemon to another of your Pokemon."""
    mine = ctx.my_pokemon_in_play()
    await ctx.move_energy_freely(mine, mine, predicate=_is_fairy_energy, max_count=1,
                                 prompt="Choose a Fairy Energy to move")


card = PokemonCardDef(
    guid="7bb23cd9-d13c-5697-ab1a-cc339c572665",
    key="XY1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Aromatisse.Name",
    display_name="Aromatisse",
    searchable_by=["Aromatisse", "Stage 1", "Aromatisse"],
    subtypes=["Stage 1"],
    collector_number=93,
    set_code="XY1",
    rarity=Rarities.RareHolo,
    hp=90,
    elements=[PokemonTypes.FAIRY],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.METAL,
    resistance_type=PokemonTypes.DARKNESS,
    resistance_amount=20,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Spritzee.Name",
    family_id=682,
    abilities=[
        Ability(
            title="Fairy Transfer",
            game_text="As often as you like during your turn (before your attack), you may move a Fairy Energy attached to 1 of your Pok\u00e9mon to another of your Pok\u00e9mon.",
            activation=Activations.UNLIMITED,
            condition=_fairy_transfer_condition,
            effect=_fairy_transfer,
        ),
        Attack(
            title="Fairy Wind",
            cost={PokemonTypes.FAIRY: 2, PokemonTypes.COLORLESS: 1},
            damage=60,
        ),
    ],
)