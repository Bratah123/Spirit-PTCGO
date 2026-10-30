from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import snipe_attack
from spirit.game.card_effects.ex import shuffle_random_from_opponent_hand


card = PokemonCardDef(
    guid="60a2e9e3-c5c1-5e3a-97f8-434b3666ecfc",
    key="EX2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Murkrow.Name",
    display_name="Murkrow",
    searchable_by=["Murkrow", "Basic", "Murkrow"],
    subtypes=["Basic"],
    collector_number=47,
    set_code="EX2",
    rarity=Rarities.Uncommon,
    hp=60,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    resistance_type=PokemonTypes.PSYCHIC,
    family_id=198,
    abilities=[
        Attack(
            title="Surprise",
            game_text="Choose 1 card from your opponent's hand without looking. Look at the card you chose, then have your opponent shuffle that card into his or her deck.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=shuffle_random_from_opponent_hand(),
        ),
        Attack(
            title="Dark Mind",
            game_text="Does 10 damage to 1 of your opponent's Benched Pok\u00e9mon. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.DARKNESS: 1, PokemonTypes.COLORLESS: 1},
            damage=20,
            effect=snipe_attack(10, also_base=True),
        ),
    ],
)
