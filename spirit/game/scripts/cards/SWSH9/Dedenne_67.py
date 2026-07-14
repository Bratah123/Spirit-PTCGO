from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, SpecialConditions
from spirit.game.card_effects.attacks_common import count_prizes_remaining


async def dede_flash(ctx):
    """20, +60 more and opponent's Active becomes Confused if they have exactly 1 Prize left."""
    bonus = count_prizes_remaining("opponent")(ctx) == 1
    await ctx.deal_damage(20 + (60 if bonus else 0))
    if bonus:
        await ctx.apply_special_condition(ctx.defender, SpecialConditions.CONFUSED)

card = PokemonCardDef(
    guid="6ad2b60b-76b3-5ed8-9724-5c7252140823",
    key="SWSH9",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Dedenne.Name",
    display_name="Dedenne",
    searchable_by=["Dedenne", "Basic", "Dedenne"],
    subtypes=["Basic"],
    collector_number=67,
    set_code="SWSH9",
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.METAL,
    family_id=702,
    abilities=[
        Attack(
            title="Dede-Flash",
            game_text="If your opponent has exactly 1 Prize card remaining, this attack does 60 more damage, and your opponent's Active Pok\u00e9mon is now Confused.",
            cost={PokemonTypes.PSYCHIC: 1},
            damage=20,
            damage_operator="+",
            effect=dede_flash,
        ),
    ],
)