from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.ex import amnesia, scavenge_trainer


card = PokemonCardDef(
    guid="eda8cbe2-e4b5-5ed2-9f5f-ac5e0d361117",
    key="POP6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Bidoof.Name",
    display_name="Bidoof",
    searchable_by=["Bidoof", "Basic", "Bidoof"],
    subtypes=["Basic"],
    collector_number=11,
    set_code="POP6",
    rarity=Rarities.Common,
    hp=50,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=399,
    abilities=[
        Attack(
            title="Amnesia",
            game_text="Choose 1 of the Defending Pok\u00e9mon's attacks. That Pok\u00e9mon can't use that attack during your opponent's next turn.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=amnesia,
        ),
        Attack(
            title="Scavenge",
            game_text="Search your discard pile for a Trainer card, show it to your opponent, an put it into your hand.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=scavenge_trainer(),
        ),
    ],
)
