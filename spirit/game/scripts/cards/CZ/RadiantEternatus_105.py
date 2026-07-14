from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.support_common import search_to_bench
from spirit.game.card_effects.trainers import is_pokemon_vmax
from spirit.game.session.effects import is_pokemon_card


def _is_vmax(card):
    return is_pokemon_card(card) and is_pokemon_vmax(card.archetype_id)


async def climactic_gate(ctx):
    """You may search up to 2 Pokemon VMAX to the Bench; using it ends the turn."""
    if not await ctx.ask_yes_no(
        "Search your deck for up to 2 Pokémon VMAX and put them onto "
        "your Bench? If you do, your turn ends."
    ):
        return
    await search_to_bench(predicate=_is_vmax, count=2)(ctx)
    ctx.ends_turn = True


card = PokemonCardDef(
    guid="d799e888-b9fa-5bb8-b022-acc672128675",
    key="CZ",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.RadiantEternatus.Name",
    display_name="Radiant Eternatus",
    searchable_by=["Radiant Eternatus", "Basic", "Radiant", "RadiantEternatus"],
    subtypes=["Basic", "Radiant"],
    collector_number=105,
    set_code="CZ",
    rarity=Rarities.RareRadiant,
    hp=170,
    elements=[PokemonTypes.DRAGON],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    family_id=890,
    abilities=[
        Ability(
            title="Climactic Gate",
            game_text="When you play this Pok\u00e9mon from your hand onto your Bench during your turn, you may search your deck for up to 2 Pok\u00e9mon VMAX and put them onto your Bench. Then, shuffle your deck. If you use this Ability, your turn ends.",
            trigger=Triggers.ON_PLAY,
            effect=climactic_gate,
        ),
        Attack(
            title="Power Beam",
            cost={PokemonTypes.FIRE: 1, PokemonTypes.DARKNESS: 1, PokemonTypes.COLORLESS: 1},
            damage=200,
        ),
    ],
)