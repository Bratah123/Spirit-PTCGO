"""STUB: effect not implemented — do not guess mechanics.
Tropius δ (EX15 #23): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.card_effects.ex import grind_per_energy, tropical_heal_on_bench
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes

card = PokemonCardDef(
    guid="d9c3c22e-84ae-5fdf-a5b4-a862b98c751b",
    key="EX15",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Tropius.Name",
    display_name="Tropius δ",
    searchable_by=["Tropius \u03b4", "Basic", "Tropius"],
    subtypes=["Basic"],
    collector_number=23,
    set_code="EX15",
    rarity=Rarities.Rare,
    hp=70,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    family_id=357,
    abilities=[
        Ability(
            title="Tropical Heal",
            game_text="Once during your turn, when you put Tropius from your hand onto your Bench, you may remove all Special Conditions, Imprison markers, and Shock-wave markers from your Pok\u00e9mon.",
            ability_type=AbilityTypes.POKE_POWER,
            # STUB: ability effect not implemented
            effect=tropical_heal_on_bench(),
        ),
        Attack(
            title="Grind",
            game_text="Does 10 damage times the amount of Energy attached to Tropius.",
            cost={PokemonTypes.METAL: 1},
            damage=10,
            damage_operator="x",
            # STUB: attack effect not implemented
            effect=grind_per_energy(10, 10),
        ),
    ],
)