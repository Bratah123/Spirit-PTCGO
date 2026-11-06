from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.pokemon import is_energy_card, energy_provides_type
from spirit.game.card_effects.attacks_common import bonus_if


def _is_fighting_energy(card):
    return is_energy_card(card) and energy_provides_type(card, PokemonTypes.FIGHTING.value)


async def _accelerating_spin(ctx):
    """Attach 2 Fighting Energy cards from your discard pile to this Pokemon; then switch it."""
    pool = [c for c in ctx.discard_pile() if is_energy_card(c) and _is_fighting_energy(c)]
    n = min(2, len(pool))
    if n:
        picks = await ctx.choose_cards(pool, n, minimum=n, prompt="Choose 2 Fighting Energy cards")
        for energy in picks or []:
            await ctx.attach_energy(energy, ctx.attacker)
    bench = ctx.my_bench()
    if bench and ctx.attacker is ctx.my_active():
        target = bench[0] if len(bench) == 1 else await ctx.choose_pokemon(bench, "Switch with which Benched Pokémon?")
        await ctx.switch_active(ctx.player_id, target or bench[0])


def _is_psychic_energy(card):
    return is_energy_card(card) and energy_provides_type(card, PokemonTypes.PSYCHIC.value)


def _has_psychic(ctx):
    return any(_is_psychic_energy(e) for e in ctx.attached_energies(ctx.attacker))


card = PokemonCardDef(
    guid="1a7f49a5-db64-5ef1-88e4-ba361c46607c",
    key="XY8",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Meloetta.Name",
    display_name="Meloetta",
    searchable_by=["Meloetta", "Basic", "Meloetta"],
    subtypes=["Basic"],
    collector_number=85,
    set_code="XY8",
    rarity=Rarities.RareHolo,
    hp=90,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=648,
    abilities=[
        Attack(
            title="Accelerating Spin",
            game_text="Attach 2 Fighting Energy cards from your discard pile to this Pok\u00e9mon. Then, switch this Pok\u00e9mon with 1 of your Benched Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=_accelerating_spin,
        ),
        Attack(
            title="Prima Rondo",
            game_text="If this Pok\u00e9mon has any Psychic Energy attached to it, this attack does 50 more damage.",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 2},
            damage=60,
            damage_operator="+",
            effect=bonus_if(_has_psychic, 50),
        ),
    ],
)