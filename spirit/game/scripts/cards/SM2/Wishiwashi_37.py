from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.attacks_common import snipe_attack
from spirit.game.attributes import AttrID


from spirit.game.data_utils import subtypes_for, Activations
from spirit.game.session.effects import is_pokemon_card


def _is_wishiwashi_gx(card):
    return (
        is_pokemon_card(card)
        and card.get_attribute(AttrID.EVOLUTION_LOGIC_NAME) == "Wishiwashi"
        and "GX" in subtypes_for(card.archetype_id)
    )


def schooling_condition(board, player_id, pokemon=None):
    hand = board.find_player_area(player_id, "hand")
    return bool(hand) and any(_is_wishiwashi_gx(c) for c in hand.children)


async def schooling(ctx):
    """Switch this Pokémon with a Wishiwashi-GX in your hand."""
    candidates = [c for c in ctx.hand() if _is_wishiwashi_gx(c)]
    picks = await ctx.choose_cards(
        candidates, 1, minimum=1,
        prompt="Choose a Wishiwashi-GX to switch with this Pokémon",
    )
    if picks:
        await ctx.identity_swap(ctx.source, picks[0], destination="hand")


card = PokemonCardDef(
    guid="e99b05f9-ce13-5ac0-94ff-1bb89ea4e402",
    key="SM2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Wishiwashi.Name",
    display_name="Wishiwashi",
    searchable_by=["Wishiwashi", "Basic", "Wishiwashi"],
    subtypes=["Basic"],
    collector_number=37,
    set_code="SM2",
    rarity=Rarities.Common,
    hp=30,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=0,
    weakness_type=PokemonTypes.LIGHTNING,
    family_id=746,
    abilities=[
        Ability(
            title="Schooling",
            game_text="Once during your turn (before your attack), you may switch this Pok\u00e9mon with a Wishiwashi-GX in your hand. Any attached cards, damage counters, Special Conditions, turns in play, and any other effects remain on the new Pok\u00e9mon.",
            ability_type=AbilityTypes.POKE_ABILITY,
            activation=Activations.ONCE_PER_TURN, condition=schooling_condition,
            effect=schooling,
        ),
        Attack(
            title="Sharpshooting",
            game_text="This attack does 10 damage to 1 of your opponent's Pok\u00e9mon. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.WATER: 1},
            effect=snipe_attack(10, pool='any', count=1),
        ),
    ],
)