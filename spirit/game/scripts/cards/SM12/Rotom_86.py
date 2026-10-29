from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.support_common import discard_then_draw
from spirit.game.card_effects.sm12 import energy_assist


card = PokemonCardDef(
    guid="917d561d-60a3-55ef-9491-38c603d20c0a",
    key="SM12",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Rotom.Name",
    display_name="Rotom",
    searchable_by=["Rotom", "Basic", "Rotom"],
    subtypes=["Basic"],
    collector_number=86,
    set_code="SM12",
    rarity=Rarities.Uncommon,
    hp=70,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=20,
    family_id=479,
    abilities=[
        Attack(
            title="Cycle Draw",
            game_text="Discard a card from your hand. If you do, draw 2 cards.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=discard_then_draw(1, 2, optional=True),
        ),
        Attack(
            title="Energy Assist",
            game_text="Attach 2 basic Energy cards from your discard pile to your Benched Pok\u00e9mon in any way you like.",
            cost={PokemonTypes.PSYCHIC: 1},
            effect=energy_assist,
        ),
    ],
)