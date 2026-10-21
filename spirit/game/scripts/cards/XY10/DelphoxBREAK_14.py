from spirit.game.data_utils import PokemonCardDef, Ability, Activations
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.pokemon import is_energy_card, energy_provides_type


def _is_fire_energy(card):
    return is_energy_card(card) and energy_provides_type(card, PokemonTypes.FIRE.value)


async def _flare_witch(ctx):
    """Search your deck for a Fire Energy card and attach it to 1 of your Pokemon. Shuffle."""
    picks = await ctx.search_deck(lambda c: is_energy_card(c) and _is_fire_energy(c), count=1, minimum=0,
                                  prompt="Choose a Fire Energy card")
    if picks:
        mine = ctx.my_pokemon_in_play()
        target = mine[0] if len(mine) == 1 else await ctx.choose_pokemon(mine, "Attach to which Pokémon?")
        if target is not None:
            await ctx.attach_energy(picks[0], target)
    await ctx.shuffle_deck()


card = PokemonCardDef(
    guid="35e9327a-fe1f-5907-b82c-2f8edf6b7578",
    key="XY10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.DelphoxBREAK.Name",
    display_name="Delphox BREAK",
    searchable_by=["Delphox BREAK", "BREAK", "DelphoxBREAK"],
    subtypes=["BREAK"],
    collector_number=14,
    set_code="XY10",
    rarity=Rarities.Rare,
    hp=180,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BREAK,
    retreat_cost=0,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Delphox.Name",
    family_id=653,
    abilities=[
        Ability(
            title="Flare Witch",
            game_text="Once during your turn (before your attack), you may search your deck for a Fire Energy card and attach it to 1 of your Pok\u00e9mon. Shuffle your deck afterward.",
            activation=Activations.ONCE_PER_TURN,
            effect=_flare_witch,
        ),
    ],
)