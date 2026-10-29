"""STUB: effect not implemented — do not guess mechanics.
Breloom (SL #5): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, SpecialConditions
from spirit.game.card_effects.attacks_common import condition_attack

card = PokemonCardDef(
    guid="e3b08a71-e9dd-5106-b92b-6e8808fe266a",
    key="SL",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Breloom.Name",
    display_name="Breloom",
    searchable_by=["Breloom", "Stage 1", "Breloom"],
    subtypes=["Stage 1"],
    collector_number=5,
    set_code="SL",
    rarity=Rarities.Common,
    hp=110,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Shroomish.Name",
    family_id=285,
    abilities=[
        Attack(
            title="Hibernation Spore",
            game_text="Your opponent's Active Pok\u00e9mon is now Asleep. Your opponent flips 2 coins instead of 1 between turns. If either of them is tails, that Pok\u00e9mon is still Asleep.",
            cost={PokemonTypes.GRASS: 1},
            effect=condition_attack(SpecialConditions.ASLEEP, checkup_coins=2),
        ),
        Attack(
            title="Magnum Punch",
            cost={PokemonTypes.COLORLESS: 3},
            damage=80,
        ),
    ],
)