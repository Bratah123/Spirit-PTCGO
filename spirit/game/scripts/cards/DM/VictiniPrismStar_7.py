from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.trainers import is_basic_energy_card

async def upstream_spirits(ctx):
    """This attack does 20 damage for each basic Energy card in your discard
    pile. Then, shuffle those cards into your deck."""
    basics = [c for c in ctx.discard_pile() if is_basic_energy_card(c)]
    await ctx.deal_damage(20 * len(basics))
    if basics:
        await ctx.shuffle_into_deck(basics)

card = PokemonCardDef(
    guid="e3ebda73-baf3-5983-b843-c53b5e5ca9dd",
    key="DM",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.VictiniPrismStar.Name",
    display_name="Victini {*}",
    searchable_by=["Victini {*}", "Basic", "Prism Star", "VictiniPrismStar"],
    subtypes=["Basic", "Prism Star"],
    collector_number=7,
    set_code="DM",
    rarity=Rarities.Prism,
    hp=90,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.WATER,
    family_id=494,
    abilities=[
        Attack(
            title="Infinity",
            game_text="This attack does 20 damage for each basic Energy card in your discard pile. Then, shuffle those cards into your deck.",
            cost={PokemonTypes.FIRE: 2},
            damage=20,
            damage_operator="x",
            effect=upstream_spirits,
        ),
    ],
)