"""STUB: effect not implemented — do not guess mechanics.
Quagsire δ (EX15 #21): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.card_effects.ex import dig_up_on_evolve_energy, pump_out_if_tool
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes

card = PokemonCardDef(
    guid="1ad49804-bbee-5428-94d9-cb618bfdcef7",
    key="EX15",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Quagsire.Name",
    display_name="Quagsire δ",
    searchable_by=["Quagsire \u03b4", "Stage 1", "Quagsire"],
    subtypes=["Stage 1"],
    collector_number=21,
    set_code="EX15",
    rarity=Rarities.Rare,
    hp=80,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Wooper.Name",
    family_id=195,
    abilities=[
        Ability(
            title="Dig Up",
            game_text="Once during your turn, when you play Quagsire from your hand to evolve 1 of your Pok\u00e9mon, you may search your discard pile for up to 2 Pok\u00e9mon Tool cards, show them to your opponent, and put them into your hand.",
            ability_type=AbilityTypes.POKE_POWER,
            # STUB: ability effect not implemented
            effect=dig_up_on_evolve_energy(2),
        ),
        Attack(
            title="Pump Out",
            game_text="If Quagsire has a Pok\u00e9mon Tool card attached to it, this attack does 50 damage plus 20 more damage.",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 2},
            damage=50,
            damage_operator="+",
            # STUB: attack effect not implemented
            effect=pump_out_if_tool(50, 20),
        ),
    ],
)