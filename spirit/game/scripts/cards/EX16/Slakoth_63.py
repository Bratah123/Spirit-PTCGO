"""STUB: effect not implemented — do not guess mechanics.
Slakoth (EX16 #63): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.ex import amnesia


card = PokemonCardDef(
    guid="b84cf17f-9f20-5d7e-921a-806737a2f2de",
    key="EX16",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Slakoth.Name",
    display_name="Slakoth",
    searchable_by=["Slakoth", "Basic", "Slakoth"],
    subtypes=["Basic"],
    collector_number=63,
    set_code="EX16",
    rarity=Rarities.Common,
    hp=40,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=287,
    abilities=[
        Attack(
            title="Amnesia",
            game_text="Choose 1 of the Defending Pok\u00e9mon's attacks. That Pok\u00e9mon can't use that attack during your opponent's next turn.",
            cost={PokemonTypes.COLORLESS: 1},
            # STUB: attack effect not implemented
            effect=amnesia,
        ),
        Attack(
            title="Scratch",
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
        ),
    ],
)