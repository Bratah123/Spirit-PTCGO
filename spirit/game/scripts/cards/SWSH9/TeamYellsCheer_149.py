from spirit.game.data_utils import SupporterCardDef, def_for
from spirit.game.attributes import Rarities
from spirit.game.session.effects import is_pokemon_card, is_supporter_card
from spirit.game.card_effects.support_common import recover_from_discard, requires_discard


def _team_yells_cheer_predicate(c):
    if not (is_pokemon_card(c) or is_supporter_card(c)):
        return False
    definition = def_for(c.archetype_id)
    return not (definition and definition.display_name == "Team Yell's Cheer")


card = SupporterCardDef(
    guid="7b2b7973-efcb-5a6f-b416-99a988a1e7e4",
    key="SWSH9",
    name="com.direwolfdigital.cake.data.archetypes.trainer.TeamYellsCheer.Name",
    display_name="Team Yell's Cheer",
    searchable_by=["Team Yell's Cheer", "Supporter"],
    subtypes=["Supporter"],
    collector_number=149,
    set_code="SWSH9",
    rarity=Rarities.Uncommon,
    effect=recover_from_discard(
        _team_yells_cheer_predicate, count=3, to="deck_shuffle",
        prompt="Choose up to 3 Pokémon and/or Supporter cards to shuffle into your deck",
    ),
    condition=requires_discard(_team_yells_cheer_predicate),
)
