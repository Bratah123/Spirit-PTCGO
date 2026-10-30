"""STUB: effect not implemented — do not guess mechanics.
Exploud (EX9 #3): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.support_common import draw_attack
from spirit.game.attributes import SpecialConditions
from spirit.game.card_effects.attacks_common import condition_attack
from spirit.game.card_effects.ex import mega_throw_ex


card = PokemonCardDef(
    guid="0b76053a-b335-52e2-9236-a9fbbf5d7f4b",
    key="EX9",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Exploud.Name",
    display_name="Exploud",
    searchable_by=["Exploud", "Stage 2", "Exploud"],
    subtypes=["Stage 2"],
    collector_number=3,
    set_code="EX9",
    rarity=Rarities.RareHolo,
    hp=120,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Loudred.Name",
    family_id=293,
    abilities=[
        Attack(
            title="Collect",
            game_text="Draw 3 cards.",
            cost={PokemonTypes.COLORLESS: 1},
            # STUB: attack effect not implemented
            effect=draw_attack(3),
        ),
        Attack(
            title="Body Slam",
            game_text="Flip a coin. If heads, the Defending Pok\u00e9mon is now Paralyzed.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=30,
            # STUB: attack effect not implemented
            effect=condition_attack(SpecialConditions.PARALYZED, flip=True),
        ),
        Attack(
            title="Hyper Voice",
            cost={PokemonTypes.COLORLESS: 3},
            damage=50,
        ),
        Attack(
            title="Mega Throw",
            game_text="If the Defending Pok\u00e9mon is Pok\u00e9mon-ex, this attack does 60 damage plus 40 more damage.",
            cost={PokemonTypes.COLORLESS: 4},
            damage=60,
            damage_operator="+",
                        effect=mega_throw_ex(60, 40),
        ),
    ],
)