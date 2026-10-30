from spirit.game.card_effects.ex import darkness_charge_self, methane_leak_between_turns
"""STUB: effect not implemented — do not guess mechanics.
Dark Weezing (EX7 #42): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.attributes import SpecialConditions
from spirit.game.card_effects.attacks_common import condition_attack


card = PokemonCardDef(
    guid="84daf00c-e741-589e-bd32-6ceeac3bfafb",
    key="EX7",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.DarkWeezing.Name",
    display_name="Dark Weezing",
    searchable_by=["Dark Weezing", "Stage 1", "DarkWeezing"],
    subtypes=["Stage 1"],
    collector_number=42,
    set_code="EX7",
    rarity=Rarities.Uncommon,
    hp=80,
    elements=[PokemonTypes.GRASS, PokemonTypes.DARKNESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.PSYCHIC,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Koffing.Name",
    family_id=109,
    abilities=[
        Ability(
            title="Methane Leak",
            trigger=Triggers.BETWEEN_TURNS,
            game_text="As long as Dark Weezing is your Active Pok\u00e9mon, put 1 damage counter on each Pok\u00e9mon that remains Poisoned between turns.",
            ability_type=AbilityTypes.POKE_BODY,
            # STUB: ability effect not implemented
            effect=methane_leak_between_turns(),
        ),
        Attack(
            title="Smog",
            game_text="The Defending Pok\u00e9mon is now Poisoned.",
            cost={PokemonTypes.COLORLESS: 1},
            # STUB: attack effect not implemented
            effect=condition_attack(SpecialConditions.POISONED),
        ),
        Attack(
            title="Darkness Charge",
            game_text="Put 2 damage counters on Dark Weezing.",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 2},
            damage=50,
            # STUB: attack effect not implemented
            effect=darkness_charge_self(),
        ),
    ],
)