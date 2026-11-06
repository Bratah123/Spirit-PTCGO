from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.support_common import discard_then_draw


card = PokemonCardDef(
    guid="130bf92e-b5d6-5657-a4f1-44cd2fe7586e",
    key="XY9",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Gible.Name",
    display_name="Gible",
    searchable_by=["Gible", "Basic", "Gible"],
    subtypes=["Basic"],
    collector_number=68,
    set_code="XY9",
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.GRASS,
    family_id=443,
    abilities=[
        Attack(
            title="Never Enough",
            game_text="Discard a card from your hand. If you do, draw 2 cards.",
            cost={PokemonTypes.FIGHTING: 1},
            effect=discard_then_draw(1, 2, optional=True),
        ),
    ],
)