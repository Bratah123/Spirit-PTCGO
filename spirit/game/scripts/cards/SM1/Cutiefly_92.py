from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.passives_common import flip_prevent_damage_passive


async def _afterimage_strike(ctx):
    """40; during the opponent's next turn, flip to prevent attack damage."""
    await ctx.deal_damage()
    ctx.add_passive_through_opponents_turn(
        ctx.attacker, flip_prevent_damage_passive("Afterimage Strike"))


card = PokemonCardDef(
    guid="38898dee-0151-5410-adfc-6bd1cfbd3ed2",
    key="SM1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Cutiefly.Name",
    display_name="Cutiefly",
    searchable_by=["Cutiefly", "Basic", "Cutiefly"],
    subtypes=["Basic"],
    collector_number=92,
    set_code="SM1",
    rarity=Rarities.Common,
    hp=30,
    elements=[PokemonTypes.FAIRY],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.METAL,
    resistance_type=PokemonTypes.DARKNESS,
    resistance_amount=20,
    family_id=742,
    abilities=[
        Attack(
            title="Fly Around",
            game_text="If any damage is done to this Pok\u00e9mon by attacks during your opponent's next turn, flip a coin. If heads, prevent that damage.",
            cost={PokemonTypes.FAIRY: 1},
            damage=10,
            effect=_afterimage_strike,
        ),
    ],
)