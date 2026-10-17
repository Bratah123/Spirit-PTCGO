from spirit.game.data_utils import PokemonCardDef, Attack, def_for
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import count_in_play


def _is_durant(pokemon):
    definition = def_for(getattr(pokemon, "archetype_id", None) or "")
    return definition is not None and definition.display_name == "Durant"


async def devour(ctx):
    """For each Durant in play, discard top of opponent's deck."""
    n = count_in_play("mine", pred=_is_durant)(ctx)
    if n:
        await ctx.discard_cards(ctx.deck_top(n, player_id=ctx.opponent_id))


card = PokemonCardDef(
    guid="f1a8f96c-a6e2-582c-88aa-4c89c0bc299a",
    key="BW3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Durant.Name",
    display_name="Durant",
    searchable_by=["Durant", "Basic", "Durant"],
    subtypes=["Basic"],
    collector_number=83,
    set_code="BW3",
    rarity=Rarities.Uncommon,
    hp=70,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.PSYCHIC,
    family_id=632,
    abilities=[
        Attack(
            title="Devour",
            game_text="For each of your Durant in play, discard the top card of your opponent's deck.",
            cost={PokemonTypes.METAL: 1},
            effect=devour,
        ),
        Attack(
            title="Vice Grip",
            cost={PokemonTypes.COLORLESS: 2},
            damage=30,
        ),
    ],
)
