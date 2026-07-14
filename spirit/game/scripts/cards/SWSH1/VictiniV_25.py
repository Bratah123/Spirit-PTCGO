from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import damage_per
from spirit.game.card_effects.pokemon import energy_provides_type
from spirit.game.card_effects.support_common import distribute_energy
from spirit.game.session.legal_actions import energy_provided_count


async def spreading_flames(ctx):
    """Attach up to 3 Fire Energy cards from your discard pile to your
    Pokemon, any way you like."""
    cards = [c for c in ctx.discard_pile() if energy_provides_type(c, PokemonTypes.FIRE.value)]
    if not cards:
        return
    picks = await ctx.choose_cards(
        cards, 3, minimum=0,
        prompt="Choose up to 3 Fire Energy cards from your discard pile to attach.",
    )
    if not picks:
        return
    candidates = ctx.my_pokemon_in_play()
    if not candidates:
        return
    await distribute_energy(ctx, picks, candidates)


def _both_actives_energy(ctx) -> int:
    total = 0
    for pokemon in (ctx.my_active(), ctx.opponent_active()):
        if pokemon is None:
            continue
        for energy in ctx.attached_energies(pokemon):
            total += energy_provided_count(energy)
    return total


card = PokemonCardDef(
    guid="3b65f1a3-5299-5b0e-8a5b-524bf177645b",
    key="SWSH1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.VictiniV.Name",
    display_name="Victini V",
    searchable_by=["Victini V", "Basic", "V", "VictiniV"],
    subtypes=["Basic", "V"],
    collector_number=25,
    set_code="SWSH1",
    rarity=Rarities.RareHoloV,
    hp=190,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.WATER,
    family_id=494,
    abilities=[
        Attack(
            title="Spreading Flames",
            game_text="Attach up to 3 Fire Energy cards from your discard pile to your Pokémon in any way you like.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=spreading_flames,
        ),
        Attack(
            title="Energy Burst",
            game_text="This attack does 30 damage for each Energy attached to both Active Pokémon.",
            cost={PokemonTypes.FIRE: 2},
            damage=30,
            damage_operator="x",
            effect=damage_per(_both_actives_energy, 30),
        ),
    ],
)
