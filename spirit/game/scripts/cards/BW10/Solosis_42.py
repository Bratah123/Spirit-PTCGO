from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.passives_common import flip_protection


card = PokemonCardDef(
    guid="e4399a15-007d-52be-84f4-87ed739ec968",
    key="BW10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Solosis.Name",
    display_name="Solosis",
    searchable_by=["Solosis", "Basic", "Solosis"],
    subtypes=["Basic"],
    collector_number=42,
    set_code="BW10",
    rarity=Rarities.Common,
    hp=30,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=577,
    abilities=[
        Attack(
            title="Hide",
            game_text="Flip a coin. If heads, prevent all effects of attacks, including damage, done to this Pok\u00e9mon during your opponent's next turn.",
            cost={PokemonTypes.PSYCHIC: 1},
            effect=flip_protection(prevent=True, effects_too=True),
        ),
    ],
)