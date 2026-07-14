from spirit.game.data_utils import PokemonToolCardDef, Attack, subtypes_for
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.attacks_common import damage_per, damage_counters_on


def _is_single_strike(board, player_id, pokemon):
    return "Single Strike" in subtypes_for(pokemon.archetype_id)


card = PokemonToolCardDef(
    guid="5233557e-7d9a-5977-8ea9-92d1bf89796a",
    key="SWSH5",
    name="com.direwolfdigital.cake.data.archetypes.trainer.SingleStrikeScrollofScorn.Name",
    display_name="Single Strike Scroll of Scorn",
    searchable_by=["Single Strike Scroll of Scorn", "Pok\u00c3\u00a9mon Tool", "Single Strike"],
    subtypes=["Pok\u00e9mon Tool", "Single Strike"],
    collector_number=133,
    set_code="SWSH5",
    rarity=Rarities.Uncommon,
    granted_abilities=[
        Attack(
            title="Furious Anger",
            game_text="This attack does 10 more damage for each damage counter on this Pok\u00e9mon.",
            cost={PokemonTypes.FIGHTING: 1},
            damage=10,
            damage_operator="+",
            effect=damage_per(damage_counters_on("self"), 10, base=10),
            condition=_is_single_strike,
        ),
    ],
)
