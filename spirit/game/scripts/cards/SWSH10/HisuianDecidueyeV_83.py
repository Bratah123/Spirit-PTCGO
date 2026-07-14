from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.support_common import search_to_hand


async def close_quarters_shooting(ctx):
    await ctx.deal_damage(ignore_target_effects=True)


card = PokemonCardDef(
    guid="6edca0e4-efec-5a00-bb40-5a49c47f1943",
    key="SWSH10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.HisuianDecidueyeV.Name",
    display_name="Hisuian Decidueye V",
    searchable_by=["Hisuian Decidueye V", "Basic", "V", "HisuianDecidueyeV"],
    subtypes=["Basic", "V"],
    collector_number=83,
    set_code="SWSH10",
    rarity=Rarities.RareHoloV,
    hp=220,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=724,
    abilities=[
        Attack(
            title="Mountain Hunt",
            game_text="Search your deck for up to 2 cards and put them into your hand. Then, shuffle your deck.",
            cost={PokemonTypes.FIGHTING: 1},
            effect=search_to_hand(count=2, minimum=0, reveal=False,
                                   prompt="Choose up to 2 cards to put into your hand."),
        ),
        Attack(
            title="Close-Quarters Shooting",
            game_text="This attack's damage isn't affected by any effects on your opponent's Active Pok\u00e9mon.",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 2},
            damage=100,
            effect=close_quarters_shooting,
        ),
    ],
)