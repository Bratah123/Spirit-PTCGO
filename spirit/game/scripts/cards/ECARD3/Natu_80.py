from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.ecard import foresight, removal_beam


card = PokemonCardDef(
    guid="a1889e42-ab96-5ecc-9c39-096f8ff03dc7",
    key="ECARD3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Natu.Name",
    display_name="Natu",
    searchable_by=["Natu", "Basic", "Natu"],
    subtypes=["Basic"],
    collector_number=80,
    set_code="ECARD3",
    rarity=Rarities.Common,
    hp=50,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=177,
    abilities=[
        Attack(
            title="Foresight",
            game_text="Look at the top 3 cards of either player's deck and rearrange them as you like.",
            cost={PokemonTypes.PSYCHIC: 1},
            effect=foresight,
        ),
        Attack(
            title="Removal Beam",
            game_text="If the Defending Pok\u00e9mon has any Energy cards attached to it, flip a coin. If heads, choose 1 of those Energy cards and discard it.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=10,
            effect=removal_beam,
        ),
    ],
)
