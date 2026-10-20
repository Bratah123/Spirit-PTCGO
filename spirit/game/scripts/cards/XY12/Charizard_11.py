from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import self_energy_discard_attack
from spirit.game.session.passives import Passive
from spirit.game.content.definitions import def_for


class _EnergyBurn(Passive):
    """All Energy attached to this Pokemon are Fire Energy instead of their usual type."""
    def modify_energy_provided(self, options, energy, holder, board):
        # The hook has no carrier: gate on the holder carrying Energy Burn
        # itself (an ability-locked holder drops out of active_passives).
        if holder is None or not options:
            return options
        if not any(getattr(a, "title", None) == "Energy Burn"
                   for a in getattr(def_for(holder.archetype_id), "abilities", None) or []):
            return options
        return [[PokemonTypes.FIRE.value] * len(o) for o in options]


card = PokemonCardDef(
    guid="b848637c-2a52-5a03-8275-f2dd0638807e",
    key="XY12",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Charizard.Name",
    display_name="Charizard",
    searchable_by=["Charizard", "Stage 2", "Charizard"],
    subtypes=["Stage 2"],
    collector_number=11,
    set_code="XY12",
    rarity=Rarities.RareHolo,
    hp=150,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.STAGE2,
    retreat_cost=3,
    weakness_type=PokemonTypes.WATER,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=20,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Charmeleon.Name",
    family_id=4,
    abilities=[
        Ability(
            title="Energy Burn",
            game_text="All Energy attached to this Pok\u00e9mon are Fire Energy instead of their usual type.",
            passive=_EnergyBurn(),
        ),
        Attack(
            title="Fire Spin",
            game_text="Discard 3 Energy attached to this Pok\u00e9mon.",
            cost={PokemonTypes.FIRE: 4},
            damage=200,
            effect=self_energy_discard_attack(count=3),
        ),
    ],
)