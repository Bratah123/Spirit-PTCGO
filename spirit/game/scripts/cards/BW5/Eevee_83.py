from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import flip_or_nothing


card = PokemonCardDef(
    guid="fac4faf4-a4ee-517a-9c1a-195a6c221365",
    key="BW5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Eevee.Name",
    display_name="Eevee",
    searchable_by=["Eevee", "Basic", "Eevee"],
    subtypes=["Basic"],
    collector_number=83,
    set_code="BW5",
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=133,
    abilities=[
        Attack(
            title="Surprise Attack",
            game_text="Flip a coin. If tails, this attack does nothing.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=20,
            effect=flip_or_nothing(),
        ),
    ],
)