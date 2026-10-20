"""STUB: effect not implemented — do not guess mechanics.
Bibarel (XY5 #118): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, SpecialConditions
from spirit.game.card_effects.attacks_common import condition_attack


card = PokemonCardDef(
    guid="d10884df-22f2-5787-a4a8-d9dc5f6acb2b",
    key="XY5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Bibarel.Name",
    display_name="Bibarel",
    searchable_by=["Bibarel", "Stage 1", "Bibarel"],
    subtypes=["Stage 1"],
    collector_number=118,
    set_code="XY5",
    rarity=Rarities.Uncommon,
    hp=120,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Bidoof.Name",
    family_id=399,
    abilities=[
        Attack(
            title="Yawn",
            game_text="Your opponent's Active Pok\u00e9mon is now Asleep.",
            cost={PokemonTypes.COLORLESS: 1},
            # STUB: attack effect not implemented
            effect=condition_attack(SpecialConditions.ASLEEP),
        ),
        Attack(
            title="Continuous Headbutt",
            game_text="Flip a coin until you get tails. This attack does 80 damage times the number of heads.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=80,
            damage_operator="x",
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)