from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AttrID
from spirit.game.card_effects.attacks_common import flip_damage
from spirit.game.card_effects.support_common import attach_from_discard
from spirit.game.card_effects.trainers import is_energy_card


def _is_water_energy_card(card):
    types = card.get_attribute(AttrID.POKEMON_TYPES) or []
    return is_energy_card(card) and PokemonTypes.WATER.value in types


card = PokemonCardDef(
    guid="341e6658-ed19-5f21-a01e-a721d6cde541",
    key="SWSH35",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.WailordV.Name",
    display_name="Wailord V",
    searchable_by=["Wailord V", "Basic", "V", "WailordV"],
    subtypes=["Basic", "V"],
    collector_number=13,
    set_code="SWSH35",
    rarity=Rarities.RareHoloV,
    hp=280,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=4,
    weakness_type=PokemonTypes.LIGHTNING,
    family_id=321,
    abilities=[
        Attack(
            title="Draw Up",
            game_text="Attach up to 3 Water Energy cards from your discard pile to this Pok\u00e9mon.",
            cost={PokemonTypes.WATER: 1},
            effect=attach_from_discard(
                predicate=_is_water_energy_card, count=3, minimum=0, target="self",
                prompt="Choose up to 3 Water Energy cards to attach to this Pokémon",
            ),
        ),
        Attack(
            title="Ocean Waves",
            game_text="Flip 3 coins. This attack does 120 damage for each heads.",
            cost={PokemonTypes.WATER: 4},
            damage=120,
            damage_operator="x",
            effect=flip_damage(coins=3, per_heads=120),
        ),
    ],
)