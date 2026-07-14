from spirit.game.card_effects.attacks_common import snipe_attack
from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities


async def aqua_report(ctx):
    """130 damage, then your opponent reveals their hand."""
    await ctx.deal_damage()
    await ctx.reveal_hand(of_player=ctx.opponent_id)


card = PokemonCardDef(
    guid="fbac666c-1eae-5815-b8f8-66976ee0d916",
    key="SWSH2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.InteleonV.Name",
    display_name="Inteleon V",
    searchable_by=["Inteleon V", "Basic", "V", "InteleonV"],
    subtypes=["Basic", "V"],
    collector_number=180,
    set_code="SWSH2",
    rarity=Rarities.RareUltra,
    hp=200,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.LIGHTNING,
    family_id=818,
    abilities=[
        Attack(
            title="Snipe Shot",
            game_text="This attack does 40 damage to 1 of your opponent's Pok\u00e9mon. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.WATER: 1},
            effect=snipe_attack(40, pool="any", count=1),
        ),
        Attack(
            title="Aqua Report",
            game_text="Your opponent reveals their hand.",
            cost={PokemonTypes.WATER: 2, PokemonTypes.COLORLESS: 1},
            damage=130,
            effect=aqua_report,
        ),
    ],
)