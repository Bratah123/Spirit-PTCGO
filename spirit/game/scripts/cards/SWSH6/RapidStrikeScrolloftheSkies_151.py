from spirit.game.data_utils import PokemonToolCardDef, Attack, subtypes_for
from spirit.game.attributes import Rarities, PokemonTypes
from spirit.game.card_effects.attacks_common import damage_per, count_energy


def _is_rapid_strike(board, player_id, pokemon):
    return "Rapid Strike" in subtypes_for(pokemon.archetype_id)


card = PokemonToolCardDef(
    guid="9ffc4f8e-975d-5a0c-829b-c2ffb5761ee1",
    key="SWSH6",
    name="com.direwolfdigital.cake.data.archetypes.trainer.RapidStrikeScrolloftheSkies.Name",
    display_name="Rapid Strike Scroll of the Skies",
    searchable_by=["Rapid Strike Scroll of the Skies", "Pok\u00c3\u00a9mon Tool", "Rapid Strike"],
    subtypes=["Pok\u00e9mon Tool", "Rapid Strike"],
    collector_number=151,
    set_code="SWSH6",
    rarity=Rarities.Uncommon,
    granted_abilities=[
        Attack(
            title="Gravdrop",
            game_text="This attack does 50 more damage for each Energy attached to your opponent's Active Pok\u00e9mon.",
            cost={PokemonTypes.LIGHTNING: 1, PokemonTypes.COLORLESS: 1},
            damage=10,
            damage_operator="+",
            effect=damage_per(count_energy("defender"), 50, base=10),
            condition=_is_rapid_strike,
        ),
    ],
)
