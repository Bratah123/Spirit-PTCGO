from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.trainers import is_basic_energy_card
from spirit.game.card_effects.attacks_common import lock_defender_attacks


async def _gather_energy(ctx):
    """Printed damage; search your deck for a basic Energy card and attach it to
    1 of your Pokemon; shuffle."""
    await ctx.deal_damage()
    picks = await ctx.search_deck(is_basic_energy_card, count=1, minimum=0,
                                  prompt="Choose a basic Energy card to attach")
    if picks:
        target = await ctx.choose_pokemon(ctx.my_pokemon_in_play(), "Choose a Pok\u00e9mon to attach it to")
        await ctx.attach_energy(picks[0], target or ctx.attacker)
    await ctx.shuffle_deck()


async def iron_breaker(ctx):
    """80. Defending Pokemon can't attack during opponent's next turn."""
    await ctx.deal_damage()
    lock_defender_attacks(ctx)


card = PokemonCardDef(
    guid="b2876ebf-d49c-5bdd-90f5-a4655c85e822",
    key="XY1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Wigglytuff.Name",
    display_name="Wigglytuff",
    searchable_by=["Wigglytuff", "Stage 1", "Wigglytuff"],
    subtypes=["Stage 1"],
    collector_number=89,
    set_code="XY1",
    rarity=Rarities.Rare,
    hp=100,
    elements=[PokemonTypes.FAIRY],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.METAL,
    resistance_type=PokemonTypes.DARKNESS,
    resistance_amount=20,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Jigglypuff.Name",
    family_id=39,
    abilities=[
        Attack(
            title="Gather Energy",
            game_text="Search your deck for a basic Energy card and attach it to 1 of your Pok\u00e9mon. Shuffle your deck afterward.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=_gather_energy,
        ),
        Attack(
            title="Hocus Pinkus",
            game_text="The Defending Pok\u00e9mon can't attack during your opponent's next turn.",
            cost={PokemonTypes.FAIRY: 1, PokemonTypes.COLORLESS: 2},
            damage=60,
            effect=iron_breaker,
        ),
    ],
)