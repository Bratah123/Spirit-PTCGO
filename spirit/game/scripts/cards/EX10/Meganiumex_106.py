"""STUB: effect not implemented — do not guess mechanics.
Meganium ex (EX10 #106): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import Activations, PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import SpecialConditions, PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.attacks_common import self_energy_discard_attack, condition_attack
from spirit.game.card_effects.ex import nurture_and_heal, nurture_and_heal_condition

card = PokemonCardDef(
    guid="660886fa-1ebf-5f39-b642-c139200a7ad6",
    key="EX10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Meganiumex.Name",
    display_name="Meganium ex",
    searchable_by=["Meganium ex", "Stage 2", "ex", "Meganiumex"],
    subtypes=["Stage 2", "ex"],
    collector_number=106,
    set_code="EX10",
    rarity=Rarities.RareHoloEX,
    hp=150,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    weakness_type=PokemonTypes.GRASS,
    resistance_type=PokemonTypes.WATER,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Bayleef.Name",
    family_id=152,
    abilities=[
        Ability(
            title="Nurture and Heal",
            game_text="Once during your turn (before your attack), you may attach a Grass Energy card from your hand to 1 of your Pok\u00e9mon. If you do, remove 1 damage counter from that Pok\u00e9mon. This power can't be used if Meganium ex is affected by a Special Condition.",
            ability_type=AbilityTypes.POKE_POWER,
            activation=Activations.ONCE_PER_TURN,
            # STUB: ability effect not implemented
            condition=nurture_and_heal_condition(),
            effect=nurture_and_heal(),
        ),
        Attack(
            title="Razor Leaf",
            cost={PokemonTypes.COLORLESS: 3},
            damage=50,
        ),
        Attack(
            title="Power Poison",
            game_text="Discard 1 Energy attached to Meganium ex. The Defending Pok\u00e9mon is now Poisoned.",
            cost={PokemonTypes.GRASS: 2, PokemonTypes.COLORLESS: 3},
            damage=90,
            # STUB: attack effect not implemented
            effect=self_energy_discard_attack(count=1, also=condition_attack(SpecialConditions.POISONED)),
            
        ),
    ],
)