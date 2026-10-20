from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, SpecialConditions
from spirit.game.card_effects.attacks_common import condition_attack
from spirit.game.card_effects.pokemon import is_energy_card


async def _siphon_off(ctx):
    """Attach 3 Energy cards from your discard pile to this Pokemon."""
    pool = [c for c in ctx.discard_pile() if is_energy_card(c)]
    n = min(3, len(pool))
    if n:
        picks = await ctx.choose_cards(pool, n, minimum=n, prompt="Choose 3 Energy cards")
        for energy in picks or []:
            await ctx.attach_energy(energy, ctx.attacker)


card = PokemonCardDef(
    guid="ae58c071-f371-5d56-8258-bcfa757d06b9",
    key="XY9",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Seismitoad.Name",
    display_name="Seismitoad",
    searchable_by=["Seismitoad", "Stage 2", "Seismitoad"],
    subtypes=["Stage 2"],
    collector_number=35,
    set_code="XY9",
    rarity=Rarities.Rare,
    hp=150,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE2,
    retreat_cost=3,
    weakness_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Palpitoad.Name",
    family_id=535,
    abilities=[
        Attack(
            title="Siphon Off",
            game_text="Attach 3 Energy cards from your discard pile to this Pok\u00e9mon.",
            cost={PokemonTypes.WATER: 1},
            effect=_siphon_off,
        ),
        Attack(
            title="Shaky Fall",
            game_text="Your opponent's Active Pok\u00e9mon is now Confused. That Pok\u00e9mon can't retreat during your opponent's next turn.",
            cost={PokemonTypes.WATER: 4},
            damage=90,
            effect=condition_attack(SpecialConditions.CONFUSED, no_retreat=True),
        ),
    ],
)