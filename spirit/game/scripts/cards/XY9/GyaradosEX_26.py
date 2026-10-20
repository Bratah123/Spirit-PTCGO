from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import spread_damage
from spirit.game.card_effects.pokemon import is_energy_card, energy_provides_type


def _is_water_energy(card):
    return is_energy_card(card) and energy_provides_type(card, PokemonTypes.WATER.value)


async def _stormy_seas(ctx):
    """Flip until tails; for each heads attach a Water Energy card from your deck to this Pokemon."""
    heads = 0
    while True:
        results = await ctx.flip_coins(1, ctx.ability.title)
        if not (results and results[0]):
            break
        heads += 1
    if heads:
        picks = await ctx.search_deck(lambda c: is_energy_card(c) and _is_water_energy(c), count=heads,
                                      minimum=0, prompt="Choose Water Energy cards to attach")
        for energy in picks or []:
            await ctx.attach_energy(energy, ctx.attacker)
    await ctx.shuffle_deck()


card = PokemonCardDef(
    guid="60a9782b-e079-599c-9cbf-44349ad35785",
    key="XY9",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.GyaradosEX.Name",
    display_name="Gyarados-EX",
    searchable_by=["Gyarados-EX", "Basic", "EX", "GyaradosEX"],
    subtypes=["Basic", "EX"],
    collector_number=26,
    set_code="XY9",
    rarity=Rarities.RareHoloEX,
    hp=180,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=4,
    weakness_type=PokemonTypes.LIGHTNING,
    family_id=130,
    abilities=[
        Attack(
            title="Stormy Seas",
            game_text="Flip a coin until you get tails. For each heads, search your deck for a Water Energy card and attach it to this Pok\u00e9mon. Shuffle your deck afterward.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=_stormy_seas,
        ),
        Attack(
            title="Splash Burn",
            game_text="This attack does 10 damage to each of your Benched Pok\u00e9mon. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.WATER: 2, PokemonTypes.COLORLESS: 2},
            damage=130,
            effect=spread_damage(10, side='mine', also_base=True),
        ),
    ],
)