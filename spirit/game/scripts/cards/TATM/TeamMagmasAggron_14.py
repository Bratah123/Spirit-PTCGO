from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.pokemon import is_energy_card, energy_provides_type
from spirit.game.card_effects.support_common import _is_damaged


def _is_fighting_energy(card):
    return is_energy_card(card) and energy_provides_type(card, PokemonTypes.FIGHTING.value)


async def _rock_stomp(ctx):
    """Discard any number of Fighting Energy attached to your Pokemon; 40x that many."""
    pool = [e for p in ctx.my_pokemon_in_play() for e in ctx.attached_energies(p) if _is_fighting_energy(e)]
    picked = await ctx.choose_cards(pool, len(pool), minimum=0, prompt="Discard any Fighting Energy") if pool else []
    if picked:
        await ctx.discard_cards(picked)
    await ctx.deal_damage(40 * len(picked))


async def _boulder_storm(ctx):
    """120; 20 to each of the opponent's damaged Benched Pokemon."""
    await ctx.deal_damage()
    for p in list(ctx.opponent_bench()):
        if _is_damaged(ctx.board, p):
            await ctx.deal_damage(20, target=p, apply_modifiers=None)


card = PokemonCardDef(
    guid="9cc137d2-308e-5ab1-9eec-0944c6a66bd8",
    key="TATM",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.TeamMagmasAggron.Name",
    display_name="Team Magma's Aggron",
    searchable_by=["Team Magma's Aggron", "Stage 2", "TeamMagmasAggron"],
    subtypes=["Stage 2"],
    collector_number=14,
    set_code="TATM",
    rarity=Rarities.RareHolo,
    hp=140,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE2,
    retreat_cost=4,
    weakness_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.TeamMagmasLairon.Name",
    family_id=304,
    abilities=[
        Attack(
            title="Rock Stomp",
            game_text="Discard as many Fighting Energy attached to your Pok\u00e9mon as you like. This attack does 40 damage times the amount of Fighting Energy you discarded.",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 1},
            damage=40,
            damage_operator="x",
            effect=_rock_stomp,
        ),
        Attack(
            title="Boulder Storm",
            game_text="This attack does 20 damage to each of your opponent's Benched Pok\u00e9mon that has any damage counters on it. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.FIGHTING: 3, PokemonTypes.COLORLESS: 1},
            damage=120,
            effect=_boulder_storm,
        ),
    ],
)