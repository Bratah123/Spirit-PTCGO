"""STUB: effect not implemented — do not guess mechanics.
Pikachu (Promo_XY #XY202): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="26effeab-6dec-5f90-aa2c-776df978c343",
    key="Promo_XY",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Pikachu.Name",
    display_name="Pikachu",
    searchable_by=["Pikachu", "Basic", "Pikachu"],
    subtypes=["Basic"],
    collector_number=202,
    set_code="Promo_XY",
    rarity=Rarities.RarePromo,
    hp=50,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    resistance_type=PokemonTypes.METAL,
    resistance_amount=20,
    family_id=25,
    abilities=[
        Attack(
            title="Charge",
            game_text="Search your deck for a Lightning Energy card and attach it to this Pok\u00e9mon. Shuffle your deck afterward.",
            cost={PokemonTypes.LIGHTNING: 1},
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Thunderbolt",
            game_text="Discard all Energy attached to this Pok\u00e9mon.",
            cost={PokemonTypes.LIGHTNING: 3},
            damage=70,
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)