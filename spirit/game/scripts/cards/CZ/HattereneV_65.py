from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.support_common import switch_self_attack
from spirit.game.card_effects.trainers import is_energy_card


async def horoscope(ctx):
    """Look at the top 3 cards of your deck. You may attach any number of
    Energy cards you find there to this Pokemon. Put the other cards back."""
    top = ctx.deck_top(3)
    if not top:
        return
    energies = [c for c in top if is_energy_card(c)]
    picks = await ctx.choose_cards(
        energies, max(len(energies), 1), minimum=0,
        prompt="Choose Energy cards to attach to this Pokémon.",
        display_cards=top,
    )
    for card in picks:
        await ctx.attach_energy(card, ctx.attacker)


card = PokemonCardDef(
    guid="81227f69-d3c2-58fa-98e1-25ea982eb0ba",
    key="CZ",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.HattereneV.Name",
    display_name="Hatterene V",
    searchable_by=["Hatterene V", "Basic", "V", "HattereneV"],
    subtypes=["Basic", "V"],
    collector_number=65,
    set_code="CZ",
    rarity=Rarities.RareHoloV,
    hp=200,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.FIGHTING,
    family_id=858,
    abilities=[
        Attack(
            title="Horoscope",
            game_text="Look at the top 3 cards of your deck. You may attach any number of Energy cards you find there to this Pok\u00e9mon. Put the other cards back in any order.",
            cost={PokemonTypes.PSYCHIC: 1},
            effect=horoscope,
        ),
        Attack(
            title="Teleportation Burst",
            game_text="Switch this Pok\u00e9mon with 1 of your Benched Pok\u00e9mon.",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 2},
            damage=80,
            effect=switch_self_attack(damage=80, optional=False),
        ),
    ],
)