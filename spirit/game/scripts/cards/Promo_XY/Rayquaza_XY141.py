from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import flip_damage
from spirit.game.card_effects.pokemon import is_energy_card, energy_provides_type


def _is_a(card):
    return is_energy_card(card) and energy_provides_type(card, PokemonTypes.FIRE.value)


def _is_b(card):
    return is_energy_card(card) and energy_provides_type(card, PokemonTypes.LIGHTNING.value)


async def _dragon_blast(ctx):
    """Printed damage; discard a Fire and a Lightning Energy attached to this Pokemon."""
    await ctx.deal_damage()
    for pred, label in ((_is_a, "Fire"), (_is_b, "Lightning")):
        if any(pred(e) for e in ctx.attached_energies(ctx.attacker)):
            await ctx.discard_energy_from(ctx.attacker, 1, predicate=pred, minimum=1,
                                          prompt=f"Discard a {label} Energy")


card = PokemonCardDef(
    guid="8e10320d-08f4-5ccd-a0cc-99ebffb7694c",
    key="Promo_XY",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Rayquaza.Name",
    display_name="Rayquaza",
    searchable_by=["Rayquaza", "Basic", "Rayquaza"],
    subtypes=["Basic"],
    collector_number=141,
    set_code="Promo_XY",
    rarity=Rarities.RarePromo,
    hp=120,
    elements=[PokemonTypes.DRAGON],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FAIRY,
    family_id=384,
    abilities=[
        Attack(
            title="Dual Claw",
            game_text="Flip 2 coins. This attack does 20 damage times the number of heads.",
            cost={PokemonTypes.FIRE: 1, PokemonTypes.COLORLESS: 1},
            damage=20,
            damage_operator="x",
            effect=flip_damage(2, per_heads=20),
        ),
        Attack(
            title="Dragon Blast",
            game_text="Discard 1 Fire Energy and 1 Lightning Energy attached to this Pok\u00e9mon.",
            cost={PokemonTypes.FIRE: 1, PokemonTypes.LIGHTNING: 1, PokemonTypes.COLORLESS: 2},
            damage=120,
            effect=_dragon_blast,
        ),
    ],
)