from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import damage_per, count_energy


async def energy_warp(ctx):
    """Move an Energy from 1 of your opponent's Benched Pokémon to their Active Pokémon."""
    opp_active = ctx.opponent_active()
    candidates = [p for p in ctx.opponent_bench() if ctx.attached_energies(p)]
    if opp_active is None or not candidates:
        return
    source = await ctx.choose_pokemon(
        candidates, "Choose 1 of your opponent's Benched Pokémon"
    )
    if source is None or ctx.effects_blocked(source):
        return
    energies = ctx.attached_energies(source)
    energy = energies[0]
    if len(energies) > 1:
        picked = await ctx.choose_cards(
            energies, 1, prompt="Choose an Energy to move to the Active Pokémon"
        )
        if not picked:
            return
        energy = picked[0]
    await ctx.move_energy(energy, opp_active)

card = PokemonCardDef(
    guid="2f9e7dac-4782-5c02-9ee7-30e1bd8bc71f",
    key="SWSH2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Xatu.Name",
    display_name="Xatu",
    searchable_by=["Xatu", "Stage 1", "Xatu"],
    subtypes=["Stage 1"],
    collector_number=77,
    set_code="SWSH2",
    rarity=Rarities.Uncommon,
    hp=120,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Natu.Name",
    family_id=177,
    abilities=[
        Attack(
            title="Energy Warp",
            game_text="Move an Energy from 1 of your opponent's Benched Pok\u00e9mon to their Active Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=energy_warp,
        ),
        Attack(
            title="Psychic",
            game_text="This attack does 30 more damage for each Energy attached to your opponent's Active Pok\u00e9mon.",
            cost={PokemonTypes.PSYCHIC: 1},
            damage=10,
            damage_operator="+",
            effect=damage_per(count_energy("defender"), 30, base=10),
        ),
    ],
)