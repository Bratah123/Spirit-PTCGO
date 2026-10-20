from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import discard_random_from_hand


async def knock_off(ctx):
    await ctx.deal_damage()
    await discard_random_from_hand(ctx, player_id=ctx.opponent_id, count=1)


card = PokemonCardDef(
    guid="32c99008-9f1f-5886-bcd5-339851e78b0e",
    key="XY8",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Pancham.Name",
    display_name="Pancham",
    searchable_by=["Pancham", "Basic", "Pancham"],
    subtypes=["Basic"],
    collector_number=86,
    set_code="XY8",
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=674,
    abilities=[
        Attack(
            title="Pompous Punch",
            game_text="Discard a random card from your opponent's hand.",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 1},
            damage=10,
            effect=knock_off,
        ),
    ],
)