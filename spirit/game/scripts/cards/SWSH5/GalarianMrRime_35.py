from spirit.game.data_utils import PokemonCardDef, Attack, Ability, def_for
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.session.effects import is_item_card


def _is_ball_item(card) -> bool:
    if not is_item_card(card):
        return False
    definition = def_for(getattr(card, "archetype_id", None) or "")
    return bool(definition and "ball" in (definition.display_name or "").lower())


async def ball_juggling(ctx):
    matches = [c for c in ctx.hand() if _is_ball_item(c)]
    picks = []
    if matches:
        picks = await ctx.discard_from_hand(
            len(matches), minimum=0, predicate=_is_ball_item,
            prompt="Discard any number of Item cards with \"Ball\" in their name",
        )
    await ctx.deal_damage(10 + 40 * len(picks))


card = PokemonCardDef(
    guid="41c348c3-92e9-536a-b841-1ac6e84e8ed6",
    key="SWSH5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.GalarianMrRime.Name",
    display_name="Galarian Mr. Rime",
    searchable_by=["Galarian Mr. Rime", "Stage 1", "GalarianMrRime"],
    subtypes=["Stage 1"],
    collector_number=35,
    set_code="SWSH5",
    rarity=Rarities.Rare,
    hp=110,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.METAL,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.GalarianMrMime.Name",
    family_id=122,
    abilities=[
        Attack(
            title="Ball Juggling",
            game_text="Discard any number of Item cards that have the word \"Ball\" in their name from your hand. This attack does 40 more damage for each card you discarded in this way.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=10,
            damage_operator="+",
            effect=ball_juggling,
        ),
        Attack(
            title="Frost Smash",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 2},
            damage=80,
        ),
    ],
)