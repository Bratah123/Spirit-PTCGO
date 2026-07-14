from spirit.game.data_utils import PokemonToolCardDef, Attack, subtypes_for
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.attacks_common import damage_all_opponents


def _rapid_strike_holder(board, player_id, pokemon):
    return "Rapid Strike" in subtypes_for(pokemon.archetype_id)


card = PokemonToolCardDef(
    guid="4e442586-f3f2-5d6a-adb6-c2d6ddc82310",
    key="SWSH5",
    name="com.direwolfdigital.cake.data.archetypes.trainer.RapidStrikeScrollofSwirls.Name",
    display_name="Rapid Strike Scroll of Swirls",
    searchable_by=["Rapid Strike Scroll of Swirls", "PokÃ©mon Tool", "Rapid Strike"],
    subtypes=["Pokémon Tool", "Rapid Strike"],
    collector_number=131,
    set_code="SWSH5",
    rarity=Rarities.Uncommon,
    granted_abilities=[
        Attack(
            title="Matchless Maelstrom",
            game_text="This attack does 30 damage to each of your opponent's Pokémon. (Don't apply Weakness and Resistance for Benched Pokémon.)",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 2},
            condition=_rapid_strike_holder,
            effect=damage_all_opponents(30),
        ),
    ],
)
