from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, SpecialConditions, AttrID
from spirit.game.card_effects.attacks_common import condition_attack
from spirit.game.card_effects.passives_common import takes_less_passive
from spirit.game.card_effects.pokemon import is_energy_card, energy_provides_type


def _ice_shielded(target, carrier):
    """Your Water Pokemon that have any Water Energy attached."""
    if target.owning_player_id != carrier.owning_player_id:
        return False
    if PokemonTypes.WATER.value not in (target.get_attribute(AttrID.POKEMON_TYPES) or []):
        return False
    return any(is_energy_card(c) and energy_provides_type(c, PokemonTypes.WATER.value)
               for c in target.children)


card = PokemonCardDef(
    guid="5069d292-7a44-5005-9e92-d9ea4e5e66ad",
    key="XY3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Aurorus.Name",
    display_name="Aurorus",
    searchable_by=["Aurorus", "Stage 1", "Aurorus"],
    subtypes=["Stage 1"],
    collector_number=26,
    set_code="XY3",
    rarity=Rarities.Rare,
    hp=130,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.METAL,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Amaura.Name",
    family_id=698,
    abilities=[
        Ability(
            title="Ice Shield",
            game_text="Any damage done by an opponent's attack to each of your Water Pok\u00e9mon that has any Water Energy attached to it is reduced by 20 (after applying Weakness and Resistance).",
            passive=takes_less_passive(20, protects=_ice_shielded),
        ),
        Attack(
            title="Icy Wind",
            game_text="Your opponent's Active Pok\u00e9mon is now Asleep.",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 3},
            damage=70,
            effect=condition_attack(SpecialConditions.ASLEEP),
        ),
    ],
)