from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.sm4 import ink_spit

card = PokemonCardDef(
    guid="25e48237-e65b-58ab-8494-1a2a090d6853",
    key="SM5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Buneary.Name",
    display_name="Buneary",
    searchable_by=["Buneary", "Basic", "Buneary"],
    subtypes=["Basic"],
    collector_number=106,
    set_code="SM5",
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=427,
    abilities=[
        Attack(
            title="Weak Kneed",
            game_text="If the Defending Pok\u00e9mon tries to attack during your opponent's next turn, your opponent flips a coin. If tails, that attack does nothing.",
            cost={PokemonTypes.COLORLESS: 1},
            # STUB: attack effect not implemented
            effect=ink_spit,
        ),
        Attack(
            title="Skip",
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
        ),
    ],
)