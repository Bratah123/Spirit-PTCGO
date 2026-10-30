from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import flip_bonus
from spirit.game.card_effects.support_common import shuffle_hand_into_deck_draw


card = PokemonCardDef(
    guid="c09f2525-56ec-5513-b58e-43a1a7b4db16",
    key="GYM1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.ErikasExeggutor.Name",
    display_name="Erika's Exeggutor",
    searchable_by=["Erika's Exeggutor", "Stage 1", "ErikasExeggutor"],
    subtypes=["Stage 1"],
    collector_number=44,
    set_code="GYM1",
    rarity=Rarities.Uncommon,
    hp=70,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.ErikasExeggcute.Name",
    family_id=102,
    abilities=[
        Attack(
            title="Psychic Exchange",
            game_text="Shuffle your hand into your deck, then draw 5 cards.",
            cost={PokemonTypes.PSYCHIC: 1},
            effect=shuffle_hand_into_deck_draw(5),
        ),
        Attack(
            title="Stomp",
            game_text="Flip a coin. If heads, this attack does 30 damage plus 10 more damage; if tails, this attack does 30 damage.",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 2},
            damage=30,
            damage_operator="+",
            effect=flip_bonus(10),
        ),
    ],
)
