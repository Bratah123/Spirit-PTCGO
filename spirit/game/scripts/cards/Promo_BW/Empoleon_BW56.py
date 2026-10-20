from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import flip_damage


async def _cold_crush(ctx):
    """Printed damage; you may discard an Energy attached to this Pokemon. If
    you do, discard an Energy attached to the Defending Pokemon."""
    await ctx.deal_damage()
    me, d = ctx.attacker, ctx.defender
    if not ctx.attached_energies(me) or not await ctx.ask_yes_no("Discard an Energy from this Pokémon to discard one from the Defending Pokémon?"):
        return
    await ctx.discard_energy_from(me, 1, minimum=1)
    if d is not None and not ctx.effects_blocked(d) and ctx.attached_energies(d):
        await ctx.discard_energy_from(d, 1, minimum=1)


card = PokemonCardDef(
    guid="2a38a46d-0517-5d37-8403-b8bac40fc7e9",
    key="Promo_BW",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Empoleon.Name",
    display_name="Empoleon",
    searchable_by=["Empoleon", "Stage 2", "Empoleon"],
    subtypes=["Stage 2"],
    collector_number=56,
    set_code="Promo_BW",
    rarity=Rarities.RarePromo,
    hp=140,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    weakness_type=PokemonTypes.LIGHTNING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Prinplup.Name",
    family_id=395,
    abilities=[
        Attack(
            title="Fury Attack",
            game_text="Flip 3 coins. This attack does 30 damage times the number of heads.",
            cost={PokemonTypes.WATER: 1},
            damage=30,
            damage_operator="x",
            effect=flip_damage(coins=3, per_heads=30),
        ),
        Attack(
            title="Cold Crush",
            game_text="You may discard an Energy attached to this Pok\u00e9mon. If you do, discard an Energy attached to the Defending Pok\u00e9mon.",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 2},
            damage=70,
            effect=_cold_crush,
        ),
    ],
)