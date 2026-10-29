from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.sm6 import lords_valley

card = PokemonCardDef(
    guid="172aca00-a998-55ff-851e-ef48f9363c08",
    key="HF",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Guzzlord.Name",
    display_name="Guzzlord",
    searchable_by=["Guzzlord", "Basic", "Ultra Beast", "Guzzlord"],
    subtypes=["Basic", "Ultra Beast"],
    collector_number=95,
    set_code="HF",
    rarity=Rarities.RareHolo,
    hp=160,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.BASIC,
    retreat_cost=4,
    weakness_type=PokemonTypes.FIGHTING,
    resistance_type=PokemonTypes.PSYCHIC,
    resistance_amount=20,
    family_id=799,
    abilities=[
        Attack(
            title="Lord's Valley",
            game_text="If you have exactly 2, 4, or 6 Prize cards remaining, discard the top 10 cards of your deck.",
            cost={PokemonTypes.DARKNESS: 4},
            damage=160,
            effect=lords_valley,
        ),
    ],
)
