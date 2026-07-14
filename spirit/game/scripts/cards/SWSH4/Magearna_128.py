from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.support_common import shuffle_hand_into_deck_draw
from spirit.game.card_effects.attacks_common import damage_per, count_bench

card = PokemonCardDef(
    guid="37ab4f04-a57e-5d9d-8cf4-54a6ea3f6675",
    key="SWSH4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Magearna.Name",
    display_name="Magearna",
    searchable_by=["Magearna", "Basic", "Magearna"],
    subtypes=["Basic"],
    collector_number=128,
    set_code="SWSH4",
    rarity=Rarities.RareHolo,
    hp=90,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.GRASS,
    family_id=801,
    abilities=[
        Attack(
            title="Overhaul",
            game_text="Shuffle your hand into your deck. Then, draw 6 cards.",
            cost={PokemonTypes.METAL: 1},
            effect=shuffle_hand_into_deck_draw(6),
        ),
        Attack(
            title="Windup Cannon",
            game_text="This attack does 20 more damage for each of your opponent's Benched Pok\u00e9mon.",
            cost={PokemonTypes.METAL: 1, PokemonTypes.COLORLESS: 1},
            damage=10,
            damage_operator="+",
            effect=damage_per(count_bench("opponent"), 20, base=10),
        ),
    ],
)