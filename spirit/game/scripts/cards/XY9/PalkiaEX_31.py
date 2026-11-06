from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import snipe_attack
from spirit.game.card_effects.pokemon import is_energy_card, energy_provides_type


def _is_water_energy(card):
    return is_energy_card(card) and energy_provides_type(card, PokemonTypes.WATER.value)


async def _aqua_turbo(ctx):
    """40; search for 2 Water Energy cards and attach them to 1 of your Benched Pokemon."""
    await ctx.deal_damage()
    bench = ctx.my_bench()
    if bench:
        target = bench[0] if len(bench) == 1 else await ctx.choose_pokemon(bench, "Attach to which Benched Pokémon?")
        picks = await ctx.search_deck(lambda c: is_energy_card(c) and _is_water_energy(c), count=2,
                                      minimum=0, prompt="Choose 2 Water Energy cards")
        for energy in picks or []:
            await ctx.attach_energy(energy, target or bench[0])
    await ctx.shuffle_deck()


card = PokemonCardDef(
    guid="d891a91d-0f55-577b-94c7-f3414805cf62",
    key="XY9",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.PalkiaEX.Name",
    display_name="Palkia-EX",
    searchable_by=["Palkia-EX", "Basic", "EX", "PalkiaEX"],
    subtypes=["Basic", "EX"],
    collector_number=31,
    set_code="XY9",
    rarity=Rarities.RareHoloEX,
    hp=180,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.GRASS,
    family_id=484,
    abilities=[
        Attack(
            title="Aqua Turbo",
            game_text="Search your deck for 2 Water Energy cards and attach them to 1 of your Benched Pok\u00e9mon. Shuffle your deck afterward.",
            cost={PokemonTypes.WATER: 2},
            damage=40,
            effect=_aqua_turbo,
        ),
        Attack(
            title="Pearl Hurricane",
            game_text="This attack does 30 damage to 1 of your opponent's Benched Pok\u00e9mon. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.WATER: 4},
            damage=120,
            effect=snipe_attack(30, also_base=True),
        ),
    ],
)