"""STUB: effect not implemented — do not guess mechanics.
Hariyama (EX9 #31): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.attributes import SpecialConditions
from spirit.game.card_effects.attacks_common import condition_attack
from spirit.game.card_effects.ex import cross_cut


card = PokemonCardDef(
    guid="ff57804b-b2b1-5886-b669-e78637becd2c",
    key="EX9",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Hariyama.Name",
    display_name="Hariyama",
    searchable_by=["Hariyama", "Stage 1", "Hariyama"],
    subtypes=["Stage 1"],
    collector_number=31,
    set_code="EX9",
    rarity=Rarities.Uncommon,
    hp=80,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Makuhita.Name",
    family_id=296,
    abilities=[
        Attack(
            title="Cross-Cut",
            game_text="If the Defending Pok\u00e9mon is an Evolved Pok\u00e9mon, this attack does 20 damage plus 20 more damage.",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 1},
            damage=20,
            damage_operator="+",
                        effect=cross_cut(20, 20),
        ),
        Attack(
            title="Shove",
            game_text="Flip a coin. If heads, the Defending Pok\u00e9mon is now Paralyzed.",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 2},
            damage=40,
            # STUB: attack effect not implemented
            effect=condition_attack(SpecialConditions.PARALYZED, flip=True),
        ),
    ],
)