from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import AttrID, PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import flip_bonus, mill_scaled_damage
from spirit.game.card_effects.pokemon import is_energy_card


def _is_fire_energy_card(card):
    types = card.get_attribute(AttrID.POKEMON_TYPES) or []
    return is_energy_card(card) and PokemonTypes.FIRE.value in types


card = PokemonCardDef(
    guid="efa066c2-52c0-5460-83c5-a4ccd257f956",
    key="GYM1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.BlainesMagmar.Name",
    display_name="Blaine's Magmar",
    searchable_by=["Blaine's Magmar", "Basic", "BlainesMagmar"],
    subtypes=["Basic"],
    collector_number=37,
    set_code="GYM1",
    rarity=Rarities.Uncommon,
    hp=60,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.WATER,
    family_id=126,
    abilities=[
        Attack(
            title="Firebreathing",
            game_text="Flip a coin. If heads, this attack does 10 damage plus 10 more damage; if tails, this attack does 10 damage.",
            cost={PokemonTypes.FIRE: 1},
            damage=10,
            damage_operator="+",
            effect=flip_bonus(10),
        ),
        Attack(
            title="Lava Burst",
            game_text="Discard the top 5 cards of your deck. (If there are fewer than 5 cards in your deck, discard all of them.) This attack does 20 damage for each Fire Energy card you discarded in this way.",
            cost={PokemonTypes.FIRE: 3},
            damage=20,
            damage_operator="x",
            effect=mill_scaled_damage(5, 20, pred=_is_fire_energy_card),
        ),
    ],
)
