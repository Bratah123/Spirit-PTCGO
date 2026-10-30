"""STUB: effect not implemented — do not guess mechanics.
Lickitung δ (EX15 #19): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.card_effects.ex import delta_mind_counters
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.support_common import draw_attack


card = PokemonCardDef(
    guid="f0668f8f-4720-51e5-a882-8c60281c1fc1",
    key="EX15",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Lickitung.Name",
    display_name="Lickitung δ",
    searchable_by=["Lickitung \u03b4", "Basic", "Lickitung"],
    subtypes=["Basic"],
    collector_number=19,
    set_code="EX15",
    rarity=Rarities.Rare,
    hp=60,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=108,
    abilities=[
        Attack(
            title="Lap Up",
            game_text="Draw 2 cards.",
            cost={PokemonTypes.COLORLESS: 1},
            # STUB: attack effect not implemented
            effect=draw_attack(2),
        ),
        Attack(
            title="Delta Mind",
            game_text="Put 1 damage counter on 1 of your opponent's Pok\u00e9mon. If that Pok\u00e9mon has \u03b4 on its card, put 3 damage counters instead.",
            cost={PokemonTypes.PSYCHIC: 1},
            # STUB: attack effect not implemented
            effect=delta_mind_counters(1, 3),
        ),
    ],
)