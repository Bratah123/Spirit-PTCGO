"""STUB: effect not implemented — do not guess mechanics.
Chimecho (EX9 #12): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.support_common import draw_attack
from spirit.game.card_effects.ex import confuse_if_evolved


card = PokemonCardDef(
    guid="067a0cb4-1fbe-5cd7-a562-9e26ae750dfa",
    key="EX9",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Chimecho.Name",
    display_name="Chimecho",
    searchable_by=["Chimecho", "Basic", "Chimecho"],
    subtypes=["Basic"],
    collector_number=12,
    set_code="EX9",
    rarity=Rarities.Rare,
    hp=70,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=358,
    abilities=[
        Attack(
            title="Collect",
            game_text="Draw a card.",
            cost={PokemonTypes.COLORLESS: 1},
            # STUB: attack effect not implemented
            effect=draw_attack(1),
        ),
        Attack(
            title="Warp Sounds",
            game_text="If the Defending Pok\u00e9mon is an Evolved Pok\u00e9mon, the Defending Pok\u00e9mon is now Confused.",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 1},
            damage=20,
                        effect=confuse_if_evolved(),
        ),
    ],
)