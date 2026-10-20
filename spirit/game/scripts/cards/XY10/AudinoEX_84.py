"""STUB: effect not implemented — do not guess mechanics.
Audino-EX (XY10 #84): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.support_common import heal_attack


card = PokemonCardDef(
    guid="407b225d-4a96-5f64-bb4b-a02336dc918c",
    key="XY10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.AudinoEX.Name",
    display_name="Audino-EX",
    searchable_by=["Audino-EX", "Basic", "EX", "AudinoEX"],
    subtypes=["Basic", "EX"],
    collector_number=84,
    set_code="XY10",
    rarity=Rarities.RareHoloEX,
    hp=180,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=531,
    abilities=[
        Attack(
            title="Drain Slap",
            game_text="Heal 20 damage from this Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=20,
            # STUB: attack effect not implemented
            effect=heal_attack(20),
        ),
        Attack(
            title="Do the Wave",
            game_text="This attack does 10 more damage for each of your Benched Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=60,
            damage_operator="+",
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)