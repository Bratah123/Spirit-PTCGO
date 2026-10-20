"""STUB: effect not implemented — do not guess mechanics.
Relicanth (XY7 #23): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import recoil_attack


card = PokemonCardDef(
    guid="508b7adf-030b-559e-8c46-d981d8e2cbd0",
    key="XY7",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Relicanth.Name",
    display_name="Relicanth",
    searchable_by=["Relicanth", "Basic", "Relicanth"],
    subtypes=["Basic"],
    collector_number=23,
    set_code="XY7",
    rarity=Rarities.Common,
    hp=90,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.GRASS,
    family_id=369,
    abilities=[
        Attack(
            title="Deep Sea Search",
            game_text="Search your deck for up to 2 Pok\u00e9mon Tool cards, reveal them, and put them into your hand. Shuffle your deck afterward.",
            cost={PokemonTypes.COLORLESS: 1},
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Take Down",
            game_text="This Pok\u00e9mon does 10 damage to itself.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=30,
            # STUB: attack effect not implemented
            effect=recoil_attack(10),
        ),
    ],
)