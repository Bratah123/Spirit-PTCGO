from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Activations
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes, SpecialConditions
from spirit.game.card_effects.attacks_common import condition_attack
from spirit.game.card_effects.support_common import search_to_hand
from spirit.game.session.effects import is_team_plasma_card


def _deck_not_empty(board, player_id, pokemon=None):
    deck = board.find_player_area(player_id, "deck")
    return bool(deck and deck.children)


card = PokemonCardDef(
    guid="66bd9143-6215-544a-9598-ee746fbe2ae9",
    key="Promo_BW",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Metagross.Name",
    display_name="Metagross",
    searchable_by=["Metagross", "Stage 2", "Team Plasma", "Metagross"],
    subtypes=["Stage 2", "Team Plasma"],
    collector_number=75,
    set_code="Promo_BW",
    rarity=Rarities.RarePromo,
    hp=140,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    weakness_type=PokemonTypes.PSYCHIC,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Metang.Name",
    family_id=374,
    abilities=[
        Ability(
            title="Plasma Search",
            game_text="Once during your turn (before your attack), you may search your deck for a Team Plasma card, reveal it, and put it in your hand. Shuffle your deck afterward. You may not use an Ability with the same name during your turn.",
            ability_type=AbilityTypes.POKE_ABILITY,
            activation=Activations.ONCE_PER_TURN,
            shared_once_per_turn="Plasma Search",
            condition=_deck_not_empty,
            effect=search_to_hand(is_team_plasma_card, count=1, minimum=0, reveal=True, prompt="Choose a Team Plasma card"),
        ),
        Attack(
            title="Mind Bend",
            game_text="The Defending Pok\u00e9mon is now Confused.",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 3},
            damage=60,
            effect=condition_attack(SpecialConditions.CONFUSED),
        ),
    ],
)