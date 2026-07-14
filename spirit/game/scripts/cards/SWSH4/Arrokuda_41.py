from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.support_common import search_to_bench


async def flock(ctx):
    """Search your deck for up to 2 Arrokuda and put them onto your Bench."""
    same_archetype = ctx.source.archetype_id
    await search_to_bench(
        lambda c: c.archetype_id == same_archetype, count=2,
        prompt="Choose up to 2 Arrokuda to put onto your Bench.",
    )(ctx)


card = PokemonCardDef(
    guid="abf209f4-394b-5963-979d-ea7ce09865c6",
    key="SWSH4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Arrokuda.Name",
    display_name="Arrokuda",
    searchable_by=["Arrokuda", "Basic", "Arrokuda"],
    subtypes=["Basic"],
    collector_number=41,
    set_code="SWSH4",
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    family_id=846,
    abilities=[
        Attack(
            title="Flock",
            game_text="Search your deck for up to 2 Arrokuda and put them onto your Bench. Then, shuffle your deck.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=flock,
        ),
        Attack(
            title="Peck",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 1},
            damage=20,
        ),
    ],
)