"""STUB: effect not implemented — do not guess mechanics.
Arbok δ (EX15 #13): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.card_effects.ex import strangle_vs_delta
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.attributes import SpecialConditions
from spirit.game.card_effects.attacks_common import condition_attack


card = PokemonCardDef(
    guid="5d74ea7c-7919-5765-870d-a5e561d38b17",
    key="EX15",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Arbok.Name",
    display_name="Arbok δ",
    searchable_by=["Arbok \u03b4", "Stage 1", "Arbok"],
    subtypes=["Stage 1"],
    collector_number=13,
    set_code="EX15",
    rarity=Rarities.Rare,
    hp=80,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Ekans.Name",
    family_id=24,
    abilities=[
        Attack(
            title="Burning Venom",
            game_text="The Defending Pok\u00e9mon is now Burned and Poisoned.",
            cost={PokemonTypes.COLORLESS: 1},
            # STUB: attack effect not implemented
            effect=condition_attack(SpecialConditions.BURNED, SpecialConditions.POISONED),
        ),
        Attack(
            title="Strangle",
            game_text="If the Defending Pok\u00e9mon has \u03b4 on its card, this attack does 50 damage plus 30 more damage.",
            cost={PokemonTypes.FIRE: 2, PokemonTypes.COLORLESS: 1},
            damage=50,
            damage_operator="+",
            # STUB: attack effect not implemented
            effect=strangle_vs_delta(50, 30),
        ),
    ],
)