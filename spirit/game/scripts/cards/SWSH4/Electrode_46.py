from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Activations
from spirit.game.attributes import AttrID, PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.pokemon import is_lightning_energy
from spirit.game.card_effects.support_common import distribute_energy


def _is_lightning_pokemon(p):
    return PokemonTypes.LIGHTNING.value in (p.get_attribute(AttrID.POKEMON_TYPES) or [])


def _on_bench(board, player_id, pokemon):
    return pokemon is not board.active_pokemon(player_id)


async def buzzap_generator(ctx):
    """Once per turn, if benched: you may search up to 2 Lightning Energy
    cards and attach them freely, then shuffle. If you did, this Pokémon is
    Knocked Out."""
    if not await ctx.ask_yes_no(
        "Search your deck for up to 2 Lightning Energy cards to attach? "
        "This Pokémon will be Knocked Out."
    ):
        return
    picks = await ctx.search_deck(
        is_lightning_energy, count=2, minimum=0,
        prompt="Choose up to 2 Lightning Energy cards to attach.",
    )
    candidates = [p for p in ctx.my_pokemon_in_play() if _is_lightning_pokemon(p)]
    if picks and candidates:
        await distribute_energy(ctx, picks, candidates)
    await ctx.shuffle_deck()
    await ctx.knock_out(ctx.source)

card = PokemonCardDef(
    guid="a4d2a52e-1f63-5225-8a8d-90393421ff2f",
    key="SWSH4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Electrode.Name",
    display_name="Electrode",
    searchable_by=["Electrode", "Stage 1", "Electrode"],
    subtypes=["Stage 1"],
    collector_number=46,
    set_code="SWSH4",
    rarity=Rarities.RareHolo,
    hp=90,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Voltorb.Name",
    family_id=100,
    abilities=[
        Ability(
            title="Buzzap Generator",
            game_text="Once during your turn, if this Pok\u00e9mon is on your Bench, you may search your deck for up to 2 Lightning Energy cards and attach them to your Lightning Pok\u00e9mon in any way you like. Then, shuffle your deck. If you searched your deck in this way, this Pok\u00e9mon is Knocked Out.",
            activation=Activations.ONCE_PER_TURN,
            condition=_on_bench,
            effect=buzzap_generator,
        ),
        Attack(
            title="Electric Ball",
            cost={PokemonTypes.LIGHTNING: 2, PokemonTypes.COLORLESS: 1},
            damage=100,
        ),
    ],
)