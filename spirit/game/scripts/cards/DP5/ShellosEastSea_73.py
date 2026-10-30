"""STUB: effect not implemented — do not guess mechanics.
Shellos East Sea (DP5 #73): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import snipe_attack


card = PokemonCardDef(
    guid="c305b3b6-41c5-5679-81e4-048d86d56fd3",
    key="DP5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.ShellosEastSea.Name",
    display_name="Shellos East Sea",
    searchable_by=["Shellos East Sea", "Basic", "ShellosEastSea"],
    subtypes=["Basic"],
    collector_number=73,
    set_code="DP5",
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.LIGHTNING,
    family_id=422,
    abilities=[
        Attack(
            title="Surf",
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
        ),
        Attack(
            title="Muddy Water",
            game_text="Does 10 damage to 1 of your opponent's Benched Pok\u00e9mon. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 1},
            damage=20,
            # STUB: attack effect not implemented
            effect=snipe_attack(10, also_base=True),
        ),
    ],
)