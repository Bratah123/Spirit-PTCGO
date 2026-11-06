from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import flip_or_nothing


card = PokemonCardDef(
    guid="35f3e5c7-6e4a-5866-a049-ce83cee74239",
    key="ECARD1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Spearow.Name",
    display_name="Spearow",
    searchable_by=["Spearow", "Basic", "Spearow"],
    subtypes=["Basic"],
    collector_number=130,
    set_code="ECARD1",
    rarity=Rarities.Common,
    hp=40,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    family_id=21,
    abilities=[
        Attack(
            title="Razor Wind",
            game_text="Flip a coin. If tails, this attack does nothing.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=20,
            effect=flip_or_nothing(),
        ),
    ],
)
