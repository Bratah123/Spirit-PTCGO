from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Activations
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.pokemon import energy_provides_type
from spirit.game.card_effects.trainers import is_energy_card


def _is_fire_energy(card) -> bool:
    return is_energy_card(card) and energy_provides_type(
        card, PokemonTypes.FIRE.value)


def _inferno_fandango_condition(board, player_id, pokemon) -> bool:
    hand = board.find_player_area(player_id, "hand")
    return bool(hand and any(_is_fire_energy(c) for c in hand.children))


async def inferno_fandango(ctx):
    """Attach a Fire Energy from hand to 1 of your Pokémon (repeatable)."""
    energies = [c for c in ctx.hand() if _is_fire_energy(c)]
    targets = ctx.my_pokemon_in_play()
    if not energies or not targets:
        return
    picks = await ctx.choose_cards(
        energies, 1, prompt="Choose a Fire Energy card to attach",
    )
    if not picks:
        return
    target = await ctx.choose_pokemon(
        targets, "Choose a Pokémon to attach the Energy to",
    )
    if target is None:
        return
    await ctx.attach_energy(picks[0], target)


card = PokemonCardDef(
    guid="ae13a7f8-10f6-5490-94a3-60c06d89fa61",
    key="BW11",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Emboar.Name",
    display_name="Emboar",
    searchable_by=["Emboar", "Stage 2", "Emboar"],
    subtypes=["Stage 2"],
    collector_number=27,
    set_code="BW11",
    rarity=Rarities.RareHolo,
    hp=150,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.STAGE2,
    retreat_cost=4,
    weakness_type=PokemonTypes.WATER,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Pignite.Name",
    family_id=498,
    abilities=[
        Ability(
            title="Inferno Fandango",
            game_text="As often as you like during your turn (before your attack), you may attach a Fire Energy card from your hand to 1 of your Pok\u00e9mon.",
            ability_type=AbilityTypes.POKE_ABILITY,
            activation=Activations.UNLIMITED,
            condition=_inferno_fandango_condition,
            effect=inferno_fandango,
        ),
        Attack(
            title="Heat Crash",
            cost={PokemonTypes.FIRE: 2, PokemonTypes.COLORLESS: 2},
            damage=80,
        ),
    ],
)
