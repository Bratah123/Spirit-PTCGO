"""STUB: effect not implemented — do not guess mechanics.
Smeargle δ (EX15 #39): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.card_effects.ex import flickering_tail_vs_ex
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.support_common import draw_attack


card = PokemonCardDef(
    guid="8c15befd-2cf3-5254-976e-f6c7b412d0f0",
    key="EX15",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Smeargle.Name",
    display_name="Smeargle δ",
    searchable_by=["Smeargle \u03b4", "Basic", "Smeargle"],
    subtypes=["Basic"],
    collector_number=39,
    set_code="EX15",
    rarity=Rarities.Uncommon,
    hp=60,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=235,
    abilities=[
        Attack(
            title="Collect",
            game_text="Draw a card.",
            cost={PokemonTypes.COLORLESS: 1},
            # STUB: attack effect not implemented
            effect=draw_attack(1),
        ),
        Attack(
            title="Flickering Tail",
            game_text="If the Defending Pok\u00e9mon is Pok\u00e9mon-ex, this attack does 10 damage plus 10 more damage and the Defending Pok\u00e9mon is now Asleep.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
            damage_operator="+",
            # STUB: attack effect not implemented
            effect=flickering_tail_vs_ex(10, 10),
        ),
    ],
)