"""STUB: effect not implemented — do not guess mechanics.
Magcargo (EX10 #41): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import AbilityTypes, PokemonStage, PokemonTypes, Rarities
from spirit.game.card_effects.attacks_common import smokescreen_attack
from spirit.game.card_effects.ex import dual_armor_if_energy, extra_vs_ex


card = PokemonCardDef(
    guid="f1f43e6f-99c9-52df-a2bb-a19c00337cb0",
    key="EX10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Magcargo.Name",
    display_name="Magcargo",
    searchable_by=["Magcargo", "Stage 1", "Magcargo"],
    subtypes=["Stage 1"],
    collector_number=41,
    set_code="EX10",
    rarity=Rarities.Uncommon,
    hp=80,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.WATER,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Slugma.Name",
    family_id=218,
    abilities=[
        Ability(
            title="Dual Armor",
            game_text="As long as Magcargo has any Fighting Energy attached to it, Magcargo is both Fire and Fighting type.",
            ability_type=AbilityTypes.POKE_BODY,
            passive=dual_armor_if_energy(PokemonTypes.FIGHTING, PokemonTypes.FIRE, PokemonTypes.FIGHTING),
        ),
        Attack(
            title="Smokescreen",
            game_text="If the Defending Pok\u00e9mon tries to attack during your opponent's next turn, your opponent flips a coin. If tails, that attack does nothing.",
            cost={PokemonTypes.FIRE: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
            # STUB: attack effect not implemented
            effect=smokescreen_attack(),
        ),
        Attack(
            title="Extra Flame",
            game_text="If the Defending Pok\u00e9mon is Pok\u00e9mon-ex, this attack does 40 damage plus 30 more damage.",
            cost={PokemonTypes.FIRE: 1, PokemonTypes.COLORLESS: 2},
            damage=40,
            damage_operator="+",
            # STUB: attack effect not implemented
            effect=extra_vs_ex(40, 30),
        ),
    ],
)