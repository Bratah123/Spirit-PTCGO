from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Triggers, def_for
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, SpecialConditions
from spirit.game.card_effects.attacks_common import condition_attack
from spirit.game.session.effects import is_item_card


def _is_rotom_item(card):
    if not is_item_card(card):
        return False
    definition = def_for(card.archetype_id)
    name = getattr(definition, "display_name", None) or ""
    return "rotom" in name.lower()


async def roto_choice(ctx):
    if not await ctx.ask_yes_no(
            "Search your deck for up to 2 Item cards that have the word "
            "\"Rotom\" in their name?"):
        return
    picks = await ctx.search_deck(
        _is_rotom_item, count=2, minimum=0,
        prompt="Choose up to 2 Item cards with \"Rotom\" in their name.",
    )
    await ctx.put_in_hand(picks, reveal=True)
    await ctx.shuffle_deck()

card = PokemonCardDef(
    guid="c3ce1412-65f6-556c-a148-09658e79cc26",
    key="SWSH45",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Rotom.Name",
    display_name="Rotom",
    searchable_by=["Rotom", "Basic", "Rotom"],
    subtypes=["Basic"],
    collector_number=34,
    set_code="SWSH45",
    rarity=Rarities.Uncommon,
    hp=80,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=479,
    abilities=[
        Ability(
            title="Roto Choice",
            game_text="When you play this Pok\u00e9mon from your hand onto your Bench during your turn, you may search your deck for up to 2 Item cards that have the word \"Rotom\" in their name, reveal them, and put them into your hand. Then, shuffle your deck.",
            trigger=Triggers.ON_PLAY,
            effect=roto_choice,
        ),
        Attack(
            title="Thunder Shock",
            game_text="Flip a coin. If heads, your opponent's Active Pok\u00e9mon is now Paralyzed.",
            cost={PokemonTypes.LIGHTNING: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
            effect=condition_attack(SpecialConditions.PARALYZED, flip=True),
        ),
    ],
)