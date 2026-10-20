from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import discard_random_from_hand


async def knock_off(ctx):
    await ctx.deal_damage()
    await discard_random_from_hand(ctx, player_id=ctx.opponent_id, count=1)


card = PokemonCardDef(
    guid="453985cd-24ac-52b8-b409-4741b3ae535b",
    key="XY5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Corphish.Name",
    display_name="Corphish",
    searchable_by=["Corphish", "Basic", "Corphish"],
    subtypes=["Basic"],
    collector_number=42,
    set_code="XY5",
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.GRASS,
    family_id=341,
    abilities=[
        Attack(
            title="Vice Grip",
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
        ),
        Attack(
            title="Knock Off",
            game_text="Discard a random card from your opponent's hand.",
            cost={PokemonTypes.COLORLESS: 2},
            effect=knock_off,
        ),
    ],
)