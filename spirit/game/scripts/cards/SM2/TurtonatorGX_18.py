from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import self_energy_discard_attack
from spirit.game.attributes import PokemonTypes


from spirit.game.scripts.cards.SWSH8.Turtonator_198 import shell_trap
from spirit.game.card_effects.pokemon import energy_provides_type
from spirit.game.card_effects.support_common import distribute_energy
from spirit.game.card_effects.trainers import is_energy_card


def _is_fire_energy(card):
    return is_energy_card(card) and energy_provides_type(card, PokemonTypes.FIRE.value)


async def nitro_tank_gx(ctx):
    """Attach 5 Fire Energy from discard to your Pokémon in any way you like."""
    pool = [c for c in ctx.discard_pile() if _is_fire_energy(c)]
    if not pool:
        return
    picks = await ctx.choose_cards(
        pool, 5, minimum=0,
        prompt="Choose up to 5 Fire Energy cards to attach",
    )
    if picks:
        await distribute_energy(ctx, picks, ctx.my_pokemon_in_play())


card = PokemonCardDef(
    guid="74d933f3-5b15-5d3c-9ff3-e6fe70059a7a",
    key="SM2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.TurtonatorGX.Name",
    display_name="Turtonator-GX",
    searchable_by=["Turtonator-GX", "Basic", "GX", "TurtonatorGX"],
    subtypes=["Basic", "GX"],
    collector_number=18,
    set_code="SM2",
    rarity=Rarities.RareHoloGX,
    hp=190,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.WATER,
    family_id=776,
    abilities=[
        Attack(
            title="Shell Trap",
            game_text="During your opponent's next turn, if this Pok\u00e9mon is damaged by an attack (even if this Pok\u00e9mon is Knocked Out), put 8 damage counters on the Attacking Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
            effect=shell_trap,
        ),
        Attack(
            title="Bright Flame",
            game_text="Discard 2 Fire Energy from this Pok\u00e9mon.",
            cost={PokemonTypes.FIRE: 2, PokemonTypes.COLORLESS: 1},
            damage=160,
            effect=self_energy_discard_attack(count=2, energy_type=PokemonTypes.FIRE),
        ),
        Attack(
            title="Nitro Tank-GX",
            game_text="Attach 5 Fire Energy cards from your discard pile to your Pok\u00e9mon in any way you like. (You can't use more than 1 GX attack in a game.)",
            cost={PokemonTypes.FIRE: 1},
            effect=nitro_tank_gx,
        ),
    ],
)