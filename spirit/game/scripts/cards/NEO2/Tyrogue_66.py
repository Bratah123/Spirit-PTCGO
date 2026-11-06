from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import flip_or_nothing


card = PokemonCardDef(
    guid="bab783d2-dcbf-5af5-9576-74ba93cbc678",
    key="NEO2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Tyrogue.Name",
    display_name="Tyrogue",
    searchable_by=["Tyrogue", "Baby", "Tyrogue"],
    subtypes=["Baby"],
    collector_number=66,
    set_code="NEO2",
    rarity=Rarities.Common,
    hp=30,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=0,
    family_id=236,
    abilities=[
        Attack(
            title="Smash Punch",
            game_text="Flip a coin. If tails, this attack does nothing.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=30,
            effect=flip_or_nothing(),
        ),
    ],
)
