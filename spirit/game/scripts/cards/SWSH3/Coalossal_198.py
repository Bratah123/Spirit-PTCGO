from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Activations
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AttrID
from spirit.game.card_effects.trainers import is_energy_card
from spirit.game.card_effects.support_common import requires_discard, distribute_energy


def _is_fire_energy_card(card):
    types = card.get_attribute(AttrID.POKEMON_TYPES) or []
    return is_energy_card(card) and PokemonTypes.FIRE.value in types


def _is_fighting_energy_card(card):
    types = card.get_attribute(AttrID.POKEMON_TYPES) or []
    return is_energy_card(card) and PokemonTypes.FIGHTING.value in types


async def tar_generator(ctx):
    """Once per turn, you may attach a Fire Energy, a Fighting Energy, or
    1 of each from your discard pile to your Pokémon in any way you like."""
    if not await ctx.ask_yes_no(
        "Attach a Fire Energy card, a Fighting Energy card, or 1 of each "
        "from your discard pile to your Pokémon?"
    ):
        return
    picks = []
    fire_cards = [c for c in ctx.discard_pile() if _is_fire_energy_card(c)]
    if fire_cards:
        picks.extend(await ctx.choose_cards(
            fire_cards, 1, minimum=0,
            prompt="Choose a Fire Energy card to attach (optional)",
        ))
    fighting_cards = [c for c in ctx.discard_pile() if _is_fighting_energy_card(c)]
    if fighting_cards:
        picks.extend(await ctx.choose_cards(
            fighting_cards, 1, minimum=0,
            prompt="Choose a Fighting Energy card to attach (optional)",
        ))
    if not picks:
        return
    await distribute_energy(ctx, picks, ctx.my_pokemon_in_play())


card = PokemonCardDef(
    guid="d0c3b8c3-ddb7-5d04-881c-0dc286bddc2f",
    key="SWSH3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Coalossal.Name",
    display_name="Coalossal",
    searchable_by=["Coalossal", "Stage 2", "Coalossal"],
    subtypes=["Stage 2"],
    collector_number=198,
    set_code="SWSH3",
    rarity=Rarities.RareSecret,
    hp=160,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE2,
    retreat_cost=4,
    weakness_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Carkol.Name",
    family_id=839,
    abilities=[
        Ability(
            title="Tar Generator",
            game_text="Once during your turn, you may attach a Fire Energy card, a Fighting Energy card, or 1 of each from your discard pile to your Pokémon in any way you like.",
            activation=Activations.ONCE_PER_TURN,
            condition=requires_discard(
                lambda c: _is_fire_energy_card(c) or _is_fighting_energy_card(c)
            ),
            effect=tar_generator,
        ),
        Attack(
            title="Flaming Avalanche",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 3},
            damage=130,
        ),
    ],
)
