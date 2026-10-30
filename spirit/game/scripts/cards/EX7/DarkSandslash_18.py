from spirit.game.card_effects.ex import poison_payback_ex7
"""STUB: effect not implemented — do not guess mechanics.
Dark Sandslash (EX7 #18): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.attacks_common import swift_attack


card = PokemonCardDef(
    guid="8f60c370-d607-59b4-bc2f-537fa3a7d36f",
    key="EX7",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.DarkSandslash.Name",
    display_name="Dark Sandslash",
    searchable_by=["Dark Sandslash", "Stage 1", "DarkSandslash"],
    subtypes=["Stage 1"],
    collector_number=18,
    set_code="EX7",
    rarity=Rarities.Rare,
    hp=70,
    elements=[PokemonTypes.FIGHTING, PokemonTypes.DARKNESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=0,
    weakness_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Sandshrew.Name",
    family_id=27,
    abilities=[
        Ability(
            title="Poison Payback",
            game_text="If Dark Sandslash is your Active Pok\u00e9mon and is damaged by an opponent's attack (even if Dark Sandslash is Knocked Out), the Attacking Pok\u00e9mon is now Poisoned.",
            ability_type=AbilityTypes.POKE_BODY,
            # STUB: ability effect not implemented
            effect=poison_payback_ex7(),
        ),
        Attack(
            title="Swift",
            game_text="This attack's damage isn't affected by Weakness, Resistance, Pok\u00e9-Powers, Pok\u00e9-Bodies, or any other effects on the Defending Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=50,
            # STUB: attack effect not implemented
            effect=swift_attack(),
        ),
    ],
)