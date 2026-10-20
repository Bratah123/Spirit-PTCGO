from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.ancient_traits import ancient_trait


async def _gaia_volcano(ctx):
    """100; +100 and discard the Stadium if any Stadium is in play."""
    if ctx.stadium_in_play() is None:
        await ctx.deal_damage()
        return
    await ctx.deal_damage(200)
    await ctx.discard_stadium()


card = PokemonCardDef(
    guid="05023339-cfc8-5d71-8e56-9acdb78039ba",
    key="XY5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.PrimalGroudonEX.Name",
    display_name="Primal Groudon-EX",
    searchable_by=["Primal Groudon-EX", "MEGA", "EX", "PrimalGroudonEX"],
    subtypes=["MEGA", "EX"],
    collector_number=151,
    set_code="XY5",
    rarity=Rarities.RareUltra,
    hp=240,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE1,
    retreat_cost=4,
    weakness_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.GroudonEX.Name",
    family_id=383,
    abilities=[
        ancient_trait('Ω Barrier'),
        Attack(
            title="Gaia Volcano",
            game_text="If there is any Stadium card in play, this attack does 100 more damage. Discard that Stadium card.",
            cost={PokemonTypes.FIGHTING: 3, PokemonTypes.COLORLESS: 1},
            damage=100,
            damage_operator="+",
            effect=_gaia_volcano,
        ),
    ],
)