from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.ex import prize_lead_bonus
from spirit.game.card_effects.ex import discard_opponent_hand_down_to

card = PokemonCardDef(
    guid="dbd32d3b-9d48-52d8-8285-cedb6edf1636",
    key="EX3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Absol.Name",
    display_name="Absol",
    searchable_by=["Absol", "Basic", "Absol"],
    subtypes=["Basic"],
    collector_number=1,
    set_code="EX3",
    rarity=Rarities.RareHolo,
    hp=70,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    resistance_type=PokemonTypes.PSYCHIC,
    family_id=359,
    abilities=[
        Attack(
            title="Bad News",
            game_text="If the number of cards in your opponent's hand is at least 6, choose a number of cards there, without looking, until your opponent has 5 cards left. Have your opponent discard the cards you chose.",
            cost={PokemonTypes.DARKNESS: 1},
            # STUB: attack effect not implemented
            effect=discard_opponent_hand_down_to(5),
        ),
        Attack(
            title="Prize Count",
            game_text="If you have more Prize cards left than your opponent, this attack does 20 damage plus 20 more damage.",
            cost={PokemonTypes.DARKNESS: 1, PokemonTypes.COLORLESS: 1},
            damage=20,
            damage_operator="+",
            # STUB: attack effect not implemented
            effect=prize_lead_bonus(20, base=20),
        ),
    ],
)