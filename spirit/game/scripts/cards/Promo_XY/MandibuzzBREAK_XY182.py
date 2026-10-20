"""STUB: effect not implemented — do not guess mechanics.
Mandibuzz BREAK (Promo_XY #XY182): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="c99e8ffc-d3dd-515a-93ed-c1bdfd353634",
    key="Promo_XY",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.MandibuzzBREAK.Name",
    display_name="Mandibuzz BREAK",
    searchable_by=["Mandibuzz BREAK", "BREAK", "MandibuzzBREAK"],
    subtypes=["BREAK"],
    collector_number=182,
    set_code="Promo_XY",
    rarity=Rarities.RarePromo,
    hp=140,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.BREAK,
    retreat_cost=0,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Mandibuzz.Name",
    family_id=630,
    abilities=[
        Attack(
            title="Wings of Disaster",
            game_text="This attack does 20 damage to each of your opponent's Pok\u00e9mon. Don't apply Weakness and Resistance. Discard all Pok\u00e9mon Tool cards attached to each of your opponent's Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 1},
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)