from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.session.effects import is_item_card
from spirit.game.content.definitions import def_for


def _is_fossil_item(card):
    return is_item_card(card) and "Fossil" in getattr(def_for(card.archetype_id), "display_name", "")


async def _fossil_clutch(ctx):
    """You may discard a Fossil Item from your hand; if you do, 50 more damage."""
    bonus = 0
    if any(_is_fossil_item(c) for c in ctx.hand()):
        gone = await ctx.discard_from_hand(1, minimum=0, predicate=_is_fossil_item,
                                           prompt="You may discard a Fossil Item card for 50 more damage")
        if gone:
            bonus = 50
    await ctx.deal_damage(ctx.ability.damage + bonus)


card = PokemonCardDef(
    guid="b2aaabac-5980-5492-9f79-9da2927e9180",
    key="BW10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Carracosta.Name",
    display_name="Carracosta",
    searchable_by=["Carracosta", "Stage 1", "Carracosta"],
    subtypes=["Stage 1"],
    collector_number=28,
    set_code="BW10",
    rarity=Rarities.Rare,
    hp=140,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=4,
    weakness_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Tirtouga.Name",
    family_id=564,
    abilities=[
        Attack(
            title="Fossil Clutch",
            game_text="You may discard an Item card that has Fossil in its name from your hand. If you do, this attack does 50 more damage.",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 2},
            damage=50,
            damage_operator="+",
            effect=_fossil_clutch,
        ),
        Attack(
            title="Waterfall",
            cost={PokemonTypes.WATER: 2, PokemonTypes.COLORLESS: 2},
            damage=80,
        ),
    ],
)