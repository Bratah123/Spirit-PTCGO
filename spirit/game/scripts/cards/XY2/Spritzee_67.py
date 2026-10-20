from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import flip_or_nothing


card = PokemonCardDef(
    guid="1476eaef-a9ca-54c6-a75f-9a541578c179",
    key="XY2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Spritzee.Name",
    display_name="Spritzee",
    searchable_by=["Spritzee", "Basic", "Spritzee"],
    subtypes=["Basic"],
    collector_number=67,
    set_code="XY2",
    rarity=Rarities.Common,
    hp=50,
    elements=[PokemonTypes.FAIRY],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.METAL,
    resistance_type=PokemonTypes.DARKNESS,
    resistance_amount=20,
    family_id=682,
    abilities=[
        Attack(
            title="Fairy Wind",
            cost={PokemonTypes.FAIRY: 1},
            damage=10,
        ),
        Attack(
            title="Fickle Attack",
            game_text="Flip a coin. If tails, this attack does nothing.",
            cost={PokemonTypes.FAIRY: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
            effect=flip_or_nothing(),
        ),
    ],
)