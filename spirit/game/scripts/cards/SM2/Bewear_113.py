from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.data_utils import Triggers
from spirit.game.card_effects.attacks_common import bonus_if
from spirit.game.session.effects import is_basic_pokemon


async def drastic_draw(ctx):
    """On evolve: you may draw 3 cards."""
    if await ctx.ask_yes_no("Draw 3 cards?"):
        await ctx.draw_cards(3)


card = PokemonCardDef(
    guid="2502d43c-307b-54de-81f9-7ca610710184",
    key="SM2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Bewear.Name",
    display_name="Bewear",
    searchable_by=["Bewear", "Stage 1", "Bewear"],
    subtypes=["Stage 1"],
    collector_number=113,
    set_code="SM2",
    rarity=Rarities.Uncommon,
    hp=130,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Stufful.Name",
    family_id=759,
    abilities=[
        Ability(
            title="Rake It In",
            game_text="When you play this Pok\u00e9mon from your hand to evolve 1 of your Pok\u00e9mon during your turn, you may draw 3 cards.",
            ability_type=AbilityTypes.POKE_ABILITY,
            trigger=Triggers.ON_EVOLVE,
            effect=drastic_draw,
        ),
        Attack(
            title="Dangerous Blow",
            game_text="If your opponent's Active Pok\u00e9mon is a Basic Pok\u00e9mon, this attack does 60 more damage.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=60,
            damage_operator="+",
            effect=bonus_if(lambda ctx: ctx.defender is not None and is_basic_pokemon(ctx.defender), 60),
        ),
    ],
)