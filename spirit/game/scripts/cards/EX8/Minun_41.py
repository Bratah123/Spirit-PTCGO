"""STUB: effect not implemented — do not guess mechanics.
Minun (EX8 #41): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.support_common import recover_from_discard
from spirit.game.card_effects.ex import spark_vs_bodies



card = PokemonCardDef(
    guid="d616de21-6170-50d5-8159-bffbaab4da0c",
    key="EX8",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Minun.Name",
    display_name="Minun",
    searchable_by=["Minun", "Basic", "Minun"],
    subtypes=["Basic"],
    collector_number=41,
    set_code="EX8",
    rarity=Rarities.Uncommon,
    hp=60,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=312,
    abilities=[
        Attack(
            title="Sniff Out",
            game_text="Put any 1 card from your discard pile into your hand.",
            cost={PokemonTypes.COLORLESS: 1},
            # STUB: attack effect not implemented
            effect=recover_from_discard(count=1, minimum=1, reveal=False, to='hand', prompt='Choose a card from your discard pile.'),
        ),
        Attack(
            title="Negative Spark",
            game_text="Does 20 damage to each of your opponent's Pok\u00e9mon that has any Pok\u00e9-Bodies. Don't apply Weakness and Resistance.",
            cost={PokemonTypes.LIGHTNING: 1},
            # STUB: attack effect not implemented
            effect=spark_vs_bodies(),
        ),
    ],
)