from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Activations
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.attacks_common import self_energy_discard_attack
from spirit.game.card_effects.ecard import (
    energy_burn,
    energy_burn_condition,
    has_energy_cards_attached,
)


card = PokemonCardDef(
    guid="0d3120ac-e3bf-5ebe-9b99-7de004059f41",
    key="BASE1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Charizard.Name",
    display_name="Charizard",
    searchable_by=["Charizard", "Stage 2", "Charizard"],
    subtypes=["Stage 2"],
    collector_number=4,
    set_code="BASE1",
    rarity=Rarities.RareHolo,
    hp=120,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.STAGE2,
    retreat_cost=3,
    weakness_type=PokemonTypes.WATER,
    resistance_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Charmeleon.Name",
    family_id=4,
    abilities=[
        Ability(
            title="Energy Burn",
            game_text="As often as you like during your turn (before your attack), you may turn all Energy attached to Charizard into Fire Energy for the rest of the turn. This power can't be used if Charizard is Asleep, Confused, or Paralyzed.",
            ability_type=AbilityTypes.POKE_POWER,
            activation=Activations.UNLIMITED,
            condition=energy_burn_condition,
            effect=energy_burn,
        ),
        Attack(
            title="Fire Spin",
            game_text="Discard 2 Energy cards attached to Charizard in order to use this attack.",
            cost={PokemonTypes.FIRE: 4},
            damage=100,
            condition=has_energy_cards_attached(2),
            effect=self_energy_discard_attack(count=2),
        ),
    ],
)
