from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import (
    AttrID, CLIENT_SPECIAL_CONDITION_NAMES, PokemonTypes, PokemonStage,
    Rarities, SpecialConditions,
)
from spirit.game.card_effects.attacks_common import condition_attack
from spirit.game.session.passives import Passive


class SludgeStreetPassive(Passive):
    """The Retreat Cost of your opponent's Poisoned Pokémon is Colorless more."""

    def modify_retreat_cost(self, cost, pokemon, carrier, board):
        if pokemon.owning_player_id == carrier.owning_player_id:
            return cost
        name = CLIENT_SPECIAL_CONDITION_NAMES[SpecialConditions.POISONED]
        if name in (pokemon.get_attribute(AttrID.SPECIAL_CONDITIONS) or []):
            return cost + 1
        return cost


card = PokemonCardDef(
    guid="f3ea16e1-582d-5344-a636-9bce3bc419f3",
    key="SWSH9",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Muk.Name",
    display_name="Muk",
    searchable_by=["Muk", "Stage 1", "Muk"],
    subtypes=["Stage 1"],
    collector_number=85,
    set_code="SWSH9",
    rarity=Rarities.Rare,
    hp=130,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Grimer.Name",
    family_id=88,
    abilities=[
        Ability(
            title="Sludge Street",
            game_text="The Retreat Cost of your opponent's Poisoned Pok\u00e9mon is Colorless more.",
            passive=SludgeStreetPassive(),
        ),
        Attack(
            title="Shrieking Poison",
            game_text="Your opponent's Active Pok\u00e9mon is now Confused and Poisoned.",
            cost={PokemonTypes.DARKNESS: 1, PokemonTypes.COLORLESS: 2},
            damage=90,
            effect=condition_attack(SpecialConditions.CONFUSED, SpecialConditions.POISONED),
        ),
    ],
)