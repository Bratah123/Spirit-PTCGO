"""STUB: effect not implemented — do not guess mechanics.
Electabuzz δ (EX15 #29): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.card_effects.ex import power_of_evolution_draw_bottom
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.attacks_common import swift_attack


card = PokemonCardDef(
    guid="4db56075-9493-55ee-87e0-4d7a66867f1f",
    key="EX15",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Electabuzz.Name",
    display_name="Electabuzz δ",
    searchable_by=["Electabuzz \u03b4", "Basic", "Electabuzz"],
    subtypes=["Basic"],
    collector_number=29,
    set_code="EX15",
    rarity=Rarities.Uncommon,
    hp=60,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=125,
    abilities=[
        Ability(
            title="Power of Evolution",
            game_text="Once during your turn (before your attack), if Electabuzz is an Evolved Pok\u00e9mon, you may draw a card from the bottom of your deck. This power can't be used if Electabuzz is affected by a Special Condition.",
            ability_type=AbilityTypes.POKE_POWER,
            # STUB: ability effect not implemented
            effect=power_of_evolution_draw_bottom(),
        ),
        Attack(
            title="Swift",
            game_text="This attack's damage isn't affected by Weakness, Resistance, Pok\u00e9-Powers, Pok\u00e9-Bodies, or any other effects on the Defending Pok\u00e9mon.",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
            # STUB: attack effect not implemented
            effect=swift_attack(),
        ),
    ],
)