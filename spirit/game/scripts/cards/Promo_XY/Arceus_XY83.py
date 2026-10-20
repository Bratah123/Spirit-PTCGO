"""STUB: effect not implemented — do not guess mechanics.
Arceus (Promo_XY #XY83): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="f73eeedd-5823-59a6-84c2-1a0a55e3979e",
    key="Promo_XY",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Arceus.Name",
    display_name="Arceus",
    searchable_by=["Arceus", "Basic", "Arceus"],
    subtypes=["Basic"],
    collector_number=83,
    set_code="Promo_XY",
    rarity=Rarities.RarePromo,
    hp=120,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=493,
    abilities=[
        Attack(
            title="Gather Light",
            game_text="Move as many Energy as you like from your Benched Pok\u00e9mon to this Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 1},
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Judgment Blast",
            game_text="This attack does 30 more damage for each different type of basic Energy attached to this Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=10,
            damage_operator="+",
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)