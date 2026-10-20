from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, TrainerType
from spirit.game.card_effects.attacks_common import snipe_attack


_snipe = snipe_attack(50, also_base=True)


async def _magical_symphony(ctx):
    """110; if you played a Supporter from hand this turn, 50 to 1 of your opponent's Benched Pokemon."""
    played = ctx.played_trainer_this_turn(lambda r: r[2] in (TrainerType.SUPPORTER, TrainerType.SUPPORTER.value))
    if played:
        await _snipe(ctx)
    else:
        await ctx.deal_damage()


card = PokemonCardDef(
    guid="431dc256-822d-57c5-9316-6c79af339988",
    key="XY10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.MAudinoEX.Name",
    display_name="M Audino-EX",
    searchable_by=["M Audino-EX", "MEGA", "EX", "MAudinoEX"],
    subtypes=["MEGA", "EX"],
    collector_number=85,
    set_code="XY10",
    rarity=Rarities.RareHoloEX,
    hp=220,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.AudinoEX.Name",
    family_id=531,
    abilities=[
        Attack(
            title="Magical Symphony",
            game_text="If you played a Supporter card from your hand during this turn, this attack does 50 damage to 1 of your opponent's Benched Pok\u00e9mon. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.COLORLESS: 3},
            damage=110,
            effect=_magical_symphony,
        ),
    ],
)