from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import flip_damage
from spirit.game.card_effects.pokemon import is_energy_card, energy_provides_type


def _is_fighting_energy(card):
    return is_energy_card(card) and energy_provides_type(card, PokemonTypes.FIGHTING.value)


async def _dig_out(ctx):
    """20; discard the top card of your deck; if it's a Fighting Energy, attach it to this Pokemon."""
    await ctx.deal_damage()
    top = ctx.deck_top(1)
    if not top:
        return
    await ctx.discard_cards(top)
    if _is_fighting_energy(top[0]):
        await ctx.attach_energy(top[0], ctx.attacker)


card = PokemonCardDef(
    guid="d2057b80-f391-5c87-8236-b41275faf1ac",
    key="XY7",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Golurk.Name",
    display_name="Golurk",
    searchable_by=["Golurk", "Stage 1", "Golurk"],
    subtypes=["Stage 1"],
    collector_number=41,
    set_code="XY7",
    rarity=Rarities.Common,
    hp=130,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE1,
    retreat_cost=4,
    weakness_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Golett.Name",
    family_id=622,
    abilities=[
        Attack(
            title="Dig Out",
            game_text="Discard the top card of your deck. If that card is a Fighting Energy card, attach it to this Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=20,
            effect=_dig_out,
        ),
        Attack(
            title="Double Lariat",
            game_text="Flip 2 coins. This attack does 90 damage times the number of heads.",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 3},
            damage=90,
            damage_operator="x",
            effect=flip_damage(coins=2, per_heads=90),
        ),
    ],
)