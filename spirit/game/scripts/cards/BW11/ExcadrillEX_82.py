from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import spread_damage
from spirit.game.card_effects.trainers import is_basic_energy_card


async def _dig_out(ctx):
    """Printed damage; discard the top card of your deck. If it is a basic
    Energy card, attach it to 1 of your Pokemon."""
    await ctx.deal_damage()
    top = ctx.deck_top(1)
    if not top:
        return
    card = top[0]
    await ctx.discard_cards([card])
    if not is_basic_energy_card(card):
        return
    mine = ctx.my_pokemon_in_play()
    if not mine:
        return
    target = mine[0] if len(mine) == 1 else await ctx.choose_pokemon(
        mine, "Choose a Pokémon to attach the Energy to")
    await ctx.attach_energy(card, target or mine[0])


card = PokemonCardDef(
    guid="e155c05a-7912-5014-8a62-4b63cd4c3029",
    key="BW11",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.ExcadrillEX.Name",
    display_name="Excadrill-EX",
    searchable_by=["Excadrill-EX", "Basic", "EX", "ExcadrillEX"],
    subtypes=["Basic", "EX"],
    collector_number=82,
    set_code="BW11",
    rarity=Rarities.RareHoloEX,
    hp=180,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.WATER,
    resistance_type=PokemonTypes.LIGHTNING,
    resistance_amount=20,
    family_id=530,
    abilities=[
        Attack(
            title="Dig Out",
            game_text="Discard the top card of your deck. If that card is a basic Energy card, attach it to 1 of your Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=40,
            effect=_dig_out,
        ),
        Attack(
            title="Break Ground",
            game_text="Does 10 damage to each of your Benched Pok\u00e9mon. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.FIGHTING: 2, PokemonTypes.COLORLESS: 2},
            damage=120,
            effect=spread_damage(10, side='mine', also_base=True),
        ),
    ],
)