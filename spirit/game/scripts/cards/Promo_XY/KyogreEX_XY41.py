from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, SpecialConditions
from spirit.game.card_effects.attacks_common import condition_attack
from spirit.game.card_effects.pokemon import is_energy_card, energy_provides_type


def _is_water_energy(card):
    return is_energy_card(card) and energy_provides_type(card, PokemonTypes.WATER.value)


async def _giant_whirlpool(ctx):
    """140; return 2 Water Energy attached to this Pokemon to your hand."""
    await ctx.deal_damage()
    pool = [e for e in ctx.attached_energies(ctx.attacker) if _is_water_energy(e)]
    if not pool:
        return
    picks = await ctx.choose_cards(pool, min(2, len(pool)), minimum=min(2, len(pool)),
                                   prompt="Return 2 Water Energy to your hand")
    if picks:
        await ctx.put_in_hand(picks, reveal=False)


card = PokemonCardDef(
    guid="bf3ae6aa-39c3-5ff9-8444-8706fc5e1f75",
    key="Promo_XY",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.KyogreEX.Name",
    display_name="Kyogre-EX",
    searchable_by=["Kyogre-EX", "Basic", "EX", "KyogreEX"],
    subtypes=["Basic", "EX"],
    collector_number=41,
    set_code="Promo_XY",
    rarity=Rarities.RarePromo,
    hp=180,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=4,
    weakness_type=PokemonTypes.GRASS,
    family_id=382,
    abilities=[
        Attack(
            title="Water Pulse",
            game_text="Your opponent's Active Pok\u00e9mon is now Asleep.",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
            effect=condition_attack(SpecialConditions.ASLEEP),
        ),
        Attack(
            title="Giant Whirlpool",
            game_text="Return 2 Water Energy attached to this Pok\u00e9mon to your hand.",
            cost={PokemonTypes.WATER: 2, PokemonTypes.COLORLESS: 2},
            damage=140,
            effect=_giant_whirlpool,
        ),
    ],
)