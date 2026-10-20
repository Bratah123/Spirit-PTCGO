"""STUB: effect not implemented — do not guess mechanics.
M Tyranitar-EX (XY7 #92): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.ancient_traits import ancient_trait

card = PokemonCardDef(
    guid="30ebf0c3-2407-5c90-8b5b-2d24f271cf5c",
    key="XY7",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.MTyranitarEX.Name",
    display_name="M Tyranitar-EX",
    searchable_by=["M Tyranitar-EX", "MEGA", "EX", "MTyranitarEX"],
    subtypes=["MEGA", "EX"],
    collector_number=92,
    set_code="XY7",
    rarity=Rarities.RareUltra,
    hp=240,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=4,
    weakness_type=PokemonTypes.FIGHTING,
    resistance_type=PokemonTypes.PSYCHIC,
    resistance_amount=20,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.TyranitarEX.Name",
    family_id=248,
    abilities=[
        ancient_trait('θ Double'),
        Attack(
            title="Destroyer King",
            game_text="This attack does 60 more damage for each damage counter on your opponent's Active Pok\u00e9mon.",
            cost={PokemonTypes.DARKNESS: 2, PokemonTypes.COLORLESS: 2},
            damage=110,
            damage_operator="+",
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)