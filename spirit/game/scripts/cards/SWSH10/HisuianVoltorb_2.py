from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.trainers import is_basic_energy_card


def _only_turn_2(board, player_id, pokemon):
    return board.turn_state.turn_number == 2


async def cheerful_charge(ctx):
    bench = ctx.my_bench()
    if not bench:
        return
    chosen = await ctx.choose_cards(
        bench, 2, minimum=0, prompt="Choose up to 2 Benched Pokémon.",
    )
    if not chosen:
        return
    for pokemon in chosen:
        picks = await ctx.search_deck(
            is_basic_energy_card, count=1, minimum=0,
            prompt="Choose a basic Energy card to attach.",
        )
        if picks:
            await ctx.attach_energy(picks[0], pokemon)
    await ctx.shuffle_deck()


card = PokemonCardDef(
    guid="fe1c3af4-e99a-5407-b5b7-098f66828cb2",
    key="SWSH10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.HisuianVoltorb.Name",
    display_name="Hisuian Voltorb",
    searchable_by=["Hisuian Voltorb", "Basic", "HisuianVoltorb"],
    subtypes=["Basic"],
    collector_number=2,
    set_code="SWSH10",
    rarity=Rarities.Common,
    hp=50,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    family_id=100,
    abilities=[
        Attack(
            title="Cheerful Charge",
            game_text="You can use this attack only if you go second, and only during your first turn. Choose up to 2 of your Benched Pok\u00e9mon. For each of those Pok\u00e9mon, search your deck for a basic Energy card and attach it to that Pok\u00e9mon. Then, shuffle your deck.",
            cost={},
            condition=_only_turn_2,
            effect=cheerful_charge,
        ),
        Attack(
            title="Ram",
            cost={PokemonTypes.GRASS: 1},
            damage=10,
        ),
    ],
)