from spirit.game.card_effects.ex import grind_per_energy, bite_off_ex
"""STUB: effect not implemented — do not guess mechanics.
Dark Tyranitar (EX7 #19): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import damage_all_opponents


card = PokemonCardDef(
    guid="fdfdd40a-1cb5-5ffa-bf78-a0a5303cc0cc",
    key="EX7",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.DarkTyranitar.Name",
    display_name="Dark Tyranitar",
    searchable_by=["Dark Tyranitar", "Stage 2", "DarkTyranitar"],
    subtypes=["Stage 2"],
    collector_number=19,
    set_code="EX7",
    rarity=Rarities.Rare,
    hp=120,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    resistance_type=PokemonTypes.PSYCHIC,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.DarkPupitar.Name",
    family_id=246,
    abilities=[
        Attack(
            title="Grind",
            game_text="Does 10 damage plus 10 more damage for each Energy attached to Dark Tyranitar.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
            damage_operator="+",
            # STUB: attack effect not implemented
            effect=grind_per_energy(),
        ),
        Attack(
            title="Spinning Tail",
            game_text="Does 20 damage to each of your opponent's Pok\u00e9mon. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.DARKNESS: 1, PokemonTypes.COLORLESS: 2},
            # STUB: attack effect not implemented
            effect=damage_all_opponents(20),
        ),
        Attack(
            title="Bite Off",
            game_text="If the Defending Pok\u00e9mon is Pok\u00e9mon-ex, this attack does 70 damage plus 50 more damage.",
            cost={PokemonTypes.DARKNESS: 2, PokemonTypes.COLORLESS: 3},
            damage=70,
            damage_operator="+",
            # STUB: attack effect not implemented
            effect=bite_off_ex(),
        ),
    ],
)