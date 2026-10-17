"""STUB: effect not implemented — do not guess mechanics.
Smeargle (XY8 #123): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="4b59e871-d207-577e-b5ba-2b8d9dec1794",
    key="XY8",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Smeargle.Name",
    display_name="Smeargle",
    searchable_by=["Smeargle", "Basic", "Smeargle"],
    subtypes=["Basic"],
    collector_number=123,
    set_code="XY8",
    rarity=Rarities.Rare,
    hp=70,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=235,
    abilities=[
        Ability(
            title="Second Coat",
            game_text="Once during your turn (before your attack), you may switch a basic Energy card attached to your Active Pok\u00e9mon with a different type of basic Energy card from your discard pile.",
            # STUB: ability effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Beat",
            cost={PokemonTypes.COLORLESS: 2},
            damage=30,
        ),
    ],
)