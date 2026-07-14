from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import damage_per, count_bench, has_attack_titled


async def dig_it_up(ctx):
    """Look at the top card of your deck. You may discard that card."""
    top = ctx.deck_top(1)
    if not top:
        return
    card = top[0]
    idx = await ctx.present_card_choice(
        card, "Discard this card?", ["Discard", "Keep on top"])
    if idx == 0:
        await ctx.discard_cards([card])


card = PokemonCardDef(
    guid="abd22956-53b9-5d80-a68a-71fab1b8a078",
    key="SWSH8",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Sandshrew.Name",
    display_name="Sandshrew",
    searchable_by=["Sandshrew", "Basic", "Sandshrew"],
    subtypes=["Basic"],
    collector_number=131,
    set_code="SWSH8",
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.GRASS,
    family_id=27,
    abilities=[
        Attack(
            title="Dig It Up",
            game_text="Look at the top card of your deck. You may discard that card.",
            cost={PokemonTypes.FIGHTING: 1},
            effect=dig_it_up,
        ),
        Attack(
            title="Let's All Rollout",
            game_text="This attack does 20 damage for each of your Benched Pok\u00e9mon that has the Let's All Rollout attack.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
            damage_operator="x",
            effect=damage_per(count_bench("mine", has_attack_titled("Let's All Rollout")), 20),
        ),
    ],
)