from spirit.game.data_utils import PokemonCardDef, Attack, Ability, def_for
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities


def _is_unidentified_fossil(card):
    definition = def_for(getattr(card, "archetype_id", None) or "")
    return getattr(definition, "display_name", None) == "Unidentified Fossil"


async def fossil_drop(ctx):
    """30, +120 if you discard an Unidentified Fossil card from your hand."""
    bonus = 0
    fossils = [c for c in ctx.hand() if _is_unidentified_fossil(c)]
    if fossils and await ctx.ask_yes_no(
        "Discard an Unidentified Fossil card from your hand? "
        "If you do, this attack does 120 more damage."
    ):
        discarded = await ctx.discard_from_hand(
            1, prompt="Discard an Unidentified Fossil card",
            predicate=_is_unidentified_fossil,
        )
        if discarded:
            bonus = 120
    await ctx.deal_damage(30 + bonus)

card = PokemonCardDef(
    guid="3f686a69-d104-5d41-8ff7-ebf38540bbb1",
    key="SWSH12",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Anorith.Name",
    display_name="Anorith",
    searchable_by=["Anorith", "Stage 1", "Anorith"],
    subtypes=["Stage 1"],
    collector_number=95,
    set_code="SWSH12",
    rarity=Rarities.Uncommon,
    hp=90,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.UnidentifiedFossil.Name",
    family_id=347,
    abilities=[
        Attack(
            title="Fossil Drop",
            game_text="You may discard an Unidentified Fossil card from your hand. If you do, this attack does 120 more damage.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=30,
            damage_operator="+",
            effect=fossil_drop,
        ),
    ],
)