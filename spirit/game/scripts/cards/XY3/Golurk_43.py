from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities


async def _wreck(ctx):
    """60; +60 and discard the Stadium if any Stadium is in play."""
    if ctx.stadium_in_play() is None:
        await ctx.deal_damage()
        return
    await ctx.deal_damage(120)
    await ctx.discard_stadium()


card = PokemonCardDef(
    guid="db4ee41e-c8d1-5812-ab7f-30a295270375",
    key="XY3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Golurk.Name",
    display_name="Golurk",
    searchable_by=["Golurk", "Stage 1", "Golurk"],
    subtypes=["Stage 1"],
    collector_number=43,
    set_code="XY3",
    rarity=Rarities.Rare,
    hp=130,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE1,
    retreat_cost=4,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=20,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Golett.Name",
    family_id=622,
    abilities=[
        Attack(
            title="Wreck",
            game_text="If there is any Stadium card in play, this attack does 60 more damage. Discard that Stadium card.",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 2},
            damage=60,
            damage_operator="+",
            effect=_wreck,
        ),
        Attack(
            title="Golurk Hammer",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 3},
            damage=100,
        ),
    ],
)