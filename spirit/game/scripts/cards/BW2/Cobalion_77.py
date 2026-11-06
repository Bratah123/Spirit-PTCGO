from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.support_common import gust_attack

card = PokemonCardDef(
    guid="687f256a-ab29-5b33-8c60-4c3ab9125956",
    key="BW2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Cobalion.Name",
    display_name="Cobalion",
    searchable_by=["Cobalion", "Basic", "Cobalion"],
    subtypes=["Basic"],
    collector_number=77,
    set_code="BW2",
    rarity=Rarities.RareHolo,
    hp=110,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.PSYCHIC,
    resistance_amount=20,
    family_id=638,
    abilities=[
        Attack(
            title="Metal Horns",
            game_text="Your opponent switches the Defending Pok\u00e9mon with 1 of his or her Benched Pok\u00e9mon.",
            cost={PokemonTypes.METAL: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
            effect=gust_attack(opponent_chooses=True),
        ),
        Attack(
            title="Sacred Sword",
            game_text="This Pok\u00e9mon can't use Sacred Sword during your next turn.",
            cost={PokemonTypes.METAL: 2, PokemonTypes.COLORLESS: 1},
            damage=100,
            locks_next_turn=True,
        ),
    ],
)
