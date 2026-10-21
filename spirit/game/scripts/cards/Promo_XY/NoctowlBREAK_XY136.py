from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.session.effects import is_trainer_card


async def _night_scan(ctx):
    """60+; the opponent reveals their hand: +30 per Trainer card in it."""
    cards = await ctx.reveal_hand(ctx.opponent_id, ctx.player_id)
    await ctx.deal_damage(ctx.ability.damage + 30 * sum(1 for c in cards or [] if is_trainer_card(c)))


card = PokemonCardDef(
    guid="04d44328-1750-5b76-bff9-bd42715bc00d",
    key="Promo_XY",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.NoctowlBREAK.Name",
    display_name="Noctowl BREAK",
    searchable_by=["Noctowl BREAK", "BREAK", "NoctowlBREAK"],
    subtypes=["BREAK"],
    collector_number=136,
    set_code="Promo_XY",
    rarity=Rarities.RarePromo,
    hp=130,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BREAK,
    retreat_cost=0,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Noctowl.Name",
    family_id=164,
    abilities=[
        Attack(
            title="Night Scan",
            game_text="Your opponent reveals his or her hand. This attack does 30 more damage for each Trainer card you find there.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=60,
            damage_operator="+",
            effect=_night_scan,
        ),
    ],
)