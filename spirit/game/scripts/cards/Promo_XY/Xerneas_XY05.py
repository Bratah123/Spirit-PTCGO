from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import self_energy_discard_attack
from spirit.game.card_effects.pokemon import is_energy_card, energy_provides_type


def _is_fairy_energy_card(card):
    return is_energy_card(card) and energy_provides_type(card, PokemonTypes.FAIRY.value)


async def _geomancy(ctx):
    """Choose 2 of your Benched Pokemon; for each, search your deck for a
    Fairy Energy card and attach it to that Pokemon. Shuffle."""
    bench = list(ctx.my_bench())
    chosen = []
    while bench and len(chosen) < 2:
        pick = bench[0] if len(bench) == 1 else await ctx.choose_pokemon(
            bench, "Choose a Benched Pokémon")
        pick = pick or bench[0]
        chosen.append(pick)
        bench.remove(pick)
    for target in chosen:
        picks = await ctx.search_deck(_is_fairy_energy_card, count=1, minimum=0,
                                      prompt="Choose a Fairy Energy card")
        for card in picks or []:
            await ctx.attach_energy(card, target)
    await ctx.shuffle_deck()


card = PokemonCardDef(
    guid="4950da81-018a-5895-af2c-b854eb73a908",
    key="Promo_XY",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Xerneas.Name",
    display_name="Xerneas",
    searchable_by=["Xerneas", "Basic", "Xerneas"],
    subtypes=["Basic"],
    collector_number=5,
    set_code="Promo_XY",
    rarity=Rarities.RarePromo,
    hp=130,
    elements=[PokemonTypes.FAIRY],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.METAL,
    resistance_type=PokemonTypes.DARKNESS,
    resistance_amount=20,
    family_id=716,
    abilities=[
        Attack(
            title="Geomancy",
            game_text="Choose 2 of your Benched Pok\u00e9mon. For each of those Pok\u00e9mon, search your deck for a Fairy Energy card and attach it to that Pok\u00e9mon. Shuffle your deck afterward.",
            cost={PokemonTypes.FAIRY: 1},
            effect=_geomancy,
        ),
        Attack(
            title="Rainbow Spear",
            game_text="Discard an Energy attached to this Pok\u00e9mon.",
            cost={PokemonTypes.FAIRY: 2, PokemonTypes.COLORLESS: 1},
            damage=100,
            effect=self_energy_discard_attack(count=1),
        ),
    ],
)