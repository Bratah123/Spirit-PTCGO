from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import bonus_if, has_damage
from spirit.game.card_effects.pokemon import is_energy_card, energy_provides_type
from spirit.game.session.effects import is_water_pokemon


def _is_water_energy(card):
    return is_energy_card(card) and energy_provides_type(card, PokemonTypes.WATER)


async def bubble_pod(ctx):
    candidates = [c for c in ctx.discard_pile() if is_water_pokemon(c)]
    if not candidates:
        return
    picks = await ctx.choose_cards(
        candidates, 1, minimum=0,
        prompt="Choose a Water Pokémon from your discard pile to put onto your Bench.",
    )
    if not picks:
        return
    pokemon = picks[0]
    if not await ctx.bench_pokemon(pokemon):
        return
    energies = [c for c in ctx.discard_pile() if _is_water_energy(c)]
    if not energies:
        return
    picks2 = await ctx.choose_cards(
        energies, 3, minimum=0,
        prompt="Choose up to 3 Water Energy cards from your discard pile to attach.",
    )
    for energy in picks2:
        await ctx.attach_energy(energy, pokemon)


card = PokemonCardDef(
    guid="45eb2749-287c-571c-8b28-bfd418da7845",
    key="SWSH7",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.VaporeonVMAX.Name",
    display_name="Vaporeon VMAX",
    searchable_by=["Vaporeon VMAX", "VMAX", "Rapid Strike", "VaporeonVMAX"],
    subtypes=["VMAX", "Rapid Strike"],
    collector_number=30,
    set_code="SWSH7",
    rarity=Rarities.RareHoloVMAX,
    hp=320,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.VMAX,
    retreat_cost=2,
    weakness_type=PokemonTypes.LIGHTNING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.VaporeonV.Name",
    family_id=134,
    abilities=[
        Attack(
            title="Bubble Pod",
            game_text="Put a Water Pok\u00e9mon from your discard pile onto your Bench. If you do, attach up to 3 Water Energy cards from your discard pile to that Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=bubble_pod,
        ),
        Attack(
            title="Max Torrent",
            game_text="If your opponent's Active Pok\u00e9mon already has any damage counters on it, this attack does 100 more damage.",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 2},
            damage=100,
            damage_operator="+",
            effect=bonus_if(has_damage("defender"), 100),
        ),
    ],
)