from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.session.effects import is_item_card
from spirit.game.card_effects.attacks_common import damage_per, count_energy


async def star_abyss(ctx):
    """VSTAR Power: you may put up to 2 Item cards from your discard pile into your hand."""
    items = [c for c in ctx.discard_pile() if is_item_card(c)]
    picks = await ctx.choose_cards(
        items, 2, minimum=0,
        prompt="Choose up to 2 Item cards to put into your hand.",
    )
    await ctx.put_in_hand(picks, reveal=False)


card = PokemonCardDef(
    guid="0e27aad5-2f95-5632-aad5-aa2779a903ab",
    key="SWSH10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.DarkraiVSTAR.Name",
    display_name="Darkrai VSTAR",
    searchable_by=["Darkrai VSTAR", "VSTAR", "DarkraiVSTAR"],
    subtypes=["VSTAR"],
    collector_number=99,
    set_code="SWSH10",
    rarity=Rarities.RareHoloVSTAR,
    hp=270,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.VSTAR,
    retreat_cost=2,
    weakness_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.DarkraiV.Name",
    family_id=491,
    abilities=[
        Ability(
            title="Star Abyss",
            game_text="During your turn, you may put up to 2 Item cards from your discard pile into your hand. (You can't use more than 1 VSTAR Power in a game.)",
            vstar=True,
            effect=star_abyss,
        ),
        Attack(
            title="Dark Pulse",
            game_text="This attack does 30 more damage for each Darkness Energy attached to all of your Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=30,
            damage_operator="+",
            effect=damage_per(count_energy("mine", energy_type=PokemonTypes.DARKNESS), 30, base=30),
        ),
    ],
)