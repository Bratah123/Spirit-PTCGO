from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import damage_per, count_discard
from spirit.game.card_effects.trainers import is_energy_card


async def fireball_fever(ctx):
    """You may discard up to 5 cards from the top of your deck: 40 more damage each."""
    top = ctx.deck_top(5)
    picks = []
    if top:
        picks = await ctx.choose_cards(
            top, len(top), minimum=0, display_cards=top,
            prompt="Choose up to 5 cards to discard from the top of your deck",
        )
        if picks:
            await ctx.discard_cards(picks)
    await ctx.deal_damage(40 + 40 * len(picks))


card = PokemonCardDef(
    guid="b5ae9386-ac08-5865-a660-4a767e26f2a6",
    key="CZ",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.SimisearVSTAR.Name",
    display_name="Simisear VSTAR",
    searchable_by=["Simisear VSTAR", "VSTAR", "SimisearVSTAR"],
    subtypes=["VSTAR"],
    collector_number=23,
    set_code="CZ",
    rarity=Rarities.RareHoloVSTAR,
    hp=260,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.VSTAR,
    retreat_cost=2,
    weakness_type=PokemonTypes.WATER,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.SimisearV.Name",
    family_id=514,
    abilities=[
        Attack(
            title="Fireball Fever",
            game_text="You may discard up to 5 cards from the top of your deck. This attack does 40 more damage for each card you discarded in this way.",
            cost={PokemonTypes.FIRE: 1, PokemonTypes.COLORLESS: 2},
            damage=40,
            damage_operator="+",
            effect=fireball_fever,
        ),
        Attack(
            title="Ember Star",
            game_text="This attack does 30 damage for each Energy card in your discard pile. (You can't use more than 1 VSTAR Power in a game.)",
            cost={PokemonTypes.FIRE: 1},
            damage=30,
            damage_operator="x",
            vstar=True,
            effect=damage_per(count_discard("mine", pred=is_energy_card), 30),
        ),
    ],
)