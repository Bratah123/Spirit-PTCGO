"""STUB: effect not implemented — do not guess mechanics.
Charizard-EX (Promo_XY #XY121): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="598255d6-d420-534f-a8a0-459770f380bb",
    key="Promo_XY",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.CharizardEX.Name",
    display_name="Charizard-EX",
    searchable_by=["Charizard-EX", "Basic", "EX", "CharizardEX"],
    subtypes=["Basic", "EX"],
    collector_number=121,
    set_code="Promo_XY",
    rarity=Rarities.RarePromo,
    hp=180,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.WATER,
    family_id=6,
    abilities=[
        Attack(
            title="Wing Attack",
            cost={PokemonTypes.COLORLESS: 3},
            damage=60,
        ),
        Attack(
            title="Combustion Blast",
            game_text="This Pok\u00e9mon can't use Combustion Blast during your next turn.",
            cost={PokemonTypes.FIRE: 2, PokemonTypes.COLORLESS: 2},
            damage=150,
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)