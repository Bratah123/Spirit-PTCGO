from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.support_common import recover_from_discard
from spirit.game.card_effects.trainers import is_basic_energy_card


card = PokemonCardDef(
    guid="95b345b3-2ea3-50fc-99e2-5f3ec6e04fd3",
    key="ECARD3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Cleffa.Name",
    display_name="Cleffa",
    searchable_by=["Cleffa", "Baby", "Cleffa"],
    subtypes=["Baby"],
    collector_number=48,
    set_code="ECARD3",
    rarity=Rarities.Common,
    hp=30,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    family_id=173,
    abilities=[
        Attack(
            title="Energy Recycle",
            game_text="Shuffle a basic Energy card from your discard pile into your deck.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=recover_from_discard(
                is_basic_energy_card, count=1, minimum=1, to="deck_shuffle",
                prompt="Choose a basic Energy card to shuffle into your deck",
            ),
        ),
    ],
)
