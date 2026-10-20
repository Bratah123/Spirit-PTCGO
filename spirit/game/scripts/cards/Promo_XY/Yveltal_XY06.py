"""STUB: effect not implemented — do not guess mechanics.
Yveltal (Promo_XY #XY06): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="5b2fbd36-e1eb-5dc0-af5f-f0c1bc331f48",
    key="Promo_XY",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Yveltal.Name",
    display_name="Yveltal",
    searchable_by=["Yveltal", "Basic", "Yveltal"],
    subtypes=["Basic"],
    collector_number=6,
    set_code="Promo_XY",
    rarity=Rarities.RarePromo,
    hp=130,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=20,
    family_id=717,
    abilities=[
        Attack(
            title="Oblivion Wing",
            game_text="Attach a Darkness Energy card from your discard pile to 1 of your Benched Pok\u00e9mon.",
            cost={PokemonTypes.DARKNESS: 1},
            damage=30,
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Darkness Blade",
            game_text="Flip a coin. If tails, this Pok\u00e9mon can't attack during your next turn.",
            cost={PokemonTypes.DARKNESS: 2, PokemonTypes.COLORLESS: 1},
            damage=100,
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)