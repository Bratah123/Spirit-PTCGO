"""STUB: effect not implemented — do not guess mechanics.
Bidoof (DP1 #70): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.ex import amnesia
from spirit.game.card_effects.dp import scavenge_trainer


card = PokemonCardDef(
    guid="366c2a31-fe88-5f60-bb65-8b2768e8480f",
    key="DP1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Bidoof.Name",
    display_name="Bidoof",
    searchable_by=["Bidoof", "Basic", "Bidoof"],
    subtypes=["Basic"],
    collector_number=70,
    set_code="DP1",
    rarity=Rarities.Common,
    hp=50,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=399,
    abilities=[
        Attack(
            title="Amnesia",
            game_text="Choose 1 of the Defending Pok\u00e9mon's attacks. That Pok\u00e9mon can't use that attack during your opponent's next turn.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=amnesia,
        ),
        Attack(
            title="Scavenge",
            game_text="Search your discard pile for a Trainer card, show it to your opponent, and put it into your hand.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=scavenge_trainer(),
        ),
    ],
)