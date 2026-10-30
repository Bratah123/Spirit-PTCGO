from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.ex import flip_discard_random_from_opponent_hand


card = PokemonCardDef(
    guid="8948c21e-ddf8-56a7-a276-73d2cbd5d469",
    key="EX1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Poochyena.Name",
    display_name="Poochyena",
    searchable_by=["Poochyena", "Basic", "Poochyena"],
    subtypes=["Basic"],
    collector_number=64,
    set_code="EX1",
    rarity=Rarities.Common,
    hp=50,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    resistance_type=PokemonTypes.PSYCHIC,
    family_id=261,
    abilities=[
        Attack(
            title="Knock Off",
            game_text="Flip a coin. If heads, choose 1 card from your opponent's hand without looking and discard it.",
            cost={PokemonTypes.DARKNESS: 1},
            effect=flip_discard_random_from_opponent_hand(),
        ),
        Attack(
            title="Rear Kick",
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
        ),
    ],
)
