from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Activations
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.passives_common import is_in_active_spot
from spirit.game.card_effects.attacks_common import damage_per, count_bench


async def _rush_in(ctx):
    """If this Pokemon is on your Bench, switch it with your Active Pokemon."""
    await ctx.switch_active(ctx.player_id, ctx.source)


def _on_bench(board, player_id, pokemon):
    return pokemon is not None and not is_in_active_spot(pokemon) \
        and board.active_pokemon(player_id) is not None


card = PokemonCardDef(
    guid="ed2b8872-2b39-5033-9704-5f509031b197",
    key="XY8",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Zoroark.Name",
    display_name="Zoroark",
    searchable_by=["Zoroark", "Stage 1", "Zoroark"],
    subtypes=["Stage 1"],
    collector_number=91,
    set_code="XY8",
    rarity=Rarities.RareHolo,
    hp=100,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    resistance_type=PokemonTypes.PSYCHIC,
    resistance_amount=20,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Zorua.Name",
    family_id=570,
    abilities=[
        Ability(
            title="Stand In",
            game_text="Once during your turn (before your attack), if this Pok\u00e9mon is on your Bench, you may switch this Pok\u00e9mon with your Active Pok\u00e9mon.",
            activation=Activations.ONCE_PER_TURN,
            condition=_on_bench,
            effect=_rush_in,
        ),
        Attack(
            title="Mind Jack",
            game_text="This attack does 30 more damage for each of your opponent's Benched Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=10,
            damage_operator="+",
            effect=damage_per(count_bench('opponent'), 30, base=10),
        ),
    ],
)