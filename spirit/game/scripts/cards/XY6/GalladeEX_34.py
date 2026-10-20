from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.support_common import opponent_switches
from spirit.game.card_effects.attacks_common import damage_per, count_prizes_remaining


async def push_down(ctx):
    await ctx.deal_damage()
    opp_active = ctx.opponent_active()
    if opp_active is None or not ctx.opponent_bench() or ctx.effects_blocked(opp_active):
        return
    if await ctx.ask_yes_no("Have your opponent switch their Active Pokémon with 1 of their Benched Pokémon?"):
        await opponent_switches(ctx)


card = PokemonCardDef(
    guid="250f6b57-c178-51cd-a598-37e7d7dcf442",
    key="XY6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.GalladeEX.Name",
    display_name="Gallade-EX",
    searchable_by=["Gallade-EX", "Basic", "EX", "GalladeEX"],
    subtypes=["Basic", "EX"],
    collector_number=34,
    set_code="XY6",
    rarity=Rarities.RareHoloEX,
    hp=170,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=475,
    abilities=[
        Attack(
            title="Swift Lunge",
            game_text="You may have your opponent switch his or her Active Pok\u00e9mon with 1 of his or her Benched Pok\u00e9mon.",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
            effect=push_down,
        ),
        Attack(
            title="Piercing Prizes",
            game_text="This attack does 20 more damage for each of your remaining Prize cards.",
            cost={PokemonTypes.PSYCHIC: 3},
            damage=50,
            damage_operator="+",
            effect=damage_per(count_prizes_remaining('mine'), 20, base=50),
        ),
    ],
)