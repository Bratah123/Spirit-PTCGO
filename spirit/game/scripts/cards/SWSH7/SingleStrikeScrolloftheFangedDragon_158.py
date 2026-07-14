from spirit.game.data_utils import PokemonToolCardDef, Attack, subtypes_for
from spirit.game.attributes import Rarities, PokemonTypes
from spirit.game.card_effects.attacks_common import self_energy_discard_attack


def _is_single_strike(board, player_id, pokemon):
    return "Single Strike" in subtypes_for(pokemon.archetype_id)


card = PokemonToolCardDef(
    guid="b4f6ffbd-a9b6-5ffb-9a69-61944acb4dc9",
    key="SWSH7",
    name="com.direwolfdigital.cake.data.archetypes.trainer.SingleStrikeScrolloftheFangedDragon.Name",
    display_name="Single Strike Scroll of the Fanged Dragon",
    searchable_by=["Single Strike Scroll of the Fanged Dragon", "Single Strike", "Item", "PokÃ©mon Tool"],
    subtypes=["Single Strike", "Item", "Pokémon Tool"],
    collector_number=158,
    set_code="SWSH7",
    rarity=Rarities.Uncommon,
    granted_abilities=[
        Attack(
            title="Superstrong Slash",
            game_text="Discard all Energy from this Pokémon.",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.METAL: 2, PokemonTypes.COLORLESS: 2},
            damage=300,
            effect=self_energy_discard_attack(all_energy=True),
            condition=_is_single_strike,
        ),
    ],
)
